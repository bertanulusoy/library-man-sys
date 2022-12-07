import os
import time
from celery_worker import Cel
from dotenv import load_dotenv

load_dotenv("../.env")

celery = celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")


# Anlık ve saat başı rapor oluştur ve gönder
@celery.task(name="create_task")
def create_task(a, b, c):
    time.sleep(a)
    return b + c
