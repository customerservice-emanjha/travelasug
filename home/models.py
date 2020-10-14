from django.db import models

# Create your models here.

class SignUp(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    activity = models.CharField(max_length=800)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    otp = models.CharField(max_length=10)

class Review(models.Model):
    user_id = models.CharField(max_length=150)
    park_id = models.CharField(max_length=30)
    park_tag = models.CharField(max_length=20)
    overall = models.CharField(max_length=20)
    service = models.CharField(max_length=20)
    behaviour = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)
    user_nm = models.CharField(max_length=50,default='none')
    p_date = models.CharField(max_length=20)

class Imd_Review(models.Model):
    rid = models.CharField(max_length=150)
    img = models.ImageField(upload_to='review',
                              verbose_name='Image')

class Feedback(models.Model):
    nm = models.CharField(max_length=100)
    em = models.CharField(max_length=100)
    feed = models.CharField(max_length=2000)
    p_date = models.CharField(max_length=20)

class Wishlist(models.Model):
    p_id = models.IntegerField()
    tag = models.CharField(max_length=10)
    u_id = models.CharField(max_length=100)

class Trending(models.Model):
    p_id = models.CharField(max_length=100)
    tag = models.CharField(max_length=10)
    dt = models.CharField(max_length=100)
    qnt = models.IntegerField()

class Twitter(models.Model):
    p_id = models.IntegerField()
    twit_text = models.CharField(max_length=2500,default='none')
    dt = models.CharField(max_length=50,default='none')
    twit_count = models.CharField(max_length=20,default='none')
    twit_id = models.CharField(max_length=100,default='none')
    twit_img = models.CharField(max_length=200,default='none')
    twit_user1 = models.CharField(max_length=100,default='none')
    twit_user2 = models.CharField(max_length=100,default='none')
    twit_like = models.CharField(max_length=20,default='none')
    twit_date = models.CharField(max_length=100,default='02-09-2020')

class Park_hotel(models.Model):
    p_id = models.IntegerField()
    h_name = models.CharField(max_length=1000, default='none')
    h_img = models.CharField(max_length=500, default='none')
    km = models.FloatField()
    cat = models.CharField(max_length=200, default='none')

class Park_hotel_city(models.Model):
    h_name = models.CharField(max_length=1000, default='none')
    h_img = models.CharField(max_length=500, default='none')
    cat = models.CharField(max_length=200, default='none')
    city = models.CharField(max_length=200, default='none')

class Search_data(models.Model):
    p_id=models.IntegerField()
    loc = models.CharField(max_length=200, default='none')
    user = models.CharField(max_length=200, default='none')
