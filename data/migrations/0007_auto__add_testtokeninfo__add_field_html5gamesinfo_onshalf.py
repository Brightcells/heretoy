# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestTokenInfo'
        db.create_table(u'data_testtokeninfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'data', ['TestTokenInfo'])

        # Adding field 'Html5GamesInfo.onshalf'
        db.add_column(u'data_html5gamesinfo', 'onshalf',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TestTokenInfo'
        db.delete_table(u'data_testtokeninfo')

        # Deleting field 'Html5GamesInfo.onshalf'
        db.delete_column(u'data_html5gamesinfo', 'onshalf')


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
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'onshalf': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'operate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'play': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_play': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'unlike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gameslikeinfo': {
            'Meta': {'object_name': 'Html5GamesLikeInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_like'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gamesplayinfo': {
            'Meta': {'object_name': 'Html5GamesPlayInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_play'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'play': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gamesplaylog': {
            'Meta': {'object_name': 'Html5GamesPlayLog'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_play_log'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gamesunlikeinfo': {
            'Meta': {'object_name': 'Html5GamesUnlikeInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_unlike'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.testtokeninfo': {
            'Meta': {'object_name': 'TestTokenInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']