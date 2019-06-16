from celery.task import task
import datetime

@task
def fun():
    print("funny time is %s" % datetime.datetime.now())
