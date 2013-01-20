# Django settings for example project.
#-*- encoding:utf-8 -*-
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'example.db')


DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': DATABASE_NAME,
}}

TIME_ZONE = 'Europe/Athens'

LANGUAGE_CODE = 'en-us'

SITE_ID = int(os.environ.get('SITE_ID', 1))

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/')
STATIC_URL = '/static/'

SECRET_KEY = '_wn95s-apfd-442cby5m^_^ak6+5(fyn3lvnvtn7!si&o)1x^w'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',

    'feincms.context_processors.add_page_if_missing',
    'aw.context_processors.application',
    'aw.context_processors.test',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'aw.urls'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'aw',	
    'news',
    'articles',
    'players',
    'schedule',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin', 
    'django.contrib.staticfiles',
    'south',

    'feincms',
   # 'feincms.module.blog',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'mptt',
)

LANGUAGES = (
    ('en', 'English'),
    ('el', 'Greek'),
)

FEINCMS_TREE_EDITOR_INCLUDE_ANCESTORS = True

SOUTH_MIGRATION_MODULES = {
    'page': 'aw.migrate.page',
    'medialibrary': 'aw.migrate.medialibrary', # if you are using the medialibrary
                                                    # which comes with FeinCMS
    }

NEWS_PAGINATOR ='4'


GLOBAL_VARS = {
    'FAQ_URL': '/hockey-world/faq/', # for footer
    'SITEMAP_URL' : '/sitemap/', # for footer 
    'NEWS_URL' :'neaanakoinwseis', #for latest news
    'ARTICLES_URL' :'ar8ra', #for article slideshow
    }
WORDS = {
    'SHOW_MORE' : 'Διαβάστε περισσότερα',
    'BACK' : 'Επιστροφή'   
    }

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'athenswarriorcontact@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': 'static/tinymce/jscripts/tiny_mce.js',
}   
