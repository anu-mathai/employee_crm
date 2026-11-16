from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from accounts.models import Employee
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreateView(View):

    def get(self,request):

        qs = Employee.objects.all().values()
        #qs is a queryset json only support python native type

        response_data = list(qs)

        return JsonResponse(response_data,safe=False)

    def post(self,request):
        form_data = loads(request.body)

        Employee.objects.create(**form_data)

        response_data = {"message":"created"}

        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeRetrieveUpdateDelete(View):

    def get(self,request,pk=None):

        instance = Employee.objects.filter(id=pk).values()

        response_data = list(instance)

        return JsonResponse(response_data,safe=False)
    
    def put(self,request,pk=None):

        form_data = loads(request.body)

        Employee.objects.filter(id=pk).update(**form_data)

        response_data = {"message":"updated...."}

        return JsonResponse(response_data)

    def delete(self,request,pk=None):

        Employee.objects.get(id=pk).delete()

        response_data = {"message":"deleted..."}

        return JsonResponse(response_data)

        