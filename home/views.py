from unicodedata import name
from django.shortcuts import render
import agrishop
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from home.models import Contact,Category,Post
from django.contrib import messages
import razorpay
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def index(request):
    products=Post.objects.all()
    cats=Category.objects.all()
    p=Paginator(products,8)
    page_number=request.GET.get('page')
    finalproducts=p.get_page(page_number)
    dataset={'products':finalproducts,'cats':cats}
    return render(request,"index.html",dataset)

def about(request):
    return render(request,'about.html')

def videos(request):
    return render(request,'videos.html')


@csrf_exempt
def success(request):
    return render(request,'success.html')
    
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your Message Sent!')

    return render(request,'contact.html')

def post(request,url):
    post=Post.objects.get(url=url)

    client = razorpay.Client(auth=("KEY", "SECRET"))

    data = { "amount": 175000, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)

    return render(request,'post.html',payment= payment)

def blog(request):
    posts=Post.objects.all()
    p=Paginator(posts,8)
    page_number=request.GET.get('page')
    finalposts=p.get_page(page_number)
    data={
        'posts':finalposts
    }
    return render(request,'blog.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    return render(request,'post.html',{'post':post})
def buy():

    client = razorpay.Client(auth=("RKEY", "RSECRET_KEY"))
    

    data = { "amount": ({{post.price}} *100), "currency": "INR", "receipt": "#11" }
    payment = client.order.create(data=data)

    return render('post.html', payment=payment)


def category(request,url):
    cat= Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
   

    return render(request,'Category.html',{'cat': cat, 'posts': posts})

def search(request):
    query=request.GET['query']
    allposts=Post.objects.filter(title__icontains=query)
    p=Paginator(allposts,6)
    page_number=request.GET.get('page')
    finalposts=p.get_page(page_number)
    params={'allposts':finalposts}
    return render(request,'search.html',params)

# def handler404(request,exception):
#     return render(request,'404.html')