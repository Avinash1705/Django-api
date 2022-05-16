from dataclasses import field, fields
from rest_framework import serializers

from webapp.models import emplyoees


class employeesSerializer(serializers.ModelSerializer):

    # class class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames'
    class Meta:
        model = emplyoees
        fields = ('firstname','lastname')
        # fields = '_all_' 