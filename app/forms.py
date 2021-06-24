from random import choices
from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateTimeBaseInput, TextInput, Textarea

from .models import CountDown


class DateInput(forms.DateInput):
    input_type = "datetime-local"


class CountDownForm(ModelForm):
    class Meta:
        model = CountDown
        fields = [ "c_happening",  "c_start", "c_status"] #"channel",
        widgets = {
            "c_happening": TextInput(
                attrs={
                    "class": "form-control w-100 m-3",
                    "placeholder": "name your countdown",
                    "required": "True",
                }
            ),

            "c_start": DateInput(
                attrs={
                    "class": "form-control w-100 m-3",
                    "required": "True",
                }
            ),

        }
