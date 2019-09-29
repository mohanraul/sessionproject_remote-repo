from django import forms

class nameform(forms.Form):
    name=forms.CharField()

class salform(forms.Form):
    salary=forms.IntegerField()

class Qualificationform(forms.Form):
    qualification=forms.CharField()
