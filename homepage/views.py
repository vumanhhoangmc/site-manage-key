from django.shortcuts import render
from time import sleep
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seriakizers import ResponseKey, SendDataKey
from django.utils import timezone, dateformat
from .forms import KeyManage
from .models import Managekey
from datetime import date
# Create your views here.

class ClassLogin(View):
    def get(self, request):
        return render(request, 'homepage/login.html')        

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse('Taì khoản không tồn tại')
            # return redirect('/')
        else:    
            login(request, my_user)        
            return redirect('/')


class ManageHome(LoginRequiredMixin, View):
    login_url = "login/"
    def get(self, request):
        f = KeyManage()
        context = {'formskey': f}
        return render(request, 'homepage/managehome.html', context)


class AddKey(LoginRequiredMixin, View):
    login_url = 'login/'
    def post(self, request):
        f = KeyManage(request.POST)
        if not f.is_valid():
            return HttpResponse("Không thể add key, chưa input đủ yêu cầu !")
        else:
            f.save()
            return HttpResponse('ADD Thành Công.')   


class ViewAPIKey(APIView):
    def get(self, request):
        return HttpResponse('Site Manage Key By Hoangdzsvip, Mua key lien he zalo 0338643708')

    def post(self, request):
        data_send = SendDataKey(request.data)
        # if not data_send.is_valid():
        #     return Response('false', status=status.HTTP_400_BAD_REQUEST)
        # else:    
        key_in_data_send = data_send.data['keytool']
        tool_in_data_send = data_send.data['tool']
        try:
            check_key = Managekey.objects.filter(key=key_in_data_send, tool=tool_in_data_send)
            ngay_het_han = check_key[0].expiration_date.split('-')
            ngay_hien_tai = dateformat.format(timezone.datetime.now(), 'Y-m-d').split('-')
            date1 = date(int(ngay_hien_tai[0]), int(ngay_hien_tai[1]), int(ngay_hien_tai[2]))
            date2 = date(int(ngay_het_han[0]), int(ngay_het_han[1]), int(ngay_het_han[2]))
            date3 = date2 - date1
            hsd = date3.days
            if hsd <= 0:
                hsd = 0
            else:
                pass         
            check_key.update(hsd=hsd)
            data_key = ResponseKey(check_key, many=True)
            return Response(data=data_key.data, status=status.HTTP_200_OK) 
        except:
            return Response('false', status=status.HTTP_400_BAD_REQUEST)        