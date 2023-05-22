from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    return render(request, 'blog/index.html')


def all_posts(request):
    return render(request, 'blog/all_posts.html')


def post(request, slug):
    return render(request, 'blog/post.html', {'id': slug})

# data = requests.get('https://dummyjson.com/quotes').json()
# quotes = data['quotes']
# blog_head = [quote['quote'] for i, quote in enumerate(quotes) if i < 1]
# print(blog_head)
