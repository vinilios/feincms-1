from django.template.loader import render_to_string
from django.db import models
from players.models import Player
from django.conf import settings
from datetime import date
from aw.settings import STATIC_URL

def calculate_age(born):
    today = date.today()
    try: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day-1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year





def players(request):
    players = Player.objects.all()
    return render_to_string(['players.html'], {'players':players, 'STATIC_URL':STATIC_URL, })
