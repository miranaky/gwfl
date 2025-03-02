# Generated by Django 3.2.5 on 2021-07-30 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diaries', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goodwords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='diary',
            name='goodwords',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to='goodwords.goodword'),
        ),
    ]
