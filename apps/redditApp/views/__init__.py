from django.shortcuts import render_to_response, get_object_or_404

from redditApp.forms import *
from redditApp.models import Link
from redditApp import strings

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
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
        context_instance=RequestContext(request),
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
            messages.error(request, strings.INACTIVE_USER)

    else:
        messages.error(request, strings.INVALID_USER_PASSWORD)
        return HttpResponseRedirect(reverse("reddit_index"))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("reddit_index"))


def vote(request, link_id, way, next):
    link = get_object_or_404(Link, pk=link_id)
    if way == "up":
        link.points += 1
    elif way == "down":
        link.points -= 1
    link.save()
    if next == "i":
        return HttpResponseRedirect(reverse("reddit_index"))
    elif next == "l":
        return HttpResponseRedirect(
            reverse("reddit_link", kwargs={"pk": link_id})
        )


def submit(request):
    linkform = LinkForm(request.POST)
    if linkform.is_valid():
        link = linkform.save(commit=False)
        link.sub_date = timezone.now()
        link.points = 0
        link.sub_by = request.user
        link.save()
    else:
        pass
        # return HttpResponseRedirect(reverse("reddit_index"))  # Cambiar a algo mas bonito.

    return HttpResponseRedirect(reverse("reddit_index"))


def register(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect(reverse("reddit_index"))
    return render_to_response(
        "myreddit/register.html",
        {"userform": userform},
        context_instance=RequestContext(request),
    )


def comment(request, pk):
    commentform = CommentForm(request.POST)
    link = get_object_or_404(Link, pk=pk)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.link = link
        comment.author = request.user
        comment.date = timezone.now()
        comment.points = 0
        comment.save()
    return HttpResponseRedirect(reverse("reddit_link", kwargs={"pk": pk}))


def vote_comment(request, link_id, way, comment):
    comment = get_object_or_404(Comment, pk=comment)
    if way == "up":
        comment.points += 1
    elif way == "down":
        comment.points -= 1
    comment.save()
    return HttpResponseRedirect(reverse("reddit_link", kwargs={"pk": link_id}))
