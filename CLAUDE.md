# Panel Attack - Project Summary

## What This Is
A Django-based multiplayer quiz game similar to Kahoot. Four teams (yellow, green, blue, pink) compete to conquer a 5x5 board of 25 panels by answering trivia questions correctly.

## Conquest Mechanic (Core Game Rule)
When a team conquers a panel, it can also capture rival panels that are "sandwiched" between two friendly panels in the same line:
- **Horizontal**: panels in the same row
- **Vertical**: panels in the same column
- **Diagonal**: panels on the same diagonal (both ↘ and ↙ directions, for ALL panels — not just the two main diagonals)

## Key Files
| File | Purpose |
|------|---------|
| `panel_attack/views.py` | Core game logic — conquest functions for row, col, diagonal |
| `panel_attack/models.py` | `Panel` model (id, row, col, color, question, correct_answer, wrong_answer_1/2/3) |
| `panel_attack/game_reset.py` | Resets colors and reloads questions from `questions.xlsx` |
| `panel_attack/templates/index.html` | Main board view |
| `panel_attack/templates/panel_detail.html` | Individual panel question page |
| `questions.xlsx` | Source of truth for all 25 questions — lives in project root (BASE_DIR) |
| `panel_attack_project/urls.py` | URL routing |
| `panel_attack_project/settings.py` | Django settings |

## Board Layout
Panels are numbered 1–25, laid out as a 5×5 grid (row 1–5, col 1–5):
```
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```

## Important Notes
- `questions.xlsx` must be at the project root (`BASE_DIR/questions.xlsx`). The path was previously hardcoded to an old PycharmProjects location — that has been fixed to use `settings.BASE_DIR`.
- The diagonal conquest function (`get_rival_panels_bound_in_diag`) was rewritten to dynamically compute diagonals using row/col math instead of hardcoded panel ID lists.
- Run with: `py manage.py runserver`
- Database: SQLite (`db.sqlite3`)