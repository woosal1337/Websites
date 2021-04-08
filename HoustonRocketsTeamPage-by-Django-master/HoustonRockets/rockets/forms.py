from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Ticket



FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue apple'),
    ('green', 'Green bananas'),
    ('black', 'Black'),
)


class SampleForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )


class SignUpForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea, required=False, help_text='Describe yourself to us.')
    avatar = forms.ImageField(required=False, help_text='Your avatar.')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','bio', 'avatar')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment;
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket;
        fields = '__all__'




