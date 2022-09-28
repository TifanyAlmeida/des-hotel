from gc import get_objects
from django.shortcuts import render, get_object_or_404
from .models import Hospedadore, Hospedagen, Recurso

def mostrar_home(request):
    banco_hotel = Hospedagen.objects.all()
    context = {
        'hospedagem':banco_hotel
    }
    return render(request, 'home/index.html', context)

def detalhes(request, id):
    det_hotel = get_object_or_404(
        Hospedagen, id=id
    )
    det_hospedador = get_object_or_404(
        Hospedadore, id=id
    )
    det_recursos = get_object_or_404(
        Recurso, id=id
    )
    return render(request,'home/detalhes.html', {'detalhes':det_hotel, 'detalhes_hosped':det_hospedador, 'detalhes_recursos':det_recursos})