from django.shortcuts import render, redirect
from .models import Post, User, Comment
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth import login, logout, authenticate, get_user_model

from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin,LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseRedirect

#class to list all products based on when they were created
class Products(ListView):
    template_name = 'home.html'
    #model = Post
    context_object_name = 'product_list'
    queryset = Post.objects.all()



#class to show a product after clicking using post id, getting the id from the frontend
class Productdetail(DetailView):
    model = Post
    context_object_name = 'product_detail'
    template_name = 'detailList.html'
    




#class and following functin for registration and user credential 
class userSignup(UserCreationForm):
    #full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
    email = forms.EmailField()
    phone = forms.CharField()
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email','phone') 

def signup(request):
    if request.method == 'POST' :
        form = userSignup(request.POST)
        if form.is_valid():
            user_form = form.save()
            user_form.save()
            raw_password = form.cleaned_data.get('password1')
            user_form = authenticate(username=user_form .username, password=raw_password)
            login(request, user_form)
            return redirect ('home')
    else:
        form = userSignup()
    return render(request, 'signup.html', {'form':form})

'''
class createpost(forms.ModelForm):    

    class Meta:
        model = Post
        fields = ['title', 'description', 'image', 'price' ] '''
        



#class for creating posts after user authentication and approval
class createProduct(UserPassesTestMixin,CreateView):    
    template_name = 'createpost.html'   
    model = Post
    context_object_name = 'create-product'    
    fields = ['title', 'description', 'image', 'price']  
    
    success_url = reverse_lazy('home')   
    def test_func(self):
        return  self.request.user.post_perm == True

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()          
        return HttpResponseRedirect(self.success_url)

    def get_initial(self, *args, **kwargs):
        initial = super(createProduct,self).get_initial(**kwargs)
        initial.copy
        initial['owner'] = self.request.user.pk
        return initial


class createComment(LoginRequiredMixin,CreateView):    
    model = Comment
    context_object_name = 'create-comment'
    fields = ['title', 'comment']
   

class userDetails(DetailView):
    model = User
    template_name = 'user.html'
    context_object_name = 'user'
    
    '''def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context[''] = self.request.user'''


