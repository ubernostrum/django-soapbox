from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import Message, MessageQuerySet
from ..models import GLOBAL_OR_LOCAL, WHERE_REQUIRED


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
        self.assertEqual(
            {1, 4}, {m.id for m in results}
        )

    def test_match_partial(self):
        """
        Test that the match() method of MessageManager correctly
        retrieves Messages which match a prefix of the URL.

        """
        results = Message.objects.match('/foo/bar/')
        self.assertEqual(len(results), 4)
        self.assertEqual(
            {1, 2, 3, 7}, {m.id for m in results}
        )

    def test_global_or_local(self):
        """
        Message instances can be global, or appear on selected pages,
        but not both.

        """
        m = Message(
            message="Invalid message that's both global and local.",
            is_global=True,
            is_active=True,
            url="/foo/"
        )
        with self.assertRaises(ValidationError, msg=GLOBAL_OR_LOCAL):
            m.clean()

        m = Message(
            message="Valid message that's both global and has an empty URL.",
            is_global=True,
            is_active=True,
            url=""
        )
        m.clean()

    def test_where_required(self):
        """
        A Message instance must either be global or specify a URL
        prefix to match.

        """
        m = Message(
            message="Invalid message that's neither global nor local.",
            is_global=False,
            is_active=True
        )
        with self.assertRaises(ValidationError, msg=WHERE_REQUIRED):
            m.clean()


class ContextProcessorTests(TestCase):
    """
    Test the context processor which automatically adds messages to
    template context.

    """
    fixtures = ['soapboxtest.json']

    def test_context_processor(self):
        """
        Test basic use of the context processor.

        """
        # Enable the context processor only for this test, since its
        # context variable name conflicts with the one used by the
        # template tag in other tests.
        with self.modify_settings(
            TEMPLATE_CONTEXT_PROCESSORS={
                'append': 'soapbox.context_processors.soapbox_messages',
                }):
            r = self.client.get('/foo/bar/baz/')
            self.assertEqual(r.status_code, 200)
            self.assertTrue('soapbox_messages' in r.context)
            self.assertEqual(
                len(r.context['soapbox_messages']), 4)
            self.assertEqual(
                {1, 2, 3, 7},
                {m.id for m in r.context['soapbox_messages']}
            )
