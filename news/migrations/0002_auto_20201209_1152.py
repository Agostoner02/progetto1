# Generated by Django 3.1.4 on 2020-12-09 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articolo',
            options={'verbose_name': 'Articolo', 'verbose_name_plural': 'Articolo'},
        ),
        migrations.AlterModelOptions(
            name='giornalista',
            options={'verbose_name': 'Giornalista', 'verbose_name_plural': 'Giornalisti'},
        ),
    ]