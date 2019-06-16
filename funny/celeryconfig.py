CELERY_IMPORTS = ("tasks")
CELERY_IGNORE_RESULT = True
BROKER_HOST = "127.0.0.1" 
BROKER_PORT = 6379
BROKER_URL = "redis://localhost:6379/0"


from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'for-testing-task.fun-to-run-on-schedule': {
        'task': 'tasks.fun',
        'schedule': timedelta(seconds=10),
        # 'schedule': timedelta(minutes=1),
    },
}
