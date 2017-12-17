from crudlfap import crudlfap
from django.urls import path

from mrsattachment.views import MRSFileDeleteView, MRSFileUploadView

from .models import PMT


urlpatterns = [
    path(
        '<pk>/delete',
        MRSFileDeleteView.as_view(model=PMT),
        name='pmt_delete'
    ),
    path(
        '<mrsrequest_uuid>/upload',
        MRSFileUploadView.as_view(model=PMT),
        name='pmt_upload'
    ),
]


def owner_or_staff(router, view):
    if view.request.user.is_staff:
        return True

    elif getattr(view, 'object', False):
        return view.object.mrsrequest.is_allowed(view.request)


class PMTRouter(crudlfap.Router):
    allow = owner_or_staff

    views = [
        crudlfap.CreateView,
        crudlfap.DeleteView,
        crudlfap.UpdateView,
        crudlfap.DetailView,
        crudlfap.FilterTables2ListView.factory(
            material_icon='local_hospital',
            filter_fields=['mrsrequest', 'creation_datetime'],
        ),
    ]

urlpatterns += PMTRouter(model=PMT).urlpatterns()
