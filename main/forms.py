from django import forms
from .models import Room

class RoomSearchForm(forms.Form):
    id = forms.CharField(label="room id:")
    password = forms.CharField(label="room password:",required=False)
