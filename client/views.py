from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from pusher import Pusher
from .models import Item

pusher = Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
)


# Create your views here.
def Home(request):
    item = Item.objects.create(
        name="Item 1",
        description="This is an item",
    )
    pusher.trigger('my-channel', 'my-event', {'message': item.to_json()})
    return HttpResponse("Hello, world. You're at the polls index.")