from redditApp.models import Link, Comment
from django.views.generic import DetailView
from redditApp.forms import CommentForm


class LinkDetailView(DetailView):
    model = Link
    context_object_name = "link"
    template_name = "myreddit/link.html"

    def get_context_data(self, **kwargs):
        context = super(LinkDetailView, self).get_context_data(**kwargs)
        context["commentform"] = CommentForm
        context["comments"] = Comment.objects.filter(link__id=self.get_object().id)
        if self.request.user.is_authenticated():
            context["username"] = self.request.user
        return context
