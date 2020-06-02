from django.shortcuts import render, redirect
from .forms import UsersRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UsersRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data['username']
            messages.success(request, f'Account created for {user_name}, You can log in now')
            return redirect('login')
    else:
        form = UsersRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    u_form=UserUpdateForm()
    p_form=ProfileUpdateForm()
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Data is updated')
    #         return redirect('users:profile')
    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)

    data = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context=data)
