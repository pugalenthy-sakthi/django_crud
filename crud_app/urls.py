from django.urls import path
from .views import UserCrud,updateuser,deleteuser

urlpatterns = [
  path(route='',view=UserCrud.as_view(),name='class_based_view'),
  path(route = 'update',view=updateuser,name='method_based_view'),
  path(route='delete/<str:email>',view=deleteuser,name='decorator_based-view')
]