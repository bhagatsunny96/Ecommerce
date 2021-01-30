from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views


app_name = "ecom"
urlpatterns = [
    # Client side pages
    path("", HomeView.as_view(), name="home"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact-us/", ContactView.as_view(), name="contact"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),

    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),

    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("stripe-request/", StripeRequestView.as_view(), name="striperequest"),

    path("register/",
         CustomerRegistrationView.as_view(), name="customerregistration"),

    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),

    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),

    path("search/", SearchView.as_view(), name="search"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html", success_url = reverse_lazy('ecom:password_reset_done')), name="password_reset"),
    path("password_reset_sent/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('ecom:password_reset_complete')), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),

    
    # Admin Side pages

    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),

    path("admin-order-<int:pk>-change/",
         AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),

    path("admin-product/list/", AdminProductListView.as_view(),
         name="adminproductlist"),
    path("admin-product/add/", AdminProductCreateView.as_view(),
         name="adminproductcreate"),
     path("admin-pending-orders/", AdminPendingOrderView.as_view(), name="adminpendingorder"),
     path("admin-all-users/", AdminAllUserView.as_view(),name="adminallusers"),
     path("logoutadmin/", AdminLogoutView.as_view(), name="adminlogout"),


]
