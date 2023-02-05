#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect

class work_upload_List(LoginRequiredMixin, UserPassesTestMixin, ListView):
    
    login_url = 'loginout/login'

    model = Post
    template_name = 'work_upload/index.html'
    ordering = '-pk'
    ...
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_active
    


    def get_context_data(self, **kwargs):

        context = super(work_upload_List, self).get_context_data()
        ...
        page = context['page_obj']
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(page.number, on_each_side=3, on_ends=1)
        context['pagelist'] = pagelist
        ...

        return context

# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(request,'work_upload/index.html',
#     {
#         'posts_vi' : posts,
#     }
    
#     )

class PostDetail(DetailView):
    model = Post
    template_name = 'work_upload/single_post_page.html'


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render( request, 'work_upload/single_post_page.html',
#     {
#         'post_vi' : post,
#     }
#     )
# Create your views here.

class PostSearch(work_upload_List):
    paginate_by = 10

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(flight_name__contains=q)).distinct()
        return post_list
    
    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'work_upload/create_work_upload.html'

    fields = ['flight_name','flight_date','flight_num','inetx_ver','cal_ver','tspi_ch','created_at','writer_name']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'work_upload/single_post_page.html'
    success_url = '/work_upload/'
    

    fields = ['flight_name','flight_date','flight_num','inetx_ver','cal_ver','tspi_ch','created_at','writer_name']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/work_upload/')