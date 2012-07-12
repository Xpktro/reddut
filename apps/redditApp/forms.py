from django.forms import ModelForm
from redditApp.models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ("description", "link",)
