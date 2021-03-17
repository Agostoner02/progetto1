# Generated by Django 3.1.2 on 2020-12-09 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='librocd',
            name='isbn',
            field=models.CharField(default='0-000-00000-0', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='librocd',
            name='autore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libri', to='libreria.autorecd'),
        ),
    ]
