from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Pessoal
from .form import formulario

@login_required
def buscaNome(nome):
    lista = [
        {'nome':'Ana', 'idade':15},
        {'nome': 'Joao', 'idade': 18},
        {'nome':'Andre', 'idade':11}
    ]
    for i in lista:
        if i['nome'] == nome:
            return i
    else:
        return "Nao localizado."
@login_required
def nomebanco(request, nome):
    a = buscaNome(nome)
    return HttpResponse(a)
@login_required
def hello(request):
    return render(request, 'HELLO.html')
@login_required
def person_list(request):
    return render(request, "HELLO.html")
@login_required
def person_lista(request):
    lista = Pessoal.objects.all()
    return render(request, 'person.html', {'lista':lista, 'tamanho':len(lista)})
@login_required
def person_new(request):
    form = formulario(request.POST or None, request.FILES or None) #request.FILES é novo, para upload de arquivo

    if form.is_valid():
        form.save()
        return redirect("person_lista")

    return render(request, 'person_form.html', {'form': form})
@login_required
def update_person(request, id):
    person = get_object_or_404(Pessoal, pk=id)
    form = formulario(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect("person_lista")

    return render(request, 'person_form.html', {'form':form})
@login_required
def delete_person(request, id):
    person = get_object_or_404(Pessoal,pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_lista')

    return render(request, 'person_delete_confirm.html', {'person':person})






