from django.test import TestCase

from ..models import Message, MessageQuerySet


class MessageTests(TestCase):
    """
    Test the methods and custom manager of the Message model.

    """
    fixtures = ['soapboxtest.json']

    def test_global_instance(self):
        """
        Test a Message with is_global=True to ensure it matches on
        arbitrary URLs.

        """
        message = Message.objects.get(pk=1)
        self.assertTrue(
            message.match('/')
        )
        self.assertTrue(
            message.match('/foo/')
        )
        self.assertTrue(
            message.match('/foo/bar/')
        )

    def test_non_global_instance(self):
        """
        Test a message with is_global=False to ensure it matches only
        on the correct URL.

        """
        message = Message.objects.get(pk=2)
        self.assertFalse(
            message.match('/')
        )
        self.assertTrue(
            message.match('/foo/')
        )

    def test_prefix_matching(self):
        """
        Test that a Message matches when its URL is a prefix of the
        supplied URL.

        """
        message = Message.objects.get(pk=2)
        self.assertTrue(
            message.match('/foo/bar/')
        )

    def test_active_queryset(self):
        """
        Test that the active() method of MessageQuerySet returns the
        correct count.

        """
        self.assertEqual(
            MessageQuerySet(Message).active().count(),
            5
        )

    def test_active_manager(self):
        """
        Test that the active() method of MessageManager correctly
        passes through to MessageQuerySet.

        """
        self.assertEqual(
            Message.objects.active().count(),
            5
        )

    def test_match_global(self):
        """
        Test that the match() method of MessageManager correctly
        retrieves global Messages.

        """
        results = Message.objects.match('/')
        self.assertEqual(len(results), 1)
        result_ids = [m.id for m in results]
        self.assertEqual([1], result_ids)

    def test_match_simple(self):
        """
        Test that the match() method of MessageManager correctly
        retrieves global Messages and exact matches when both are
        present.

        """
        results = Message.objects.match('/bar/')
        self.assertEqual(len(results), 2)
        result_ids = [m.id for m in results]
        self.assertTrue(1 in result_ids)
        self.assertTrue(4 in result_ids)

    def test_match_partial(self):
        """
        Test that the match() method of MessageManager correctly
        retrieves Messages which match a prefix of the URL.

        """
        results = Message.objects.match('/foo/bar/')
        self.assertEqual(len(results), 4)
        result_ids = [m.id for m in results]
        self.assertTrue(1 in result_ids)
        self.assertTrue(2 in result_ids)
        self.assertTrue(3 in result_ids)
        self.assertTrue(7 in result_ids)
