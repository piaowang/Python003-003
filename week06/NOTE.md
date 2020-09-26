学习笔记
启动
python manage.py runserver


从 Django 到 SQL
• python manage.py migrate
• 从 SQL 到 Django
• python manage.py inspectdb


 forloop.counter 来作为页面显示的自然序号
 
 
 在index这个app中增加一个方法用来输出movie_comment
 
 影评的sql放在index_comment.sql中
 
 get方法有两种，一个就是直接用？隔开，这种方法传递进去的本身还是在本页面。 路由跳转不出去。
 需要进行一个表单指定的路由，告知，点击就是查询路径下进行的get方法，然后将结果传入对应的模板即可。