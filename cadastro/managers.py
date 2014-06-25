# -*- coding: utf-8 -*-
from django.db import models


class ClientesManager(models.Manager):

    def get_queryset(self):
        qs = super(ClientesManager, self).get_queryset()
        qs = qs.objects.with_counts()
        return qs
