# Generated by Django 4.2 on 2024-09-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_servicereview_servicepricing_serviceinquiry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='services/'),
        ),
    ]