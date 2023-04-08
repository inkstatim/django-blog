# Generated by Django 4.2 on 2023-04-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollar'), ('UAH', 'Hrivnya')], default='UAH', max_length=3),
        ),
    ]
