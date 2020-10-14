from django.urls import path, include
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('activity-data/<int:id>', views.activity_data, name='activity_data'),
path('facilities-data/<int:id>', views.facilities_data, name='facilities_data'),
path('park-detail/<int:id>', views.park_detail, name='park_detail'),
path('save-park', views.save_park, name='save_park'),
path('trending', views.trending, name='trending'),
path('message', views.message, name='message'),
path('feedback', views.feedback, name='feedback'),
path('faq', views.faq, name='faq'),
path('signin', views.signin, name='signin'),
path('signup', views.signup, name='signup'),
path('covid', views.covid, name='covid'),
path('virtual/<int:id>', views.virtual, name='virtual'),
path('virtual_list', views.virtual_list, name='virtual_list'),
path('nearby', views.nearby, name='nearby'),
path('usa_all_park', views.usa_all_park, name='usa_all_park'),
path('state_park/<str:id>', views.state_park, name='state_park'),
path('us_national_park/<str:id>', views.us_national_park, name='us_national_park'),
path('us_national_state/<str:id>', views.us_national_state, name='us_national_state'),
path('us_national_details/<str:id>', views.us_national_details, name='us_national_details'),
path('us_national_alpha/<str:id>', views.us_national_alpha, name='us_national_alpha'),
path('by_country', views.by_country, name='by_country'),
path('country_alphabet_in',views.country_alphabet_in, name='country_alphabet_in'),
path('logout1', views.logout1, name='logout1'),
path('review', views.review, name='review'),
path('wishlist', views.wishlist, name='wishlist'),
path('wishlist_delete', views.wishlist_delete, name='wishlist_delete'),
path('after_review/<str:tag>,<str:id>', views.after_review, name='after_review'),
path('wish_detail/<int:id>', views.wish_detail, name='wish_detail'),
path('wish_detail1/<int:id>', views.wish_detail1, name='wish_detail1'),
path('res_sidebar', views.res_sidebar, name='res_sidebar'),
path('news', views.google_news, name='google_news'),
path('search/<str:s>', views.search, name='search'),
path('google_news_api/<str:park_city>', views.google_news_api, name='google_news_api'),
path('park_hotel/<str:p_id>', views.park_hotel, name='park_hotel'),


















]
