from django import forms
from .models import Call

class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['client', 'reason', 'operator', 'is_resolved', 'tags']
        widgets = {
            'is_resolved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tags': forms.CheckboxSelectMultiple,
        }