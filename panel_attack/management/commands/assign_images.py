import os
from django.core.management.base import BaseCommand
from django.conf import settings
from panel_attack.models import Panel


class Command(BaseCommand):
    help = "Auto-assign images to panels by filename (e.g. 25.png → panel 25)"

    def handle(self, *args, **options):
        images_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'questions')
        if not os.path.isdir(images_dir):
            self.stdout.write(self.style.ERROR(f"Directory not found: {images_dir}"))
            return

        assigned = 0
        skipped = 0

        for filename in os.listdir(images_dir):
            name, ext = os.path.splitext(filename)
            if not ext:
                continue
            try:
                panel_id = int(name)
            except ValueError:
                self.stdout.write(f"  Skipping '{filename}' (name is not a number)")
                skipped += 1
                continue

            try:
                panel = Panel.objects.get(id=panel_id)
            except Panel.DoesNotExist:
                self.stdout.write(f"  Skipping '{filename}' (no panel with id={panel_id})")
                skipped += 1
                continue

            panel.image = filename
            panel.save()
            self.stdout.write(self.style.SUCCESS(f"  Panel {panel_id} ← {filename}"))
            assigned += 1

        self.stdout.write(f"\nDone: {assigned} assigned, {skipped} skipped.")
