from django.core.management.base import BaseCommand
from quote.models import *
import datetime


_characters = [
    ('Guy Fieri', 'guyfieri.txt', 'guyfieri', 'Welcome to Flavortown!'),
    ('Senor Cardgage', 'cardgage.txt', 'cardgage', 'Dump Tell No Mandy!'),
    ('Homsar', 'homsar.txt', 'homsar', 'Legitimate Business!'),
    ('Hacker News', 'hackernews.txt', 'hackernews', 'Presented by Y Combinator!'),
    ('Drew Gottlieb', 'drewgottlieb.txt', 'drew', 'Hmm.'),
]

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'


    def _create_characters(self):

        user = User.objects.get(username='harlan')
        Homestarkov.objects.all().delete()

        for name, filename, path, tagline in _characters:
            with open(filename) as corpus_file:
                Homestarkov.objects.create(name=name, path=path, corpus=corpus_file.read(), tagline=tagline, submitter=user)

    def handle(self, *args, **options):
        self._create_characters()
