from django.shortcuts import render, get_object_or_404
from .models import Credits
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.core.paginator import Paginator


# Create your views here.
def albums(request):
    rec = Credits.objects.order_by('artist')
    return render(request, 'record/albums.html', {
        'rec': rec
    })


def credits(request, credits_id):
    # cred = Credits.objects.get(id=credits_id)
    cred = get_object_or_404(Credits, id=credits_id)
    return render(request, 'record/credits.html', {
    'cred': cred
    })


def find(request):
    term = request.GET.get('term')
    albums = Credits.objects.order_by('artist').filter(
        Q(artist__icontains=term),
        show=True
    )
    
    return render(request, 'record/find.html',{
        'albums':albums
    })