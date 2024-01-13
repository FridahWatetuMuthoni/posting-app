from django.shortcuts import redirect, render
from .forms import CustomUserForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = CustomUserForm()
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            form.save()
            return redirect('blog:blog-home')
    context = {
        'form':form
    }
    return render(request,'users/register.html', context)