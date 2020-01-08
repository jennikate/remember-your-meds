# Generated by Django 3.0.2 on 2020-01-08 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prescriptions', '0003_auto_20200108_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user.reminder+', to=settings.AUTH_USER_MODEL),
        ),
    ]
