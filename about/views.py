from django.shortcuts import render

# Create your views here.
def about(request):
    print('pagina about')
    context = {"title": "Sobre nós", "page": "Sobre nós"}
    return render(request, "about/index.html", context)
