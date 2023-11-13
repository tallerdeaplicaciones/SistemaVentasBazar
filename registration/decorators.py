from django.shortcuts import redirect

def redirect_home_based_on_credentials(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_jefeVentas:  # Supongamos que tienes un campo personalizado is_jefeVentas en tu modelo de usuario
                return redirect('home_jefeVentas')
            elif request.user.is_vendedor:  # Supongamos que tienes un campo personalizado is_vendedor en tu modelo de usuario
                return redirect('home_vendedor')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
