from django.urls import path
from . import views

urlpatterns = [ 
   path('register/', views.RegisterView.as_view(), name='register'),
   path('me/', views.RetrieveUserView.as_view(), name='get user')
]