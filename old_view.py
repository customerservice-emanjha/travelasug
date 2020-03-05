from django.shortcuts import render
from .models import Facilities, Activities, Categories, Api_document, Location_add
from .serializers import FacilitiesSerializer, ActivitiesSerializer, CategoriesSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from array import *
import json, requests
import ast
# Admin Panel Dashboad section start here
def dashboard(request):
    return render(request,'dashboard.html')

# Admin Panel Dashboard end here


# XXXXXXXX---------  Start Facilities Section --------XXXXXXXXX

 # Facilities API start here
class FacilitiesView(viewsets.ModelViewSet):
    """API URLS FOR VIEW Facilities API : http://127.0.0.1:8000/facilities_api"""
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializer
 # Facilities API END

def facilities(request):
    # Here we do Facilities add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        image = request.FILES.get('image','image_empty')
        insert = Facilities(name=name,image=image)
        insert.save()
        return render(request,'facilities.html',{'msg':'Facilities Added Successfully..'})
        # end Facilities add to db section
    else:
        data = Facilities.objects.all().order_by('-id')
        return render(request,'facilities.html',{'data':data})

    # facilities_delete section start
def facilities_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Facilities.objects.filter(id=id).delete()
        return render(request,'facilities.html',{'msg':'Facilities Deleted Successfully..'})
    # end facilities_delete section

# XXXXXXXX------- End Facilities -------XXXXXXXXX

# XXXXXXXXXX------- Start Activities Section -------XXXXXXXXXX

# Activities API start here
class ActivitiesView(viewsets.ModelViewSet):
   """API URLS FOR VIEW Activities API : http://127.0.0.1:8000/activities_api"""
   queryset = Activities.objects.all()
   serializer_class = ActivitiesSerializer


# print(green.queryset)
# def testing(request):
#     '''this is only for testing  our code'''
#     x = requests.get("http://127.0.0.1:8000/categories_api/")
#     m = {'name':x,'num':'97364'}
#     # l = json.dumps(m)
#
#     print(m)
#     return HttpResponse(m)
# end code tester
 # Activities API END
def activities(request):
    # Here we do Activities add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        image = request.FILES.get('image','image_empty')
        insert = Activities(name=name,image=image)
        insert.save()
        return render(request,'activities.html',{'msg':'Activities Added Successfully..'})
        # end Activities add to db section
    else:
        data = Activities.objects.all().order_by('-id')
        return render(request,'activities.html',{'data':data})

    # Activities delete section start
def activities_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Activities.objects.filter(id=id).delete()
        return render(request,'activities.html',{'msg':'Activities Deleted Successfully..'})
    # end Activities delete section

#  XXXXXXX-------- End Activities -------XXXXXXX


# XXXXXXXX---------  Start Categories Section --------XXXXXXXXX

 # Categories API start here
class CategoriesView(viewsets.ModelViewSet):
    """API URLS FOR VIEW Categories API : http://127.0.0.1:8000/categories_api"""
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
 # Categories API END

def categories(request):
    # Here we do Categories add to db section
    if request.method =='POST':
        name = request.POST.get('name','empty')
        image = request.FILES.get('image','image_empty')
        insert = Categories(name=name,image=image)
        insert.save()
        return render(request,'categories.html',{'msg':'Categories Added Successfully..'})
        # end Categories add to db section
    else:
        data = Categories.objects.all().order_by('-id')
        return render(request,'categories.html',{'data':data})

    # Categories_delete section start
def categories_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete = Categories.objects.filter(id=id).delete()
        return render(request,'categories.html',{'msg':'Categories Deleted Successfully..'})
    # end Categories_delete section

# XXXXXXXX------- End Categories -------XXXXXXXXX

# XXXXXXXXXX-------API DOCUMENTS SECTION START-------XXXXXXXXXXXX

def api_document(request):
    if request.method =='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        api_url = request.POST.get('api_url')
        insert = Api_document(name=name,desc=desc,api_url=api_url).save()
        return render(request,'document.html',{'msg':'Documents Added Successfully....!'})
    else:
        data = Api_document.objects.all()
        return render(request,'document.html',{'data':data})

# XX---END DOCUMENY---XX

# XXXXXX---------START LOCATION Section------------XXXXXXXXXXXXXX

#XXXXXX-------Start all Location Section----XXXXX
def location(request):
    location_data = Location_add.objects.all().order_by('-id')
    return render(request,'location.html',{'data':location_data})

