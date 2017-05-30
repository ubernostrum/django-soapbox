import re

from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe


GLOBAL_OR_LOCAL = (u"A Message can be global, or can appear on only "
                   u"some pages, but not both.")
WHERE_REQUIRED = (u"A Message must either be global, or specify a "
                  u"URL prefix it will match.")


class MessageQuerySet(models.QuerySet):
    """
    Custom QuerySet implementing an active() method for only
    retrieving active Messages.

    """
    def active(self):
        return self.filter(is_active=True)


class MessageManager(models.Manager):
    """
    Custom manager using MessageQuerySet and implementing a query
    method for Messages which match a particular URL.

    """
    def get_queryset(self):
        return MessageQuerySet(self.model)

    def active(self):
        return self.get_queryset().active()

    def match(self, url):
        """
        Return a list of all active Messages which match the given
        URL.

        """
        return list({
            message for message in self.active() if
            message.is_global or message.match(url)
        })


@python_2_unicode_compatible
class Message(models.Model):
    """
    A message which may be displayed on some or all pages of a site.

    """
    message = models.TextField()
    is_global = models.BooleanField(
        default=False,
        help_text=u"If checked, this message will display on all pages."
    )
    is_active = models.BooleanField(
        default=True,
        help_text=u"Only active messages will be displayed."
    )
    is_regex = models.BooleanField(
        default=False,
        help_text=u"If checked, the URL field will be treated as a regular "
                  u"expression while matching. Regular expression must match "
                  u"on the entire request URL starting from the beginning."
    )
    url = models.CharField(
        "URL", max_length=255, blank=True, null=True,
        help_text=u"Message will be displayed on any URL which matches this."
    )

    objects = MessageManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return mark_safe(self.message)

    def clean(self):
        if self.is_global and self.url not in EMPTY_VALUES:
            raise ValidationError(GLOBAL_OR_LOCAL)
        if not self.is_global and self.url in EMPTY_VALUES:
            raise ValidationError(WHERE_REQUIRED)

    def match(self, url):
        """
        Determine whether this Message matches a given URL.

        The matching algorithm will return True if the Message is
        global, or if the Message's URL is a (case-sensitive) prefix
        of the supplied URL, and False otherwise.

        """
        if self.is_global:
            return True

        if self.is_regex:
            return bool(re.match(self.url, url))
        else:
            # For easy comparison, we strip leading and trailing slashes,
            # and then split both self.url and the supplied URL on
            # slashes, to get two lists of path components we can compare.
            self_bits = self.url.strip('/').split('/')
            url_bits = url.strip('/').split('/')

            # If self.url produced a longer list of path components than
            # the supplied URL, it can't be a match.
            if len(self_bits) > len(url_bits):
                return False

            return self_bits == url_bits[:len(self_bits)]
