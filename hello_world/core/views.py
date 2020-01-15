from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse(f'<h1>Hello {nome}</h1>')

def soma(request, n1, n2):
    return HttpResponse(f'A soma de {n1} mais {n2} é {n1+n2}')

def subtracao(request, n1, n2):
    return HttpResponse(f'A subtracao de {n1} menos {n2} é {n1-n2}')

def multiplicacao(request, n1, n2):
    return HttpResponse(f'A multiplicacao entre {n1} e {n2} é {n1*n2}')

def divisao(request, n1, n2):
    return HttpResponse(f'A divisao entre {n1} e {n2} é {n1/n2}')