from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('uj_edesseg/', views.edessegUpload, name = 'edesseg-upload'),
    path('edesseg_modositasa/<int:id>/', views.edessegUpdate, name = 'edesseg-update'),
    path('edesseg_torlese/<int:id>/', views.edessegUpdate, name = 'edesseg-delete'),

    path('edesseg/<int:id>/', views.edessegDetail, name = 'edesseg-detail')
]
