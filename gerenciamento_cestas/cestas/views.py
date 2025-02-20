from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InstituicaoForm, DoadorForm, CestaBasicaForm
from .models import Instituicao, Doador, CestaBasica

def home(request):
    return render(request, 'home.html')

@login_required
def lista_instituicoes(request):
    instituicoes = Instituicao.objects.all()
    return render(request, 'cestas/lista_instituicoes.html', {'instituicoes': instituicoes})

@login_required
def lista_doadores(request):
    doadores = Doador.objects.all()
    return render(request, 'cestas/lista_doadores.html', {'doadores': doadores})

@login_required
def lista_cestas(request):
    cestas = CestaBasica.objects.all()
    return render(request, 'cestas/lista_cestas.html', {'cestas': cestas})

@login_required
def criar_instituicao(request):
    if request.method == 'POST':
        form = InstituicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_instituicoes')
    else:
        form = InstituicaoForm()
    return render(request, 'cestas/criar_instituicao.html', {'form': form})

@login_required
def criar_doador(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_doadores')
    else:
        form = DoadorForm()
    return render(request, 'cestas/criar_doador.html', {'form': form})

@login_required
def criar_cesta(request):
    if request.method == 'POST':
        form = CestaBasicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cestas')
    else:
        form = CestaBasicaForm()
    return render(request, 'cestas/criar_cesta.html', {'form': form})