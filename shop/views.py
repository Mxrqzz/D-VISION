from django.shortcuts import render


# Create your views here.
def shop(request):
    print('pagina shop')
    context = {"title": "Shop", "page": "Shop"}
    return render(request, "shop/index.html", context)
