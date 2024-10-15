import numpy as np

from .models import Panel
import pandas as pd

def reset_colors():
    for i in range(1, 25 + 1):
        p = Panel.objects.get(id=i)
        p.color = '#f0f5f5'
        p.save()

def load_questions():
    df=pd.read_excel(r"C:\Users\Matan\PycharmProjects\panel_attack_project\panel_attack\questions.xlsx")
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

def reset_game():
    reset_colors()
    load_questions()