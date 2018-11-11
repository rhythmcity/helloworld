from  django.http import HttpResponse
from  django.shortcuts import render_to_response
import json
from datetime import datetime
import time
from  helloworld import  models
def hello(request):
    param = {}
    if request.method == 'GET':
        for q in request.GET:
            param[q] = request.GET[q]

        user_list = models.UserInfo.objects.all()
        value = []
        for userInfo in user_list:
            value.append({'id': userInfo.id, 'user': userInfo.user, 'pwd': userInfo.pwd, 'ctime': str(userInfo.ctime)})

        return HttpResponse(json.dumps({'data': value}))


    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        if password and username:
            try:
                obj = models.UserInfo.objects.get(user=username)
                obj.pwd = password
                obj.ctime =  str(datetime.now())
                obj.save()
            except models.UserInfo.DoesNotExist:
                models.UserInfo.objects.create(user=username, pwd=password,ctime=str(datetime.now()))

            user_list = models.UserInfo.objects.all()
            value = []
            for userInfo in user_list:
                print(userInfo.ctime)
                value.append({'id': userInfo.id, 'user': userInfo.user, 'pwd': userInfo.pwd, 'ctime': str(userInfo.ctime)})

            return HttpResponse(json.dumps({'data': value}))
        else:
            return HttpResponse(json.dumps({'status': '缺少参数'}))








