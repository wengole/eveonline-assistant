# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attribute.slot'
        db.add_column(u'skills_attribute', 'slot',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Attribute.slot'
        db.delete_column(u'skills_attribute', 'slot')


    models = {
        u'skills.attribute': {
            'Meta': {'object_name': 'Attribute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slot': ('django.db.models.fields.IntegerField', [], {})
        },
        u'skills.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
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
            'Meta': {'ordering': "['name']", 'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skills'", 'to': u"orm['skills.Group']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'primary_attribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_for'", 'to': u"orm['skills.Attribute']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'required_skills': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'provided_skills'", 'symmetrical': 'False', 'to': u"orm['skills.Requirement']"}),
            'secondary_attribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'secondary_for'", 'to': u"orm['skills.Attribute']"})
        }
    }

    complete_apps = ['skills']