# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Link.link'
        db.alter_column('redditApp_link', 'link', self.gf('django.db.models.fields.URLField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Link.link'
        db.alter_column('redditApp_link', 'link', self.gf('django.db.models.fields.CharField')(max_length=800))

    models = {
        'redditApp.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'sub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['redditApp']