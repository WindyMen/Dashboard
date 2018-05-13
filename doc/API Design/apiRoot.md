Host: 172.18.159.245:8000/api/

api的根目录，可用浏览器直接输入172.18.159.245:8000/api/即可查看根目录，如下：  

Response 200 (application/json)  
HTTP/1.1 200 OK
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "users": "http://172.18.159.245:8000/api/user/",
    "rooms": "http://172.18.159.245:8000/api/room/",
    "countrys": "http://172.18.159.245:8000/api/country/",
    "provinces": "http://172.18.159.245:8000/api/province/",
    "citys": "http://172.18.159.245:8000/api/city/",
    "towns": "http://172.18.159.245:8000/api/town/",
    "orders": "http://172.18.159.245:8000/api/order/",
    "comments": "http://172.18.159.245:8000/api/comment/"
}
```

然后可以在浏览器上点击对应的链接来获得想要的api