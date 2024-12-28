from django.shortcuts import render

# Create your views here.

def gallery(request):
    print("pagina gallery")
    context = {"title": "Gallery", "page": "Galeria"}
    return render(request, "gallery/gallery.html", context)
