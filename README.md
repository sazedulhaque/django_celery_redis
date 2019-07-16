This is a Django project for understanding basic of Celery periodic task runner

Run the Following command  in system:

    pip install pipenv
    
Then run the following command to activate the virtual environment:

    pipenv shell
    
After that run:

    pipenv install
    
to install require file from pipfile.lock. Now you application is ready you just need to ensure redis is installed or not.

you can follow the link to install redis in your os if it is not installed.

https://redis.io/

Run  the following command:

    celery worker -l info -B
or,

    celery worker -l info --beat
    celery -A picha beat -l info

We will see following 

````
 -------------- celery@Sazeduls-MacBook-Pro.local v4.3.0 (rhubarb)
---- **** ----- 
--- * ***  * -- Darwin-18.6.0-x86_64-i386-64bit 2019-06-16 18:36:47
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         celery_redis_django:0x103c56f28
- ** ---------- .> transport:   redis://localhost:6379//
- ** ---------- .> results:     redis://localhost:6379/
- *** --- * --- .> concurrency: 8 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . celery_redis_django.celery.debug_task
  . second_task
  . task_display_funny_time

[2019-06-16 18:36:47,748: INFO/Beat] beat: Starting...
[2019-06-16 18:36:47,756: INFO/MainProcess] Connected to redis://localhost:6379//
[2019-06-16 18:36:47,770: INFO/MainProcess] mingle: searching for neighbors
[2019-06-16 18:36:47,777: INFO/Beat] Scheduler: Sending due task task_display_funny_time (task_display_funny_time)
[2019-06-16 18:36:47,794: INFO/Beat] Scheduler: Sending due task second_task (second_task)
[2019-06-16 18:36:48,798: INFO/MainProcess] mingle: all alone
[2019-06-16 18:36:48,813: INFO/MainProcess] celery@Sazeduls-MacBook-Pro.local ready.
[2019-06-16 18:36:49,112: INFO/MainProcess] Received task: task_display_funny_time[ac4dea08-af2c-421c-b9cc-6601181af9fa]  
[2019-06-16 18:36:49,115: INFO/MainProcess] Received task: second_task[69df00d1-3711-423f-a07a-98ce0716cb86]  
[2019-06-16 18:36:49,116: WARNING/ForkPoolWorker-9] funny time is 2019-06-16 18:36:49.115487
[2019-06-16 18:36:49,117: INFO/ForkPoolWorker-9] task_display_funny_time[ac4dea08-af2c-421c-b9cc-6601181af9fa]: Hurray its working
[2019-06-16 18:36:49,118: INFO/ForkPoolWorker-9] Task task_display_funny_time[ac4dea08-af2c-421c-b9cc-6601181af9fa] succeeded in 0.00285962900000003s: None
[2019-06-16 18:36:49,118: WARNING/ForkPoolWorker-3] Second Task's time is = 2019-06-16 18:36:49.117875
[2019-06-16 18:36:49,119: INFO/ForkPoolWorker-3] second_task[69df00d1-3711-423f-a07a-98ce0716cb86]: Second Task
[2019-06-16 18:36:49,120: INFO/ForkPoolWorker-3] Task second_task[69df00d1-3711-423f-a07a-98ce0716cb86] succeeded in 0.0027296290000000667s: None
[2019-06-16 18:36:57,761: INFO/Beat] Scheduler: Sending due task task_display_funny_time (task_display_funny_time)
[2019-06-16 18:36:57,764: INFO/MainProcess] Received task: task_display_funny_time[604b5d3c-6c36-4674-924a-202527ce9c06] 
````

Then it seems working.

If want to know more then follow the Documentation of celery

http://docs.celeryproject.org/en/latest/index.html#contents

Thanks
