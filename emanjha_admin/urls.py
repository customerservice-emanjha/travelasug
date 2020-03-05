from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('facilities_api',views.FacilitiesView)
router.register('activities_api',views.ActivitiesView)
router.register('categories_api',views.CategoriesView)
router.register('location_api',views.LocationView)




urlpatterns = [
# path('testing', views.testing, name='testing'),

path('', views.dashboard, name='dashboard'),
path('api_document', views.api_document, name='api_document'),
path('', include(router.urls)),

# XXXXX-----FACILITIES SECTION FOR URL-----XXXXXX
path('facilities', views.facilities, name='facilities'),
path('facilities_delete', views.facilities_delete, name='facilities_delete'),
path('facilities_update', views.facilities_update, name='facilities_update'),

# XXX--END FACILITIES Section--XXX

# XXXXX-----Activities SECTION FOR URL-----XXXXXX
path('activities', views.activities, name='activities'),
path('activities_delete', views.activities_delete, name='activities_delete'),
path('activities_update', views.activities_update, name='activities_update'),
# XXX--END Activities Section--XXX

# XXXXX-----Categories SECTION FOR URL-----XXXXXX
path('categories', views.categories, name='categories'),
path('categories_delete', views.categories_delete, name='acategories_delete'),
path('categories_update', views.categories_update, name='categories_update'),
# XXX--END Categories Section--XXX

# XXXXXX-------LOCATION SECTION START-------XXXXXXXX
path('location', views.location, name='location'),
path('add_location',views.add_location, name='add location'),
path('single-location/<int:id>', views.single_location, name='single_location'),
path('location_delete/<int:id>', views.location_delete, name='location_delete'),

# XXX----END LOCATION Section---XXXX

]
