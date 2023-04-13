from django.forms import forms


class GalleryUploadFrom(forms.Form):
    image = forms.FileField()
