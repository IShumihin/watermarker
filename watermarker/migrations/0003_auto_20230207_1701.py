# Generated by Django 3.2.16 on 2023-02-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watermarker', '0002_auto_20181106_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watermark',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='watermark',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='is active'),
        ),
    ]