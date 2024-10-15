from django.db import models

# Create your models here.
class Panel(models.Model):
    id=models.AutoField(primary_key=True)
    row=models.IntegerField()
    col = models.IntegerField()
    color = models.CharField(max_length=100)
    question=models.CharField(max_length=1000)
    correct_answer=models.CharField(max_length=1000)
    wrong_answer_1=models.CharField(max_length=1000)
    wrong_answer_2=models.CharField(max_length=1000)
    wrong_answer_3=models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)