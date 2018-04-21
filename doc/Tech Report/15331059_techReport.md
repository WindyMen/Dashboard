## Vue框架之路由技术学习报告



### 创建组件

首先引入vue.js和vue-router.js：

```<script src="js/vue.js"></script>```  

```<script src="js/vue-router.js"></script>```  

然后创建两个组件构造器Home和About：  

```
var Home = Vue.extend({  
    template: '<div><h1>Home</h1><p>{{msg}}</p></div>',
    data: function() {
        return {
            msg: 'Hello, vue router!'
        }
    }
})  
var About = Vue.extend({
    template: '<div><h1>About</h1><p>This is the tutorial about vue-router.</p></div>'
})
```

### 创建Router

var router = new VueRouter()
调用构造器VueRouter，创建一个路由器实例router。

### 映射路由

```router.map({
    '/home': { component: Home },
    '/about': { component: About }
})```  

调用router的map方法映射路由，每条路由以key-value的形式存在，key是路径，value是组件。
例如：'/home'是一条路由的key，它表示路径；{component: Home}则表示该条路由映射的组件。

### 使用v-link指令

```<div class="list-group">
    <a class="list-group-item" v-link="{ path: '/home'}">Home</a>
    <a class="list-group-item" v-link="{ path: '/about'}">About</a>
</div>```  

在a元素上使用v-link指令跳转到指定路径。

### 使用<router-view>标签

```<router-view></router-view>```  

在页面上使用<router-view></router-view>标签，它用于渲染匹配的组件。

### 启动路由

```var App = Vue.extend({})
router.start(App, '#app')
```
  
路由器的运行需要一个根组件，router.start(App, '#app') 表示router会创建一个App实例，并且挂载到#app元素。
注意：使用vue-router的应用，不需要显式地创建Vue实例，而是调用start方法将根组件挂载到某个元素。