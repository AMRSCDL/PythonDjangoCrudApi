from django import forms
from CRUDAPP.models import kullanici
class kullaniciForm(forms.ModelForm):
    class Meta:
        model = kullanici
        fields = ['name','email','contact']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
       