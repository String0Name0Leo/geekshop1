import json

from django.core.management import BaseCommand
from django.conf import settings

from mainapp.models import Category


class Command(BaseCommand):

    @staticmethod
    def _load_data_from_file(file_name):
        with open(f'{settings.BASE_DIR}/mainapp/json/{file_name}.json') as json_file:
            return json.load(json_file)


    '''Зачистим базу'''
    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories_list = self._load_data_from_file('categories')

        for cat in categories_list:
            Category.objects.create(
                name=cat['name'],
                description=cat['description']
            )
