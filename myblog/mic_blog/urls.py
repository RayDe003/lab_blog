from django.urls import path
from . import views
from .views import signup, signin, profile, edit_profile, delete_profile, user_list, user_profile, post_detail, \
    comment_edit, comment_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('profile/', profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('user_list/', user_list, name='user_list'),
    path('profile/<int:user_id>/', user_profile, name='user_profile'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('comment/<int:comment_id>/edit/', comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/', comment_delete, name='comment_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)