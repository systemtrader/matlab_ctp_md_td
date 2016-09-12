使用apt或者zypper安装依赖库：
libboost_python
libboost_thread

比如ubuntu/mint下：
sudo apt install libboost-python-dev libboost-thread-dev

1.
使用的是linux版CTP，不准备在windows里面支持(因为这是个服务器程序，岂有服务器不用linux的道理)，编写完成以后老夫会把程序打包成docker镜像，部署的时候直接使用docker挂载就可以执行容器。如果你硬要在windows下面使用它，可以在windows下安装docker加载此程序。

2.模块之间传送消息使用文本的帧形式：
如果是通知，指令和事件型的消息，第一行是各字段的表头，第二行就是各字段对应的值
如果是序列型的消息，则消息帧的左上角(即第一行第一列的格子注明为series)，其后的第一列各格子都为时间戳(或者其他的有序索引)，每行为该时间戳对应的序列点实例
另外行宽度最好小于缓冲区长度(主要是接收方)，如果缓冲区不够大的话会写入硬盘的临时文件，造成性能瓶颈

3.