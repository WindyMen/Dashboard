- version1

  由于使用的是django的rest_frame框架  
  大体上的开发可以使用可视化的API  
  在浏览器中输入  
  http://172.18.159.245:8000/api/  
  即可访问API，点解链接可以跳转对应的json信息  
  同时提供后台数据库修改的管理员权限，浏览器输入：  
  http://172.18.159.245:8000/admin/  
  账号：superadmin  
  密码: superadmin  
  可修改数据库里的数据
  
  
- version2
由于后期决定写小程序，所以不能用本地ip  
小程序的安全性要求比较高，要求有ssl证书以及https访问  
所以需要租用服务器，并且备案，获得能用的域名  
但是我发现域名的申请比较贵  
而且是比较加急的域名备案  
怕时间赶不及  
所以用内网穿透来实现小程序的测试开发  
我们购买natapp的一些隧道来实现，具体看官网：  
https://natapp.cn/  
所以可以访问:  
https://windymen.mynatapp.cc/  
即可访问我们的可视化API。  
