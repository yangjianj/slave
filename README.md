# slave
执行：  
开启redis服务  
slave_run.py文件：web接口,提供对slave的其他操作  
slave_task_consumer.py文件：任务监听处理入口+心跳  

功能描述：    
1.ui,api自动化任务执行器    
2.任务执行完日志收集及上传    
3.提供slave机器系统参数上报接口   
4.从ftpserver下载ui用例

实现介绍：   
1.ui自动化：yml存放页面元素定位信息，unittest组织用例结构，selenium驱动浏览器    
2.api自动化：根据任务传输的api case信息通过封装好的方法带入case信息而执行case    
3.redis实现任务的收发（redis简单无需安装，适合放在git上）   


详情：    
1.任务格式：    
    task = {"id": 5662356461,
            "type": "api",
            "slave": "1.1.1.1",
            "version": "0.0.1",
             "cases": [
                     {"caseid": "api_00002",  "project": "wuliu", "api_name": "login",
                      "url": "http://www.kuaidi100.com/query",
                      "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                      "params":{"type":"yunda","postid":"3835494398576"},
                      "data": '{"q":"w"}',
                      "status":"unfinished",
                      "expected": {"type": "object",
                                   "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                  "data": {"type": "array"}}}},
                     {"caseid": "api_00001", "project": "wuliu", "api_name": "login",
                      "url": "http://www.kuaidi100.com/query",
                      "protocol": "http", "headers": {"Content-Type":"application/json;charset=UTF-8"}, "method": "post",
                      "params":{"type":"yuantong","postid":"823753023765"},
                      "data": '{"q":"w"}',
                      "status":"unfinished",
                      "expected": {"type": "object",
                                   "properties": {"nu": {"type": "string"}, "status": {"type": "string"},
                                                  "data": {"type": "array"}}}}
                 ]
                     }

    task = {"id": 5662356461,
            "type": "ui",
            "slave":"1.1.1.1",
            "version": "0.0.1",
            "project": "lianjia",
             "cases": [
                    {"suitename": "ui_lianjia_test_001", "project": "lianjia","function": "login","status":"unfinished"},
                    {"suitename": "ui_lianjia_test_001","project": "lianjia", "function": "login","status":"unfinished"},
                     ]
                     }