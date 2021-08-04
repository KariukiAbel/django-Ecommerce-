from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'products/products.html')

def product_details_view(request):
    # context = {}
    return(request, 'products/details.html')
