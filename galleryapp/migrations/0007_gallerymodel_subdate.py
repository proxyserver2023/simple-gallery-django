# Generated by Django 2.1.2 on 2018-10-25 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0006_auto_20181025_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerymodel',
            name='SubDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]