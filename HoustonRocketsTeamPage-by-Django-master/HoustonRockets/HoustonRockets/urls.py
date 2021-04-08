"""HoustonRockets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rockets import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index, name='index'),
    url(r'^report$',views.report, name='report'),
    url(r'^original_template/',views.original_template, name='original_template'),
    url(r'^player/(?P<player>.+)/(?P<player_id>[0-9]+)/', views.player, name='player'),
    url(r'^players/', views.players, name='playerpage'),
    url(r'^matches/', views.matches, name='matchpage'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^about/', views.about, name='about'),
    url(r'^quiz/(?P<player_id>[0-9]+)/', views.exp, name='exp'),
    url(r'^match/(?P<match>.+)/(?P<match_id>[0-9]+)/', views.match_page, name='match_page'),
    url(r'^stats/', views.stats, name='stats'),
    url(r'^user_page/(?P<user_id>[0-9]+)/', views.user_page, name='userpage'),
    url(r'^match_video/(?P<match_id>[0-9]+)/', views.match_video, name='match_video'),
    url(r'^buy_ticket/(?P<match_id>[0-9]+)/', views.buy_ticket, name='buy_ticket'),
    url(r'^pre_match/', views.pre_match, name='prematchpage'),
    url(r'^next_match/', views.next_match, name='nextmatchpage'),
    url(r'^filter/', views.filtering),

]

# user account related
urlpatterns += [
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^logout/$', views.logout_view, name='logout'),
  url(r'^login/$', views.login_view, name='login'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
