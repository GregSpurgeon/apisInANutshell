from django.core.management.base import BaseCommand
from shoebox.models import ShoeColor, ShoeType


class Command(BaseCommand):
    styles = ['sneaker',
              'boot',
              'sandel',
              'dress',
              'other'
              ]
    colors = ['Red',
              'Orange',
              'Yellow',
              'Green',
              'Blue',
              'Indigo',
              'Violet',
              'White',
              'Black'
              ]

    def handle(self, *args, **options):
        for style in self.styles:
            try:
                ShoeType.objects.create(
                  style=style
                )
            except Exception as e:
                print(e)

        for color in self.colors:
            try:
                ShoeColor.objects.create(
                    color_name=color
                )
            except Exception as e:
                print(e)
