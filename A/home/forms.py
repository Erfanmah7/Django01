from re import I
from tkinter.tix import Form

from django import forms


from django import forms
from .models import Todo

class todoCreateForm(forms.Form):

  Name = forms.CharField(label='firstname',required=False)
  Text = forms.CharField()
  DateTime = forms.DateTimeField()


class todoUpdateForm(forms.ModelForm):

    class Meta:

      model = Todo
      #__all__
      fields = ('Name','Text','DateTime')