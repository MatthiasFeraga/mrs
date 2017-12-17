from crudlfap import crudlfap
from django.urls import path

from mrsattachment.views import MRSFileDeleteView, MRSFileUploadView

from .models import Bill, Transport


urlpatterns = [
    path(
        '<pk>/delete',
        MRSFileDeleteView.as_view(model=Bill),
        name='bill_delete'
    ),
    path(
        '<mrsrequest_uuid>/upload',
        MRSFileUploadView.as_view(model=Bill),
        name='bill_upload'
    ),
]

# material_icon='card_travel',
# directions_car
urlpatterns += crudlfap.Router(
    model=Transport, url_prefix='').urlpatterns()
urlpatterns += crudlfap.Router(model=Bill, url_prefix='bill/').urlpatterns()
