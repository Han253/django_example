from django.http.response import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
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

#Author detail page
def detail_author(request,author_id):   
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404("Author doesn't exist.")
    return render(request,'books/author_detail.html',{'author':author})


#Create Autor Page
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


#Update Autor Page
def update_author(request,author_id):

    #Diccionario con los datos iniciales
    context = {}
    #buscar el author en base de datos.
    author = get_object_or_404(Author, pk = author_id)

    #Pasar el objeto a una instancia del formulario. 
    form = AuthorForm(request.POST or None, instance=author)

    #Guardar los datos y redirigir a la página de authores.
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('authors'))
    
    #Agregar el formulario al contexto
    context["form"] = form
    
    return render(request, 'books/update_author.html', {'form':form})


#Delete Autor Page
def delete_author(request,author_id):

    #Diccionario con los datos iniciales
    context = {}
    #buscar el author en base de datos.
    author = get_object_or_404(Author, pk = author_id)

    if request.method == "POST":
        #eliminar author
        author.delete()
        #redireccionar a pagina de autores
        return HttpResponseRedirect(reverse('authors'))
    
    #Agregar el formulario al contexto
    context["author"] = author
    
    return render(request, 'books/delete_author.html', context)

#Index books page
def index(request):
    template = loader.get_template('books/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
