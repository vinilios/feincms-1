import models
from django.contrib import admin

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None                   , {'fields':['full_name','number',]}),
        ('Personal Information' , {'fields':['birth_date','weight','height','cv','cv_image','roster_image']}),
        ('Skills'               , {'fields':['stick','position','speed','agility','shoot','puck_control', ]}),
            
    ]

admin.site.register(models.Player, PlayerAdmin)

