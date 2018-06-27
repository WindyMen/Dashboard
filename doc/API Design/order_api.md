# Order [order/]

## 获取所有订单信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK  

```
{
    "url": "https://windymen.mynatapp.cc/order/1/",
    "id": 1,
    "user": "https://windymen.mynatapp.cc/user/open_id/",
    "room": "https://windymen.mynatapp.cc/room/2/",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
},
{
    "url": "https://windymen.mynatapp.cc/order/2/",
    "id": 2,
    "user": "https://windymen.mynatapp.cc/user/open_id/",
    "room": "https://windymen.mynatapp.cc/room/1/",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
},
```

## 创建订单 [POST]
- Request (application/json)  

```
{
    "user": "open_id",
    "room": "2",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
}
```

- Response 201 (application/json)  
HTTP/1.1 200 CREATED  
返回的信息：  

```
{
    "user": "open_id",
    "room": "2",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
}
```

- Response 400  
HTTP/1.1 400 BAD REQUEST  

- Response 500  
HTTP/1.1 500 INNER SERVER ERROR  
无法保存进数据库，主要是uer或者room不存在，或者时间出错  

# Order-info [order/$id/]
## 获取特定id的订单信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK
```
{
    "url": "https://windymen.mynatapp.cc/order/1/",
    "id": 1,
    "user": "https://windymen.mynatapp.cc/user/open_id/",
    "room": "https://windymen.mynatapp.cc/room/2/",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
}
```

- Response 404 (application/json)  
HTTP/1.1 404 Not Found
```
{
    "detail": "Not Found."
}
```

## 更新订单信息 [PATCH]
- Request (application/json)  
以下的字段均为可选
```
{
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-14T12:00:00Z"
}
```

- Resonse 200 (application/json)  
HTTP/1.1 200 OK
更新后的信息：
```
{
    "url": "https://windymen.mynatapp.cc/order/1/",
    "id": 1,
    "user": "https://windymen.mynatapp.cc/user/open_id/",
    "room": "https://windymen.mynatapp.cc/room/2/",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
}
```

- Response 400 (application/json)  
HTTP/1.1 400 Bad Request  
```
{
    "detail": "Bad Request"
}
```

- Response 500 (application/json)  
HTTP/1.1 500 Inner Server Request  

```
{
    "detail": "Inner Server Request"
}
```

# 删除订单 [DELETE]
- Response 200 (application/json) 
HTTP/1.1 200 OK

- Response 404 (application/json)  
HTTP/1.1 404 Not Found


