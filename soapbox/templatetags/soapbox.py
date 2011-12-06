from django import template

from soapbox.models import Message


register = template.Library()


class MessagesForPageNode(template.Node):
    def __init__(self, url, varname):
        self.url = template.Variable(url)
        self.varname = varname

    def render(self, context):
        try:
            url = self.url.resolve(context)
        except template.VariableDoesNotExist:
            return ''
        context[self.varname] = Message.objects.match(url)
        return ''


def get_messages_for_page(parser, token):
    bits = token.split_contents()
    if len(bits) != 4 or bits[2] != 'as':
        raise template.TemplateSyntaxError("%s syntax must be '{% %s [url] as [varname] %}" % (bits[0], bits[0]))
    return MessagesForPageNode(bits[1], bits[3])
