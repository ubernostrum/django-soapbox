from django import template

from ..models import Message


register = template.Library()


@register.assignment_tag(takes_context=True)
def get_messages_for_page(context, url):
    if url == context.template.engine.string_if_invalid:
        return []
    return Message.objects.match(url)
