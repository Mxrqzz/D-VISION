from django.shortcuts import render


# Create your views here.
def projects(request):
    print("pagina projects")
    context = {"title": "Projetos", "page": "Projetos"}
    return render(request, "projects/index.html", context)
