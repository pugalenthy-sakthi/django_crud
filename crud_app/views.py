from django.http import HttpRequest,JsonResponse
from django.views import View
from .models import User
from .forms import UserForm
import json
from .utils import hashing
from rest_framework.decorators import api_view
import traceback


class UserCrud(View):
  
  def get(self,request:HttpRequest):
    try:
      userlist = [
        {
          'name':user.name,
          'emai':user.email
        }
        for user in User.objects.all()
      ]
      print(userlist)
      return JsonResponse(data = {'data':userlist},status = 200)
    except Exception as e:
      print(e)
      return JsonResponse(data = {'error':'Internal Server Error'},status = 500)
  
  
  def post(self,request:HttpRequest):
    
    try:
      json_data = json.loads(request.body)    
      form_data = UserForm(json_data)     
      user = User()
      user.name = form_data.data['name']
      user.email=form_data.data['email']
      user.password=hashing.gethashpwd(form_data.data['password']).decode('utf-8')
      user.save()
      return JsonResponse(data={'message':'CREATED'},status =201)
    except json.JSONDecodeError:
      return JsonResponse(data={'error':"Invalid Data"},status = 400)
    except Exception :
      return JsonResponse(data={'error':"Internal Server Error"},status = 500)
    
    
def updateuser(request):
  if request.method == 'PUT':
    try:
      json_data = json.loads(request.body)    
      form_data = UserForm(json_data)     
      user = User.objects.filter(email= form_data.data['email']).first()
      if user is None:
        return JsonResponse(data={'mesage':'data not found'},status = 404)
      user.name = form_data.data['name']
      user.password=hashing.gethashpwd(form_data.data['password']).decode('utf-8')
      user.save()
      return JsonResponse(data={'message':'UPDATED'},status =200)
    except json.JSONDecodeError:
        return JsonResponse(data={'error':"Invalid Data"},status = 400)
    except Exception as e:
      traceback.print_exception(e)
      return JsonResponse(data={'error':"Internal Server Error"},status = 500)

@api_view(['DELETE'])
def deleteuser(request,email):
  try:
    user = User.objects.filter(email = email).first()
    user.delete()
    return JsonResponse(data={'message':'DELETED'},status =200)
  except Exception :
    return JsonResponse(data={'error':"Internal Server Error"},status = 500)
    
  