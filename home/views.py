from django.shortcuts import render, redirect
from emanjha_admin.models import Virtual, Activities, Facilities, Location_add, Categories,Usa_state
from django.contrib.auth.models import User, auth
from .models import  *
import ast
from django.http import JsonResponse
import json, requests
import urllib.request
import time
import reverse_geocoder as rg
# pip install reverse_geocoder
import pprint
import socket
# pip3 install js2py
from django.http import JsonResponse
from .mmail import tabmail
import random
from django.core.mail import BadHeaderError, send_mail
import datetime
from datetime import date
from GoogleNews import GoogleNews
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from math import sin, cos, sqrt, atan2, radians
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

# twitter api start here
import tweepy
from textblob import TextBlob
asecret = '9VK7wy1q8zeWsmoeflxRmitru3Xj2mPJQ1QaBzCWllhJa'
akey = '984689745581064192-iMSQFTTXhGK5Aezz8OYInicZSlp51st'
csecret = 'EZsRWFVZ814qaVWfjlyKErAvATPu0wHE1kyoDNka8DiTafwaTM'
ckey = 'LJRTLQkwzAVroGDmVJOlsIQjb'
def twitter(twitloc,id):
    Twitter.objects.all().delete()
    twit_data1 = Twitter.objects.filter(p_id=id)
    twit_data = twit_data1.count()
    if twit_data == 0:
        auth = tweepy.OAuthHandler(ckey,csecret)
        auth.set_access_token(akey,asecret)
        api = tweepy.API(auth)
        public_tweets = tweepy.Cursor(api.search, q=twitloc).items(10)
        for twit in public_tweets:
            twit_text = twit.text
            twit_count = twit.retweet_count
            twit_id = twit.id
            # twit_img = twit.__dict__['_json']['entities']['media'][0]['media_url']
            twit_img = twit.user.profile_image_url
            # twit_user1 = twit.__dict__['_json']['entities']['user_mentions'][0]['name']
            twit_date = twit.created_at
            twit_user2 = twit.user.name
            twit_like = twit.favorite_count
            dt = date.today()
            twit_insert = Twitter(p_id=id,twit_text=twit_text,dt=dt,twit_count=twit_count,twit_id=twit_id,twit_img=twit_img,twit_user2=twit_user2,twit_like=twit_like,twit_date=twit_date).save()

        twitter_data = Twitter.objects.filter(p_id=id)
    else:
        twitter_data = twit_data1
    return twitter_data
#xxxxxxx-------end-------xxxxxxx

# XXXXXXXXXXX------------SEARCH DATA-----------XXXXXXXXXXXXXXX
def search(request,s):
    search = Location_add.objects.filter(name__icontains=s)
    return render(request,'search.html',{'search':search})

# XXXXXXXXXXX------------END SEARCH------------XXXXXXXXXXXXXXX

