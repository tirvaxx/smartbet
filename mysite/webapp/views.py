from django.shortcuts import render
from django.http import HttpResponse
from mailchimp3 import Mailchimp

def index(request) :
    mc = Mailchimp()
    # Trigger the action on the given list
    added = mc.add_member_to_list(settings.MAILCHIMP_LIST_ID, email)
    if added:
    	print("Email successfully added")
    
    return HttpResponse('<h2>HEY!</h2>')
# Create your views here.


