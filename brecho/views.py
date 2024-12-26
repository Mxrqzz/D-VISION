from django.shortcuts import render

# Create your views here.
def brecho(request):
    print("PAGINA BRECHO")
    return render(request,  'brecho/index.html')
