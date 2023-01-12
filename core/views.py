from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request, nome: str) -> HttpResponse:
    return HttpResponse(f'<h1>Hello {nome}!</h1>')


def add(request, x: int, y: int) -> HttpResponse:
    return HttpResponse(f'<h1>A soma {x}+{y} resulta em {x+y}.</h1>')


def sub(request, x: int, y: int) -> HttpResponse:
    return HttpResponse(f'<h1>A subtração {x}-{y} resulta em {x-y}.</h1>')


def mul(request, x: int, y: int) -> HttpResponse:
    return HttpResponse(f'<h1>A multiplicação {x}x{y} resulta em {x*y}.</h1>')


def div(request, x: int, y: int) -> HttpResponse:
    return HttpResponse(f'<h1>A divisão {x}/{y} resulta em {x/y}.</h1>')
