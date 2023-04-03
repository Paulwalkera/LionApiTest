####  💎介绍

这是一款提效于API自动化的工具，基于HttpRunner封装的的接口自动化测试平台，主要采用Python+Django+Vue开发，能从0打造所属项目的api自动化，快速上手，搭建落地建设项目接口自动化。

#### ⛏ 在线体验

[🎁 快点我](https://github.com/Paulwalkera/LionApiTest-front)

![image](https://user-images.githubusercontent.com/67620367/229406903-393be6d9-7ffa-4746-815d-43319d4d5ef5.png)

#### 🎉 技术栈

- [x]  🎨 Django
- [x]  🎶 Django Rest Framework
- [x]  🎉 Httprunner
- [x]  🎃 MariaDB
- [x]  🏐 Gunicorn(内含uvicorn，部署服务) 
- [x]  🎲 Nginx(反向代理，https配置等)

#### ⚽ 前端地址

[🎁 快点我](https://github.com/Paulwalkera/LionApiTest-front)


#### 🔥 已有功能

| 功能点         | 状态 |
| :------------- | ---- |
| HttpRunner特性 | ✅    |
| http测试       | ✅    |
| 全局变量       | ✅    |
| 参数提取       | ✅    |
| 后台管理       | ✅    |
| 场景测试       | ✅    |
| 测试报告       | ✅    |
| 测试集合       | ✅    |
| 自定义脚本     | ✅    |
| 项目管理       | ✅    |

#### 🚚 即将到来

| 功能点             | 敬请期待 |
| ------------------ | -------- |
| CI/CD              | 🎉🎉🎉      |
| har接口导入        | 🎉🎉🎉      |
| Locust             | 🎉🎉🎉      |
| Mock               | 🎉🎉🎉      |
| 数据工厂           | 🎉🎉🎉      |
| 流量回放           | 🎉🎉🎉      |
| 企微/钉钉/飞书通知 | 🎉🎉🎉      |

#### ⭐ 本地开发

##### 1.拉取代码

```shell
$ git clone https://github.com/Paulwalkera/LionApiTest
$ cd LionApiTest
```

##### 2.安装依赖

```shell
# 可换豆瓣源或者清华源安装依赖
$ pip install -r requirements.txt
```

##### 3.安装mysql数据库

##### 4.新建数据库

##### 5.修改dev07/settings.py数据库连接信息

##### 6.启动服务

```shell
python manage.py
```

##### 7.打开浏览器`http://localhost:8866`进入登录页

#### ⭐ Docker部署

##### 1.修改.env

##### 2.安装Docker

```shell
docker-compose -p myapp up -d
```


