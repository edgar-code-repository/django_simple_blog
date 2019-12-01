from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Post


class PostList(ListView):
    model = Post
    context_object_name = "posts_list"
    template_name = "main/posts.html"
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        categories_list = []

        page = self.request.GET.get('page')
        if page is None:
            page = "1"
        
        print("[PostList][Page: " + str(page) + "]")

        posts_all = Post.objects.all()
        paginator = Paginator(posts_all, 5)
        paginator_page = paginator.page(int(page))

        print("[PostList][paginator_page: " + str(paginator_page.object_list) + "]")

        return context
