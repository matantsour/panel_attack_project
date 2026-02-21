# Panel Attack - Project Summary

## What This Is
A Django-based multiplayer quiz game similar to Kahoot. Four teams (yellow, green, blue, pink) compete to conquer a 5x5 board of 25 panels by answering trivia questions correctly. Displayed on a large TV for up to 20 players.

## Conquest Mechanic (Core Game Rule)
When a team conquers a panel, it can also capture rival panels that are "sandwiched" between two friendly panels in the same line:
- **Horizontal**: panels in the same row
- **Vertical**: panels in the same column
- **Diagonal**: panels on the same diagonal (both ↘ and ↙ directions, for ALL panels — not just the two main diagonals)

## Key Files
| File | Purpose |
|------|---------|
| `panel_attack/views.py` | Core game logic — conquest functions for row, col, diagonal |
| `panel_attack/models.py` | `Panel` model (id, row, col, color, question, correct_answer, wrong_answer_1/2/3, image) |
| `panel_attack/game_reset.py` | Resets colors, reloads questions from `questions.xlsx`, auto-assigns images |
| `panel_attack/management/commands/assign_images.py` | Standalone command to assign images without full reset |
| `panel_attack/templates/index.html` | Main board view |
| `panel_attack/templates/panel_detail.html` | Individual panel question page |
| `questions.xlsx` | Source of truth for all 25 questions — lives in project root (BASE_DIR) |
| `static/style.css` | All styling (Nunito + Heebo fonts, TV-friendly sizing) |
| `static/images/questions/` | Optional per-panel images, named by panel ID (e.g. `13.jpg`) |
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

## Panel Model Fields
- `id` — panel number (1–25)
- `row`, `col` — position on the board
- `color` — current team color (hex), default `#f0f5f5`
- `question`, `correct_answer`, `wrong_answer_1/2/3` — loaded from `questions.xlsx`
- `image` — optional filename in `static/images/questions/` (e.g. `'13.jpg'`), nullable

## Image Assignment
Images are named by panel ID and placed in `static/images/questions/`. Assignment is automatic on `reset_game` or via:
```
py manage.py assign_images
```
`reset_game` clears ALL image assignments first, then re-assigns only files that currently exist in the directory. This means removing a file and resetting will correctly clear it.

## Answer Comparison Bug (Fixed)
Browsers submit textarea/form newlines as `\r\n`. The DB stores answers with `\n`. The fix is in `views.py`:
```python
answer = form.cleaned_data['answer'].replace('\r\n', '\n').replace('\r', '\n')
```
Do not remove this normalization.

## UI / Design Notes
- Fonts: `Nunito` (UI/Latin) + `Heebo` (Hebrew text) from Google Fonts
- Root font-size: `15px` — all rem values scale from this. Adjust here to resize everything.
- Panel cell size: `90px × 90px` fixed — adjust in `.panel-cell` and matching `.panel-number` `line-height`
- Team selector on question page: colored clickable tiles (not a dropdown), backed by `<input type="radio" name="color">`
- Answer cards: CSS grid 2×2, `<label>` wrapping hidden radio, `:has(:checked)` highlights selected
- Question/answer text uses `direction: rtl` for Hebrew

## Important Notes
- `questions.xlsx` must be at the project root (`BASE_DIR/questions.xlsx`)
- The diagonal conquest function (`get_rival_panels_bound_in_diag`) dynamically computes diagonals using row/col math
- Run with: `py manage.py runserver`
- Database: SQLite (`db.sqlite3`)
