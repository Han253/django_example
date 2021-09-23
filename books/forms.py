from django import forms

from .models import Author

"""-------------------------------------------------------------------####
Formulario para cargar de Autores                                           ]
###--------------------------------------------------------------------"""
class AuthorForm(forms.ModelForm):

	class Meta:
		model = Author

		fields = [
			'first_name',
			'last_name',
			'country',
		]
		labels = {
			'first_name':'Nombre',
			'last_name':'Apellidos',
			'country':'Pais',
		}
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control','required':''}),
            'last_name': forms.TextInput(attrs={'class':'form-control','required':''}),
            'country': forms.TextInput(attrs={'class':'form-control','required':''}),
		}
