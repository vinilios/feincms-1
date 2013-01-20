from django.db import models
from django.template.loader import render_to_string
from django.conf.urls import patterns, url, include
from feincms.module.medialibrary.models import MediaFile
from feincms.module.medialibrary.fields import MediaFileForeignKey


class Player(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    birth_date = models.DateField(blank=False)
    weight = models.IntegerField(help_text="Insert weight in Kgr", default=0, blank=True, null=True)    
    height = models.IntegerField(help_text="Insert height in cm", default=0, blank=True, null=True)
    STICK_OPTIONS = (
        ('RT', 'Right'),
        ('LT', 'Left'),
    )
    stick = models.CharField(max_length=2, choices=STICK_OPTIONS, default='RT')
    number = models.IntegerField(help_text="Jersey number", default=0, blank=True, null=True)   
    POSITION_OPTIONS = (
        ('G', 'Goalie'),
        ('D', 'Defense Men'),
        ('F', 'Forward'),
	('C', 'Coach'),
    )    
    position = models.CharField(max_length=1, choices=POSITION_OPTIONS )
    cv = models.TextField(blank=True, null=True)
    cv_image = MediaFileForeignKey(MediaFile,blank=True,null=True, related_name='cv_image')
    speed = models.IntegerField(help_text="insert a number from 0 to 100", default=0, blank=True, null=True)
    agility = models.IntegerField(help_text="insert a number from 0 to 100",default=0, blank=True, null=True )
    shoot = models.IntegerField(help_text="insert a number from 0 to 100",default=0, blank=True, null=True)          
    puck_control = models.IntegerField(help_text="insert a number from 0 to 100", default=0, blank=True, null=True )    
    roster_image = MediaFileForeignKey(MediaFile,blank=True,null=True, related_name='roster_image', help_text='This should be a transparent image')

    def __unicode__(self):
        return self.full_name
