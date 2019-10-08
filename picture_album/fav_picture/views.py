from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import FavPictureModel
from .forms import FavEntryForm
from . import forms


# Create your views here.
def index(req):
    pix = FavPictureModel.objects.all()

    return render(req, 'fav_picture/home.html', {'pix': pix})

def view_fav(req,pk):
    pix = get_object_or_404(FavPictureModel,pk=pk)
    print(pix)

    return render(req, 'fav_picture/view.html', {'pix': pix})

def add_fav(req):
    form = FavEntryForm(req.POST or None)  # Preload data if post, otherwise blank
    if req.method == 'POST':
        if form.is_valid():
            # save form
            form.save(commit=True)


    return render(req, 'fav_picture/add.html', {'form': form})
