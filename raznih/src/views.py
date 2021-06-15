from django.shortcuts import render
import razorpay
from .models import Coffee
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def home(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         #amount = request.POST.get('amount') * 100
        
#         client = razorpay.Client(auth =("rzp_test_QPpyRhWJXGXqlE" , "4Vst3krNqMkuIxkaekCBKXGU"))
#         payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        

        
#         #print(payment)
#         coffee = Coffee(name = name , amount = amount , payment_id = payment['id'])
#         #coffee.save()
        
#         return render(request, 'index.html' ,{'payment' :payment})
#     return render(request, 'index.html')
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        # amount = int(request.POST.get('amount')) * 100
        client = razorpay.Client(auth =("rzp_test_QPpyRhWJXGXqlE" , "4Vst3krNqMkuIxkaekCBKXGU"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        print(payment)
        coffee = Coffee(name = name , amount = amount , payment_id = payment['id'])
        coffee.save()
        
        return render(request, 'index.html' ,{'payment':payment})
    return render(request, 'index.html')

@csrf_exempt   
def success(request):
    if request.method == "POST":
        a= request.POST
        print(a)
    return render(request,"success.html")