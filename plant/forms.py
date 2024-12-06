from django import forms
class EmployeeRegistr(forms.Form):
    name = forms.CharField(max_length=50, label= 'ФИО:')
    position = forms.CharField(max_length=50, label= 'Должность:')
    boss = forms.BooleanField(label= 'Руководитель:')
    # activ = forms.BooleanField(label= 'Должность:')
    brigade = forms.CharField(max_length=50, label= 'Бригада:')
    # age = forms.IntegerField(min_value=18,max_value=103, label="Введите свой возраст:")