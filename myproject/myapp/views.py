from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Item

# Create your views here.

def item_list(request):
    object_list = Item.objects.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {'items': items}

    return render(request, 'item_list.html', context)