#XXX----End all Location---XXX

#XXX---Start single-location Section---XXX
def single_location(request, id):
    location_single = Location_add.objects.all().filter(id=id)


    for cat_id in location_single:
        location_cat = cat_id.category
        location_category = location_cat.strip('][').split(', ')

        location_fat = cat_id.facility
        location_facility = location_fat.strip('][').split(', ')

        location_act = cat_id.activity
        location_activity = location_act.strip('][').split(', ')

    cat_l = []
    fat_l = []
    act_l = []

#XXX---getting category filter data---XXX
    for cx in location_category:
        ca1 = ast.literal_eval(cx)
        cd = int(ca1)
        cat_l.append(cd)
    cat_data = Categories.objects.all().filter(pk__in=cat_l)
# XXX----END-----XXXX

#XXX---getting facility filter data---XXX
    for fx in location_facility:
        fa1 = ast.literal_eval(fx)
        fd = int(fa1)
        fat_l.append(fd)
    fat_data = Facilities.objects.all().filter(pk__in=fat_l)
# XXX----END-----XXXX

#XXX---getting Activities filter data---XXX
    for ax in location_activity:
        aa1 = ast.literal_eval(ax)
        ad = int(aa1)
        act_l.append(ad)
    act_data = Activities.objects.all().filter(pk__in=act_l)
# XXX----END-----XXXX

    return render(request,'single-location.html',{'location_single':location_single,'cat_id':cat_data,'fat_id':fat_data,'act_id':act_data})



#XXX---End single-location---XXX

#XXXX-----START ADD LOCATION SECTION----XXXXX
def add_location(request):
    if request.method == 'POST':
        name = request.POST.get('name','name_empty')
        city = request.POST.get('city','city_empty')
        state = request.POST.get('state','state_empty')
        country = request.POST.get('country','country_empty')
        zipcode = request.POST.get('zipcode','zipcode_empty')
        address = request.POST.get('address','address_empty')
        logitude = request.POST.get('logitude','logitude_empty')
        latitude = request.POST.get('latitude','latitude_empty')
        overview = request.POST.get('overview','name_empty')
        categories = request.POST.getlist('category','category_empty')
        facilities = request.POST.getlist('facility','facility_empty')
        activities = request.POST.getlist('activity','activity_empty')
        thumbnail1 = request.FILES.get('thumbnail1','thumbnail1_empty')
        thumbnail2 = request.FILES.get('thumbnail2','thumbnail2_empty')
        thumbnail3 = request.FILES.get('thumbnail3','thumbnail3_empty')
        other1 = request.FILES.get('other1','other1_empty')
        other2 = request.FILES.get('other2','other2_empty')
        other3 = request.FILES.get('other3','other3_empty')
        # category convert into list
        c1 = []
        for cx in categories:
            ca1 = ast.literal_eval(cx)
            cd = int(ca1)
            c1.append(cd)
            # end
        # activities convert into list
        a1 = []
        for ax in activities:
            aa1 = ast.literal_eval(ax)
            ad = int(aa1)
            a1.append(ad)
            # end

        # facilities convert into list
        f1 = []
        for fx in facilities:
            fa1 = ast.literal_eval(fx)
            fd = int(fa1)
            f1.append(fd)
            # end

        Location_add(name=name,city=city,state=state,country=country,zipcode=zipcode,address=address,logitude=logitude,
        latitude=latitude,overview=overview,category=c1,facility=f1,activity=a1,
        thumbnail1=thumbnail1,thumbnail2=thumbnail2,thumbnail3=thumbnail3,other1=other1,
        other2=other2,other3=other3).save()
        return render(request,'add_location.html',{'msg':'Location Added Successfully..!'})

    else:
        facility = Facilities.objects.all().order_by('-id')
        activity = Activities.objects.all().order_by('-id')
        category = Categories.objects.all()
        return render(request,'add_location.html',{'facility_data':facility,'activity_data':activity,'category_data':category})

#XXX---END ADD LOCATION SECTION---XXX

# location_delete section start
def location_delete(request,id):
    delete = Location_add.objects.filter(id=id).delete()
    return render(request,'location.html',{'msg':'Deleted Successfully..'})
# end location_delete section
# XXXXXXXXXX--------END LOCATION Section---------XXXXXXXXXXX
