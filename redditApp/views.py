from django.shortcuts import render_to_response, get_object_or_404
from redditApp.models import Link
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template import RequestContext

def index(request):
    link_list = Link.objects.all().order_by('-points')[:10]
    return render_to_response("myreddit/index.html", {"link_list": link_list}, context_instance=RequestContext(request))

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
    return HttpResponseRedirect(reverse("redditApp.views.index"))

def submit(request):
    try:
        name = request.POST["name"]
        url = request.POST["link"]
    except:
        return HttpResponseRedirect(reverse("redditApp.views.index")) #Cambiar a algo mas bonito.
    else:
        l = Link(link=url, description=name, sub_date=timezone.now(), points=0)
        l.save()
    return HttpResponseRedirect(reverse("redditApp.views.index"))
