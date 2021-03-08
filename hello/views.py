from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', 
#     domain=None, secure=None, httponly=False, samesite=None)
def myview(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('0c0134e3 '+str(oldval))
    if oldval : 
        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close
    else : 
        resp.set_cookie('zap', '0c0134e3') # No expired date = until browser close
    resp.set_cookie('dj4e_cookie', '0c0134e3',  max_age=1000) # seconds until expire
    return resp

