# Generated by Django 2.0 on 2019-09-23 14:06

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]