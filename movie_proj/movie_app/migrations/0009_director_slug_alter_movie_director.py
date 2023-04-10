# Generated by Django 4.2 on 2023-04-08 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie_app.director'),
        ),
    ]