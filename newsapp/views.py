from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Category,Sub_Category,Post,StudentUser,Footer
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from newsapp.forms import BlogPost
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from datetime import date

# Create your views here.
def index(request):
    recentpost=Post.objects.order_by('-date')[0:3]
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    post=Post.objects.order_by('-date')
      # for pagination
    paginator=Paginator(post,15)
    page_number=request.GET.get('page')
    postfinal=paginator.get_page(page_number)
    totalpage=postfinal.paginator.num_pages
    context={
        'post':postfinal,
        'lastpage':totalpage,
        'totalpagelist':[ n+1 for n in range(totalpage) ],
        'category':category,
        'sub_category':sub_category,
        'recentpost':recentpost

    }
  
    return render(request,'index.html',context)


def blog(request,id):
    post=Post.objects.filter(sub_category=id).order_by('-date')
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    
    
    context={
        'post':post,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'blog.html',context)

def blog_details(request,slug):
    post=Post.objects.filter(slug=slug)
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    context={
        'post':post,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'blog_details.html',context)

def userpost_details(request,slug):
    post=Post.objects.filter(slug=slug)
    # category=Category.objects.all()
    # sub_category=Sub_Category.objects.all()
    context={
        'post':post,
       
    }
    return render(request,'userpost_details.html',context)

# add post section
def add_post(request):
    post=Post.objects.all()
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    context={
        'post':post,
        'category':category,
        'sub_category':sub_category,
    }
    if request.method=="POST":
        category=request.POST['category']
        sub_category=request.POST['sub_category']
        title=request.POST['title']
        image=request.FILES['image']
        blogger=request.POST['blogger']
        desc=request.POST['desc']
        user=request.user
        studentuser=StudentUser.objects.get(user=user)

        addpost=Post.objects.create(author=studentuser,category=category,sub_category=sub_category,title=title,image=image,blogger=blogger,desc=desc,date=date.today())
        addpost.save()
        messages.info(request,'successfully add post ')
        return redirect('add_post')
    return render(request,'add_post.html',context)


def add_post2(request):
    if request.method=='POST':
        fm=BlogPost(request.POST,files=request.FILES)
        if fm.is_valid():
            author=fm.cleaned_data['author']
            category=fm.cleaned_data['category']
            sub_category=fm.cleaned_data['sub_category']
            title=fm.cleaned_data['title']
            desc=fm.cleaned_data['desc']
            image=fm.cleaned_data['image']
            post=Post(author=author,category=category,sub_category=sub_category,title=title,image=image,desc=desc)
            fm.save()
            messages.info(request,'Successfully add post')
            
            fm=BlogPost()
            return redirect('add_post2')
    else:
        fm=BlogPost()
    post=Post.objects.all()
    return render(request,'add_post2.html',{'form':fm,'post':post})

# login
def userlogin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
           
            user1 = StudentUser.objects.get(user=user)
      
            if user1.type == "user":
                login(request, user)
                messages.success(request, 'Successfully logged In')
                return redirect("add_post2")

            else:
                messages.info(request, 'This is not Registered')
                return redirect('usersignup')

        else:
            messages.info(request, 'Check username or Password')
            return redirect('userlogin')

    return render(request,'userlogin.html')


# user registeration
def usersignup(request):
    if request.method == "POST":
        username = request.POST['username']
        # email= request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect("usersignup")


        if pass1 != pass2:
            messages.info(request, "Password do not matched")
            return redirect("usersignup")

        
        user = User.objects.create_user(
            username=username, password=pass1)
        StudentUser.objects.create(
            user=user,  type="user")

        messages.success(request, "User Created")
        return redirect("userlogin")

    return render(request,'usersignup.html')

def userlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')


# user post list
def post_list(request,):
    user=request.user
    studentuser=StudentUser.objects.get(user=user)
    post=Post.objects.filter(author=studentuser)
      # for pagination
    paginator=Paginator(post,15)
    page_number=request.GET.get('page')
    postfinal=paginator.get_page(page_number)
    totalpage=postfinal.paginator.num_pages
    context={
        'post':postfinal,
        'lastpage':totalpage,
        'totalpagelist':[ n+1 for n in range(totalpage) ]
        }
    
    return render(request,'post_list.html',context)


def edit_post2(request,id):
    # post=Post.objects.get(id=id)
    
    if request.method=='POST':
        pi=Post.objects.get(id=id)
        fm=BlogPost(request.POST, instance=pi,files=request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        pi=Post.objects.get(id=id)
        fm=BlogPost(instance=pi)
        messages.info(request,'Updated Sucessfully')

    context={
        'form':fm

    }
    return render(request,'edit_post2.html',context)


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post_list')


# footer
def disclaimer(request):
    disclaimer=Footer.objects.all
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    context={
        'disclaimer':disclaimer,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'footer/disclaimer.html',context)

def fraud_alert(request):
    fraud_alert=Footer.objects.all
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    context={
        'fraud_alert':fraud_alert,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'footer/fraud_alert.html',context)

def terms_condition(request):
    terms_condition=Footer.objects.all
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    context={
        'terms_condition':terms_condition,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'footer/terms_condition.html',context)

def faq(request):
    faq=Footer.objects.all
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    context={
        'faq':faq,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'footer/faq.html',context)

def privacy_policy(request):
    privacy_policy=Footer.objects.all
    category=Category.objects.all()
    sub_category=Sub_Category.objects.all()
    context={
        'privacy_policy':privacy_policy,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'footer/privacy_policy.html',context)