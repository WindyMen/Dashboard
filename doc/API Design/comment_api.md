# Comment [comment/]

## 获取所有评论信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK  

```
{
    "url": "https://windymen.mynatapp.cc/comment/1/",
    "id": 1,
    "user": "https://windymen.mynatapp.cc/user/open_id/",
    "room": "https://windymen.mynatapp.cc/room/1/",
    "text": "测试评论",
    "rating": 4,
    "photo": "https://windymen.mynatapp.cc/image/comments/xxx.jpg"
},
{
    "url": "https://windymen.mynatapp.cc/comment/2/",
    "id": 2,
    "user": "https://windymen.mynatapp.cc/user/open_id/",
    "room": "https://windymen.mynatapp.cc/room/2/",
    "text": "测试评论",
    "rating": 5,
    "photo": "https://windymen.mynatapp.cc/image/comments/xxx.jpg"
}

```

## 创建订单 [POST]
- Request (application/json)  
photo可以不填，默认为null  
```
{
    "user": "open_id",
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
    "user": "open_id",
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

# Comment-info [comment/$id/]
## 获取特定id的评论信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK
```
{
    "url": "https://windymen.mynatapp.cc/comment/1/",
    "id": 1,
    "user": "https://windymen.mynatapp.cc/user/fengyh/",
    "room": "https://windymen.mynatapp.cc/room/1/",
    "text": "测试评论",
    "rating": 4,
    "photo": "https://windymen.mynatapp.cc/image/comments/xxx.jpg"
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
    "url": "https://windymen.mynatapp.cc/comment/1/",
    "id": 1,
    "user": "https://windymen.mynatapp.cc/user/fengyh/",
    "room": "https://windymen.mynatapp.cc/room/1/",
    "text": "测试patch",
    "rating": 5,
    "photo": "https://windymen.mynatapp.cc/image/comments/xxx.jpg"
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


