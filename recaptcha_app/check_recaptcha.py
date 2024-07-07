import requests
from recaptcha.settings import RECAPTCHA_PRIVATE_KEY

class CheckCaptcha:
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def grecaptcha_verify(self, request):
        if request.method == 'POST':
            captcha_rs = request.POST.get('g-recaptcha-response')
            url = "https://www.google.com/recaptcha/api/siteverify"
            params = {
                'secret': RECAPTCHA_PRIVATE_KEY,
                'response': captcha_rs,
                'remoteip': self.get_client_ip(request)
            }
            verify_rs = requests.get(url, params=params, verify=True)
            return verify_rs.json()