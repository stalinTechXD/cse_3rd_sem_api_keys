from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.views.generic import View
from rest_framework.parsers import JSONParser
from testapp.models import Student
from testapp.serializers import StudentSerializer
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#@method_decorator(csrf_exempt,name='dispatch')
class StudentCrud(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  #  authentication_classes=[TokenAuthentication,]
    #permission_classes = [IsAuthenticated,]









#    def get(self,request,*args,**kwargs):
 #       json_data = request.body
#        stream = io.BytesIO(json_data)
#        pdata = JSONParser().parse(stream)
 #       id = pdata.get('id',None)
  #      if id is not None:
   #         emp = Student.objects.get(id = id)
    #        serializer = StudentSerializer(emp)
     #       json_data= JSONRenderer().render(serializer.data)
      #      return HttpResponse(json_data,content_type='applicaion/json') 
       # qs = Student.objects.all()
        #serializer = StudentSerializer(qs,many = True)
        #json_data= JSONRenderer().render(serializer.data)
       # return HttpResponse(json_data,content_type='applicaion/json')     


   # def post(self,request,*args,**kwargs):
    #    json_data = request.body
     #   stream = io.BytesIO(json_data)
      #  pdata = JSONParser().parse(stream)      
       # serializer = StudentSerializer(data = pdata)
      # if serializer.is_valid():
        #   serializer.save()
   #         msg = {'msg':'resource crereatd successfully'}
    #      json_data = JSONRenderer().render(msg)
     #       return HttpResponse(json_data,content_type='applicaton/json')
         
      #  json_data = JSONRenderer().render(serializer.errors)
       # return HttpResponse(json_data,content_type='applicaton/json',status = 400)          


    #def put(self,request,*args,**kwargs):
     #   json_data = request.body
      #  stream = io.BytesIO(json_data)
       # pdata = JSONParser().parse(stream)  
        #id = pdata.get('id')
        #emp = Student.objects.get(id=id)
        #serializer = StudentSerializer(emp,data = pdata,partial =True)     
        #if serializer.is_valid()  :
         #   serializer.save()  
          #  msg = {'msg':'resource update successfully'}
           # json_data = JSONRenderer().render(msg)
            #return HttpResponse(json_data,content_type='applicaton/json')
         
       # json_data = JSONRenderer().render(serializer.errors)
       # return HttpResponse(json_data,content_type='applicaton/json',status = 400)  

   # def delete(self,request,*args,**kwargs)    :
    #    json_data = request.body
     #   stream = io.BytesIO(json_data)
      #  pdata = JSONParser().parse(stream)  
       # id = pdata.get('id')
        #emp = Student.objects.get(id=id)        
        #emp.delete()
        #msg = {'msg':'resource deleted  successfully'}
        #json_data = JSONRenderer().render(msg)
        #return HttpResponse(json_data,content_type='applicaton/json')        




