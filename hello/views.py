from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.timezone import now
from django.views.generic import ListView

from hello.forms import LogMessageForm
from hello.models import LogMessage

# Create your views here.

def hello_there(request, name):
    print(request.build_absolute_uri())  # Opcional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

class HomeListView(ListView):
    model = LogMessage
    template_name = 'hello/home.html'  # Especificando o nome do template (se necessário)
    context_object_name = 'message_list'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = now()
            message.save()
            return redirect("home")
    return render(request, "hello/log_message.html", {"form": form})

