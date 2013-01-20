# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        db.create_table('aw_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('logo', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True)),
            ('favicon', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(blank=True, related_name='as_favicon', null=True, to=orm['medialibrary.MediaFile'])),
            ('background_image', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(blank=True, related_name='as_background_image', null=True, to=orm['medialibrary.MediaFile'])),
            ('ad_image', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(blank=True, related_name='as_ad_image', null=True, to=orm['medialibrary.MediaFile'])),
            ('twitter_username', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('facebook_username', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ad_link', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('extra_styles', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('footer_bottom', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('aw', ['Application'])


    def backwards(self, orm):
        # Deleting model 'Application'
        db.delete_table('aw_application')


    models = {
        'aw.application': {
            'Meta': {'object_name': 'Application'},
            'ad_image': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'blank': 'True', 'related_name': "'as_ad_image'", 'null': 'True', 'to': "orm['medialibrary.MediaFile']"}),
            'ad_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'background_image': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'blank': 'True', 'related_name': "'as_background_image'", 'null': 'True', 'to': "orm['medialibrary.MediaFile']"}),
            'extra_styles': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'facebook_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'favicon': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'blank': 'True', 'related_name': "'as_favicon'", 'null': 'True', 'to': "orm['medialibrary.MediaFile']"}),
            'footer_bottom': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'aw.category': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['aw.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'aw.reporter': {
            'Meta': {'object_name': 'Reporter'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['aw']