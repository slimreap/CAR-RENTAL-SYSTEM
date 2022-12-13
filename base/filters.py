import django_filters
from .models import *

class Carfilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['Price','Brand_Name','Mod_Name']