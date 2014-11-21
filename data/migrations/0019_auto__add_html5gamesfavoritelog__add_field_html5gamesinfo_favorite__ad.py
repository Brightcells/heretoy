# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Html5GamesFavoriteLog'
        db.create_table(u'data_html5gamesfavoritelog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('h5game', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='h5game_favorite_log', null=True, to=orm['data.Html5GamesInfo'])),
            ('favorite', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'data', ['Html5GamesFavoriteLog'])

        # Adding field 'Html5GamesInfo.favorite'
        db.add_column(u'data_html5gamesinfo', 'favorite',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Html5GamesInfo.real_favorite'
        db.add_column(u'data_html5gamesinfo', 'real_favorite',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Html5GamesPlayInfo.favorite'
        db.add_column(u'data_html5gamesplayinfo', 'favorite',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Html5GamesFavoriteLog'
        db.delete_table(u'data_html5gamesfavoritelog')

        # Deleting field 'Html5GamesInfo.favorite'
        db.delete_column(u'data_html5gamesinfo', 'favorite')

        # Deleting field 'Html5GamesInfo.real_favorite'
        db.delete_column(u'data_html5gamesinfo', 'real_favorite')

        # Deleting field 'Html5GamesPlayInfo.favorite'
        db.delete_column(u'data_html5gamesplayinfo', 'favorite')


    models = {
        u'data.html5gamesclassifyinfo': {
            'Meta': {'object_name': 'Html5GamesClassifyInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gamesfavoritelog': {
            'Meta': {'object_name': 'Html5GamesFavoriteLog'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_favorite_log'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gamesinfo': {
            'Meta': {'object_name': 'Html5GamesInfo'},
            'audit': ('django.db.models.fields.CharField', [], {'default': "'audit_ing'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'boutique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'classify1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'classify1'", 'null': 'True', 'to': u"orm['data.Html5GamesClassifyInfo']"}),
            'classify2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'classify2'", 'null': 'True', 'to': u"orm['data.Html5GamesClassifyInfo']"}),
            'commit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'developer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'first_publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nail': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'onshalf': ('django.db.models.fields.CharField', [], {'default': "'test'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'operate': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'play': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_favorite': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_nail': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'real_play': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reject_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'screen': ('django.db.models.fields.CharField', [], {'default': "'vertical'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sole': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'submit_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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
        u'data.html5gamesnaillog': {
            'Meta': {'object_name': 'Html5GamesNailLog'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_nail_log'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.html5gamesplayinfo': {
            'Meta': {'object_name': 'Html5GamesPlayInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'favorite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_play'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        u'data.lunbotuinfo': {
            'Meta': {'object_name': 'LunbotuInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_lubotugame'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lbt_classify': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'onshalf': ('django.db.models.fields.CharField', [], {'default': "'test'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'share_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.testtokeninfo': {
            'Meta': {'object_name': 'TestTokenInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'data.topicgamesinfo': {
            'Meta': {'object_name': 'TopicGamesInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'h5game': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_topicgame'", 'null': 'True', 'to': u"orm['data.Html5GamesInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'h5game_topic'", 'null': 'True', 'to': u"orm['data.TopicInfo']"})
        },
        u'data.topicinfo': {
            'Meta': {'object_name': 'TopicInfo'},
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']