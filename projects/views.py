from django.shortcuts import render

# Create your views here.
def projects(request):
    print("PAGINA PROJETOS")
    return render(request, 'projects/index.html')