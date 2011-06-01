# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Pessoa'
        db.create_table('pessoa_pessoa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('dt_nasc', self.gf('django.db.models.fields.DateField')()),
            ('matricula', self.gf('django.db.models.fields.CharField')(max_length=5, unique=True, null=True, blank=True)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=15, unique=True, null=True, blank=True)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=11, unique=True, null=True, blank=True)),
            ('endereco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['endereco.Endereco'])),
            ('responsavel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pessoa.Pessoa'])),
        ))
        db.send_create_signal('pessoa', ['Pessoa'])


    def backwards(self, orm):
        
        # Deleting model 'Pessoa'
        db.delete_table('pessoa_pessoa')


    models = {
        'endereco.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cep': ('django.db.models.fields.IntegerField', [], {}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logradouro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'pessoa.pessoa': {
            'Meta': {'object_name': 'Pessoa'},
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '11', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'dt_nasc': ('django.db.models.fields.DateField', [], {}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['endereco.Endereco']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'responsavel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pessoa.Pessoa']"}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['pessoa']
