from django.urls import include, path

from myContact import views

urlpatterns = [
    path('form1/', views.controleform1, name='form1'),
    path('form2/', views.controleform2, name='form2'),
    path('form3/', views.controleform3, name='form3'),
]