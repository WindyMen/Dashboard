# Order [api/order/]

## 获取所有订单信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK  

```
{
    "url": "http://172.18.159.245:8000/api/order/1/",
    "id": 1,
    "user": "http://172.18.159.245:8000/api/user/fengyh/",
    "room": "http://172.18.159.245:8000/api/room/2/",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
},
{
    "url": "http://172.18.159.245:8000/api/order/2/",
    "id": 2,
    "user": "http://172.18.159.245:8000/api/user/gaomian/",
    "room": "http://172.18.159.245:8000/api/room/1/",
    "orderTime": "2018-05-11T10:57:07Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-13T12:00:00Z"
},
{
    "url": "http://172.18.159.245:8000/api/order/3/",
    "id": 3,
    "user": "http://172.18.159.245:8000/api/user/fengzw/",
    "room": "http://172.18.159.245:8000/api/room/5/",
    "orderTime": "2018-05-11T10:57:07Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-14T12:00:00Z"
}
```

## 创建订单 [POST]
- Request (application/json)  

```
{
    "user": "fengyh",
    "room": "7",
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
    "user": "fengyh",
    "room": "7",
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

# Order-info [api/order/$id/]
## 获取特定id的订单信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK
```
{
    "url": "http://172.18.159.245:8000/api/order/1/",
    "id": 1,
    "user": "http://172.18.159.245:8000/api/user/fengyh/",
    "room": "http://172.18.159.245:8000/api/room/2/",
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
    "url": "http://172.18.159.245:8000/api/order/1/",
    "id": 1,
    "user": "http://172.18.159.245:8000/api/user/fengyh/",
    "room": "http://172.18.159.245:8000/api/room/2/",
    "orderTime": "2018-05-11T10:56:23Z",
    "arrivalData": "2018-05-12T12:00:00Z",
    "departureData": "2018-05-14T12:00:00Z"
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


