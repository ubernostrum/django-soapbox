from django.db import models


class MessageManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def match(self, url):
        results = []
        for message in self.active():
            if message.match(url):
                results.append(message)
        return results


class Message(models.Model):
    message = models.TextField()
    is_global = models.BooleanField(help_text="If checked, this message will display on all pages.")
    is_active = models.BooleanField(default=True, help_text="Only active messages will be displayed.")
    url = models.TextField("URL", max_length=255, blank=True, null=True,
                           help_text="Message will be displayed on any URL which matches this.")

    objects = MessageManager()

    def __unicode__(self):
        return self.message

    def match(url):
        return url.find(self.url) == 0
