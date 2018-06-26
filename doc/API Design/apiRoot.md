Host: https://windymen.mynatapp.cc/

api的根目录，可用浏览器直接输入https://windymen.mynatapp.cc/ 即可查看根目录，如下：  

Response 200 (application/json)  
HTTP/1.1 200 OK
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "users": "https://windymen.mynatapp.cc/user/",
    "rooms": "https://windymen.mynatapp.cc/room/",
    "countrys": "https://windymen.mynatapp.cc/country/",
    "provinces": "http://172.18.159.245:8000/api/province/",
    "citys": "https://windymen.mynatapp.cc/city/",
    "towns": "https://windymen.mynatapp.cc/town/",
    "orders": "https://windymen.mynatapp.cc/order/",
    "comments": "https://windymen.mynatapp.cc/comment/"
}
```

然后可以在浏览器上点击对应的链接来获得想要的api
