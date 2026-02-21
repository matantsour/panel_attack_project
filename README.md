# Panel Attack

A Django-based multiplayer quiz game for groups. Four teams compete to conquer a 5×5 board of 25 panels by answering trivia questions correctly. Designed to be displayed on a large TV for up to 20 players.

---

## Setup

**Requirements:** Python 3.11+, pip

```bash
pip install django pandas openpyxl numpy
py manage.py migrate
py manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

---

## How to Play

1. The board shows 25 numbered panels. Click any panel to open its question.
2. Select your **team color** (yellow / green / blue / pink) using the colored tiles.
3. Select the correct answer from the four cards.
4. Press **OK — I'm Sure** to submit.
5. If correct, the panel turns your team's color.
6. **Conquest:** A correct answer can also flip rival panels that are sandwiched between two of your panels — horizontally, vertically, or diagonally.
7. Click **reset game** at the bottom of the board to restart (resets all colors and reloads questions and images).

---

## Questions

Questions are loaded from `questions.xlsx` in the project root. The file must have these columns:

| Column | Description |
|--------|-------------|
| `panel` | Panel ID (1–25) |
| `row` | Row on the board (1–5) |
| `col` | Column on the board (1–5) |
| `question` | Question text |
| `correct_answer` | The correct answer |
| `wrong_answer_1` | Wrong answer 1 |
| `wrong_answer_2` | Wrong answer 2 |
| `wrong_answer_3` | Wrong answer 3 |

After editing `questions.xlsx`, click **reset game** in the browser to reload.

---

## Adding Images to Questions

Place image files in `static/images/questions/`. Name each file after its panel ID:

```
static/images/questions/
    1.jpg      ← assigned to panel 1
    07.png     ← assigned to panel 7
    25.jpeg    ← assigned to panel 25
```

Images are auto-assigned when you click **reset game**, or manually via:

```bash
py manage.py assign_images
```

Removing an image file and running reset game will clear it from that panel.

---

## Key Files

| File | Purpose |
|------|---------|
| `questions.xlsx` | Source of truth for all 25 questions |
| `static/images/questions/` | Optional per-question images |
| `panel_attack/views.py` | Core game logic and conquest functions |
| `panel_attack/models.py` | Panel model |
| `panel_attack/game_reset.py` | Reset logic: colors, questions, images |
| `panel_attack/management/commands/assign_images.py` | Management command to assign images |
| `static/style.css` | All styling |
| `panel_attack/templates/` | HTML templates |
| `panel_attack_project/settings.py` | Django settings |

---

## Board Layout

```
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```

---

## Admin

Django admin is available at `http://127.0.0.1:8000/admin/`. You can manually edit panel fields (including the `image` filename) from there.

To create an admin user:
```bash
py manage.py createsuperuser
```
