from django.shortcuts import render

# Create your views here.
def about(request):
    print("PAGINA SOBRE")
    return render(request, 'about/index.html')
