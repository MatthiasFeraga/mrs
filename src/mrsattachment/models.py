import io

from django.db import models


class MRSAttachmentField(models.BinaryField):
    pass


class MRSAttachment(models.Model):
    filename = models.CharField(max_length=255)
    creation_datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Heure d\'enregistrement du fichier')
    binary = MRSAttachmentField(verbose_name='Justificatif')

    @classmethod
    def get_upload_body(cls, upload):
        body = io.BytesIO()
        for chunk in upload.chunks():
            body.write(chunk)
        body.seek(0)  # rewind read point to beginning of registry
        return body.read()
