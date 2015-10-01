# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        try:
            orm.BuildEnvironment.objects.get(pk = 1)
        except:
            from django.utils import timezone
            orm.BuildEnvironment.objects.create(pk = 1,
                created = timezone.now(),
                updated = timezone.now(),
                betype = 0)

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'bldcontrol.brlayer': {
            'Meta': {'object_name': 'BRLayer'},
            'commit': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'dirpath': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'giturl': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'req': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bldcontrol.BuildRequest']"})
        },
        u'bldcontrol.brtarget': {
            'Meta': {'object_name': 'BRTarget'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'req': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bldcontrol.BuildRequest']"}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'bldcontrol.brvariable': {
            'Meta': {'object_name': 'BRVariable'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'req': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bldcontrol.BuildRequest']"}),
            'value': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'bldcontrol.buildenvironment': {
            'Meta': {'object_name': 'BuildEnvironment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'bbaddress': ('django.db.models.fields.CharField', [], {'max_length': '254', 'blank': 'True'}),
            'bbport': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'bbstate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bbtoken': ('django.db.models.fields.CharField', [], {'max_length': '126', 'blank': 'True'}),
            'betype': ('django.db.models.fields.IntegerField', [], {}),
            'builddir': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lock': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sourcedir': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'bldcontrol.buildrequest': {
            'Meta': {'object_name': 'BuildRequest'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orm.Build']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orm.Project']"}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'orm.build': {
            'Meta': {'object_name': 'Build'},
            'bitbake_version': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'build_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'completed_on': ('django.db.models.fields.DateTimeField', [], {}),
            'cooker_log_path': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'distro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'distro_version': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'errors_no': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'outcome': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orm.Project']", 'null': 'True'}),
            'started_on': ('django.db.models.fields.DateTimeField', [], {}),
            'timespent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'warnings_no': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'orm.project': {
            'Meta': {'object_name': 'Project'},
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['bldcontrol']
    symmetrical = True