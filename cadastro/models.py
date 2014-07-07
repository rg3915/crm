# -*- coding: utf-8 -*-
from django.db import models


class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ['criado_em']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')

    def __unicode__(self):
        return self.nome

    def _get_dobro_idade(self):
        return self.idade * 2
    dobro_idade = property(_get_dobro_idade)
