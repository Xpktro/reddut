from django.shortcuts import render_to_response, get_object_or_404

from redditApp.models import Link
from redditApp.forms import LinkForm

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


def index(request):
    link_list = Link.objects.all().order_by("-points")[:10]
    if request.user.is_authenticated():
        usrnm = request.user.username
    else:
        usrnm = None
    return render_to_response(
        "myreddit/index.html",
        {"link_list": link_list, "username": usrnm, "submitform": LinkForm, },
        context_instance=RequestContext(request)
    )


def login_view(request):
    username = request.POST["username"]
    password = request.POST["pass"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse("reddit_index"))
        else:
            pass  # <-!
    else:
        return HttpResponseRedirect(reverse("reddit_index"))  # <-!


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("reddit_index"))


def vote(request, link_id, way):
    link = get_object_or_404(Link, pk=link_id)
    if way == "up":
        link.points += 1
    elif way == "down":
        link.points -= 1
    link.save()
    return HttpResponseRedirect(reverse("reddit_index"))


def submit(request):
    linkform = LinkForm(request.POST)
    if linkform.is_valid():
        link = linkform.save(commit=False)
        link.sub_date = timezone.now()
        link.points = 0
        link.sub_by = request.user
        link.save()
        linkform.save()
    else:
        pass
        # return HttpResponseRedirect(reverse("reddit_index"))  # Cambiar a algo mas bonito.

    return HttpResponseRedirect(reverse("reddit_index"))
