from django.shortcuts import render

# Create your views here.
def shop(request):
    print("PAGINA SHOP")
    return render(request, 'shop/index.html')