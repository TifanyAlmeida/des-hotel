from gc import get_objects
from django.shortcuts import render, get_object_or_404
from .models import Hospedadore, Hospedagen, Recurso, Endereco

def mostrar_home(request):
    banco_hotel = Hospedagen.objects.all()
    context = {
        'hospedagem':banco_hotel
    }
    return render(request, 'home/index.html', context)

def detalhes(request, pk):
    det_hotel = get_object_or_404(
        Hospedagen, id=pk
    )
    det_hospedador = get_object_or_404(
        Hospedadore, id=pk
    )
    det_recursos = get_object_or_404(
        Recurso, id=pk
    )
    det_endereco = get_object_or_404(
        Endereco, id=pk
    )
    return render(request,'home/detalhes.html', {'detalhes':det_hotel, 'detalhes_hosped':det_hospedador, 'detalhes_recursos':det_recursos, 'detalhes_endereco':det_endereco})