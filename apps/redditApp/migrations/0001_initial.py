# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table('redditApp_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('redditApp', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table('redditApp_link')


    models = {
        'redditApp.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'sub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['redditApp']