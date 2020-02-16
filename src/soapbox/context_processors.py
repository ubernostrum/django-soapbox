from .models import Message


def soapbox_messages(request):
    """
    Context processor which will retrieve all Message objects for the
    request URL and insert them into the context as the variable
    ``soapbox_messages``.

    """
    return {"soapbox_messages": Message.objects.match(request.path)}
