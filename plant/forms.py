from django import forms
from plant.models import *
class EmployeeRegistr(forms.Form):
    name = forms.CharField(max_length=50, label= 'ФИО:')
    position = forms.CharField(max_length=50, label= 'Должность:')
    boss = forms.BooleanField(label='Руководитель:', required=False)
    # brigade = forms.ChoiceField(choices=[(b.id, b.name) for b in Brigade.objects.all()], label='Бригада:')
    # .values_list('name', flat=True)
    # brigade = forms.ModelChoiceField(queryset=Brigade.objects.all().values_list('name', flat=True), label='brigade')
    brigade = forms.CharField(max_length=50, label= 'Бригада:')
