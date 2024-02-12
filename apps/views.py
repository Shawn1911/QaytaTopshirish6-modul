from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from apps.forms import RegisterForm
from apps.models import Ads


# Create your views here.

class IndexView(ListView):
    model = Ads
    template_name = 'apps/index.html'
    context_object_name = 'ads'


class AdCreateView(CreateView):
    model = Ads
    template_name = 'apps/create_user.html'
    fields = ['title', 'ad_source', 'image']
    success_url = reverse_lazy('index_page')


class AdUpdateView(UpdateView):
    model = Ads
    template_name = 'apps/update_user.html'
    fields = ['title', 'ad_source', 'image']
    context_object_name = 'ad'
    success_url = reverse_lazy('index_page')


class AdDeleteView(DeleteView):
    model = Ads
    template_name = 'apps/delete_user.html'
    context_object_name = 'ad'
    success_url = reverse_lazy('index_page')


class CustomLoginView(LoginView):
    template_name = 'apps/login.html'
    next_page = reverse_lazy('index_page')


class RegisterFormView(FormView):
    template_name = 'apps/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('Invalid')
