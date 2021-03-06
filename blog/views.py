from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, RoomCategory
from .filters import PostFilter

# from django.http import HttpResponse
# def about(request):
#     return HttpResponse("<h1>Tirth's Blog About</h1>")

# posts = [
# {
#         "hostel_name": "Prime HOstel",
#         "address": "My first updated post!\r\n\r\nThis is exciting!",
#         "author_id": 1,"area":"Gota","city":"Ahmedabad","rating":"2","breakfast":"True","lunch":"False","dinner":"True","transportation":"True","cctv":"False","fridge":"False","washing_machine":"True","geyser":"True","ac":"True"
#     },
#     {
#         "hostel_name": "Ravi Hostel",
#         "address": "This is a post from a different user...",
#         "author_id": 2,"area":"Gota","city":"Ahmedabad","rating":"2","breakfast":"True","lunch":"False","dinner":"True","transportation":"True","cctv":"False","fridge":"False","washing_machine":"True","geyser":"True","ac":"True"
#     },
#     {
#         "hostel_name": "Top 5 ",
#         "address": "Te melius apeirian postulant cum, labitur admodu",
#         "author_id": 1,"area":"Gota","city":"Ahmedabad","rating":"2","breakfast":"True","lunch":"False","dinner":"True","transportation":"True","cctv":"False","fridge":"False","washing_machine":"True","geyser":"True","ac":"True"
#     }
# ]


def home(request):
    posts_list = Post.objects.all()
    query = request.GET.get('q')
    # area = request.GET.get('a')
    # city = request.GET.get('c')
    if query:
        posts_list = Post.objects.filter(hostel_name__icontains=query).order_by("date_posted")
    # if area:
    #     posts_list = posts_list.filter(area__icontains=area).order_by("date_posted")
    # if city:
    #     posts_list = posts_list.filter(city__icontains=city).order_by("date_posted")
    
    myFilter = PostFilter(request.GET, queryset=posts_list)
    posts_list = myFilter.qs
    context = {
        "posts": posts_list,
        'myFilter':myFilter,
       
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]  # - sigh for decending
    paginate_by = 9


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    # ordering = ['-date_posted'] # - sigh for decending   # comented b'cod it is written in `get_query_set` method
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


def post_detail_view(request,*args,**kwargs):
    h = Post.objects.get(id=kwargs['pk'])
    # if request.method == 'GET':
    #     query = request.GET.get('q')
    #     submitbutton = request.GET.get('submit')
    #     if query is not None:
    #         h = Post.objects.get(id=kwargs['pk'])
    # p=Post.objects.filter(hostel_name="tirth's home")
    room_cat = RoomCategory.objects.filter(hostel_id=h.id)
    context = {
        'object' : h,
        'posts' : room_cat
    }
    template_name = "blog/post_detail.html"
    return render(request, "blog/post_detail.html", context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        "hostel_name",
        "address",
        "area",
        "city",
        "contact",
        "rating",
        "breakfast",
        "lunch",
        "dinner",
        "transportation",
        "cctv",
        "fridge",
        "washing_machine",
        "geyser",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RoomCategoryView(DetailView):
    model = RoomCategory

class RoomCategoryCreateView(LoginRequiredMixin, CreateView):
    model = RoomCategory
    fields = [
        "hostel",
        "sharing",
        "price"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        "hostel_name",
        "address",
        "area",
        "city",
        "contact",
        "rating",
        "breakfast",
        "lunch",
        "dinner",
        "transportation",
        "cctv",
        "fridge",
        "washing_machine",
        "geyser",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = RoomCategory
    success_url = "/"
    fields = [
        "sharing",
        "price",
    ]
    def test_func(self):
        room_cat = self.get_object()
        post  = Post.objects.get(pk = room_cat.hostel_id)
        if self.request.user == post.author:
            return True
        return False

class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = RoomCategory
    success_url = "/"
    
    def test_func(self):
        return True

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {"title": "About2"})
