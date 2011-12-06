from django.db import models


class MessageManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def match(self, url):
        results = []
        for message in self.active():
            if message.is_global or message.match(url):
                results.append(message)
        return list(set(results))


class Message(models.Model):
    message = models.TextField()
    is_global = models.BooleanField(help_text="If checked, this message will display on all pages.")
    is_active = models.BooleanField(default=True, help_text="Only active messages will be displayed.")
    url = models.CharField("URL", max_length=255, blank=True, null=True,
                           help_text="Message will be displayed on any URL which matches this.")

    objects = MessageManager()

    def __unicode__(self):
        return self.message

    def match(self, url):
        if self.is_global:
            return True
        self_bits = self.url.strip('/').split('/')
        url_bits = url.strip('/').split('/')
        if len(self_bits) > len(url_bits):
            return False
        return self_bits == url_bits[:len(self_bits)]
