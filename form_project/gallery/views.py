from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadFrom
from .models import Gallery
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'

# def storage_file(file):
#     with open(f'gallery_tmp/{file.name}.jpg', 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)
class CreateGalleryView(CreateView):
    model = Gallery
    template_name = 'gallery/load_file.html'
    fields = '__all__'
    success_url = 'load_img'

# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadFrom()
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = GalleryUploadFrom(request.POST, request.FILES)
#         if form.is_valid():
#             new_img = Gallery(image=form.cleaned_data['image'])
#             new_img.save()
#             return HttpResponseRedirect('load_img')
#         return render(request, 'gallery/load_file.html', {'form': form})
#


# Create your views here.
