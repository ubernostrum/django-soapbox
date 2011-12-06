from django.test import TestCase

from soapbox.models import Message


class MessageTests(TestCase):
    fixtures = ['soapboxtest.json']

    def test_active(self):
        # Fixture has four active messages.
        self.assertEqual(Message.objects.active().count(), 4)

    def test_match_simple(self):
        # Should match the global and the '/bar/' messages.
        results = Message.objects.match('/bar/')
        self.assertEqual(len(results), 2)

    def test_match_partial(self):
        # Should match the global, the '/foo/' and the '/foo/bar/'
        # messages.
        results = Message.objects.match('/foo/bar/')
        self.assertEqual(len(results), 3)

    def test_match_global(self):
        # Should match only the global message.
        results = Message.objects.match('/')
        self.assertEqual(len(results), 1)
