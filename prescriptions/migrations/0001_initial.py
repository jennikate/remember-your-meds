# Generated by Django 3.0.2 on 2020-01-07 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url_fragment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_doses', models.IntegerField(blank=True, null=True)),
                ('doses_per_day', models.IntegerField(blank=True, null=True)),
                ('number_repeats', models.IntegerField(blank=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='prescriptions.Doctor')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='prescriptions.Medicine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_time', models.DateTimeField()),
                ('reminder_time', models.DateTimeField()),
                ('reminder_type', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reminder', to='prescriptions.Doctor')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminder', to='prescriptions.Prescription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
