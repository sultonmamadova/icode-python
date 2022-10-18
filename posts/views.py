
from django.views import generic
from posts.models import Post

# Create your views here.
class PostListsView(generic.ListView):
    model=Post
    template_name="posts/post_list.html"

class PostDetailView(generic.DetailView):
    model1=Post
    template_name2="posts/post_detail.html"

    