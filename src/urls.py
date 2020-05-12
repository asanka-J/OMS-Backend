from django.contrib import admin
from django.urls import path , include
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from src.accounts.views import (index ,test ,not_available ,about, faq , register, login, comming_soon,
    forgot_password, customer_dashboard, logout)
from django.views.generic import RedirectView
from django.views.generic import TemplateView



from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('',index, name='home-page'),
    path('dashboard/', include('src.dashboard.urls')),
    path('category/', include('src.product.urls') ),
    path('test/',test, name='test-page'),
    path('404/',not_available, name='404-page'),
    path('about/',about, name='about-page'),
    path('faq/',faq, name='faq-page'),
    path('register/',register, name='register-page'),
    path('login/',login, name='login-page'),
    path('login/',login, name='login-page'),
    path('forgot-password/',forgot_password, name='forgot-password'),
    path('my-account/',customer_dashboard, name='my-account'),
    path('logout/',logout, name='logout'),
    



    path('comming-soon/',comming_soon, name='comming-soon'),





    
   



]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
