由于微信小程序的API的照片的上传每次只能上传一张，所以需要写API来额外的保存照片。
##保存房间照片 [saveRoomPhoto/]

'''
- request (multipartform-data/json)
{
	"room_id":1,
	"file":xxx.jpg
}
'''

##获取房间照片 [getRoomPhoto/]

'''
- request (multipartform-data/json)
{
	"room_id":1
}

- response (multipartform-data/json)
这里一共有0-9次返回
{
	photo:"https://windymen.mynatapp.cc/image/rooms/xxx.jpg"
}
'''

##保存评论照片 [saveCommentPhoto/]

'''
- request (multipartform-data/json)
{
	"comment_id":1,
	"file":xxx.jpg
}
'''
##获取评论照片 [getCommentPhoto/]

'''
- request (multipartform-data/json)
{
	"comment_id":1
}

- response (multipartform-data/json)
这里一共n次返回
{
	photo:"https://windymen.mynatapp.cc/image/comments/xxx.jpg"
}
'''

其中返回的code与其他的api一致。
