from django.urls import path
from . import views
from .views import ProductCreateView, ProductListView, ProductDetailView, OrderListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# #set namespace
app_name = 'productAdd'

urlpatterns = [
    path('add',views.ProductCreateView.as_view(), name='addproducts'), 
    path('listproducts/',views.ProductListView.as_view(), name='listproducts'),
    path('listorder/',views.OrderListView.as_view(), name='order_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='cart_detail'),  
    path('cart/',views.addtoCart, name='addtoCart'),
    # path('search/',views.search_product, name='search_product'),
    # path('removeFromCart/',views.removeFromCart, name='removeFromCart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 