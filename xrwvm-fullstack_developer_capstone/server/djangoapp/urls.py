# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),

    # Logout
    path(route='logout', view=views.logout_request, name='logout'),

    # Register
    path(route='register', view=views.registration, name='register'),
    # path for dealer reviews view
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealer/', view=views.get_dealer_details, name='get_dealer'),

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
