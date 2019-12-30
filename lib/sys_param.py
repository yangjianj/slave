import psutil

def collect_net_io():
    #返回网卡流量统计
    result = {}
    for (k,v) in psutil.net_io_counters(pernic=True).items():
        result[k] = v._asdict()
    return  result

def collect_net_if_addrs():
    #返回网卡信息
    result = {}
    for (k,v) in psutil.net_if_addrs().items():
        result[k] = v
    return result

def collect_process():
    print(psutil.pids())

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
    result = []
    for part in psutil.disk_partitions():
        result.append(part._asdict())
        if part.fstype != '':
            result[-1].update(psutil.disk_usage(part.device)._asdict())
    result.append(psutil.disk_io_counters()._asdict())
    return result

def collect_memery():
    memoery = psutil.virtual_memory()._asdict()  #nametuple -> dict
    return memoery

def collect_cpu():
    return psutil.cpu_percent(interval=1, percpu=True)


#collect_cpu()
#collect_memery()
#collect_disk()
#collect_net_io()
#collect_net_if_addrs()
#collect_cpu()
