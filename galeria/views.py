from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request,"Usuário não logado")
        return redirect('login')
    # Código responsavel para restringir quem não tem login
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    # Esses varios metodos, ordenam e mostram na pagina html cada instancia de acordo com oque quero
    return render (request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})
    # Esse código todo faz retornar a foto especifica do card especifico

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,"Usuário não logado")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})