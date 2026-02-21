import numpy as np
import os
from django.conf import settings

from .models import Panel
import pandas as pd

def reset_colors():
    for i in range(1, 25 + 1):
        p = Panel.objects.get(id=i)
        p.color = '#f0f5f5'
        p.save()

def load_questions():
    # Use BASE_DIR from settings to find the questions.xlsx file
    questions_path = os.path.join(settings.BASE_DIR, 'questions.xlsx')
    df=pd.read_excel(questions_path)
    for idx,row in df.iterrows():
        panel=Panel.objects.get(id=int(row['panel']))
        panel.row=row['row']
        panel.col = row['col']
        panel.question=row['question']
        panel.correct_answer=row['correct_answer']
        panel.wrong_answer_1 = row['wrong_answer_1'] if not pd.isna(row['wrong_answer_1']) else " "
        panel.wrong_answer_2 = row['wrong_answer_2'] if not pd.isna(row['wrong_answer_2'])  else " "
        panel.wrong_answer_3 = row['wrong_answer_3'] if not pd.isna(row['wrong_answer_3'])  else " "
        panel.save()

def assign_images():
    Panel.objects.all().update(image=None)
    images_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'questions')
    if not os.path.isdir(images_dir):
        return
    for filename in os.listdir(images_dir):
        name, ext = os.path.splitext(filename)
        if not ext:
            continue
        try:
            panel = Panel.objects.get(id=int(name))
            panel.image = filename
            panel.save()
        except (ValueError, Panel.DoesNotExist):
            continue

def reset_game():
    reset_colors()
    load_questions()
    assign_images()