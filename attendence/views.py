from django.shortcuts import render,redirect
from attendence.models import Attendence,date_wise
from django.contrib.auth.models import auth
from .models import CustomUser
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
User=settings.AUTH_USER_MODEL
def home(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        staff_id=request.POST['staff_id']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request,"user exists")
            return redirect('register')

        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('register')
        else:

          user=CustomUser.objects.create_user(username=username,email=email,password=password,staff_id=staff_id)
          user.save()
          return redirect('login')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
          staff_id=request.POST['staff_id']
          username=request.POST['username']
          password=request.POST['password']
          user=auth.authenticate(username=username,password=password,staff_id=staff_id)
          if user is not None:
            auth.login(request,user)
            return redirect('welcome')
          else:
            messages.info(request,'invalid')
            return redirect('login')

    """else:
        return render(request,'login.html')"""
    return render(request,'login.html')
def welcome(request):
    return render(request,'welcome.html')
def att(request):
    re=request.GET["class"]
    at = Attendence.objects.filter(classes__name__contains=re)
    context = {
         'one': at,

     }
    return render(request,'attendence.html',context)
class Att(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        at = Attendence.objects.filter(classes__name__contains=re)


            # pass into context
        context = {
                'one': at,
            }


            # render the template
        return render(request, 'attendence.html', context)

    def post(self,request,*args,**kwargs):
        names={
           'nst':[],
           'p':[],
        }
        absent={
           'nt':[],
           'o':[],
        }
        name_list=request.POST.getlist('items[]')
        print(name_list)
        for name in name_list:
            names1 = Attendence.objects.get(pk__contains=int(name))
            name_data = {
                #'id':names1.pk,
                'name': names1.name,
                'phone':names1.phone_number,

                #'quantity':menu_item.quantity


            }
            names['nst'].append(name_data)
            names['p'].append(name_data['phone'])
            print(names['nst'])
            #print(names['p'][1]['phone'])



        context = {
            'name': names['nst'],
            'total':len(name_list),
            #'quantity':quantity
        }
        item_ids = []
        #for item in names['nst']:
            #item_ids.append(item['id'])

        nam=date_wise.objects.create()
        nam.name.add(*item_ids)
        print(len(name_list))
        #b=[names['p']]
        #for i in range(2):
         #  b.append(names['p'])
        #print(b)
        a=names['p']
        b=names['nst']
        return render(request, 'present.html',context)
