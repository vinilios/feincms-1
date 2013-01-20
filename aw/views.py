from django.shortcuts import render_to_response
from django.db import models
from aw.models import Category
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

