from django import forms
from.models import Vehiculo,Marca,Modelo,Tipo_combustible,Pais_fabricacion,Comentario,Proveedor,ImagenAuto

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca','modelo','fabricado_el','cantidad_puertas','cilindrada','tipo_combustible','pais_fabricacion','precio_dolares','color']

        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'modelo': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'fabricado_el':forms.NumberInput(attrs={'class': 'form-control custom-class', 'placeholder': 'Año de Fabricación'}),
            'cantidad_puertas': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),               
            'cilindrada': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),
            'tipo_combustible': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'pais_fabricacion': forms.Select(attrs={'class': 'form-control  custom-class'}),
            'precio_dolares': forms.NumberInput(attrs={'class': 'form-control  custom-class'}),
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

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields= ['nombre','direccion','telefono']

        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'direccion':forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'telefono':forms.NumberInput(attrs={'class': 'form-control custom-class'}),
        }  

#DUDA:
class ImagenAutoForm(forms.ModelForm):
    class Meta:
        model = ImagenAuto
        fields = ['vehiculo', 'image', 'description']
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }