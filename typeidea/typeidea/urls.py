"""typeidea URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views

import xadmin

from .custom_site import custom_site
from blog.views import (
    IndexView,
    PostDetailView,
    CategoryView,
    TagView,
    SearchView,
    AuthorView,
    LinkListView,
    CommentView,
    )
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap


urlpatterns = [
    url('^$', IndexView.as_view()),
    url('^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url('^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url('^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),

    url('^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),

    #
    url('^links/$', LinkListView.as_view(), name='links'),

    #
    url('^comment/$', CommentView.as_view(), name='comment'),

    # search
    url('^search/$', SearchView.as_view(), name='search'),

    # admin
    url(r'^admin/', admin.site.urls),
    url(r'^custom_admin/', custom_site.urls),

    # rss and sitemap
    url('^rss|feed/', LatestPostFeed(), name='rss'),
    url('^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),

    # xadmin
    url(r'^xadmin/', xadmin.site.urls, name='xadmin'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
