from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from admin.forms import LoginForm


@require_http_methods(["GET", "POST"])
def login(request):
    """
    Users' authentication controller
    """

    if request.method == 'POST':
        data = request.POST.dict()
        username = data.get('username')
        password = data.get('password')

        # aut must always user 'username' argument
        user = auth.authenticate(username=username, password=password, request=request)

        if user is not None:

            if not user.is_active:
                messages.error(request, "Invalid credentials.", extra_tags='alert-danger')
                return HttpResponseRedirect(reverse('logout-controller'))

            # A backend authenticated the credentials
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home-controller'))

        else:
            # Could not validate user agains any auth backend
            messages.error(request, "Invalid credentials.", extra_tags='alert-danger')

    if request.method == 'GET':

        user = request.user

        if user.is_authenticated:
            return HttpResponseRedirect(reverse('home-controller'))

    template = 'login.html'
    form = LoginForm()
    return render(request, template, {'form': form})


@require_http_methods(["GET"])
def logout(request):
    """
    Logout controller.
    Should redirect to login controller / screen
    """

    auth.logout(request)
    return HttpResponseRedirect(reverse('login-controller'))


@login_required(login_url='/login')
@require_http_methods(["GET"])
def home(request):
    """ 
    Main page controller. Used after user is successfully validated
    Only authenticaded users will access this controller.
    Please notice @login_required decorator
    """

    user = request.user

    if user.is_superuser:
        str_response = "Hello superuser"

    elif user.is_nurse:
        str_response = "Hello nurse user"

    elif user.is_patiente:
        str_response = "Hello patiente user"

    return HttpResponse(str_response)