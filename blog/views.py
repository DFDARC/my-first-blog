from django.shortcuts import render
from django.utils import timezone  # Importar timezone
from .models import Post

def post_list(request):
    # Filtrar posts con fecha de publicación menor o igual a la fecha y hora actual
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
