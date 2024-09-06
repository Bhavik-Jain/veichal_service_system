from django.urls import path
from .views import (
    ComponentList,
    ComponentDetail,
    VehicleList,
    VehicleDetail,
    IssueList,
    IssueDetail,
    TransactionList,
    TransactionDetail
)

urlpatterns = [
    path('api/components/', ComponentList.as_view(), name='component-list'),
    path('api/components/<int:pk>/', ComponentDetail.as_view(), name='component-detail'),
    
    path('api/vehicles/', VehicleList.as_view(), name='vehicle-list'),
    path('api/vehicles/<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
    
    path('api/issues/', IssueList.as_view(), name='issue-list'),
    path('api/issues/<int:pk>/', IssueDetail.as_view(), name='issue-detail'),
    
    path('api/transactions/', TransactionList.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
]
