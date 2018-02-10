from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return HttpResponse('<h2>HEY!</h2>')
# Create your views here.
from django.http import HttpResponseRedirect
from mailchimp import utils

MAILCHIMP_LIST_ID = 'spamspamspamspameggsspamspam' # DRY :)
REDIRECT_URL_NAME = '/mailing_list_success/'
def add_email_to_mailing_list(request):
    if request.POST['email']:
	email_address = request.POST['email']
	list = utils.get_connection().get_list_by_id(MAILCHIMP_LIST_ID)
   	list.subscribe(email_address, {'EMAIL': email_address})
	return HttpResponseRedirect('/mailing_list_success/')
    else:
	return HttpResponseRedirect('/mailing_list_failure/')



