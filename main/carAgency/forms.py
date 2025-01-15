from django.forms import ModelForm
from .models import Car, Client

class CreateCarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'