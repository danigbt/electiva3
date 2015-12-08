from django import forms
from models import Compra, Producto, Marca, Categoria


class CompraForm(forms.ModelForm):

	class Meta:
		model = Compra
		fields = ['usuario', 'email', 'tarjeta', 'direccion', 'telefono']
		widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required data-validation-required-message':'Ingrese su nombre.'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required data-validation-required-message':'Ingrese su email.'}),
        	'tarjeta' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tarjeta de credito', 'required data-validation-required-message':'Ingrese su tarjeta de credito.'}),
        	'direccion' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion', 'required data-validation-required-message':'Ingrese su direccion.'}),
        	'telefono' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono', 'required data-validation-required-message':'Ingrese su telefono.'}),
        }


class ProductoForm(forms.ModelForm):
	marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label="--Marca--", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Marca', 'required data-validation-required-message':'Seleccione la marca.'}))
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="--Categoria--", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria', 'required data-validation-required-message':'Seleccione la categoria.'}))
	imagen = forms.ImageField(required=False)

	class Meta:
		model = Producto
		fields = ['nombre', 'descripcion', 'imagen', 'marca', 'categoria', 'precio']
		widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required data-validation-required-message':'Ingrese el nombre del producto.'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion', 'required data-validation-required-message':'Ingrese la descripcion del producto.'}),
        	#'imagen' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagen', 'required data-validation-required-message':'Ingrese una imagen.'}),
        	# 'marca' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Marca', 'required data-validation-required-message':'Seleccione la marca.'}),
        	# 'categoria' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria', 'required data-validation-required-message':'Seleccione la categoria.'}),
        	'precio' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio', 'required data-validation-required-message':'Ingrese el precio del producto.'}),
        }
