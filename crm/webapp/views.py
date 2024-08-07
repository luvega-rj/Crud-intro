from django.shortcuts import render

from .forms import CreateUserForm, LoginForm
def home(request):
    
    # return HttpResponse('Hello world!')
    return render(request,'webapp/index.html')

# register

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
       
       form = CreateUserForm(request.POST)

       if form.is_valid():
          
          form.save()

        #   return redirect('')

    context = {'form' : form}

    return render(request,'webbapp/register.html', context=context)