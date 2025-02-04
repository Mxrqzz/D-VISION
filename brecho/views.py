from django.shortcuts import render


# Create your views here.
def brecho(request):
    print("pagina brecho")
    context = {"title": "Brecho", "page": "Brecho"}
    return render(request, "brecho/index.html", context)
