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

We will see following 

````
 -------------- celery@Sazeduls-MacBook-Pro.local v4.3.0 (rhubarb)
---- **** ----- 
--- * ***  * -- Darwin-18.6.0-x86_64-i386-64bit 2019-06-16 21:43:17
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         default:0x1013ce358 (.default.Loader)
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 8 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.fun

[2019-06-16 21:43:17,231: INFO/Beat] beat: Starting...
[2019-06-16 21:43:17,248: INFO/MainProcess] Connected to redis://localhost:6379/0
[2019-06-16 21:43:17,260: INFO/MainProcess] mingle: searching for neighbors
[2019-06-16 21:43:17,264: INFO/Beat] Scheduler: Sending due task for-testing-task.fun-to-run-on-schedule (tasks.fun)
[2019-06-16 21:43:18,292: INFO/MainProcess] mingle: all alone
[2019-06-16 21:43:18,308: INFO/MainProcess] celery@Sazeduls-MacBook-Pro.local ready.
[2019-06-16 21:43:18,311: INFO/MainProcess] Received task: tasks.fun[0c9429c6-814c-423c-804c-76b5e1273327]  
[2019-06-16 21:43:18,313: WARNING/ForkPoolWorker-9] funny time is 2019-06-16 21:43:18.313381
[2019-06-16 21:43:18,314: INFO/ForkPoolWorker-9] Task tasks.fun[0c9429c6-814c-423c-804c-76b5e1273327] succeeded in 0.0017055150000000463s: None
[2019-06-16 21:43:27,248: INFO/Beat] Scheduler: Sending due task for-testing-task.fun-to-run-on-schedule (tasks.fun)
[2019-06-16 21:43:27,251: INFO/MainProcess] Received task: tasks.fun[ee6fb293-ca0f-4a1e-bf6b-019ce3bf1059]  
[2019-06-16 21:43:27,254: WARNING/ForkPoolWorker-3] funny time is 2019-06-16 21:43:27.253708
[2019-06-16 21:43:27,255: INFO/ForkPoolWorker-3] Task tasks.fun[ee6fb293-ca0f-4a1e-bf6b-019ce3bf1059] succeeded in 0.0017719039999999353s: None
````

Then it seems working.

If want to know more then follow the Documentation of celery

http://docs.celeryproject.org/en/latest/index.html#contents

Thanks