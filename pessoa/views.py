# Create your views here.
#from django.core.urlresolvers import reverse
#from django.http import HttpResponse, HttpResponseRedirect
from pessoa.forms import PessoaForm
from endereco.forms import EnderecoForm, TelefoneForm
from pessoa.models import Pessoa
from endereco.models import Endereco, Telefone
from django.template import RequestContext
from django.shortcuts import render_to_response

def new(request):
	pessoaForm = PessoaForm(instance=Pessoa())
	enderecoForm = EnderecoForm(instance=Endereco())
	context = RequestContext(request, {'pessForm':pessoaForm, 'endForm': enderecoForm})
	return render_to_response('new.html', context)

def create(request):
	pessoaForm = PessoaForm(request.POST, instance=Pessoa())
	enderecoForm = EnderecoForm(request.POST, instance=Endereco())
	
	#if pessoaForm['responsavel']=="" and (not pessoaForm['rg'].is_null() and not pessoaForm['cpf'].is_null()):
	
	
	if pessoaForm.is_valid() and endrecoForm.is_valid():
		newPessoa = pessoaForm.save()
		pessoaForm['responsavel'] = newPessoa.self
		newEndereco = enderecoForm.save()
		return HttpResponseRedirect(reverse('pessoa:success', args=[ pessoa.pk ]))
	
	else:
		context = RequestContext(request, {'pessForm':pessoaForm, 'endForm': enderecoForm})
		return render_to_response('new.html', context)

	pessoa = form.save()
    # notifica o cadastro
    #send_subscription_email(subscription)
	return HttpResponseRedirect(reverse('pessoa:success', args=[ pessoa.pk ]))


def manter(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def success(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    context = RequestContext(request, {'pessoa': pessoa})
    return render_to_response('success.html', context)