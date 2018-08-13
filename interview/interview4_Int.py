'''
1. OSI七层和TCP/IP四层的关系
1.1 OSI引入了服务、接口、协议、分层的概念，TCP/IP借鉴了OSI的这些概念建立TCP/IP模型。
1.2 OSI先有模型，后有协议，先有标准，后进行实践；而TCP/IP则相反，先有协议和应用再提出了模型，且是参照的OSI模型。
1.3 OSI是一种理论下的模型，而TCP/IP已被广泛使用，成为网络互联事实上的标准。
TCP：transmission control protocol 传输控制协议
UDP：user data protocol 用户数据报协议
七层：应用层（Application）、表示层（Presentation）、会话层（Session）、传输层（Transport）
      网络层（Network）、数据链路层（Data Link）、物理层（Physical）
七层结构记忆方法：应、表、会、传、网、数、物
应用层协议需要掌握的是：HTTP（Hyper text transfer protocol）、FTP（file transfer protocol）、
                      SMTP（simple mail transfer rotocol）、POP3（post office protocol 3）、
                      IMAP4（Internet mail access protocol）

TCP/IP四层模型
应用层：对应OSI中的应用层、表示层、会话层
物理链路层：对应OSI中的数据链路层、物理层（也有叫网络接口层）
