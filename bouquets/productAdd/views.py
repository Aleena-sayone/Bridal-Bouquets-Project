from django.shortcuts import render
from productAdd.forms import ProductForm
from .models import Product, Order
from user.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
class ProductCreateView(CreateView):
        model = Product        
        template_name = 'productAdd/addnew.html'
        form_class = ProductForm #it is a variable so don't use quotes.
        success_url = '../'

class OrderListView(ListView):
    model = Order
    template_name = '/productAdd/order_list.html'  # <app>/<model>_<viewtype>.html
    queryset = Order.objects.all()
    context_object_name = 'order_list'

    def get_queryset(self):
        # if (productAdd.Product not None):
        # if(None not in Order.products.all()):
        return Order.objects.all()


class ProductListView(ListView):
    model = Product
    template_name = '/productAdd/product_list.html'  # <app>/<model>_<viewtype>.html
    queryset = Product.objects.all()
    context_object_name = 'Product_list'

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    # template_name = '/productAdd/product_detail.html'

# @login_required    
# def removeFromCart(request,):    
#     product =  get_object_or_404(Product, id=request.POST.get('product_id'))
#     add_cart = True
#     user = request.user
#     print(user)
#     profile = Profile.objects.get(user= user)
#     # *************************************
#     print(profile.cart.all())
#     print(user)
#     # *************************************
#     if(product in profile.cart.all()):
#         print("product removed from cart")
#         profile.cart.remove(product)
#         add_cart = False
#     else:
#         # print("product added to cart")
#         # profile.cart.add(product)
#         # add_cart= True
#         pass
#     # return redirect('productAdd:listproducts')
#     return HttpResponseRedirect(product.get_absolute_url())

# def search_product(request):
#     if(request.method == 'GET'):
#         item = request.Get('search')
#         search_item = Product.req
@login_required    
def addtoCart(request,):    
    product =  get_object_or_404(Product, id=request.POST.get('product_id'))
    add_cart = False
    user = request.user
    print(user)
    profile = Profile.objects.get(user= user)
    # *************************************
    print(profile.cart.all())
    print(user)
    # *************************************
    if(product in profile.cart.all()):
        pass
        # print("product removed from cart")
        # profile.cart.remove(product)
        # add_cart = False
    else:
        print("product added to cart")
        profile.cart.add(product)
        add_cart= True
    # return redirect('productAdd:listproducts')
    return HttpResponseRedirect(product.get_absolute_url())
    




