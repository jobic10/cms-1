from django.http import HttpResponse
from django.shortcuts import redirect



def unauthenticated(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='1':
                return redirect('dashboard')
            if request.user.user_type=='2':
                return redirect('cms')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper

