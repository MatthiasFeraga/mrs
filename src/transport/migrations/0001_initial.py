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
            name='Bill',
            fields=[
                ('mrsattachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mrsattachment.MRSAttachment')),
            ],
            options={
                'verbose_name': 'Justificatif',
                'ordering': ['transport', 'id'],
            },
            bases=('mrsattachment.mrsattachment',),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_depart', models.DateField(help_text='Date du trajet aller', null=True, verbose_name='Aller')),
                ('date_return', models.DateField(help_text='Date du trajet retour', null=True, verbose_name='Retour')),
                ('distance', models.IntegerField(help_text='Kilométrage total parcouru', null=True, verbose_name='Distance (km)')),
                ('expense', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Parking et/ou péage ou justificatif(s) de transport en commun', max_digits=6, verbose_name='Montant total des frais')),
                ('mrsrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrsrequest.MRSRequest')),
            ],
            options={
                'ordering': ['mrsrequest'],
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='transport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.Transport'),
        ),
    ]
