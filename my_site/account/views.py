from django.shortcuts import render
# HttpResponse za to, kar ne bom vracal cez render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            # check if login is correct
            if user is not None:
                # if user exists
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'account/../templates/registration/login.html', {'form': form})




