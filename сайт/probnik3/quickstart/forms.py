from .models import BankClients, BankWorkers, InvestType, MoneyCourse, InvestRegist
from django.forms import ModelForm, TextInput

class bankClientsForm(ModelForm):
    class Meta:
        model = BankClients
        fields = ['surname','name','secondName']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Имя'
            }),
            "secondName": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Отчество'
            })
        }
    
class bankWorkersForm(ModelForm):
    class Meta:
        model = BankWorkers
        fields = ['surname','name','secondName','job', 'salary']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Имя'
            }),
            "secondName": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Отчество'
            }),
            "job": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Должность'
            }),
            "salary": TextInput(attrs={
                'class':'form',
                'placeholder': 'Зарплата'
            })
        }

class investTypeForm(ModelForm):
    class Meta:
        model = InvestType
        fields = ['name','minTime','minAmount','code','percent']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Название'
            }),
            "minTime": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Время возврата'
            }),
            "minAmount": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Кол-во'
            }),
            "code": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Код'
            }),
            "percent": TextInput(attrs={
                'class':'form',
                'placeholder': 'Процент'
            })
        }

class moneyCourseForm(ModelForm):
    class Meta:
        model = MoneyCourse
        fields = ['name','course']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Валюта'
            }),
            "course": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Курс'
            })
        }

class investRegistForm(ModelForm):
    class Meta:
        model = InvestRegist
        fields = ['client','code','dateIn','dateOut','amount','status','worker']

        widgets = {
            "client": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Клиент'
            }),
            "code": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Код'
            }),
            "dateIn": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Дата вноса'
            }),
            "dateOut": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Дата выдачи'
            }),
            "amount": TextInput(attrs={
                'class':'form',
                'placeholder': 'Сумма'
            }),
            "status": TextInput(attrs={
                'class':'form',
                'placeholder': 'Статус'
            }),
            "worker": TextInput(attrs={
                'class':'form',
                'placeholder':'Работник'
            })
        }