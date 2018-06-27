# Room [room/]
## 获取所有房间信息 [GET]
- Response 200 (application/json)    
HTTP/1.1 200 OK  

```
{
        "url": "https://windymen.mynatapp.cc/room/1/",  
        "id": 1,  
        "owner": "https://windymen.mynatapp.cc/user/o_yxxxf6HFudpr-Is/",  
        "price": 123.4
        "description": "test patch",  
        "publish": "2018-05-11T10:52:23Z",  
        "startTime": "2018-05-01T12:00:00Z",   
        "endTime": "2018-05-31T12:00:00Z",  
        "city": "广州市",  
        "specificAddress": "小谷围中山大学慎思园六号522",  
        "otherOption": "test patch2",  
        "title": "中大宿舍",  
        "photo1": null,  
        "photo2": null,  
        "photo3": null,  
        "photo4": null,  
        "photo5": null,  
        "photo6": null,  
        "photo7": null,  
        "photo8": null,  
        "photo9": null,  
        "rating": 5,  
        "room_comments": [  
            "https://windymen.mynatapp.cc/comment/1/"  
        ]  
    },  
    {  
        "url": "https://windymen.mynatapp.cc/room/1/", 
        "id": 2,
        "owner": "https://windymen.mynatapp.cc/user/o_yAE5qCnxxFudpr-Is/",
        "price": 666.0
        "description": "无",
        "publish": "2018-05-11T10:53:44Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "city": "广州市",
        "specificAddress": "小谷围中山大学慎思园七号",
        "title": "中大宿舍",
        "photo1": null,
        "photo2": null,
        "photo3": null,
        "photo4": null,
        "photo5": null,
        "photo6": null,
        "photo7": null,
        "photo8": null,
        "photo9": null,
        "rating": 5,
        "room_comments": []
    }

```



## 创建房间信息 [POST]
- Request (application/json)  

```
{  
        "owner": "xxxxxxxxxx(open_id)",
        "price": 123.4
        "description": "无",  
        "publish": "2018-05-12T01:35:43Z",  
        "startTime": "2018-05-01T12:00:00Z",  
        "endTime": "2018-05-31T12:00:00Z",  
        "city": "大同",  
        "specificAddress": "test",   
        "title": "test",  
        "photo1": xxx.jpg,
        "photo2": xxx.jpg,
        "photo3": xxx.jpg,
        "photo4": xxx.jpg,
        "photo5": xxx.jpg,
        "photo6": xxx.jpg,
        "photo7": xxx.jpg,
        "photo8": xxx.jpg,
        "photo9": xxx.jpg,
        "rating": 5  
}
```

- Response 201 (application/json)  
HTTP/1.1 201 Created

```
{  
        "owner": "xxxxxxxxxx(open_id)",
        "price": 123.4
        "description": "无",  
        "publish": "2018-05-12T01:35:43Z",  
        "startTime": "2018-05-01T12:00:00Z",  
        "endTime": "2018-05-31T12:00:00Z",  
        "city": "大同",  
        "specificAddress": "test",   
        "title": "test",  
        "photo1": xxx.jpg,
        "photo2": xxx.jpg,
        "photo3": xxx.jpg,
        "photo4": xxx.jpg,
        "photo5": xxx.jpg,
        "photo6": xxx.jpg,
        "photo7": xxx.jpg,
        "photo8": xxx.jpg,
        "photo9": xxx.jpg,
        "rating": 5  
}
```


- Response 400 (application/json) 
HTTP/1.1 400 Bad Request  
owner/city/或者图片错误  
信息不对应  

- Response 500 (application/json)
HTTP/1.1 500 Bad Inner Server Error
无法保存进数据库


# Room-info [room/$id/]
## 通过id获取房间信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK  

```
{  
        "url": "https://windymen.mynatapp.cc/room/1/", 
        "id": 2,
        "owner": "https://windymen.mynatapp.cc/user/o_yAE5xxxxf6HFudpr-Is/",
        "price": 666.0
        "description": "无",
        "publish": "2018-05-11T10:53:44Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "city": "广州市",
        "specificAddress": "小谷围中山大学慎思园七号",
        "title": "中大宿舍",
        "photo1": null,
        "photo2": null,
        "photo3": null,
        "photo4": null,
        "photo5": null,
        "photo6": null,
        "photo7": null,
        "photo8": null,
        "photo9": null,
        "rating": 5,
        "room_comments": []
    }
```


- Response 404 (application/json)  
HTTP/1.1 404 NOT FOUND  

```
{  
    "detail": "Not found."  
}
```

## 更新房间信息 [PATCH]
- Request(application/json)   
以下所有均可选，不一样全部Request，注意最后没有','否则会400  

```
{  
    "price": 123.4,
    "description": "test",  
    "publish": "2018-05-12T01:35:43Z",  
    "startTime": "2018-05-01T12:00:00Z",  
    "endTime": "2018-05-31T12:00:00Z",  
    "city": "大同",  
    "specificAddress": "test patch",   
    "title": "快去主席家玩",  
    "photo1": xxx.jpg,
    "photo2": xxx.jpg,
    "photo3": xxx.jpg,
    "photo4": xxx.jpg,
    "photo5": xxx.jpg,
    "photo6": xxx.jpg,
    "photo7": xxx.jpg,
    "photo8": xxx.jpg,
    "photo9": xxx.jpg,
    "rating": 5  
}
```

- Response 200(application/json)    
HTTP/1.1 200 OK

```
{   "owner": "xxxx",
    "price": 123.4,
    "description": "test",  
    "publish": "2018-05-12T01:35:43Z",  
    "startTime": "2018-05-01T12:00:00Z",  
    "endTime": "2018-05-31T12:00:00Z",  
    "city": "大同",  
    "specificAddress": "test patch",   
    "title": "快去主席家玩",  
    "photo1": xxx.jpg,
    "photo2": xxx.jpg,
    "photo3": xxx.jpg,
    "photo4": xxx.jpg,
    "photo5": xxx.jpg,
    "photo6": xxx.jpg,
    "photo7": xxx.jpg,
    "photo8": xxx.jpg,
    "photo9": xxx.jpg,
    "rating": 5  
}
```


- Response 400(application/json)  
Request的参数错误

- Response 500(application/json)  
无法保存入数据库

## 删除房间信息 [DELETE]
HTTP/1.1 200 OK  
然后会再GET一次 就会抛出404  
HTTP 404 Not Found  

```
{  
    "detail": "Not found."  
}
```
