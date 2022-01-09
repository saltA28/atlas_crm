> 

# 开发环境
- Django 2.2.1
- Python 3.6
- Mysql 5.7

# 目录
- rbac **权限与菜单组件**
- stark **路由组件**
- web **业务逻辑**
- static **静态文件**
- Company.sql **数据库文件**
- GetFont.py **获取图标爬虫(不须使用)**



# 使用说明
1. 根目录下 `Company.sql` 为数据库， 需要先导入到自己数据库中！！！（数据库是我已经准备好的 ，需要导入一下）
2. 在 CompanyQuiry -> setting.py 中该部分设置导入后的数据库连接
   
    ```python
    DATABASES = {
        'default': {
            # 连接数据库类型 在末尾写入mysql即可
            'ENGINE': 'django.db.backends.mysql',
            # 数据库地址
            'HOST': '127.0.0.1',
            # 端口
            'PORT': 3306,
            # 数据库名
            'NAME': 'Company',
            # 用户
            'USER': 'root',
            # 密码
            'PASSWORD': ''
        }
    }
    ```
3. 启动Django项目

# 常见问题
- [添加菜单后页面访问失败] 
   ![](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/images/20191226/WX20191226-110123%402x.png)
    原因：菜单设置的路径名与model中不匹配导致无法自动寻找到路由
    ![](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/images/20191226/WX20191226-110354%402x.png)
    ![](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/images/20191226/WX20191226-110423%402x.png)
   



