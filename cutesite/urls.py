from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from account.openid_consumer import PinaxConsumer
from microblogging.feeds import TweetFeedAll, TweetFeedUser, TweetFeedUserWithFriends


tweets_feed_dict = {"feed_dict": {
    'all': TweetFeedAll,
    'only': TweetFeedUser,
    'with_friends': TweetFeedUserWithFriends,
}}

if settings.ACCOUNT_OPEN_SIGNUP:
    signup_view = "account.views.signup"
else:
    signup_view = "signup_codes.views.signup"


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "homepage.html"}, name="home"),

    url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user', name="admin_invite_user"),
    url(r'^account/signup/$', signup_view, name="acct_signup"),

    (r'^cute/', include('poster.urls')),

    (r'^about/', include('about.urls')),
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),
    (r'^bbauth/', include('bbauth.urls')),
    (r'^authsub/', include('authsub.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^tags/', include('tag_app.urls')),
    (r'^invitations/', include('friends_app.urls')),
    (r'^notices/', include('notification.urls')),
    (r'^messages/', include('messages.urls')),
    (r'^announcements/', include('announcements.urls')),
    (r'^tweets/', include('microblogging.urls')),
    (r'^comments/', include('threadedcomments.urls')),
    (r'^robots.txt$', include('robots.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^admin/(.*)', admin.site.root),
    (r'^avatar/', include('avatar.urls')),
    (r'^flag/', include('flag.urls')),
    (r'^locations/', include('locations.urls')),

    (r'^feeds/tweets/(.*)/$', 'django.contrib.syndication.views.feed', tweets_feed_dict),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'staticfiles.views.serve')
    )

from microblogging.models import Tweet

friends_tweets_kwargs = {
    "template_name": "microblogging/friends_tweets.html",
    "friends_objects_function": lambda users: Tweet.objects.filter(sender_id__in=[user.id for user in users], sender_type__name='user'),
}

urlpatterns += patterns('',
#    url('^photos/friends_photos/$', 'friends_app.views.friends_objects', kwargs=friends_photos_kwargs, name="friends_photos"),
#    url('^blog/friends_blogs/$', 'friends_app.views.friends_objects', kwargs=friends_blogs_kwargs, name="friends_blogs"),
    url('^tweets/friends_tweets/$', 'friends_app.views.friends_objects', kwargs=friends_tweets_kwargs, name="friends_tweets"),
#    url('^bookmarks/friends_bookmarks/$', 'friends_app.views.friends_objects', kwargs=friends_bookmarks_kwargs, name="friends_bookmarks"),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'staticfiles.views.serve')
    )
