# User [/user/]
https://windymen.mynatapp.cc/user/
由于使用微信小程序，所以只需要保存从微信获得的open_id即可，然后再保存用户在微信的信息

## 获取所有用户信息[GET]
-Response 200 (application/json)  
HTTP/1.1 200 OK  

```
[  
    {  
        "url": "http://windymen.mynatapp.cc/user/o_yAE5qCnd1N-XccUf6Hxxxxxxxs/",  
        "openid": "o_yAE5qCnd1N-XccUf6HFudpr-Is",  
        "nickname": "Fengzw",  
        "email": "13690760178@qq.com",  
        "phone": "13690760178",  
        "photo": "https://wx.qlogo.cn/mmopen/vi_32/oJh4gicrmVaahbDKEterBgAUW87C6rZ5VdibVicdoZFmDiaficanTic2UoHBuhhVEcj2sNjM3gXcI0K4hemSd2uLOJPw/132",  
        "owner_rooms": [  
            "http://windymen.mynatapp.cc/room/57/",  
            "http://windymen.mynatapp.cc/room/58/",  
            "http://windymen.mynatapp.cc/room/59/",  
            "http://windymen.mynatapp.cc/room/62/",  
            "http://windymen.mynatapp.cc/room/63/",  
            "http://windymen.mynatapp.cc/room/64/"  
        ],  
        "user_order": [],  
        "user_comments": []  
    },  
    {  
        "url": "http://windymen.mynatapp.cc/user/o_yAE5ocPzTshI0xxxx/",  
        "openid": "o_yAE5ocPzTshI0bNCi55ivfaOk4",  
        "nickname": "咸蛋～",  
        "email": "test",  
        "phone": "15521094460",  
        "photo":  "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIFLHTQnrg2hFqoceSD85X5pgK5jm8Z1JzfzlQSZb9sPHYK1FA0lWonF5uu7jdN0eqzU466ZZUqxA/132",  
        "owner_rooms": [],  
        "user_order": [],  
        "user_comments": []  
    },  
    {
        "url": "http://windymen.mynatapp.cc/user/o_yAE5gKD6Ivli7xxxxxx/",  
        "openid": "o_yAE5gKD6Ivli7DiRemq7cfQwtQ",  
        "nickname": "木公",  
        "email": "22112",  
        "phone": "1221",  
        "photo":  "https://wx.qlogo.cn/mmopen/vi_32/6iaSSKMHMVCr0XRyPftCmZA06oe0WvOWfoyQHjnopjZZsh5s3FicWau4jRr8IY7wAvkSzbh9wHWH2s2kMBq12hsw/132",  
        "owner_rooms": [  
            "http://windymen.mynatapp.cc/room/60/",  
            "http://windymen.mynatapp.cc/room/61/"  
        ],  
        "user_order": [],  
        "user_comments": []  
    },  
    {  
        "url": "http://windymen.mynatapp.cc/user/oxxx-8z-qAWAQCOnZI/",  
        "openid": "o_yAE5lIqhX78d-8z-qAWAQCOnZI",  
        "nickname": "风猫",  
        "email": "null",  
        "phone": "null",  
        "photo": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJXZz2yX937P1x4jcdRQfsQXX7ImszHQlYOmdbSsKMHH8zBFs6nVdjLInYBuCXaGmPtJ9GLN52SMA/132",  
        "owner_rooms": [],  
        "user_order": [],  
        "user_comments": []  
    }  
]  
  
``` 

# User-info [/api/user/$open_id/]
## 获取用户信息[GET]  
可用于获取对应用户所新建的所有房间(owner_rooms)
- Response 200  (application/json)  
HTTP/1.1 200 OK  

```
{  
        "url": "http://windymen.mynatapp.cc/user/o_yAE5ocPzTshI0xxxx/",  
        "openid": "o_yAE5ocPzTshI0bNCi55ivfaOk4",  
        "nickname": "咸蛋～",  
        "email": "test",  
        "phone": "15521094460",  
        "photo":  "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIFLHTQnrg2hFqoceSD85X5pgK5jm8Z1JzfzlQSZb9sPHYK1FA0lWonF5uu7jdN0eqzU466ZZUqxA/132",  
        "owner_rooms": [],  
        "user_order": [],  
        "user_comments": []  
    }, 
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
        "nickname": "咸蛋～",  
        "email": "test",  
        "phone": "15521094460",  
        "photo":  "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIFLHTQnrg2hFqoceSD85X5pgK5jm8Z1JzfzlQSZb9sPHYK1FA0lWonF5uu7jdN0eqzU466ZZUqxA/132"  
    }, 
```

- Response 200 (application/json) 
HTTP/1.1 200 OK   
返回修改后的信息

```
{  
        "url": "http://windymen.mynatapp.cc/user/o_yAE5ocPzTshI0xxxx/",  
        "openid": "o_yAE5ocPzTshI0bNCi55ivfaOk4",  
        "nickname": "咸蛋～",  
        "email": "test",  
        "phone": "15521094460",  
        "photo":  "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIFLHTQnrg2hFqoceSD85X5pgK5jm8Z1JzfzlQSZb9sPHYK1FA0lWonF5uu7jdN0eqzU466ZZUqxA/132",  
        "owner_rooms": [],  
        "user_order": [],  
        "user_comments": []  
    }, 
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
