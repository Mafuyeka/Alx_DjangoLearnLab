# blog/views.py
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from .models import Post, Comment
from .forms import PostForm, CommentForm, UserRegisterForm, UserUpdateForm, ProfileForm

# --- Posts (CRUD) ---
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comment_form'] = CommentForm()
        return ctx

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_confirm_delete.html'

# --- Comments (CRUD) ---
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        return redirect(post.get_absolute_url())

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    def test_func(self):
        return self.get_object().author == self.request.user

# --- Auth: register & profile ---
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save(); p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {'u_form':u_form,'p_form':p_form})

# --- Search & Tags ---
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    def get_queryset(self):
        q = self.request.GET.get('q','').strip()
        return Post.objects.filter(
            Q(title__icontains=q) | Q(content__icontains=q) | Q(tags__name__icontains=q)
        ).distinct()

class TagPostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs['tag_name'])
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['active_tag'] = self.kwargs['tag_name']
        return ctx
