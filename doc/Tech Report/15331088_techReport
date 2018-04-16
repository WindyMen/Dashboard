# mysql数据库设计项目案例

标签（空格分隔）：mysql

---

因为设计数据库要从具体的案例着手，所以就以新闻发布数据库为例来设计数据表。
## 1.系统概述
    通过该新闻发布系统，管理员可以发布新闻信息、管理新闻信息。该新闻发布系统所要实现的功能有：新闻信息添加、新闻信息修改、新闻信息删除、显示全部新闻信息、按类别显示新闻信息、按关键字查询新闻信息、按关键字查询。

## 2.系统功能
    具体包括5个功能：用户管理、管理员管理、权限管理、新闻管理和评论管理。
## 3.数据库设计和实现
### 3.1设计表
首先设计名为webnews的数据库
```mysql
CREATE DATABASE webnews;
USE webnews;
```
设计user表
```mysql
CREATE TABLE user(
userID INT PRIMARY KEY UNIQUE NOT NULL,
userNmae VACHAR(20) NOT NULL,
userPassword VACHAR(20) NOT NULL,
sex VACHAR(10) NOT NULL,
userEmail VARCHAR(20) NOT NULL
);
```
设计admin表
```
CREATE TABLE admin(
adminID INT PRIMARY KEY UNIQUE NOT NULL,
adminNmae VACHAR(20) NOT NULL,
adminPassword VACHAR(20) NOT NULL,
);
```

设计roles表
```
CREATE TABLE admin(
adminID INT PRIMARY KEY UNIQUE NOT NULL,
adminName VARCHAR(20) NOT NULL,
adminPassword VARCHAR(20) NOT NULL
);
```

设计news表
```
CREATE TABLE news(
newsID INT PRIMARY KEY UNIQUE NOT NULL,
newsTITLE VARCHAR(50) NOT NULL,
newsContent TEXT NOT NULL,
newsDate TIMESTAMP,
newsDesc VACHAR(50) NOT NULL,
newsImagePath VARCHAR(50),
newsRate INT NOT NULL,
newsIsCheck BIT NOT NULL,
newsIsTop BIT NOT NULL
);
```

设计category表
```
CREATE TABLE category(
categoryID INT PRIMARY KEY UNIQUE NOT NULL,
categoryName VACHAR(50) NOT NULL,
categoryDesc VACHAR(50) NOT NULL
);
```

设计comment表
```
CREATE TABLE comment(
commentID INT PRIMARY KEY UNIQUE NOT NULL,
commentTITLE VARCHAR(50) NOT NULL,
commentContent TEXT NOT NULL,
commentDate DATETIME
);
```

设计admin_Roles表
```
CREATE TABLE admin_Roles(
aRID INT PRIMARY KEY UNIQUE NOT NULL,
adminID INT NOT NULL,
roleID INT NOT NULL
);
```

设计news_Comment表
```
CREATE TABLE news_Comment(
nCommentID INT PRIMARY KEY UNIQUE NOT NULL,
newsID INT NOT NULL,
commentID INT NOT NULL
);
```

设计user_Comment表
```
CREATE TABLE user_Comment(
uCID INT PRIMARY KEY UNIQUE NOT NULL,
userID INT NOT NULL,
commentID INT NOT NULL
);
```
### 3.2设计索引
索引可以对表上的某列值进行排序，提高查询速度
在news表上建立索引
```
CREATE INDEX index_new_title ON news (newsTitle);
```

在categroy表上建立索引
```
CREATE INDEX index_categroy ON categroy (categroyName);
```

在comment上建立索引
```
CREATE INDEX index_comment_title ON comment (commentTitle);
CREATE INDEX index_comment_date ON comment (commentDate);
```

### 3.3设计视图
视图可以方便用户对数据库的访问
创建news_view的视图
```
CREATE VIEW news_view
AS SELECT c.commentID, n.newsRate,n.newsTitle,n.newsContent,n.newsDate
FROM news_Comment c,news n
WHERE news_Comment.newsID=news.newsID;
```

### 3.4设计触发器
触发器用于满足某些特定操作，可以让程序自动进行，保证操作一致性。
设计update触发器

```
DELIMITER && 
CREATE TRIGGER update_newID AFTER UPDATE 
ON news FOR EACH ROW 
BEGIN 
    UPDATE news_Comment SET newsID=NEW.newID
END
&&
DELIMITER;
```

设计delete触发器
```
DELIMITER && 
CREATE TRIGGER delete_user AFTER DELETE 
ON user FOR EACH ROW 
BEGIN 
    DELETE FROM users_Comment WHERE userID=OLD.userID
END
&&
DELIMITER;
```


