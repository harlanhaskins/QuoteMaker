from django.core.management.base import BaseCommand
from quote.models import *
import datetime
import sys


_quotemakers = [
    ('Guy Fieri', 'guyfieri.txt', 'guyfieri', 'Welcome to Flavortown!'),
    ('Senor Cardgage', 'cardgage.txt', 'cardgage', 'Dump Tell No Mandy!'),
    ('Homsar', 'homsar.txt', 'homsar', 'Legitimate Business!'),
    ('Hacker News', 'hackernews.txt', 'hackernews', 'Presented by Y Combinator!'),
    ('Drew Gottlieb', 'drewgottlieb.txt', 'drew', 'Hmm.'),
    ('George Costanza', 'george.txt', 'costanza', 'Moops!'),
]

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_quotemakers(self):
        email = 'harlan@harlanhaskins.com'
        user = User.objects.create_superuser(username=email,
                email=email, password=sys.argv[2],
                first_name="Harlan", last_name="Haskins")
        QuoteMaker.objects.all().delete()

        for name, filename, path, tagline in _quotemakers:
            with open(filename) as corpus_file:
                QuoteMaker.objects.create(name=name, path=path, corpus=corpus_file.read(), tagline=tagline, submitter=user)

    def handle(self, *args, **options):
        self._create_quotemakers()
