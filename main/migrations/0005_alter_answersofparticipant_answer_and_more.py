# Generated by Django 4.1.2 on 2022-10-10 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_quizs_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersofparticipant',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_ques', to='main.answers'),
        ),
        migrations.AlterField(
            model_name='answersofparticipant',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_que', to='main.questions'),
        ),
    ]