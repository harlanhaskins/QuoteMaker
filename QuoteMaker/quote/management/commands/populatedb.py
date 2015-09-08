from django.core.management.base import BaseCommand
from quote.models import *
import datetime
import sys


_quotemakers = [
    ('Guy Fieri', 'guyfieri.txt', 'Welcome to Flavortown!'),
    ('Senor Cardgage', 'cardgage.txt', 'Dump Tell No Mandy!'),
    ('Homsar', 'homsar.txt', 'Legitimate Business!'),
    ('Hacker News', 'hackernews.txt', 'Presented by Y Combinator!'),
    ('Drew Gottlieb', 'drewgottlieb.txt', 'Hmm.'),
    ('George Costanza', 'george.txt', 'Moops!'),
    ('Jony Ive', 'jonyive.txt', "There are a thousand no's for every yes."),
    ('Albert Einstein', 'einstein.txt', "e = mc²"),
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

        for name, filename, tagline in _quotemakers:
            with open(filename) as corpus_file:
                QuoteMaker.objects.create(name=name, corpus=corpus_file.read(), tagline=tagline, submitter=user)
                print("Added %s" % name)

    def handle(self, *args, **options):
        self._create_quotemakers()
