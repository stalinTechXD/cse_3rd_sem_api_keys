from rest_framework import serializers
from testapp.models import Student

   # name = serializers.CharField(max_length=64)
   # daa =  serializers.IntegerField()
   # os = serializers.IntegerField()
   # fafl=serializers.IntegerField()
   # math4=serializers.IntegerField()
   # se = serializers.IntegerField()
   # mpmc=serializers.IntegerField()    
   # def create(self,validated_data):
    #    return  Student.objects.create(**validated_data)
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields = '__all__'

    def validate_ca(self,value):
       if value  < 50:
          raise serializers.ValidationError('daa marks should be more than 78')
       return value    
    
    def validate_ddt(self,value):
       if value  < 50:
          raise serializers.ValidationError('daa marks should be more than 78')
       return value   
    def validate_dd(self,value):
        if value  < 50:
          raise serializers.ValidationError('daa marks should be more than 78')
        return value   
    def validate_da(self,value):
        if value  < 50:
            raise serializers.ValidationError('daa marks should be more than 78')
        return value      
    
   #def create(self,validated_data):
    #   return  Student.objects.create(**validated_data)       



    #def validate(self,data):
    #    name = data.get('name')
     #   daa = data.get('daa')
      #  if name.lower() == 'stalin':
       #         if daa<78:
        #            raise serializers.ValidationError('rayan marks  should be more then 78')
        #return data        

   # def update(self,instance,validated_data):
       # instance.name = validated_data.get('name',instance.name)    
       # instance.daa = validated_data.get('daa',instance.daa) 
       # instance.os = validated_data.get('os',instance.os) 
       #instance.math4 = validated_data.get('math4',instance.math4) 
       # instance.se = validated_data.get('se',instance.se) 
       # instance.mpmc = validated_data.get('mpmc',instance.mpmc) 
       # instance.save()
       # return instance
