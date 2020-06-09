 curl -v -s 'localhost:8081/hi?param1=value1&param2=value2'
*   Trying ::1...
* TCP_NODELAY set
* Connection failed
* connect to ::1 port 8081 failed: Connection refused
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8081 (#0)
> GET /hi?param1=value1&param2=value2 HTTP/1.1
> Host: localhost:8081
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: BaseHTTP/0.6 Python/3.6.4
< Date: Tue, 09 Jun 2020 13:08:08 GMT
< Hello: BasicHTTP!
< Content-Lengt: 13
< Content-Type: text/plain; charset=utf-8
< 
* Closing connection 0
192.168.33.1%             
