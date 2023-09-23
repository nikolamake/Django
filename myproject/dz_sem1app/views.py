import logging
import random
from django.http import HttpResponse

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')


def home(request):
    html = '<!DOCTYPE html>' \
           '<html lang="en">' \
           ' <head><meta charset="UTF-8"> ' \
           ' <title>Title</title>' \
           '</head> ' \
           '<body> ' \
           '<h1> Мой первый проект </h1>' \
           '</body>' \
           ' </html>'
    logger.info(f'{request} request received')
    return HttpResponse(html)


def about(request):
    html = '<!DOCTYPE html>' \
           '<html lang="en">' \
           ' <head><meta charset="UTF-8"> ' \
           ' <title>Title</title>' \
           '</head> ' \
           '<body> ' \
            '<h1>Информация о мне:</h1>' \
           '<h2>Николай Макеев</h2>' \
           '<h3>Мое начало изучения Django</h3>' \
           '</body>' \
           ' </html>'
    logger.info(f'{request} request received')
    return HttpResponse(html)