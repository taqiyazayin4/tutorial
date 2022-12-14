from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_json_by_id #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_xml_by_id
from wishlist.views import register #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import login_user
from wishlist.views import logout_user 
from wishlist.views import show_ajax
from wishlist.views import create_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #sesuaikan dengan nama fungsi yang dibuat
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_ajax, name='show_ajax'),
    path("ajax/submit", create_ajax, name="create_ajax"),
]