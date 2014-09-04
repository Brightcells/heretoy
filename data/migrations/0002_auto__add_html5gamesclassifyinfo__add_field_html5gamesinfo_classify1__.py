# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Html5GamesClassifyInfo'
        db.create_table(u'data_html5gamesclassifyinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('second', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Html5GamesClassifyInfo'])

        # Adding field 'Html5GamesInfo.classify1'
        db.add_column(u'data_html5gamesinfo', 'classify1',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='classify1', null=True, to=orm['data.Html5GamesClassifyInfo']),
                      keep_default=False)

        # Adding field 'Html5GamesInfo.classify2'
        db.add_column(u'data_html5gamesinfo', 'classify2',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='classify2', null=True, to=orm['data.Html5GamesClassifyInfo']),
                      keep_default=False)

        # Adding field 'Html5GamesInfo.source'
        db.add_column(u'data_html5gamesinfo', 'source',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Html5GamesInfo.version'
        db.add_column(u'data_html5gamesinfo', 'version',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Html5GamesInfo.commit'
        db.add_column(u'data_html5gamesinfo', 'commit',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Html5GamesClassifyInfo'
        db.delete_table(u'data_html5gamesclassifyinfo')

        # Deleting field 'Html5GamesInfo.classify1'
        db.delete_column(u'data_html5gamesinfo', 'classify1_id')

        # Deleting field 'Html5GamesInfo.classify2'
        db.delete_column(u'data_html5gamesinfo', 'classify2_id')

        # Deleting field 'Html5GamesInfo.source'
        db.delete_column(u'data_html5gamesinfo', 'source')

        # Deleting field 'Html5GamesInfo.version'
        db.delete_column(u'data_html5gamesinfo', 'version')

        # Deleting field 'Html5GamesInfo.commit'
        db.delete_column(u'data_html5gamesinfo', 'commit')


    models = {
        u'data.html5gamesclassifyinfo': {
            'Meta': {'object_name': 'Html5GamesClassifyInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gamesinfo': {
            'Meta': {'object_name': 'Html5GamesInfo'},
            'classify1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'classify1'", 'null': 'True', 'to': u"orm['data.Html5GamesClassifyInfo']"}),
            'classify2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'classify2'", 'null': 'True', 'to': u"orm['data.Html5GamesClassifyInfo']"}),
            'commit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'play': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'unlike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']