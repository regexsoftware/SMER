from django.shortcuts import render , redirect
from register.models import User
from django.http import HttpResponse
import requests

def send_otp(request):
    if(request.COOKIES.get('loggedIn')):
        responsetoredirect = redirect('/single/')
        return responsetoredirect
    elif(request.method == 'POST'):
        no = request.POST['number']
        response = requests.get('https://2factor.in/API/V1/8b16b93c-ef4f-11e9-b828-0200cd936042/SMS/%s/AUTOGEN' % no)
        msg = response.json()
        return render(request, 'confirm_otp.html', {
            'Status': msg['Status'],
            'Details': msg['Details'],
            'cno' : no
        })
    return render(request,'login.html')

def verify_otp(request):
    if(request.method == 'POST'):
        otp = request.POST['otp']
        session_id = request.POST['Details']
        response = requests.get('https://2factor.in/API/V1/8b16b93c-ef4f-11e9-b828-0200cd936042/SMS/VERIFY/%s/%s' % (session_id , otp))
        msg = response.json()
        if(msg['Status'] == 'Success'):
            responsetosend = render(request, 'welcome.html',{
                'Status': msg['Status'],
                'Details': msg['Details']
            })  
            responsetosend.set_cookie(key='loggedIn', value=True , max_age=60*60*24)
            responsetosend.set_cookie(key='ucno', value='Contact Number goes here',max_age=60*60*24)
            return responsetosend
        return render(request, 'confirm_otp.html', {
            'Status': msg['Status'],
            'Details': msg['Details']
        })
    return render(request,'confirm_otp.html')


def forgot_view(request):
    return render(request,'forgot_pass.html')