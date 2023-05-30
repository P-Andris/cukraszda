from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from .models import Kategoria, Edesseg
from .forms import EdessegForm
from .filters import EdessegFilter

def index(request):
    edessegek = Edesseg.objects.all()

    edessegFilter = EdessegFilter(request.GET, queryset = edessegek)

    context = {
        'edessegek': edessegek,
        'edessegFilter': edessegFilter
    }

    return render(request, 'index.html', context = context)

def edessegDetail(request, id):
    edesseg = list(Edesseg.objects.filter(Q(edesseg_azon__exact = id)).values())
    return JsonResponse(edesseg, safe = False)

def edessegUpload(request):
    form = EdessegForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    else:
        form = EdessegForm()

    context = {
        'form': form
    }

    return render(request, 'upload.html', context = context)

def edessegUpdate(request, id):
    edesseg = get_object_or_404(Edesseg, pk = id)
    form = EdessegForm(request.POST or None, instance = edesseg)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    
    context = {
        'form': form
    }

    return render(request, 'update.html', context = context)

def edessegDelete(request, id):
    edesseg = get_object_or_404(Edesseg, pk = id)
    edesseg.delete()
    return redirect(index)