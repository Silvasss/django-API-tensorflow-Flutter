# Generated by Django 3.2.5 on 2022-05-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='array',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]