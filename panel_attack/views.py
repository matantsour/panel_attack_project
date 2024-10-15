from django.shortcuts import render
from .models import Panel
from django.http import Http404, HttpResponse
from django.views import View
from .forms import panelForm
from .game_reset import *
import random
# Create your views here.

default_color='#f0f5f5'

def convert_those_panels(panels,color):
    for panel in panels:
        panel.color=color
        panel.save()
    return True

def rival_to_convert_lookup(panels_scan_list,current):
    potential_to_conquest = []
    for panel in panels_scan_list:
        if panel.color!=current.color and panel.color!=default_color: #we know that the current color has been changed
            potential_to_conquest.append(panel)
        elif panel.color==current.color: #we can convert all panels in the list: potential_to_conquest
            convert_those_panels(potential_to_conquest,current.color)
        else:# panel.color==default_color:
            potential_to_conquest=[] #we don't have an ally on the other side, so we can't convert any panels.
    return True

def convert_rival_panels_bound_in_row(current):
    all_panels_in_row=list(Panel.objects.filter(row=current.row))
    to_the_left_rev = reversed(all_panels_in_row[:all_panels_in_row.index(current)])
    rival_to_convert_lookup(to_the_left_rev, current)
    to_the_right = all_panels_in_row[all_panels_in_row.index(current)+1:]
    rival_to_convert_lookup(to_the_right, current)
    return True

def get_rival_panels_bound_in_col(current):
    all_panels_in_col = list(Panel.objects.filter(col=current.col))
    upper_panels_rev = reversed(all_panels_in_col[:all_panels_in_col.index(current)])
    rival_to_convert_lookup(upper_panels_rev, current)
    lower_panels = all_panels_in_col[all_panels_in_col.index(current) + 1:]
    rival_to_convert_lookup(lower_panels, current)
    return True

def get_rival_panels_bound_in_diag(current):
    if current.id in [1,7,13,19,25]:
        all_panels_numbers_in_diag = [1,7,13,19,25]
    elif current.id in [5,9,13,17,21]:
        all_panels_numbers_in_diag = [5,9,13,17,21]
    else:
        return False
    all_panels_in_diag=list(Panel.objects.filter(id__in=all_panels_numbers_in_diag))
    print(all_panels_in_diag)
    to_the_left_rev = reversed(all_panels_in_diag[:all_panels_in_diag.index(current)])
    rival_to_convert_lookup(to_the_left_rev, current)
    to_the_right = all_panels_in_diag[all_panels_in_diag.index(current)+1:]

    rival_to_convert_lookup(to_the_right, current)
    return True

class index(View):
    def get(self,request):
        panels = Panel.objects.all()
        return render(request, 'index.html', {'panels': panels,})

    def post(self,request):
        form = panelForm(request.POST)
        if form.is_valid():
            panel_id=form.cleaned_data['panel_id']
            color = form.cleaned_data['color']
            answer = form.cleaned_data['answer']

            panel_ob=Panel.objects.get(id=int(panel_id))
            if answer==panel_ob.correct_answer:
                panel_ob.color=color
                panel_ob.save() #saved the correct answer ! now it's time to see if some rival panes are bounded in respective row, column or diagonal
                convert_rival_panels_bound_in_row(panel_ob)
                get_rival_panels_bound_in_col(panel_ob)
                get_rival_panels_bound_in_diag(panel_ob)
        panels = Panel.objects.all()
        return render(request, 'index.html', {'panels': panels,})


def panel_detail(request, panel_id):
    try:
        panel = Panel.objects.get(id=panel_id)
        form = panelForm()
    except Panel.DoesNotExist:
        raise Http404('panel not found')
    question_phrase = panel.question
    questions_mixed=[panel.correct_answer,panel.wrong_answer_1,panel.wrong_answer_2,panel.wrong_answer_3]
    random.shuffle(questions_mixed)
    return render(request, 'panel_detail.html', {
        'panel': panel,
        'question_phrase':str(question_phrase) ,
        'questions_mixed':questions_mixed,
        'form':form
    })

def reset_game_click(request):
    reset_game()
    panels = Panel.objects.all()
    return render(request, 'index.html', {'panels': panels,})
