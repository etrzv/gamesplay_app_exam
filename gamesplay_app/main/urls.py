from django.urls import path
from gamesplay_app.main.views.games import delete_game, edit_game, details_game, create_game
from gamesplay_app.main.views.generic import show_home, show_dashboard
from gamesplay_app.main.views.profile import create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_home, name='show index'),
    path('dashboard/', show_dashboard, name='show dashboard'),

    path('profile/create', create_profile, name='create profile'),
    path('profile/details', details_profile, name='details profile'),
    path('profile/edit', edit_profile, name='edit profile'),
    path('profile/delete', delete_profile, name='delete profile'),

    path('game/create', create_game, name='create game'),
    path('game/details/<int:pk>', details_game, name='details game'),
    path('game/edit/<int:pk>', edit_game, name='edit game'),
    path('game/delete/<int:pk>', delete_game, name='delete game'),
)

'''
http://localhost:8000/ - home page
http://localhost:8000/dashboard/ - dashboard page

http://localhost:8000/profile/create - create profile page
http://localhost:8000/profile/details/ - details profile page
http://localhost:8000/profile/edit/ - edit profile page
http://localhost:8000/profile/delete/ - delete profile page

http://localhost:8000/game/create/ - create game page
http://localhost:8000/game/details/<id>/ - details game page
http://localhost:8000/game/edit/<id>/ - edit game page
http://localhost:8000/game/delete/<id>/ - delete game page
'''