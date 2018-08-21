'''
haproxy是什么以及作用？
haproxy和keepalived的综合理解参照：https://blog.csdn.net/tuolaji8/article/details/52870791
haproxy原理：https://www.cnblogs.com/skyflask/p/6970151.html

HAProxy与LVS的异同
通过之前文章的介绍，大家应该基本清楚了HAProxy负载均衡与LVS负载均衡的优缺点和异同了。下面就这两种负载均衡软件的异同做一个简单总结：
1）两者都是软件负载均衡产品，但是LVS是基于Linux操作系统实现的一种软负载均衡，而HAProxy是基于第三应用实现的软负载均衡。
2）LVS是基于四层的IP负载均衡技术，而HAProxy是基于四层和七层技术、可提供TCP和HTTP应用的负载均衡综合解决方案。
3）LVS工作在ISO模型的第四层，因此其状态监测功能单一，而HAProxy在状态监测方面功能强大，可支持端口、URL、脚本等多种状态检测方式。
4）HAProxy虽然功能强大，但是整体处理性能低于四层模式的LVS负载均衡，而LVS拥有接近硬件设备的网络吞吐和连接负载能力。
综上所述，HAProxy和LVS各有优缺点，没有好坏之分，要选择哪个作为负载均衡器，要以实际的应用环境来决定。

