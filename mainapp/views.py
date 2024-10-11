from django.shortcuts import render,redirect
from.forms import ProfileForm,PostForm,EditForm
from django.contrib.auth.models import User
from.models import Profiles,Blogs

def blogs(request):
    posts=Blogs.objects.all().order_by("-date_created")
    context={
        "posts":posts
    }
    return render(request, 'app/blogs.html',context)

def create_blog(request):
    form=PostForm()
    if request.method=='POST':
       form=PostForm(request.POST) 
       if form.is_valid():
           instance=form.save(commit=False)
           instance.user=request.user
           instance.save()
           return redirect('mainapp:blogs')
    context={
        'form':form        
        }
    return render(request, 'app/createblog.html',context)

def blog(request, id):
    post=Blogs.objects.get(id=id)
    context={
        "post":post
    }
    return render(request, 'app/blog.html',context)
def editblog(request,pk):
    post=Blogs.objects.get(id=pk)
    if request.method=='POST':
        form=EditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('mainapp:blog',id=post.id)
    else:
        form=EditForm(instance=post)
    context={
        'form':form,
        'post':post
    }
    return render(request, 'app/editblog.html', context)

def deleteblog(request,pk):
    post=Blogs.objects.get(id=pk)
    post.delete()
    return redirect('mainapp:blogs')


def searchblog(request):
    if request.method=='POST':
        search=request.POST['search']
        post_searched=Blogs.objects.filter(post__contains=search).order_by("-date_created")
        # return redirect("mainapp:searchblog")
    
        context={
            'post_searched':post_searched,
            'searche':search,
        }
    return render(request, 'app/search.html', context)


def profile(request,pk):
    # if request.user.is_authenticated:
    profile=Profiles.objects.get(user_id=pk)
    if request.method=='POST':
        current_user=request.user.profiles
        action = request.POST["follows"]
        if action=='unfollows':
            current_user.follows.remove(profile)
        elif  action=='follow':
            current_user.follows.add(profile)
    try:
        profile=Profiles.objects.get(user_id=pk)
        blogs=Blogs.objects.filter(user_id=pk)
        
    except Profiles.DoesNotExist:
        return render(request,'app/error.html',{'message':"doesn't exist"})
    context={
        'profile':profile,
        'blogs':blogs
    }
    return render(request, 'app/profile.html',context)


def updateprofile(request):
    user=request.user.profiles
    profform=ProfileForm(instance=user)
    if request.method=='POST':
        profform=ProfileForm( request.POST, request.FILES, instance=user)
        if profform.is_valid():
            profform.save()
            return redirect('home')
    else:
        profform=ProfileForm(instance=user)
    return render(request, 'app/updateprofile.html',{'form':profform})


#python manage.py runserver
#python manage.py makemigrations
#python manage.py migrate