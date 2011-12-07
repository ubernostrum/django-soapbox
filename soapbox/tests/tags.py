from django.test import TestCase


class TagTests(TestCase):
    fixtures = ['soapboxtest.json']
    urls = 'soapbox.tests.urls'

    def test_success_root(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.context['soapbox_messages']), 1)
        self.assertContains(r, "This is a global message.")

    def test_success_with_match(self):
        r = self.client.get('/foo/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.context['soapbox_messages']), 2)
        self.assertContains(r, "This is a global message.")
        self.assertContains(r, "This message appears on /foo/ and on /foo/bar/.")

    def test_success_with_multiple_match(self):
        r = self.client.get('/foo/bar/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.context['soapbox_messages']), 3)
        self.assertContains(r, "This is a global message.")
        self.assertContains(r, "This message appears on /foo/ and on /foo/bar/.")
        self.assertContains(r, "This message appears only on /foo/bar/.")

    def test_fail_syntax(self):
        from django import template
        self.assertRaises(template.TemplateSyntaxError,
                          self.client.get,
                          '/fail/')
        
