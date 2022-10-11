from django.contrib import admin
from .models import *

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Quizs)
admin.site.register(AnswersOfParticipant)