# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ApiKey'
        db.create_table(u'characters_apikey', (
            ('key_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('verification_code', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'characters', ['ApiKey'])

        # Adding model 'Character'
        db.create_table(u'characters_character', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('apikey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.ApiKey'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('skillpoints', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'characters', ['Character'])

        # Adding model 'SkillTrained'
        db.create_table(u'characters_skilltrained', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Character'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.Skill'])),
            ('skillpoints', self.gf('django.db.models.fields.IntegerField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'characters', ['SkillTrained'])

        # Adding model 'AttributeValues'
        db.create_table(u'characters_attributevalues', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Character'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.Attribute'])),
            ('base', self.gf('django.db.models.fields.IntegerField')()),
            ('bonus', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'characters', ['AttributeValues'])


    def backwards(self, orm):
        # Deleting model 'ApiKey'
        db.delete_table(u'characters_apikey')

        # Deleting model 'Character'
        db.delete_table(u'characters_character')

        # Deleting model 'SkillTrained'
        db.delete_table(u'characters_skilltrained')

        # Deleting model 'AttributeValues'
        db.delete_table(u'characters_attributevalues')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'characters.apikey': {
            'Meta': {'object_name': 'ApiKey'},
            'key_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'verification_code': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'characters.attributevalues': {
            'Meta': {'object_name': 'AttributeValues'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skills.Attribute']"}),
            'base': ('django.db.models.fields.IntegerField', [], {}),
            'bonus': ('django.db.models.fields.IntegerField', [], {}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'characters.character': {
            'Meta': {'object_name': 'Character'},
            'apikey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.ApiKey']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'skillpoints': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"})
        },
        u'characters.skilltrained': {
            'Meta': {'object_name': 'SkillTrained'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skills.Skill']"}),
            'skillpoints': ('django.db.models.fields.IntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'skills.attribute': {
            'Meta': {'object_name': 'Attribute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'skills.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'skills.requirement': {
            'Meta': {'object_name': 'Requirement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skills.Skill']"})
        },
        u'skills.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['skills.Group']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'primary_attribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_for'", 'to': u"orm['skills.Attribute']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'required_skills': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'provided_skills'", 'symmetrical': 'False', 'to': u"orm['skills.Requirement']"}),
            'secondary_attribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'secondary_for'", 'to': u"orm['skills.Attribute']"})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['characters']