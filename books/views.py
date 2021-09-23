from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Author
from .forms import AuthorForm

# Create your views here.

#Home application
def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))

#Authors page
def authors(request):
    autores = Author.objects.all()
    template = loader.get_template('books/authors.html')
    context = {'autores':autores,}
    return HttpResponse(template.render(context,request))

#Crete Autor Page
def new_author(request):
    #Se ejecuta cuando el usuario envía el formulario con los datos.
    if request.method == 'POST':
        #Crea una instancia de un autor.
        form = AuthorForm(request.POST)
        #Evaluamos si el formulario es correcto lo guardamos y redireccionamos        
        if form.is_valid():
            #Obtenemos los datos del formulario
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']
            pais = form.cleaned_data['country']
            author = Author(first_name=nombre,last_name=apellido,country=pais)
            author.save()
            return HttpResponseRedirect(reverse('authors'))

    else:
        #se ejecuta cuando el usuario va a llenar el formulario
        form =  AuthorForm()
    
    return render(request, 'books/create_authors.html', {'form':form})

#Index books page
def index(request):
    template = loader.get_template('books/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
