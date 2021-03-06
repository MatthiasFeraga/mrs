# Generated by Django 2.0 on 2017-12-27 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mrsattachment', '0001_initial'),
        ('mrsrequest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PMT',
            fields=[
                ('mrsattachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mrsattachment.MRSAttachment')),
                ('mrsrequest', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mrsrequest.MRSRequest')),
            ],
            options={
                'ordering': ['mrsrequest', 'id'],
            },
            bases=('mrsattachment.mrsattachment',),
        ),
    ]
