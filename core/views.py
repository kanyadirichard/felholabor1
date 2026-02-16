from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Photo
from .forms import SignUpForm, UserLoginForm

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'image']
    template_name = 'core/photo_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'core/photo_detail.html'
    context_object_name = 'photo'
    
class PhotoListView(ListView):
    model = Photo
    template_name = 'core/photo_list.html'
    context_object_name = 'photos'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort')
        
        if sort_by == 'name':
            return queryset.order_by('title')
        elif sort_by == 'date_asc':
            return queryset.order_by('uploaded_at')
        else:
            return queryset.order_by('-uploaded_at')
        
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'