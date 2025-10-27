from celery import Celery
import redis
import json
from datetime import datetime
import time

from config import settings


celery_app = Celery("app.tasks", broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)

celery_app.conf.update(
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    task_reject_on_worker_lost=True,
)

# sync redis client for publishing status updates
r = redis.from_url(settings.REDIS_URL, decode_responses=True)

@celery_app.task(bind=True)
def start_recalculation(self, task_id: int, reporting_date: datetime, systems: list[str]):
    r.publish("celery_updates", json.dumps({"task_id": task_id, "status": "STARTED"}))
    time.sleep(5)
    r.publish("celery_updates", json.dumps({"task_id": task_id, "status": "SUCCESS"}))
    return {"task_id": task_id, "status": "SUCCESS"}