# XXXXXXXXXXX-----------DISTANCE FROM LAT,LONG------XXXXXXXX
def get_distance(lat1, lon1, lat2, lon2):
	R = 6373.0
	lat1 = radians(lat1)
	lon1 = radians(lon1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return round(distance, 2)
# XXXXXXXXX-----------END---------------XXXXXXXXXXX



# XXXXXXXXXXX-----------START HOTEL SECTION--------XXXXXXXXXXXX
def park_hotel(request,p_id):
    # Park_hotel.objects.all().delete()
    p_id = int(p_id)
    location_single = Location_add.objects.filter(id=p_id)
    for loc in location_single:
        park_loc = loc.city
        logitude = loc.logitude
        latitude = loc.latitude

    park_data1 = Park_hotel.objects.filter(p_id=p_id)
    park_data = park_data1.count()
    a = []
    if park_data == 0:
        url = "https://tripadvisor1.p.rapidapi.com/locations/search"
        querystring = {"location_id":"1","limit":"20","sort":"relevance","offset":"0","lang":"en_US","currency":"USD","units":"km","query":park_loc}
        headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "6627e8d370mshd8cc18968140872p16f9c5jsnf6009960500f"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        park_json = response.text
        hoteldata = json.loads(park_json)['data']
        z = 0

        for i in hoteldata:
            m = hoteldata[z]['result_object']
            try:
                h_img = m['photo']['images']['large']['url']
                h_name = m['name']
                lat2 = m['latitude']
                lon2 = m['longitude']
                cat = m['category']['key']
            except KeyError:
                pass
            # Main Function
            km = get_distance(float(latitude),float(logitude),float(lat2),float(lon2))
            km = km/1.609344
            hotel_insert = Park_hotel(p_id=p_id,h_name=h_name,h_img=h_img,km=km,cat=cat).save()
            z = z+1

        hotel_data = Park_hotel.objects.filter(p_id=p_id).order_by('km')
    else:
        hotel_data = park_data1.order_by('km')
    return render(request,'park_api_data.html',{'hotel_api':hotel_data})
# XXXXXXXXXXX----------END HOTEL SECTION-----------XXXXXXXXXXXX

# XXXXXXXXXXX-----------START BY CITY HOTEL SECTION--------XXXXXXXXXXXX
def park_city(city):
    # Park_hotel.objects.all().delete()
    park_city1 = Park_hotel_city.objects.filter(city=city)
    park_city = park_city1.count()
    a = []
    if park_city == 0:
        url = "https://tripadvisor1.p.rapidapi.com/locations/search"
        querystring = {"location_id":"1","limit":"20","sort":"relevance","offset":"0","lang":"en_US","currency":"USD","units":"km","query":city}
        headers = {
        'x-rapidapi-host': "tripadvisor1.p.rapidapi.com",
        'x-rapidapi-key': "6627e8d370mshd8cc18968140872p16f9c5jsnf6009960500f"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        park_json = response.text
        hoteldata = json.loads(park_json)['data']
        z = 0

        for i in hoteldata:
            m = hoteldata[z]['result_object']
            try:
                h_img = m['photo']['images']['large']['url']
                h_name = m['name']
                cat = m['category']['key']
            except KeyError:
                pass
            # Main Function

            hotel_insert = Park_hotel_city(h_name=h_name,h_img=h_img,cat=cat,city=city).save()
            z = z+1

        hotel_city = Park_hotel_city.objects.filter(city=city)
    else:
        hotel_city = park_city1
    return hotel_city
# XXXXXXXXXXX----------END HOTEL BY CITY SECTION-----------XXXXXXXXXXXX


# XXXXX------Side bar load----XXXXXXX
def res_sidebar(request):
    return render(request,'res_sidebar.html')
# XXXXXX------END------XXXXXX
# login
def signin(request):
    if request.method=='POST':
        em=request.POST['em']
        ps=request.POST['ps']
        # send_mail('subject', 'tabish', 'tabishadnan9@gmail.com', ['tabishadnan8@gmail.com'])
        user = auth.authenticate(username=em,password=ps)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request,'signin.html',{'msg':'User Name Not Exits..!'})

    else:
        return render(request,'signin.html')
# end
# XXXXXXXXX---------SIGN-UP-------XXXXXXXXXXXX
def signup(request):
    if request.method == 'POST':
        nm = request.POST.get('nm')
        ps = request.POST.get('ps')
        em = request.POST.get('em')
        activity = request.POST.getlist('activity')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        otp = random.randint(0,9999)
        # activities convert into list
        a1 = []
        for ax in activity:
            aa1 = ast.literal_eval(ax)
            ad = int(aa1)
            a1.append(ad)
            # end

        # tabmail(em,otp)
        insert = SignUp(name=nm,password=ps,email=em,activity=a1,city=city,state=state,country=country,otp=otp)
        insert.save()
        if User.objects.filter(username=em).exists():
            return render(request,'signup.html',{'msg':'User Name Exits..!'})
        else:
            user = User.objects.create_user(username=em,password=ps,email=em,first_name=nm,is_superuser=0)
            user.save()
            auth.login(request, user)
            return render(request, 'signup.html',{'msg':'Registered Successfully...'})

    activity = Activities.objects.all().order_by('-id')
    return render(request, 'signup.html',{'activity_data':activity})


def logout1(request):
    auth.logout(request)
    return redirect('/')
# XXXXX------END------XXXXXX

# XXXX----IMAGE REVIEW----XXXXX
def img_review():
    image1 = Imd_Review.objects.all()
    return  image1
# XXXX----END----XXXX

# wishlist function fetch
def wish_fetch():
    wish_fetch1 = Wishlist.objects.all()
    return  wish_fetch1
# end
#XXXXX--------WEATHER------XXXXXXXXX
def cweather(city):
    api_key = "0c60c309811553f3e83e6d5f66032080"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    y = x['main']
    a = x['wind']
    v = x['visibility']
    w = x['weather'][0]
    return y,a,v,w

# XXXXXX-----END WEATHER------XXXXXXX
# XXXXXX------GOOGLE API FOR NEWS-----XXXXXXX
def google_news_api(request,park_city):
    park_name = park_city
    googlenews = GoogleNews()
    googlenews = GoogleNews('en','d')
    googlenews.search(park_name)
    googlenews.getpage(1)
    a = googlenews.result()
    if not a:
        googlenews.search(park_city)
        googlenews.getpage(1)
        b = googlenews.result()
    else:
        b = a
    res_list = []
    for i in range(len(b)):
        if b[i] not in b[i + 1:]:
            res_list.append(b[i])
    return render(request,'news_update.html',{'news_api':res_list})
# XXXXXXX--------END-------XXXXXX
# XXXXXXX-------COUNTRY IP DATA ----XXXXX
def country_ip():
    with urllib.request.urlopen("https://ipinfo.io/json") as url:
        data = json.loads(url.read().decode())
        cnt = data['country']
        return cnt

#   xxxxx------end-----xxxxx
def home(request):
    # Park_hotel.objects.all().delete()
    virtual = Virtual.objects.all()
    activity = Activities.objects.all()
    facility = Facilities.objects.all()
    country_ip1 = country_ip()

    IPAddr = socket.gethostbyname("google.com")
    print("Your Computer IP Address is:" + IPAddr)

# XXXXXXXXXX-----------NEAR BY SECTION--------XXXXXXXXXX
    return render(request,'home.html',{'virtual':virtual,'activity':activity,'facility':facility,'country':country_ip1,'IPAddr':IPAddr})

# XXXXXX------END------XXXXXX

def nearby(request):
    # XXXXXXXXXX-----------NEAR BY SECTION--------XXXXXXXXXX
    # g-map api : AIzaSyAiqlCyo-hqpavT5JRjZ-Rwr1KbG0NtIig
    if request.method=='POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        near = Location_add.objects.all()
        city = []
        for n in near:
            lon2 = float(n.logitude)
            lat2 = float(n.latitude)
            km = get_distance(float(lat),float(lon),float(lat2),float(lon2))
            print('km',km)
            if km < 100:
                city.append(n.city)
                break

        # url2 = "https://maps.googleapis.com/maps/api/geocode/json?"
        # url2 += "latlng=%s,%s&sensor=false,&key=AIzaSyAiqlCyo-hqpavT5JRjZ-Rwr1KbG0NtIig" % (lat,lon)
        # v = urllib.request.urlopen(url2)
        # j = json.loads(v.read())
        # # components = j['results'][4]['address_components']
        # # state=components[3]['long_name']
        state=city[0]
        if len(city) !=0:
            live_data = park_city(state)
        else:
            live_data = near

        return render(request,'nearyou.html',{'near':near,'state':state,'live_data':live_data})


    # XXXXXX------END------XXXXXX

# XXXXXXXXXXXXX-----START ACTIVITY DATA-----XXXXXXXXXXXX
def activity_data(request,id):
    location = Location_add.objects.all()
    lid = []
    for i in location:
        location_act = i.activity
        id1 = i.id
        location_activity = location_act.strip('][').split(', ')

        for a in location_activity:
            a = int(a)
            if a  == id:
                lid.append(id1)


    new_location = Location_add.objects.all().filter(pk__in=lid)
    Search_data1 = Search_data.objects.all()
    print('Search_data : ',Search_data1)
    country_ip1 = country_ip()
    return render(request,'activity_data.html',{'location':new_location,'id':id,'country':country_ip1})
# XXXXXX-----END ACTIVITY DATA-----XXXXXXX

# XXXXXXXXXXXXX-----START Facilities DATA-----XXXXXXXXXXXX
def facilities_data(request,id):
    location = Location_add.objects.all()
    lid = []
    for i in location:
        location_act = i.facility
        id1 = i.id
        location_activity = location_act.strip('][').split(', ')

        for a in location_activity:
            a = int(a)
            if a  == id:
                lid.append(id1)

    new_location = Location_add.objects.all().filter(pk__in=lid)

    wish_data = wish_fetch()
    country_ip1 = country_ip()
    return render(request,'activity_data.html',{'location':new_location,'wish_fetch':wish_data,'country':country_ip1})
# XXXXXX-----END Facilities DATA-----XXXXXXX

# XXXXXXXXXXXXXX-----START PARK DETAILS DATA-----XXXXXXXXXXXXXXX
def park_detail(request,id):
        location_single = Location_add.objects.filter(id=id)

        for cat_id in location_single:
            location_cat = cat_id.category
            location_category = location_cat.strip('][').split(', ')

            location_fat = cat_id.facility
            location_facility = location_fat.strip('][').split(', ')

            location_act = cat_id.activity
            location_activity = location_act.strip('][').split(', ')
            location_city = cat_id.city
            park_name = cat_id.name
            logitude = cat_id.logitude
            latitude = cat_id.latitude

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

        #XXXXXXX-------Recommended section start--------XXXXXXXXX
        location = Location_add.objects.all()
        lid = []
        for i in location:
            location_act = i.activity
            id1 = i.id
            location_activity = location_act.strip('][').split(', ')

            for a in location_activity:
                a = int(a)
                if a  == act_l[0]:
                    lid.append(id1)

        recomm_loc = Location_add.objects.all().filter(pk__in=lid)
        # XXXXXXXX--------END-------XXXXX

        review = Review.objects.all().filter(park_tag='local',park_id=id)
        image = img_review()
        review_count = Review.objects.filter(park_id=id).count()

        #xxxxx------trending section------xxxxx
        trend_insert(id,'home')
        #xxxxx-----end-----xxxxx
        # XXXX----WEATHER----XXXXXX
        wther = cweather(location_city)
        # XXXXX-----END-----XXXXXX

        # xxxx------twitter api----xxxxxxx
        twit_api = twitter(park_name,id)
        # xxxxxx-------end------xxxxxx

        # XXXXXXXX--------SEARCH DATA INSERT-------XXXXXXXXXXX
        u = request.user.is_authenticated
        if u:
            user = User.objects.get(username=request.user.username)
            Search_data(user=user,p_id=id,loc=location_city).save()
        # XXXXXXXXX---------END----------XXXXXXXXXX
        random1 = random.randint(1,5)

        return render(request,'park_detail.html',{'location_single':location_single,'cat_id':cat_data,'fat_id':fat_data,'act_id':act_data,'id':id,'review':review,'tag':'local','image':image,'r_cnt':review_count,'recomm_loc':recomm_loc,'random':random1,'wther':wther,'twit_api':twit_api})

# XXXXXX-----END PARK DETAILS DATA-----XXXXXXX

# XXXXXXXX-------USA ALL PARK-------XXXXXXXXXXXX
def usa_all_park(request):
    us_state = Usa_state.objects.all()

    return render(request,'usa_all_park.html',{'state_name':us_state})

# XXXX-----END----XXXXX

# XXXXXXXX-------USA state_park PARK-------XXXXXXXXXXXX
def state_park(request,id):
    near = Location_add.objects.all()
    return render(request,'nearyou.html',{'near':near,'state':id})

# XXXX-----END----XXXXX

def message(request):
    return render(request, 'message.html')


def faq(request):
    return render(request, 'faq.html')

def covid(request):
    return render(request, 'covid.html')

def virtual(request,id):
    data = Virtual.objects.all().filter(id=id)
    return render(request, 'virtualdata.html',{'data':data})

def virtual_list(request):
    virtual = Virtual.objects.all()
    return render(request,'virtual_list1.html',{'virtual':virtual})

# XXXXXX--------US NATIONAL STATE-----XXXXXXX
def us_national_park(request,id):
    if id == 'state':
        us_state = Usa_state.objects.all()
        return render(request,'us_national_park.html',{'state_name':us_state})
    else:
        return render(request,'us_alphabet.html')


def us_national_state(request,id):
    us_state = Usa_state.objects.filter(id=id)
    for u in us_state:
        url1 = u.api_url
        s_name = u.name

    r = requests.get(url1)
    data = r.json()

    return render(request,'us_national_state.html',{'state_name':data['data'],'s_name':s_name})

def us_national_details(request,id):
    r = requests.get(f'https://mychaps.net/us-state-single-api/{id}')
    data1 = r.json()
    data = data1['data']

    #XXXXXX--------Reccommend section start here-------XXXXXX
    act_data = Activities.objects.all()
    activity_id_list = []
    park_name = []
    location_city = []
    for d in data:
        park_name.append(d['fullName'])
        location_city.append(d['addresses'][1]['city'])
        for z in d['activities']:
            nps_activity = z['name']
            for main_activity in act_data:
                main_activity1 = main_activity.name
                hist = main_activity.history
                if main_activity1.lower() == nps_activity.lower():
                    activity_id_list.append(hist)

    #XXXXXXX-------Recommended section start--------XXXXXXXXX

    recomm_loc = Location_add.objects.all().filter(city=location_city[0])
    # XXXXXXXX--------END-------XXXXX

    review = Review.objects.all().filter(park_tag='nsp',park_id=id)
    image = img_review()
    review_count = Review.objects.filter(park_id=id).count()
    #xxxxx------trending section------xxxxx
    trend_insert(id,'nsp')
    #xxxxx-----end-----xxxxx
    # XXXX----WEATHER----XXXXXX
    wther = cweather(location_city[0])
    # XXXXX-----END-----XXXXXX
    # xxxxx----google new api----xxxxx
    news_api = google_news_api(park_name[0],location_city[0])
    # xxxx-----end-----xxxxx
    return render(request,'us_national_details.html',{'state_name':data,'id':id,'tag':'nsp','review':review,'image':image,'r_cnt':review_count,'recomm_loc':recomm_loc,'news_api':news_api,'wther':wther})

def us_national_alpha(request,id):
    r = requests.get(f'https://mychaps.net/us-state-alphabet-api/{id}')
    data1 = r.json()
    data = data1['data']
    return render(request,'us_national_state.html',{'state_name':data})

# XXXXXX------END------XXXXXXX

# XXXXXXXXXXXXX--------COUNTRY WISE------XXXXXXXXXX
def by_country(request):
    return render(request,'by_country.html')

def country_alphabet_in(request):
    return render(request,'country_alphabet_in.html')


# XXXXXXXXXX-------END-------XXXXXXXX

# XXXXXXXXXX----------review---------XXXXXXXXXXXX
def review(request):
    if request.method == 'POST':
        overall = int(request.POST.get('overall',1))
        behav = int(request.POST.get('behaviour',1))
        service = int(request.POST.get('service',1))
        comt = request.POST.get('comt')
        img = request.FILES.getlist('img')
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        user_id = request.POST.get('user_id')
        user_nm = request.POST.get('user_nm')
        p_date = datetime.date.today()

        insert = Review(user_id=user_id,park_id=id,park_tag=tag,overall=overall,service=service,behaviour=behav,comment=comt,p_date=p_date,user_nm=user_nm)
        insert.save()
        rid = insert.id
        for f in img:
            print('rid:',rid)
            photo = Imd_Review(rid=int(rid), img=f)
            photo.save()

        return redirect(f'after_review/{tag},{id}')
        # if tag == 'old':
        #     return redirect(f'nearby-data/{id}',{'msg':'inserted Successfully'})
        # elif tag == 'nsp':
        #     return redirect(f'us_national_details/{id}',{'msg':'inserted Successfully'})
        # else:
        #     return redirect(f'park-detail/{id}')


    else:
        return render(request, 'home.html')

def after_review(request,tag,id):
    if tag == 'nsp':
        id = str(id)
    else:
        id = int(id)
    review = Review.objects.all().filter(park_tag=tag,park_id=id).order_by('-id')
    image = img_review()
    review_count = Review.objects.filter(park_id=id).count()
    return render(request, 'after_review.html',{'review':review,'image':image,'review_count':review_count,'tag':tag,'id':id})


# XXXXXXXX--------END-------XXXXXXXXXX

# XXXXXXXXXXXXX--------Feedback-------XXXXXXXXXXXXX
def feedback(request):
    if request.method == 'POST':
        nm = request.POST.get('nm')
        em = request.POST.get('em')
        feed =request.POST.get('feed')
        p_date = datetime.date.today()
        Feedback(nm=nm,em=em,feed=feed,p_date=p_date).save()
    return render(request, 'feedback.html')
# XXXX-----END-----XXXXXX

# XXXXXXXX--------WISHLIST-------XXXXXXXXXXXX
def wishlist(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        user = request.POST.get('user')
        Wishlist(p_id=id,tag=tag,u_id=user).save()
    return render(request, 'feedback.html')

def save_park(request):
    user = User.objects.get(username=request.user.username)
    w_list = []
    a = []
    wish_data = Wishlist.objects.all().filter(u_id=user)
    for w in wish_data:
        if w.tag == 'old':
            aa = w.p_id
            a.append(aa)
        w_list.append(w.p_id)
    new_location = Location_add.objects.all().filter(pk__in=w_list)



    return render(request,'save_park.html',{'location':new_location,'api_id':a})

def wishlist_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        user = request.POST.get('user')
        Wishlist.objects.all().filter(p_id=id,u_id=user).delete()
        return render(request,'save_park.html')
    return render(request,'wish_detail.html')

# wish detail here
def wish_detail(request,id):
    user = User.objects.get(username=request.user.username)
    wish_data = Wishlist.objects.all().filter(u_id=user,p_id=id).count()

    return render(request,'wish_detail.html',{'wish_data':wish_data,'id':id,'z':wish_data})

def wish_detail1(request,id):
    user = User.objects.get(username=request.user.username)
    wish_data = Wishlist.objects.all().filter(u_id=user,p_id=id).count()

    return render(request,'wish_detail1.html',{'wish_data':wish_data,'id':id,'z':wish_data})

# end
# XXXXXXXXXX----------Trending-------XXXXXXXXX
def trending(request):
    trend = Trending.objects.all().filter(qnt__gte=3)
    hm_list = []
    old_list = []
    nsp_list = []

    for w in trend:
        if w.tag == 'home':
            a1 = w.p_id
            hm_list.append(a1)
        elif w.tag == 'old_api':
            a2 = w.p_id
            old_list.append(a2)
        else:
            a3 = w.p_id
            nsp_list.append(a3)

    new_location = Location_add.objects.all().filter(pk__in=hm_list)


    return render(request,'most_view.html',{'location':new_location,'api_id':old_list})

def trend_insert(pid,tag):
    p_date = datetime.date.today()
    trend = Trending.objects.filter(p_id=pid,tag=tag)
    if trend.count() == 0:
        insert = Trending(p_id=pid,tag=tag,dt=p_date,qnt=1).save()
    else:
        for t in trend:
            q = t.qnt
            q = q+1
            update = Trending.objects.filter(p_id=pid,tag=tag).update(qnt=q)
#XXXX------END------XXXXXXX

# XXXXXXX--------GOOGLE NEWS-------XXXXXXXXXX
def google_news(request):
    return render(request,'google_news.html')
# XXXXXXXX-------END-------XXXXXXXX
