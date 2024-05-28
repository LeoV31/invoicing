from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('investors/', views.investor_list, name='investor-list'),
    path('investor/<int:pk>/', views.investor_detail, name='investor-detail'),
    path('investments/', views.investment_list, name='investment-list'),
    path('investment/<int:pk>/', views.investment_detail, name='investment-detail'),
    path('bills/', views.bill_list, name='bill-list'),
    path('bill/<int:pk>/', views.bill_detail, name='bill-detail'),
    path('grouped-bills/', views.grouped_bills_view, name='grouped-bills'),
    path('cashcalls/', views.cashcall_list, name='cashcall-list'),
    path('cashcall/<int:pk>/', views.cashcall_detail, name='cashcall-detail'),
]
