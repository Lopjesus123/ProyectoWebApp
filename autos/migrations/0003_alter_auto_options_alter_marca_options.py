# Generated by Django 5.1.7 on 2025-04-23 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_auto_created_auto_updated_marca_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto',
            options={'verbose_name': 'Auto', 'verbose_name_plural': 'Autos'},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
    ]
