from django.urls import path
from . import views

urlpatterns = [
    path('', views.CallListView.as_view(), name='call_list'),
    path('<int:pk>/', views.CallDetailView.as_view(), name='call_detail'),
    path('create/', views.CallCreateView.as_view(), name='call_create'),
    path('<int:pk>/update/', views.CallUpdateView.as_view(), name='call_update'),
    path('<int:pk>/delete/', views.CallDeleteView.as_view(), name='call_delete'),
]