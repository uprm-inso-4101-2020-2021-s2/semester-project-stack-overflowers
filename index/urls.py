from django.urls import include, path
from rest_framework import routers
from . import views

from register import views as v
router = routers.DefaultRouter()
router.register(r'users', views.PlayerAccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about-us/', views.aboutUs, name="about-us"),
    path('backlog/', views.backlog, name="backlog"),
    path('game-article-template/', views.gameArticleTemplate, name="game-article-template"),
    path('library/', views.library, name="library"),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace="rest framework")),
    path('tips-tricks/', views.tips, name="tips-tricks"),
    path('games/', views.games, name="games"),
    path('games/popular', views.popGames, name="popGames"),



]

