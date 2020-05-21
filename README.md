# slave
执行：
slave_run.py文件：web接口
slave_task_consumer.py文件：任务监听处理入口+心跳

功能描述：    
1.ui,api自动化任务执行器    
2.任务执行完日志收集及上传    
3.提供slave机器系统参数上报接口   
4.从ftpserver下载ui用例

实现介绍：   
1.ui自动化：yml存放页面元素定位信息，unittest组织用例结构，selenium驱动浏览器    
2.api自动化：根据任务传输的api case信息通过封装好的方法带入case信息而执行case    