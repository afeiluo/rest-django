from django.urls import include, path
from rest_framework import routers
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial import views
from snippets import views as snippet_views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('snippets/', snippet_views.snippet_list),
    path('snippets/<int:pk>/', snippet_views.snippet_detail),
    path('snippets/wrap', snippet_views.wrap_snippet_list),
    path('snippets/wrap/<int:pk>/', snippet_views.wrap_snippet_detail),
    path('snippets/class', snippet_views.SnippetList.as_view()),
    path('snippets/class/<int:pk>/', snippet_views.SnippetDetail.as_view()),
    path('snippets/mixin', snippet_views.SnippetMixinList.as_view()),
    path('snippets/mixin/<int:pk>/', snippet_views.SnippetMixinDetail.as_view()),
    path('snippets/users/', snippet_views.UserList.as_view()),
    path('snippets/users/<int:pk>/', snippet_views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
