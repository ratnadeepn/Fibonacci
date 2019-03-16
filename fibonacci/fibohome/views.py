from django.shortcuts import render, redirect
from rest_framework.views import APIView
#from rest_framework.response import Response
import time
from fibohome.Calculation import CalcClass
from .serializers import HomeViewSerializer


class HomeView(APIView):

    template_name = 'fibohome/home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        value = request.POST['value']
        if value is '':
            return redirect('home')
        else:
            start_time = time.time()
            obj = CalcClass(value)
            result=obj.calculate()
            end_time = time.time() - start_time
            dictionary={}
            dictionary['result']=result
            dictionary['end_time']=end_time
            output=[]
            output.append(dictionary)
            results=HomeViewSerializer(output, many=True).data
            return render(request, 'fibohome/home.html', {'results':results[0]})


