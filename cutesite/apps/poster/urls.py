from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from django.contrib.auth.models import User
from models import Language, Code, Tag
from poster.views import code
from voting.views import vote_on_object


# Info for generic views.
base_generic_dict = {
    'paginate_by': 20,
    }

language_info_dict = dict(base_generic_dict,
                          queryset=Language.objects.all())

code_info_dict = dict(base_generic_dict,
                         queryset=Code.objects.all())

tag_info_dict = dict(base_generic_dict,
                     queryset=Tag.objects.all())

# Code
urlpatterns = patterns('',
                       (r'^(?P<code_id>\d+)/$', code.code_detail),
                       (r'^add/$', code.add_code),
                       (r'^edit/(?P<code_id>\d+)/$', code.edit_code),

    # Generic view to vote on Link objects
                       (r'(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$',
                        vote_on_object, dict(model=Code, template_object_name='code',
                                             allow_xmlhttprequest=True)),

)

# Generic views
urlpatterns += patterns('',
                        (r'^$', object_list, code_info_dict),
                        (r'^languages/$', object_list, language_info_dict),
                        )
