from django.conf import settings
from aw.models import Application
from feincms.module.medialibrary.models import Category

def application(request):
    try:
        return {'APP': Application.current(), 'WORDS': settings.WORDS, 'GLOBAL_VARS': settings.GLOBAL_VARS,}
    except:
      return {'APP': 'aw'}

def test(request):
    galleries = Category.objects.filter(parent__title='Gallery').values()
    try:
	return { 'galleries':galleries }
    except:
	return { 'galleries': '[1,2]' }
