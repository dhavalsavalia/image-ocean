from django.views import generic

from posts.models import Post
from posts.helpers import get_posts


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return get_posts()
