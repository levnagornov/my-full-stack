from celery import Celery
import redis
import json
import os

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
def dry_run(self, order_id: str, duration: int = 5):
    tid = self.request.id
    r.publish("celery_updates", json.dumps({"task_id": tid, "status": "STARTED", "order_id": order_id}))
    import time
    for i in range(duration):
        time.sleep(1)
        r.publish("celery_updates", json.dumps({"task_id": tid, "status": f"PROGRESS {(i+1)/duration:.2%}", "order_id": order_id}))
    r.publish("celery_updates", json.dumps({"task_id": tid, "status": "SUCCESS", "order_id": order_id}))
    return {"order_id": order_id, "status": "done"}
