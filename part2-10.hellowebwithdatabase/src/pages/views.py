from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
	msg_id = int(request.GET['id'])
	responseMessage = Message.objects.get(pk=msg_id).content
	return HttpResponse(responseMessage)