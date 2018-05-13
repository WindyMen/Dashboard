# 通过国家/省份/城市/区来搜索房间 [api/country/$country_id/rooms/][api/province/$province_id/rooms/][api/city/$city_id/rooms/][api/town/$town_id/rooms/]

## 获取某城市的房间 [GET]
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
    }
```



- Response 404 (application/json)   
HTTP 404 Not Found  

```
{  
    "detail": "Not found."   
}
```