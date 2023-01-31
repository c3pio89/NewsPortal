from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'NewsList.html'
    context_object_name = 'NewsList'
    def get_queryset(self):
        return Post.objects.filter(categoryType='NW').order_by('dateCreation')


class CurrentNews(DetailView):
    model = Post
    template_name = 'CurrentNews.html'
    context_object_name = 'CurrentNews'
    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')

