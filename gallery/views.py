from django.shortcuts import render

# Create your views here.

def gallery(request):
    print("PAGINA GALERIA")
    return render(request, 'gallery/gallery.html')