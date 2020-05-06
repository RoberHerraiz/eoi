from django.shortcuts import render

from .models import MetaHuman, Team
<<<<<<< HEAD


from .models import MetaHuman
=======
>>>>>>> e428c7a107ee62527848e4e4586cfbb34e7f6d16

# Create your views here.

def list_all_metahumans(request):
    items = MetaHuman.objects.all()
    return render(request, "metahumans/list_metahumans.html", {
        "items": items,
        })

<<<<<<< HEAD

=======
    
>>>>>>> e428c7a107ee62527848e4e4586cfbb34e7f6d16
def list_all_teams(request):
    items = Team.objects.all()
    return render(request, "metahumans/list_teams.html", {
        "items": items,
<<<<<<< HEAD
        })
=======
    })

>>>>>>> e428c7a107ee62527848e4e4586cfbb34e7f6d16
