from django.shortcuts import render
from .models import BlogPost
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogPageView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, "auth/login.html")
        else:
            search = request.GET.get("search")
            if not search:
                posts = BlogPost.objects.all()
                context = {
                    "posts": posts,
                    "search": search,
                }
                return render(request, "main/blog.html", context)
            else:
                posts = BlogPost.objects.filter(title__icontains=search)
                if posts:
                    context = {
                        "posts": posts,
                        "search": search,
                    }
                    return render(request, "main/blog.html", context)
                else:
                    return render(request, "main/404.html")


class BlogDetailPageView(View):
    def get(self, request, slug):
        posts = BlogPost.objects.all()
        comments = BlogPost.objects.all()
        post = BlogPost.objects.get(slug=slug)
        context = {
            "posts": posts,
            "post": post,
            "comments": comments,
        }
        return render(request, "main/single.html", context)


