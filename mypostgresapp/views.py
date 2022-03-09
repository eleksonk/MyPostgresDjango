from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import vm_vh_class, vt_owner

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']    
        email = request.POST['email']
        password= request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already exist")
                return redirect(registration)
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email already used")
                return redirect(registration)
            else:
                user = User.objects.create(username = username, email = email, password = password)
                user.save()
                messages.info(request, "Success")
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect(registration)
    else:
        return render(request, 'registration.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username'] 
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

def vehicleClassEntry(request):
    if request.method == 'POST':
        vh_class_code=request.POST['vh_class_code']
        vh_class_desc=request.POST['vh_class_desc']
        trans_catg =request.POST['catg']
        if vh_class_code!="":
            if vm_vh_class.objects.filter(code = vh_class_code).exists():
                messages.info(request, "Code Already exists for vehicle class")
                return redirect(vehicleClassEntry)
            elif vm_vh_class.objects.filter(descr = vh_class_desc).exists():
                messages.info(request, "Vehicle class already exists")
                return redirect(vehicleClassEntry)
            else:
                vhclass=vm_vh_class.objects.create(code=vh_class_code, descr=vh_class_desc, transport_catg = trans_catg)
                vhclass.save()
                messages.info(request, "Success")
                return redirect(vehicleClassEntry)
        else:
                return redirect(vehicleClassEntry)
    else:
        return render(request, 'vehicleClassEntry.html')

def vehicleAll(request):
    vehicles = vt_owner.objects.all()
    return render(request, 'vehicleAll.html',{'vehicles': vehicles})


def vehicleUrl(request, veh_no):
    vehicle = vt_owner.objects.get(regn_no__exact=veh_no)
    #print(vehicle.owner_name)
    return render(request, 'vehicleUrl.html', {'vehicle': vehicle})

def vehicleParticular(request):
    if request.method == 'POST':
        veh_no = request.POST['veh_no'].upper()
        #print(veh_no)        
        if vt_owner.objects.filter(regn_no = veh_no).exists():
            vehicle = vt_owner.objects.get(regn_no__exact=veh_no)
            return render(request, 'vehicleParticular.html', {'vehicle': vehicle})
        else:
            messages.info(request, "Vehicle No does not exist")
            return redirect('vehicleParticular')
    else:
        return render(request, 'vehicleParticular.html')

#First method of binding dropdownlist with db - 1
def vehicleEntry(request):
    results = vm_vh_class.objects.all()
    return render(request, 'vehicleEntry.html',{'veh_classes': results})

def saveVehicle(request):
    if request.method == 'POST':        
        veh_no = request.POST['regn_no'].upper()    
        o_name = request.POST['owner_name']
        reg_dt= request.POST['regn_dt']
        cyl_no = request.POST['no_cyl']
        veh_class = request.POST['veh_class']
        
        if veh_no != "" and o_name!="" and reg_dt!="" and cyl_no!="" and veh_class!="--Select--":        
            if vt_owner.objects.filter(regn_no = veh_no).exists():
                messages.info(request, "Vehicle No. already exist")
                return redirect('vehicleEntry')
            else:
                owner = vt_owner.objects.create(regn_no = veh_no, owner_name = o_name, regn_dt = reg_dt, no_cyl = cyl_no, vh_class_id= veh_class)
                owner.save()
                #messages.info(request, "Success")
                return redirect('vehicleAll')
        else:
            messages.info(request, "Check entered data")
            return redirect('vehicleEntry')
    else:
        return render(request, 'vehicleEntry.html')


#another method of binding dropdownlist with db - 2
def entryForm(request):
    results=vm_vh_class.objects.all()
    return render(request, "dropdown.html",{"classes":results})

def entrySave(request):
    if request.method == 'POST':        
        veh_no = request.POST['regn_no'].upper()    
        o_name = request.POST['owner_name']
        reg_dt= request.POST['regn_dt']
        cyl_no = request.POST['no_cyl']
        veh_class = request.POST['veh_class']
        
        if veh_no != "" and o_name!="" and reg_dt!="" and cyl_no!="" and veh_class!="--Select--":        
            if vt_owner.objects.filter(regn_no = veh_no).exists():
                messages.info(request, "Vehicle No. already exist")
                return redirect('entryForm')
            else:
                owner = vt_owner.objects.create(regn_no = veh_no, owner_name = o_name, regn_dt = reg_dt, no_cyl = cyl_no, vh_class_id= veh_class)
                owner.save()
                #messages.info(request, "Success")
                return redirect('vehicleAll')
        else:
            messages.info(request, "Check entered data")
            return redirect('entryForm')
    else:
        return render(request, 'Veh_entry_2nd.html')

def base(request):    
    return render(request, "base_news.html")
