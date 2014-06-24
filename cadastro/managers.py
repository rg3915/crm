# -*- coding: utf-8 -*-
from django.db import models


class ClientesManager(models.Manager):

    def get_query_set(self):
        qs = super(ClientesManager, self).get_query_set()
        qs = qs.objects.with_counts()
        return qs
