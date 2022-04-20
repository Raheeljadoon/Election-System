from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('a',views.elections, name='elections'),
    path('', views.updates_votes, name='candidate-name'),
    path('register', views.register, name='candidate-register'),
    path('submit',views.submit, name='submit_vootes')


]