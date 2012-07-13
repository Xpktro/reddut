from django.forms import ModelForm, Textarea
from redditApp.models import Link, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ("description", "link",)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", )


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", )
        widgets = {
            "comment": Textarea(
                            attrs={
                                'cols': 60,
                                'rows': 4
                            }
            ),
        }
