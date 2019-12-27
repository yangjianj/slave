import psutil

def collect_network():
    print(psutil.net_io_counters())  # 获取网络总的io情况
    print(psutil.net_io_counters(pernic=True))  # 获取网络总的io情况
    print(psutil.net_if_addrs())
    print(psutil.net_if_stats())
    print(psutil.net_connections())
    pass

def collect_process():
    print(psutil.pids())
    print(psutil.test())
    pass

def process_handler(process_id):
    p = psutil.Process(process_id)
    p.name()
    p.cwd()
    p.status()
    p.create_time()
    p.memory_percent()
    p.memory_info()
    p.num_threads()

def collect_disk():
    print(psutil.disk_partitions())
    print(psutil.disk_usage('C:\\'))
    print(psutil.disk_io_counters())

def collect_memery():
    print(psutil.virtual_memory())

def collect_cpu():
    print(psutil.cpu_count())
    print(psutil.cpu_times())

    for i in range(2):
        print(psutil.cpu_percent(interval=1, percpu=True))

