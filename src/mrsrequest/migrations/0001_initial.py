# Generated by Django 2.0 on 2017-12-27 14:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MRSRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name="Date et heure d'enregistrement du formulaire")),
                ('status', models.IntegerField(choices=[(0, 'Soumise'), (1, 'Validée'), (2, 'Rejettée')], default=0)),
                ('insured', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.Person')),
            ],
        ),
    ]
