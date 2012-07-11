from django.shortcuts import render_to_response, get_object_or_404

from redditApp.models import Link
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


def index(request):
    link_list = Link.objects.all().order_by('-points')[:10]
    if request.user.is_authenticated():
        usrnm = request.user.username
    else:
        usrnm = None
    return render_to_response(
        "myreddit/index.html",
        {"link_list": link_list, "username": usrnm},
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


def link(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return render_to_response("myreddit/link.html", {"link": link})


def vote(request, link_id, way):
    link = get_object_or_404(Link, pk=link_id)
    if way == "up":
        link.points += 1
    elif way == "down":
        link.points -= 1
    link.save()
    return HttpResponseRedirect(reverse("reddit_index"))


def submit(request):
    try:
        name = request.POST["name"]
        url = request.POST["link"]
    except:
        return HttpResponseRedirect(reverse("reddit_index"))  # Cambiar a algo mas bonito.
    else:
        l = Link(
                 link=url,
                 description=name,
                 sub_date=timezone.now(),
                 points=0,
                 sub_by=request.user,
        )
        l.save()
    return HttpResponseRedirect(reverse("reddit_index"))
