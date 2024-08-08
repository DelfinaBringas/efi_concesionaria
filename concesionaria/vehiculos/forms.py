from django import forms
from.models import Vehiculo,Marca,Modelo,Tipo_combustible,Pais_fabricacion,Comentario,Proveedor

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca','modelo','cantidad_puertas','cilindrada','tipo_combustible','pais_fabricacion','precio_dolares','color']

        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'modelo': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'cant_puertas': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),               
            'cilindrada': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),
            'combustible': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'pais_fabricacion': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'precio_en_dolares': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),
            'color': forms.Select(attrs={'class': 'form-control custom-class'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['vehiculo', 'author', 'texto']
        
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-control custom-class'}),
            'author': forms.Select(attrs={'class': 'form-control custom-class'}),
            'texto': forms.Textarea(attrs={'class': 'form-control custom-class', 'rows': 5}),
        }