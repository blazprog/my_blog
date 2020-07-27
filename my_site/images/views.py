from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Image


def image_list(request):
    images = Image.objects.all()
    return render(request, 'images/images.html', {
        'images': images
    })


def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'images/image.html', {"image": image})


def image_next(request, pk):
    next_image = Image.objects.filter(id__gt=pk)
    if next_image:
        next_image = next_image[0]
    else:
        next_image = get_object_or_404(Image, pk=pk)

    return render(request, 'images/image.html', {"image": next_image})


def image_previous(request, pk):
    previous_image = Image.objects.filter(id__lt=pk)
    if previous_image:
        previous_image = previous_image[len(previous_image)-1]
    else:
        previous_image = get_object_or_404(Image, pk=pk)

    return render(request, 'images/image.html', {"image": previous_image})
