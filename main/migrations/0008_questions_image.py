# Generated by Django 4.1.2 on 2022-10-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_quizs_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]