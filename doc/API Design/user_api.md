# User [/api/user/]

## 注册[POST]

- Request (application/json)  
```
{
    "username": "fengyh",
    "password": "123456",
    "nickname": "xiandan"
}
```
- Response 201(application/json)  
HTTP/1.1 201 Created   
创建的信息：  
```
{
    "url": "http://172.18.159.245:8000/api/user/testpost/",
    "username": "testpost",
    "password": "123456",
    "nickname": "test",
    "owner_rooms": [],
    "user_order": [],
    "user_comments": []
}
```

- Response 400(application/json)  
HTTP/1.1 400 Bad Request  

```
{
    "username": [
        "user with this username already exists."
    ]
}
```


- Response 500 (application/json)  
Inner Server Error  
数据库保存不成功  

## 获取所有用户信息[GET]
-Response 200 (application/json)  
HTTP/1.1 200 OK  


```
{
    "url": "http://172.18.159.245:8000/api/user/fengyh/",
    "username": "fengyh",
    "password": "888888",
    "nickname": "xiandan",
    "owner_rooms": [
        "http://172.18.159.245:8000/api/room/1/",
        "http://172.18.159.245:8000/api/room/6/",
        "http://172.18.159.245:8000/api/room/9/"
    ],
    "user_order": [
        "http://172.18.159.245:8000/api/order/1/"
    ],
    "user_comments": [
        "http://172.18.159.245:8000/api/comment/1/"
    ]
},
{
    "url": "http://172.18.159.245:8000/api/user/gaomian/",
    "username": "gaomian",
    "password": "123456",
    "nickname": "nicho~",
    "owner_rooms": [
        "http://172.18.159.245:8000/api/room/2/"
    ],
    "user_order": [
        "http://172.18.159.245:8000/api/order/2/"
    ],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/fengzw/",
    "username": "fengzw",
    "password": "123456",
    "nickname": "weige",
    "owner_rooms": [
        "http://172.18.159.245:8000/api/room/3/",
        "http://172.18.159.245:8000/api/room/7/"
    ],
    "user_order": [
        "http://172.18.159.245:8000/api/order/3/"
    ],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/gaoxr/",
    "username": "gaoxr",
    "password": "123456",
    "nickname": "ruige",
    "owner_rooms": [
        "http://172.18.159.245:8000/api/room/4/"
    ],
    "user_order": [],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/fujt/",
    "username": "fujt",
    "password": "123456",
    "nickname": "主席",
    "owner_rooms": [
        "http://172.18.159.245:8000/api/room/5/"
    ],
    "user_order": [],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/testman/",
    "username": "testman",
    "password": "123456",
    "nickname": "test",
    "owner_rooms": [],
    "user_order": [],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/test2/",
    "username": "test2",
    "password": "123456",
    "nickname": "test2",
    "owner_rooms": [],
    "user_order": [],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/'test3'/",
    "username": "'test3'",
    "password": "123456",
    "nickname": "test patch1",
    "owner_rooms": [],
    "user_order": [],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/test3/",
    "username": "test3",
    "password": "'123456'",
    "nickname": "test patch",
    "owner_rooms": [],
    "user_order": [],
    "user_comments": []
},
{
    "url": "http://172.18.159.245:8000/api/user/testpost/",
    "username": "testpost",
    "password": "123456",
    "nickname": "test",
    "owner_rooms": [],
    "user_order": [],
    "user_comments": []
}

```

# User-info [/api/user/$username/]
## 获取用户信息[GET]  
可用于获取对应用户所新建的所有房间(owner_rooms)
- Response 200  (application/json)  
HTTP/1.1 200 OK  

```
{
    "url": "http://172.18.159.245:8000/api/user/fengyh/",
    "username": "fengyh",
    "password": "888888",
    "nickname": "xiandan",
    "owner_rooms": [
        "http://172.18.159.245:8000/api/room/1/",
        "http://172.18.159.245:8000/api/room/6/",
        "http://172.18.159.245:8000/api/room/9/"
    ],
    "user_order": [
        "http://172.18.159.245:8000/api/order/1/"
    ],
    "user_comments": [
        "http://172.18.159.245:8000/api/comment/1/"
    ]
}
```
- Response 404 (application/json)   
HTTP/1.1 404 Not Found  

```
{
    "detail": "Not found."
}
```


## 更新用户信息 [PATCH]
- Request (application/json)  
其中"password"和"nickname"均为可选  

```
{
    "password": "888888",
    "nickname": "xiandan"
}
```

- Response 200 (application/json) 
HTTP/1.1 200 OK   
返回修改后的信息

```
{
    "url": "http://172.18.159.245:8000/api/user/fengyh/",
    "username": "fengyh",
    "password": "888888",
    "nickname": "xiandan",
    "owner_rooms": [
        "http://172.18.159.245:8000/api/room/1/",
        "http://172.18.159.245:8000/api/room/6/",
        "http://172.18.159.245:8000/api/room/9/"
    ],
    "user_order": [
        "http://172.18.159.245:8000/api/order/1/"
    ],
    "user_comments": [
        "http://172.18.159.245:8000/api/comment/1/"
    ]
}
```


- Response 400 (application/json)  
HTTP/1.1 400 Bad Request  

```
{
    "detail": "request error."
}
```


## 删除用户 [DELETE]
HTTP/1.1 200 OK  
然后会再GET一次 就会抛出404  
HTTP 404 Not Found  

```
{  
    "detail": "Not found."  
}  
```



## 登陆
由于是开发微信小程序，所以在用户登陆方面只需要验证微信接口提供的id即可。
