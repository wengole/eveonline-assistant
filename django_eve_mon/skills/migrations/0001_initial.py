# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'skills_group', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'skills', ['Group'])

        # Adding model 'Skill'
        db.create_table(u'skills_skill', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.Group'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('primary_attribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='primary_for', to=orm['skills.Attribute'])),
            ('secondary_attribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='secondary_for', to=orm['skills.Attribute'])),
        ))
        db.send_create_signal(u'skills', ['Skill'])

        # Adding M2M table for field required_skills on 'Skill'
        m2m_table_name = db.shorten_name(u'skills_skill_required_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('skill', models.ForeignKey(orm[u'skills.skill'], null=False)),
            ('requirement', models.ForeignKey(orm[u'skills.requirement'], null=False))
        ))
        db.create_unique(m2m_table_name, ['skill_id', 'requirement_id'])

        # Adding model 'Requirement'
        db.create_table(u'skills_requirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skills.Skill'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'skills', ['Requirement'])

        # Adding model 'Attribute'
        db.create_table(u'skills_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'skills', ['Attribute'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'skills_group')

        # Deleting model 'Skill'
        db.delete_table(u'skills_skill')

        # Removing M2M table for field required_skills on 'Skill'
        db.delete_table(db.shorten_name(u'skills_skill_required_skills'))

        # Deleting model 'Requirement'
        db.delete_table(u'skills_requirement')

        # Deleting model 'Attribute'
        db.delete_table(u'skills_attribute')


    models = {
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
        }
    }

    complete_apps = ['skills']