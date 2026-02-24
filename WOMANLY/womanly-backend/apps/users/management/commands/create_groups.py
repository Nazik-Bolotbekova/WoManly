from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create groups'

    def handle(self,*args,**kwargs):
        admin_group, created = Group.objects.get_or_create(name='admin')
        editor_group, created = Group.objects.get_or_create(name='editor')

        self.stdout.write(self.style.SUCCESS('Groups created successfully'))