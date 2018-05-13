# 全部国家/省份/城市/区的信息 [api/country/][api/province/][api/city/][api/town/]
## 获取全部国家/省份/城市/区的名称和id [GET]
- Response 200 (application/json)  

```
{  
        "id": 1,  
        "countryname": "中国"  
}
```


# 通过id获取某国家/省份/城市/区的信息 [api/country/$id/][api/province/$id/][api/city/$id/][api/town/$id/]
## 获取某国家/省份/城市/区的名称和id [GET]
- Response 200 (application/json) 


```
{
    "id": 1,
    "countryname": "中国"
}
```


- Response 404 (application/json)   
HTTP 404 Not Found  

```
{  
    "detail": "Not found."  
}
```


Province/City/Town的api和上面一样