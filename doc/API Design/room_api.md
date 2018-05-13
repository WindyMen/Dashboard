# Room [api/room/]
## 获取所有房间信息 [GET]
- Response 200 (application/json)    
HTTP/1.1 200 OK  

```
{
        "url": "http://172.18.159.245:8000/api/room/1/",
        "id": 1,
        "owner": "http://172.18.159.245:8000/api/user/fengyh/",
        "roomName": "慎思园六号",
        "roomType": "宿舍",
        "description": "test patch",
        "publish": "2018-05-11T10:52:23Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 4,
        "numOfBathroom": 1,
        "country": "中国",
        "province": "广东省",
        "city": "广州市",
        "town": "番禺区",
        "specificAddress": "小谷围中山大学慎思园六号522",
        "otherOption": "test patch2",
        "title": "中大宿舍",
        "photo1": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440.jpg",
        "photo2": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_COojanq.jpg",
        "photo3": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_4KGdjee.jpg",
        "photo4": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_uRqKbV4.jpg",
        "photo5": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_K9fladg.jpg",
        "photo6": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_6HhsMyK.jpg",
        "photo7": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_cMLHi60.jpg",
        "photo8": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_wXzUEtC.jpg",
        "photo9": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_NWpSjUs.jpg",
        "rating": 5,
        "room_comments": [
            "http://172.18.159.245:8000/api/comment/1/"
        ]
    },
    {
        "url": "http://172.18.159.245:8000/api/room/2/",
        "id": 2,
        "owner": "http://172.18.159.245:8000/api/user/gaomian/",
        "roomName": "慎思园七号",
        "roomType": "宿舍",
        "description": "无",
        "publish": "2018-05-11T10:53:44Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 4,
        "numOfBathroom": 1,
        "country": "中国",
        "province": "广东省",
        "city": "广州市",
        "town": "番禺区",
        "specificAddress": "小谷围中山大学慎思园七号",
        "otherOption": "无",
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
    },
    {
        "url": "http://172.18.159.245:8000/api/room/3/",
        "id": 3,
        "owner": "http://172.18.159.245:8000/api/user/fengzw/",
        "roomName": "慎思园六号",
        "roomType": "宿舍",
        "description": "test patch",
        "publish": "2018-05-11T10:52:23Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 4,
        "numOfBathroom": 1,
        "country": "中国",
        "province": "广东省",
        "city": "广州市",
        "town": "番禺区",
        "specificAddress": "小谷围中山大学慎思园六号522",
        "otherOption": "无",
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
    },
    {
        "url": "http://172.18.159.245:8000/api/room/4/",
        "id": 4,
        "owner": "http://172.18.159.245:8000/api/user/gaoxr/",
        "roomName": "慎思园六号",
        "roomType": "宿舍",
        "description": "无",
        "publish": "2018-05-11T10:52:23Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 4,
        "numOfBathroom": 1,
        "country": "中国",
        "province": "广东省",
        "city": "广州市",
        "town": "番禺区",
        "specificAddress": "小谷围中山大学慎思园六号522",
        "otherOption": "无",
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
    },
    {
        "url": "http://172.18.159.245:8000/api/room/5/",
        "id": 5,
        "owner": "http://172.18.159.245:8000/api/user/fujt/",
        "roomName": "山西主席家",
        "roomType": "民居",
        "description": "无",
        "publish": "2018-05-12T01:35:43Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 3,
        "numOfBathroom": 2,
        "country": "中国",
        "province": "山西省",
        "city": "大同",
        "town": "平城",
        "specificAddress": "主席家",
        "otherOption": "无",
        "title": "快去主席家玩",
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
    },
    {
        "url": "http://172.18.159.245:8000/api/room/6/",
        "id": 6,
        "owner": "http://172.18.159.245:8000/api/user/fengyh/",
        "roomName": "山西主席家",
        "roomType": "民居",
        "description": "无",
        "publish": "2018-05-12T01:35:43Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 3,
        "numOfBathroom": 2,
        "country": "中国",
        "province": "山西省",
        "city": "大同",
        "town": "平城",
        "specificAddress": "主席家",
        "otherOption": "无",
        "title": "快去主席家玩",
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
    },
    {
        "url": "http://172.18.159.245:8000/api/room/7/",
        "id": 7,
        "owner": "http://172.18.159.245:8000/api/user/fengzw/",
        "roomName": "山西主席家",
        "roomType": "民居",
        "description": "无",
        "publish": "2018-05-12T01:35:43Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 3,
        "numOfBathroom": 2,
        "country": "中国",
        "province": "山西省",
        "city": "大同",
        "town": "平城",
        "specificAddress": "主席家",
        "otherOption": "无",
        "title": "快去主席家玩",
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
    },
    {
        "url": "http://172.18.159.245:8000/api/room/9/",
        "id": 9,
        "owner": "http://172.18.159.245:8000/api/user/fengyh/",
        "roomName": "test",
        "roomType": "test",
        "description": "无",
        "publish": "2018-05-12T01:35:43Z",
        "startTime": "2018-05-01T12:00:00Z",
        "endTime": "2018-05-31T12:00:00Z",
        "numOfPerson": 4,
        "numOfBed": 3,
        "numOfBathroom": 2,
        "country": "中国",
        "province": "山西省",
        "city": "大同",
        "town": "平城",
        "specificAddress": "test",
        "otherOption": "无",
        "title": "test",
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
        "owner": "fengyh",  
        "roomName": "test",  
        "roomType": "test",  
        "description": "无",  
        "publish": "2018-05-12T01:35:43Z",  
        "startTime": "2018-05-01T12:00:00Z",  
        "endTime": "2018-05-31T12:00:00Z",  
        "numOfPerson": 4,  
        "numOfBed": 3,  
        "numOfBathroom": 2,  
        "country": "中国",  
        "province": "山西省",  
        "city": "大同",  
        "town": "平城",  
        "specificAddress": "test",  
        "otherOption": "无",  
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
        "owner": "fengyh",  
        "roomName": "test",  
        "roomType": "test",  
        "description": "无",  
        "publish": "2018-05-12T01:35:43Z",  
        "startTime": "2018-05-01T12:00:00Z",  
        "endTime": "2018-05-31T12:00:00Z",  
        "numOfPerson": 4,  
        "numOfBed": 3,  
        "numOfBathroom": 2,  
        "country": "中国",  
        "province": "山西省",  
        "city": "大同",  
        "town": "平城",  
        "specificAddress": "test",  
        "otherOption": "无",  
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
owner/country/province/city/town/或者图片错误  
信息不对应  

- Response 500 (application/json)
HTTP/1.1 500 Bad Inner Server Error
无法保存进数据库


# Room-info [api/room/$id/]
## 通过id获取房间信息 [GET]
- Response 200 (application/json)  
HTTP/1.1 200 OK  

```
{
    "url": "http://172.18.159.245:8000/api/room/1/",
    "id": 1,
    "owner": "http://172.18.159.245:8000/api/user/fengyh/",
    "roomName": "慎思园六号",
    "roomType": "宿舍",
    "description": "test patch",
    "publish": "2018-05-11T10:52:23Z",
    "startTime": "2018-05-01T12:00:00Z",
    "endTime": "2018-05-31T12:00:00Z",
    "numOfPerson": 4,
    "numOfBed": 4,
    "numOfBathroom": 1,
    "country": "中国",
    "province": "广东省",
    "city": "广州市",
    "town": "番禺区",
    "specificAddress": "小谷围中山大学慎思园六号522",
    "otherOption": "test patch2",
    "title": "中大宿舍",
    "photo1": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440.jpg",
    "photo2": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_COojanq.jpg",
    "photo3": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_4KGdjee.jpg",
    "photo4": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_uRqKbV4.jpg",
    "photo5": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_K9fladg.jpg",
    "photo6": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_6HhsMyK.jpg",
    "photo7": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_cMLHi60.jpg",
    "photo8": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_wXzUEtC.jpg",
    "photo9": "http://172.18.159.245:8000/image/room/137880_6_96_6f027bc98d16440_NWpSjUs.jpg",
    "rating": 5,
    "room_comments": [
        "http://172.18.159.245:8000/api/comment/1/"
    ]
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
    "roomName": "test",  
    "roomType": "test",  
    "description": "test",  
    "publish": "2018-05-12T01:35:43Z",  
    "startTime": "2018-05-01T12:00:00Z",  
    "endTime": "2018-05-31T12:00:00Z",  
    "numOfPerson": 4,  
    "numOfBed": 3,  
    "numOfBathroom": 2,  
    "country": "中国",  
    "province": "山西省",  
    "city": "大同",  
    "town": "平城",  
    "specificAddress": "test patch",  
    "otherOption": "无",  
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
{  
    "roomName": "test",  
    "roomType": "test",  
    "description": "test",  
    "publish": "2018-05-12T01:35:43Z",  
    "startTime": "2018-05-01T12:00:00Z",  
    "endTime": "2018-05-31T12:00:00Z",  
    "numOfPerson": 4,  
    "numOfBed": 3,  
    "numOfBathroom": 2,  
    "country": "中国",  
    "province": "山西省",  
    "city": "大同",  
    "town": "平城",  
    "specificAddress": "test patch",  
    "otherOption": "无",  
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
