from django.urls import path
from django.views.generic import TemplateView  # Import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views  # Import the views module

app_name = 'djangoapp'
urlpatterns = [
    # Path for login (serves the React app's index.html)
    path('login/', TemplateView.as_view(template_name="index.html")),

    # Path for registration
    path(route='register', view=views.registration, name='register'),  # Registration route

    # Path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # Path for dealerships
    path(route='dealerships', view=views.get_dealerships, name='dealerships'),

    # Path for dealer reviews
    path(route='dealer/<int:dealer_id>/reviews', view=views.get_dealer_reviews, name='dealer_reviews'),

    # Path for dealer details
    path(route='dealer/<int:dealer_id>/details', view=views.get_dealer_details, name='dealer_details'),

    # Path for adding a review
    path(route='add_review', view=views.add_review, name='add_review'),

    path(route='get_cars', view=views.get_cars, name ='getcars'),
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
