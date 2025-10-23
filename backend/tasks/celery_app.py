"""
Celery application configuration
"""

from celery import Celery
from config import settings

# Create Celery app
app = Celery(
    "leadgear_tasks",
    broker=settings.celery_broker_url,
    backend=settings.celery_result_backend
)

# Configure Celery
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes max
    task_soft_time_limit=25 * 60,  # 25 minutes soft limit
)

# Auto-discover tasks
app.autodiscover_tasks(["tasks"])
