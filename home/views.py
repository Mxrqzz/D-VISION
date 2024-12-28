from django.shortcuts import render


# Create your views here.
def home(request):
    print("pagina home")
    context = {"page": "Home"}
    return render(request, "home/index.html", context)
