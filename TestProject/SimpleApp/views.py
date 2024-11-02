from django.shortcuts import render, get_object_or_404, redirect
from .models import SimpleModel
from django.urls import reverse
from .forms import SimpleModelForm

def model_list_view(request):
    objects = SimpleModel.objects.all()
    return render(request, 'SimpleApp/model_list.html', {'objects': objects})

def model_update_view(request, pk):
    obj = get_object_or_404(SimpleModel, pk=pk)
    form = SimpleModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('model_list')
    return render(request, 'SimpleApp/model_form.html', {'form': form})

def model_delete_view(request, pk):
    obj = get_object_or_404(SimpleModel, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('model_list')
    return render(request, 'SimpleApp/model_confirm_delete.html', {'object': obj})
