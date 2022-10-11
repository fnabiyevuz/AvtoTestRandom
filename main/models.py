from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    question = models.TextField(max_length=900)

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="ans_que", null=True)
    answer = models.TextField(max_length=900)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.answer + ' ' + str(self.status)


class Quizs(models.Model):
    # participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quiz_user")
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizs_user', null=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.SmallIntegerField(default=0)
    true = models.SmallIntegerField(default=0)
    false = models.SmallIntegerField(default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_finished = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)


class AnswersOfParticipant(models.Model):
    quiz = models.ForeignKey(Quizs, on_delete=models.CASCADE, related_name='answer_quizs', null=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answer_que', null=True)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='answer_ques', null=True, blank=True)

    def __str__(self):
        return str(self.id)