from django.contrib import admin
from testapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','math','ddt','dat','ca','dm','op','dd','da','es']

admin.site.register(Student,StudentAdmin)    