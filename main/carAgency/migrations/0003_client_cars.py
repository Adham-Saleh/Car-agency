# Generated by Django 4.2.18 on 2025-01-15 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carAgency', '0002_remove_client_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cars',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carAgency.car'),
        ),
    ]
