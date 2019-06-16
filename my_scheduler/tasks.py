from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery import task

logger = get_task_logger(__name__)
import datetime
from datetime import timedelta

@periodic_task(
    run_every=timedelta(seconds=10),
    # run_every=10.0,
    # run_every=(crontab(second='*/15')),
    name="task_display_funny_time",
    ignore_result=True
)
# @task
def task_display_funny_time():
    """
    Saves latest image from Flickr
    """
    print("funny time is %s" % datetime.datetime.now())
    logger.info("Hurray its working")


@periodic_task(
    run_every=timedelta(seconds=15),
    # run_every=10.0,
    # run_every=(crontab(second='*/15')),
    name="second_task",
    ignore_result=True
)
# @task
def second_task():
    """
    Saves latest image from Flickr
    """
    print("Second Task's time is = %s" % datetime.datetime.now())
    logger.info("Second Task")
