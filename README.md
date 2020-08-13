# rest-django学习代码

## 教程

[地址1](https://www.django-rest-framework.org/tutorial/quickstart/#testing-our-api)
[地址2](https://www.django-rest-framework.org/tutorial/1-serialization/)

## 命令

* 创建一个项目叫做tutorial  
```django-admin startproject tutorial```

* 创建一个app叫snippets  
```python manage.py startapp snippets```

* 创建model变更  
```python manage.py makemigrations app```

* 查看model变更内容  
```python manage.py sqlmigrate app 0001```

* 将model变更更新到数据库  
```python manage.py migrate app```

* 创建用户  
```python manage.py createsuperuser```

* 查看数据库  
```python manage.py dbshell```
[sqlite命令](https://www.runoob.com/sqlite/sqlite-commands.html)

* 启动服务  
```python manage.py runserver```
