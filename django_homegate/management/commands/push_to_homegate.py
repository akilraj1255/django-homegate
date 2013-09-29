from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model
from django.conf import settings

class Command(BaseCommand):
    args = '<name name ..>'
    help = 'Say hello to <name(s)>'

    def handle(self, *args, **options):
        
        
        RealEstateModel = get_model(*model_string.split('.'))
        
        
            self.stdout.write('Hello %s.' % name)