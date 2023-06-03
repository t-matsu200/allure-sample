# -*- encoding: utf-8 -*-
import multiprocessing
import os

n_core = multiprocessing.cpu_count()
n_worker_pre_core = 1.0

bind = os.getenv('API_BIND', '0.0.0.0:8080')

loglevel = os.getenv('LOG_LEVEL', 'info')

workers = os.getenv('API_WORKERS', 'auto')
if workers == 'auto':
    workers = max(int(n_core * n_worker_pre_core), 1)
else:
    workers = int(workers)

accesslog = os.getenv('API_ACCESS_LOG', '-')

errorlog = os.getenv('API_ERROR_LOG', '-')

graceful_timeout = int(os.getenv('GRACEFUL_TIMEOUT', 120))

timeout = int(os.getenv('TIMEOUT', 120))

keepalive = int(os.getenv('KEEPALIVE', 5))

max_requests = int(os.getenv('MAX_REQUESTS', 10000))

max_requests_jitter = int(os.getenv('MAX_REQUESTS_JITTER', 200))
