# Generated by Django 5.1.4 on 2025-02-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg_ctaima_app', '0022_remove_resource_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
