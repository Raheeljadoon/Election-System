from django.forms import ModelForm
from .models import Votes , Candidates
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Field,
    Submit,
)


class ElectionForms(ModelForm):
    class Meta:
        model = Votes
        fields = '__all__'


class CandidateForm(ModelForm):

    class Meta:
        model = Candidates
        fields = '__all__'
       

        
