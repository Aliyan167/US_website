# Generated by Django 4.2 on 2024-09-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_challenge_project_result_project_solution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
    ]
