from django import forms

from .models import LogMessage


class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ['message', 'log_date']
        widgets = {
            'log_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
