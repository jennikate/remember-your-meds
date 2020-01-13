# Generated by Django 3.0.2 on 2020-01-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0010_auto_20200110_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='reminder_type',
            field=models.CharField(choices=[('take-am', 'Take medicine'), ('take-mid', 'Take medicine'), ('take-pm', 'Take medicine'), ('order prescription', 'Order prescription'), ('make appointment', 'Make doctors appointment')], max_length=30),
        ),
    ]