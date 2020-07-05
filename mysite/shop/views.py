from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from .PayTm import checksum

MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'

def index(request):
    allprods=[]
    catprods=Product.objects.values('category')
    cats={x['category'] for x in catprods}
    for cat in cats:
        prods=Product.objects.filter(category=cat)
        n=len(prods)
        nSlides=n//4+ ceil(n/4-(n//4))
        allprods.append([prods,range(1,nSlides),nSlides])
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)

def searchMatch(query,item):
    query=query.lower()
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower() or query in item.subcategory.lower():
        return True
    return False

def search(request):
    query=request.GET.get('search')
    allprods=[]
    catprods=Product.objects.values('category')
    cats={x['category'] for x in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prods=[item for item in prodtemp if searchMatch(query,item)]
        n=len(prods)
        nSlides=n//4+ ceil(n/4-(n//4))
        if n!=0:
            allprods.append([prods,range(1,nSlides),nSlides])
    params={'allprods':allprods, 'msg' : ''}
    if len(allprods)==0 or len(query) < 4 :
        params={'msg' : "Please make sure to enter relevant search query"}
    return render(request,'shop/search.html',params)

def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    if request.method=='POST':
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0 :
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text' : item.update_desc,'time' : item.timestamp})
                response=json.dumps({'status' : 'success','updates' : updates,'itemsJson' : order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{'status' : 'no item'}")
        except Exception as e:
            return HttpResponse("{'status' : 'error'}")
    return render(request,'shop/tracker.html')



def contact(request):
    thank=False
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank=True
    return render(request,'shop/contact.html',{'thank' : thank})

def checkout(request):
    if request.method=='POST':
        itemsJson=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address1','')+' '+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        order=Orders(amount=amount,name=name,email=email,phone=phone,city=city,state=state,zip_code=zip_code,address=address,items_json=itemsJson)
        order.save()
        thank=True
        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        id=order.order_id
        # return render(request,'shop/checkout.html',{'thank' : thank,'id' : id})
        param_dict = {
            #provide your own mid and merchant key for payment gateway
            'MID':'WorldP64425807474247',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,'shop/paytm.html',{'param_dict' : param_dict})

    return render(request,'shop/checkout.html')



def productView(request, myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/prodView.html',{'product': product[0]} )



@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict={}
    check_sum=''
    for i in form.keys():
        response_dict[i]=form[i]
        if i== 'CHECKSUMHASH':
            check_sum=form[i]
    verify=checksum.verify_checksum(response_dict,MERCHANT_KEY,check_sum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order unsuccessful due to '+response_dict['RESPMSG'])
    return render(request,'shop/paymentstatus.html',{'response' : response_dict})
