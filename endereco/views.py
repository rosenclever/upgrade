# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from endereco.forms import EnderecoForm
from django.template import RequestContext
from django.shortcuts import render_to_response

def newEndereco(request):
	form = EnderecoForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('endereco/new.html', context)

def manterEndereco(request):
    if request.method == 'POST':
        return createEndereco(request)
    else:
        return newEndereco(request)

def newTelefone(request):
	form = TelefoneForm()
	context = RequestContext(request, {'form': form})
	return render_to_response('telefone/new.html', context)

def manterTelefone(request):
    if request.method == 'POST':
        return createTelefone(request)
    else:
        return newTelefone(request)