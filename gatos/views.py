from django.views.generic.base import TemplateView
import requests

from django.views.generic import ListView


from .models import Gato

class HomePageView(ListView):
    template_name = "gatos/home.html"
    context_object_name = 'gatos'

    url = 'https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key='
    llave = 'f221c99b-304d-4404-b111-cbd3ddccf31a'

    PARAMS = {'address':llave}
    r = requests.get(url, params=PARAMS)
    data = r.json()
    

    def get_queryset(self):
        return Gato.objects.all()
    
class GatoApi(ListView):


    def get_queryset(self):
        return super().get_queryset()
    


    

