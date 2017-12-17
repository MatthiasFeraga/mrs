from crudlfap import crudlfap
from django.urls import path

from . import models
from . import views


urlpatterns = [
    path(
        'wizard',
        views.MRSRequestCreateView.as_view(),
        name='mrsrequest_wizard'
    ),
]


class MRSRequestRouter(crudlfap.Router):
    pass


urlpatterns += MRSRequestRouter(models.MRSRequest).urlpatterns()
