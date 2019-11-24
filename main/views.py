from django.views.generic import ListView

from .models import Post


class PostList(ListView):
    model = Post
    context_object_name = "posts_list"
    template_name = "main/posts.html"
    paginate_by = 10

