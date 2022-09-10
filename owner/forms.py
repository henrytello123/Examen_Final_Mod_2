from django.forms import ModelForm
from .models import Owner
from django import forms


class OwnerForm(ModelForm):
   class Meta:
       model = Owner
       fields = '__all__'