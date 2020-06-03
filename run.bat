cd  %~dp0
../Redis/redis-server.exe
python slave_run.py
python slave_task_consumer.py
