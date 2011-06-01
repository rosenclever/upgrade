# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Endereco'
        db.create_table('endereco_endereco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logradouro', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('cep', self.gf('django.db.models.fields.IntegerField')()),
            ('complemento', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('endereco', ['Endereco'])

        # Adding model 'Telefone'
        db.create_table('endereco_telefone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('pessoa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pessoa.Pessoa'])),
        ))
        db.send_create_signal('endereco', ['Telefone'])


    def backwards(self, orm):
        
        # Deleting model 'Endereco'
        db.delete_table('endereco_endereco')

        # Deleting model 'Telefone'
        db.delete_table('endereco_telefone')


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
        'endereco.telefone': {
            'Meta': {'object_name': 'Telefone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'pessoa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pessoa.Pessoa']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '3'})
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

    complete_apps = ['endereco']
