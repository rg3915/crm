# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator

from cadastro.models import Inscricao
from cadastro.forms import InscricaoForm


def home(request):
    return render(request, 'index.html')


class Criar(CreateView):
    template_name = 'cadastro.html'
    model = Inscricao
    success_url = reverse_lazy('lista')


class Listar(ListView):
    template_name = 'lista.html'
    model = Inscricao
    context_object = 'inscricao_list'
    paginate_by = 5


def lista(request):
    # pagination
    inscricoes_list = Inscricao.objects.all()
    paginator = Paginator(inscricoes_list, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        inscricao = paginator.page(page)
    except(EmptyPage, InvalidPage):
        inscricao = paginator.page(paginator.num_pages)
    return render_to_response('lista.html',
                              {'inscricao': inscricao})
