from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model
from django.conf import settings

import homegate

class Command(BaseCommand):
    help = 'Collect all real estate model and it\'s IDX records to push to Homegate.'

    def handle(self, *args, **options):
        '''
        '''
        appName, modelName = settings.HOMEGATE_REAL_ESTATE.split('.')
        RealEstateModel = get_model(appName, modelName)
        rems = RealEstateModel.objects.ready_to_push()
        objs = []
        for rem in rems:
            objs.append(rem.get_idx_record())
        
        
        #self.stdout.write('Hello %s.' % name)