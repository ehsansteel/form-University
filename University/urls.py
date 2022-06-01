from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("form_app.urls")),
    path("form2/", include("form_app.urls")),
    path("form/", include("login_app.urls"))

]
