from gc import get_objects
from django.shortcuts import render, get_object_or_404
from .models import Hospedagen

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
    return render(request,'home/detalhes.html', {'detalhes':det_hotel})