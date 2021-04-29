# Generated by Django 2.2.19 on 2021-04-29 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0001_initial'),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='subscription',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='subscriptions.Subscription', verbose_name='Subscription'),
        ),
        migrations.AddField(
            model_name='app',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]