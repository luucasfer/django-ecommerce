from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from userauths.models import User


def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)  
        if form.is_valid():
            new_user = form.save()  # Registra os dados preenchidos do form utilizando o meu model do userauths
            username = form.cleaned_data['username']
            messages.success(request, f"Olá, {username}! Sua conta foi criada com sucesso")
            new_user = authenticate(
                username=form.cleaned_data['email'],
                password = form.cleaned_data['password1']
            )
            # Autentica o novo usuario
            login(request, new_user)  
            # Redireciona para a home page
            # index é o 'name' atribuido no core/urls.py
            return redirect("core:index")  
    else:
        form = UserRegisterForm() 
        messages.warning(request, "Não foi possivel registrar o usuario")
 
    context = {
        'form': form
    }
    return render(request, "userauths/sign-up.html", context)


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Voce já está autenticado")
        return redirect("core:index") 
    
    if request.method == 'POST':
        email_from_form = request.POST.get('email')
        password_from_form = request.POST.get('password') 
        
        try:
            user = User.objects.get(email=email_from_form)
            user = authenticate(request, email=email_from_form, password=password_from_form)
            if user is not None:
                login(request, user)
                messages.success(request, "Bem-vindo!")
                return redirect("core:index")
            else:
                messages.warning(request, f"Usuario não encontrado")
        except:
            messages.warning(request, f"Erro ao tentar fazer login")

    return render(request, "userauths/sign-in.html")
    

def logout_view(request):
    logout(request)
    messages.success(request, "Você foi desconectado")
    return redirect("userauths:sign-in")

