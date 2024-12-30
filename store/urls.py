from django.urls import path
from store import views
from store.views import Index
from store.checkout import CheckOut
from store.orders import OrderView


urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('cart/',views.cart,name='cart'),
    path('check-out',CheckOut.as_view(),name="checkout"),
    path('orders',OrderView.as_view(),name="checkout"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
]