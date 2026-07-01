from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DeleteView,UpdateView,DetailView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_object_or_404,redirect
from .forms import RoomSearchForm
from .models import Room
from django.http import JsonResponse
import json
# Create your views here.

class BaseView(TemplateView):
    template_name="main.html"


class RoomSearchView(FormView):
    template_name = "roomjoin.html"
    form_class = RoomSearchForm

    def form_valid(self, form):
        room_id = form.cleaned_data['id']
        self.room = get_object_or_404(Room, id = room_id)
        self.room.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('room', kwargs={'pk':self.room.id} )
    


class RoomView(DetailView):
    model = Room
    template_name="player.html"
    context_object_name = "vid"
    

class CreateRoomView(CreateView):
    template_name = "create.html"
    model = Room
    fields = ["id","password"]

    def form_valid(self, form, **kwargs):
        form.instance.host = self.request.user 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('room', kwargs={'pk':self.object.id} )


class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = "login.html"

class UserLogoutView(LogoutView):
    ...


def VideoSaveView(request,pk):
    room = Room.objects.get(pk=pk) 
    data = json.loads(request.body)
    room.video = data['value']
    room.save()
    return JsonResponse({})
