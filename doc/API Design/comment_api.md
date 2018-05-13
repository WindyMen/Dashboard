# Comment [api/comment/]

## 获取所有评论信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK  

```
{
    "url": "http://172.18.159.245:8000/api/comment/1/",
    "id": 1,
    "user": "http://172.18.159.245:8000/api/user/fengyh/",
    "room": "http://172.18.159.245:8000/api/room/1/",
    "text": "测试评论",
    "rating": 4,
    "photo": "http://172.18.159.245:8000/image/comments/137880_6_96_6f027bc98d16440.jpg"
},
{
    "url": "http://172.18.159.245:8000/api/comment/2/",
    "id": 2,
    "user": "http://172.18.159.245:8000/api/user/gaomian/",
    "room": "http://172.18.159.245:8000/api/room/2/",
    "text": "测试评论2",
    "rating": 5,
    "photo": null
}

```

## 创建订单 [POST]
- Request (application/json)  
photo可以不填，默认为null  
```
{
    "user": "fengyh",
    "room": "3",
    "text": "房间很好",
    "rating": 5,
    "photo": "xxx.jpg"
}

```

- Response 201 (application/json)  
HTTP/1.1 200 CREATED  
返回的信息：  

```
{
    "user": "fengyh",
    "room": "3",
    "text": "房间很好",
    "rating": 5,
    "photo": "xxx.jpg"
}
```

- Response 400    
HTTP/1.1 400 BAD REQUEST  

```
{
    "detail": "Bad Request"
}
```



- Response 500  
HTTP/1.1 500 INNER SERVER ERROR  

```
{
    "detail": "Inner Server Error"
}
```

无法保存进数据库，主要是uer或者room不存在，或者时间出错  

# Comment-info [api/comment/$id/]
## 获取特定id的评论信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK
```
{
    "url": "http://172.18.159.245:8000/api/comment/1/",
    "id": 1,
    "user": "http://172.18.159.245:8000/api/user/fengyh/",
    "room": "http://172.18.159.245:8000/api/room/1/",
    "text": "测试评论",
    "rating": 4,
    "photo": "http://172.18.159.245:8000/image/comments/137880_6_96_6f027bc98d16440.jpg"
}
```

- Response 404 (application/json)  
HTTP/1.1 404 Not Found
```
{
    "detail": "Not Found."
}
```

## 更新评论信息 [PATCH]
- Request (application/json)  
以下的字段均为可选
```
{
    "text": "测试patch",
    "rating": 5,
    "photo": "xxx.jpg"
}
```

- Resonse 200 (application/json)  
HTTP/1.1 200 OK
更新后的信息：
```
{
    "url": "http://172.18.159.245:8000/api/comment/1/",
    "id": 1,
    "user": "http://172.18.159.245:8000/api/user/fengyh/",
    "room": "http://172.18.159.245:8000/api/room/1/",
    "text": "测试patch",
    "rating": 5,
    "photo": "http://172.18.159.245:8000/image/comments/137880_6_96_6f027bc98d16440.jpg"
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


