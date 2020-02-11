from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import ToDo
from django.utils import timezone
# Create your views here.


def index(request):
    if request.method == 'POST':
        content = request.POST['content']
        item = ToDo(content=content, date_added=timezone.now())
        item.save()
    items = ToDo.objects.all()

    return render(request, 'main/index.html', {'list_items': items})


def delete(request, item_id):
    obj = ToDo.objects.get(pk=item_id)
    obj.delete()
    return HttpResponseRedirect(reverse('main:index'))






