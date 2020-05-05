from django.shortcuts import render
from .models import MetaHuman

from .models import MetaHuman

# Create your views here.

def list_all_metahumans(request):
    items = MetaHuman.objects.all()
    return render(request, "metahumans/list_metahumans.html", {
        "items": items,
<<<<<<< HEAD
        })
=======
    })

    
>>>>>>> 962ff782e31f1673615e4e69fa766cd5febe78db
