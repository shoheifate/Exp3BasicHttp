# Please show HTTP Request and Response using curl command

[centos@ip-10-10-150-78 ~]$ curl -v 'localhost:8081/hi'
* About to connect() to localhost port 8081 (#0)
*   Trying ::1...
* 接続を拒否されました
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8081 (#0)
> GET /hi HTTP/1.1
> User-Agent: curl/7.29.0
> Host: localhost:8081
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: BaseHTTP/0.6 Python/3.6.8
< Date: Wed, 03 Jun 2020 11:20:20 GMT
< Hello: BasicHTTP!
< Content-Lengt: 13
< Content-Type: text/plain; charset=utf-8
< 
* Closing connection 0
10.10.150.78[centos@ip-10-10-150-78 ~]$ 
