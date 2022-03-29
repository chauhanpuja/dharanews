from django.urls import path
from .import views


urlpatterns = [
        path('',views.index,name="index"),
        path('blog/category/<int:id>',views.blog,name="blog"),
        path('blog_details/<str:slug>',views.blog_details,name="blog_details"),
        path('userpost_details/<str:slug>',views.userpost_details,name="userpost_details"),
        path('userlogin',views.userlogin,name="userlogin" ),
        path('userlogout',views.userlogout,name="userlogout" ),
        path('usersignup',views.usersignup,name="usersignup" ),
        path('add_post',views.add_post,name="add_post" ),
        path('add_post2',views.add_post2,name="add_post2" ),
        path('post_list',views.post_list,name="post_list" ),
        path('edit_post2/<int:id>',views.edit_post2,name="edit_post2" ),
        path('delete_post/<int:id>',views.delete_post,name='delete_post'),
        # footer
        path('disclaimer',views.disclaimer,name="disclaimer" ),
        path('privacy_policy',views.privacy_policy,name="privacy_policy" ),
        path('terms_condition',views.terms_condition,name="terms_condition" ),
        path('fraud_alert',views.fraud_alert,name="fraud_alert" ),
        path('faq',views.faq,name="faq"),
        




]