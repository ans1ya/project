from django.shortcuts import redirect

def sign_in_required(func):
    def wrapper(req,*args,**kwargs):
        if not req.user.is_authenticated:
            return redirect('login')
        else:
            return func(req,*args,**kwargs)
    return wrapper

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            return view_func(request,*args,**kwargs)
        return wrapper_func
    return decorator