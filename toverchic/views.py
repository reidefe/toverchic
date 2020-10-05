from django.shortcuts import render, redirect
from models import Post, User, Comment
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin,LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms

#class to list all products based on when they were created
class Products(ListView):
    template_name = './templates/home.html'
    model = Post
    context_object_name = 'product_list'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['pk'])


#class to show a product after clicking using post id, getting the id from the frontend
class Productdetail(DetailView):
    model = Post
    context_object_name = 'product_detail'
    template_name = './templates/detailList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['pk'])



#class and following functin for registration and user credential 
class userSignup(UserCreationForm):
    user_name = forms.CharField(max_length=250)
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ['full_name', 'email', 'phone']    

def signup(request):
    if request.method == 'POST' :
        form = userSignup(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect ('home')
    else:
        form = userSignup()
    return render(request, 'templates/signup.html', {'form':form})




#class for creating posts after user authentication and approval
class createProduct(PermissionRequiredMixin,LoginRequiredMixin,UserPassesTestMixin,CreateView):
    login_url= '/account/login/'
    template_name = '.templates/createpost.html'
    model = Post
    context_object_name = 'create-product'
    permission_required = 'users.post_perm'
   


class createComment(LoginRequiredMixin,CreateView):    
    model = Comment
    context_object_name = 'create-comment'
    fields = ['title', 'comment']

   

        