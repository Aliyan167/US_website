# Generated by Django 4.2 on 2024-09-20 10:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Exarth', help_text='Application name', max_length=100)),
                ('short_name', models.CharField(default='EX', help_text='Your application short name', max_length=10)),
                ('tagline', models.CharField(default='Your digital partner', help_text='Your application business line', max_length=100)),
                ('description', models.TextField(default='Your technology partner in innovations, automation and business intelligence.', help_text='Application description')),
                ('favicon', models.ImageField(blank=True, help_text='Application favicon', null=True, upload_to='core/application/images')),
                ('logo', models.ImageField(blank=True, help_text='Application real colors logo', null=True, upload_to='core/application/images')),
                ('logo_dark', models.ImageField(blank=True, help_text='For dark theme only', null=True, upload_to='core/application/images')),
                ('logo_light', models.ImageField(blank=True, help_text='For light theme only', null=True, upload_to='core/application/images')),
                ('contact_email1', models.EmailField(default='support@exarth.com', help_text='Application contact email 1', max_length=100)),
                ('contact_email2', models.EmailField(default='support@exarth.com', help_text='Application contact email 2', max_length=100)),
                ('contact_phone1', phonenumber_field.modelfields.PhoneNumberField(default='+923419387283', help_text='Application contact phone 1', max_length=128, region=None)),
                ('contact_phone2', phonenumber_field.modelfields.PhoneNumberField(default='+923259575875', help_text='Application contact phone 2', max_length=128, region=None)),
                ('address', models.CharField(default='123 Main St, Abbotabad, KPK Pakistan', help_text='office address', max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, default=23.7, help_text='latitude', max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, default=90.3, help_text='longitude', max_digits=10)),
                ('terms_url', models.URLField(default='https://exarth.com/terms-of-use/', help_text='Terms and Conditions page link', max_length=255)),
                ('version', models.CharField(default='1.0.0', help_text='Current version', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Application',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('short_name', models.CharField(help_text='ISO 3166-1 alpha-2', max_length=2, unique=True)),
                ('language', models.CharField(blank=True, default='en', help_text='ISO 639-1', max_length=3, null=True)),
                ('currency', models.CharField(blank=True, default='USD', help_text='ISO 4217', max_length=3, null=True)),
                ('phone_code', models.CharField(blank=True, default='+1', help_text='e.g. +1', max_length=4, null=True)),
                ('is_services_available', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
    ]
