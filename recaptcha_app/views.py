from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from recaptcha_app.forms import FormWithCaptcha
from recaptcha_app.check_recaptcha import CheckCaptcha


INDEX_RECAPTCHA_PATH = 'recaptcha_app/index.html'
CAPTCHA_COMPLETE = 'Капча пройдена'
CAPTCHA_NOT_COMPLETE = 'Капча не пройдена'

def recaptcha(request):
    if request.method == 'GET':
        return render(request, INDEX_RECAPTCHA_PATH, context={'recaptcha': FormWithCaptcha})
    
    if request.method == 'POST':
        result_captcha = CheckCaptcha().grecaptcha_verify(request)
        if result_captcha['success'] == True:
            return HttpResponse(CAPTCHA_COMPLETE)
        else:
            return HttpResponse(CAPTCHA_NOT_COMPLETE)