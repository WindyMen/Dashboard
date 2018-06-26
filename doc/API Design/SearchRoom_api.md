# 通过国家/省份/城市/区来搜索房间 [country/$country_id/rooms/][province/$province_id/rooms/][city/$city_id/rooms/][town/$town_id/rooms/]

## 获取某城市的房间 [POST]
通过城市名以及入住时间、离店时间来搜索房间
'''
- request (application/json)
{
        "cityname":广州,
        "date_from_year":2018,
        "date_from_month":6,
        "date_from_day":20,
        "date_to_year":2018,
        "date_to_year":6,
        "date_to_year":21,
}
'''

- Response 200 (application/json)  
HTTP/1.1 200 OK  

```
{
        "url": "https://windymen.mynatapp.cc/room/1/",
        "id": 1,
        "owner": "https://windymen.mynatapp.ccuser/open_id/",
        "description": "test patch",
        "publish": "2018-06-20T10:52:23Z",
        "startTime": "2018-06-20T12:00:00Z",
        "endTime": "2018-06-21T12:00:00Z",
        "city": "广州市",
        "specificAddress": "小谷围中山大学慎思园六号522",
        "title": "中大宿舍",
        "photo1": "https://windymen.mynatapp.cc/image/room/1.jpg",
        "photo2": "https://windymen.mynatapp.cc/image/room/2.jpg",
        "photo3": "https://windymen.mynatapp.cc/image/room/3.jpg",
        "photo4": "https://windymen.mynatapp.cc/image/room/4.jpg",
        "photo5": "https://windymen.mynatapp.cc/image/room/5.jpg",
        "photo6": "https://windymen.mynatapp.cc/image/room/6.jpg",
        "photo7": "https://windymen.mynatapp.cc/image/room/7.jpg",
        "photo8": "https://windymen.mynatapp.cc/image/room/8.jpg",
        "photo9": "https://windymen.mynatapp.cc/image/room/9.jpg",
        "rating": 5,
        "room_comments": [
            "https://windymen.mynatapp.cc/comment/1/"
        ]
    },
    {
        "url": "https://windymen.mynatapp.cc/room/2/",
        "id": 2,
        "owner": "https://windymen.mynatapp.ccuser/open_id/",
        "description": "test patch",
        "publish": "2018-06-20T10:52:23Z",
        "startTime": "2018-06-20T12:00:00Z",
        "endTime": "2018-06-21T12:00:00Z",
        "city": "广州市",
        "specificAddress": "小谷围中山大学慎思园六号522",
        "title": "中大宿舍",
        "photo1": "https://windymen.mynatapp.cc/image/room/1.jpg",
        "photo2": "https://windymen.mynatapp.cc/image/room/2.jpg",
        "photo3": "https://windymen.mynatapp.cc/image/room/3.jpg",
        "photo4": "https://windymen.mynatapp.cc/image/room/4.jpg",
        "photo5": "https://windymen.mynatapp.cc/image/room/5.jpg",
        "photo6": "https://windymen.mynatapp.cc/image/room/6.jpg",
        "photo7": "https://windymen.mynatapp.cc/image/room/7.jpg",
        "photo8": "https://windymen.mynatapp.cc/image/room/8.jpg",
        "photo9": "https://windymen.mynatapp.cc/image/room/9.jpg",
        "rating": 5,
        "room_comments": [
            "https://windymen.mynatapp.cc/comment/2/"
        ]
    }
```



- Response 404 (application/json)   
HTTP 404 Not Found  

```
{  
    "detail": "Not found."   
}
```
