from django.urls import path

from instagram.users.views import (
    explore_users_view,
    follow_users_view,
    unfollow_users_view,
    user_profile_view,
    user_followers_view,
    user_following_view,
)

app_name = "users"
urlpatterns = [
    path("explore", view=explore_users_view, name="explore_users"),
    path("<int:user_id>/follow", view=follow_users_view, name="follow_users"),
    path("<int:user_id>/unfollow", view=unfollow_users_view, name="unfollow_users"),
    path("<username>", view=user_profile_view, name="user_profile"),
    path("<username>/followers", view=user_followers_view, name="user_follower"),
    path("<username>/following", view=user_following_view, name="user_following")
]
