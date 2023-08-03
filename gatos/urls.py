from django.urls import path
from gatos.views    import HomePageView
app_name ="gato_app"
urlpatterns = [
    
    path ('', HomePageView.as_view(), name='home')
]