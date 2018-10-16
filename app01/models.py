from django.db import models

# Create your models here.

#创建表语句

# class UserGroup(models.Model):
#     uid = models.AutoField(primary_key=True)#自己写的主键，attoField指自增字段
#     caption = models.CharField(max_length=64,unique=True)#unique是添加唯一性索引
#     ctime = models.DateTimeField(auto_now_add=True,null=True)#null指是否可以为空,以后修改时这个字段的时间不再改变
#     mtime = models.DateTimeField(auto_now=True,null=True)#auto_now指修改时自动更新时间
#
# class UserInfo(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     email = models.CharField(max_length=20,null=True)
#     user_group = models.ForeignKey("UserGroup",to_field="uid",default=1,on_delete=models.CASCADE)
#     #外键关联方式，on_delete是django2.0后必须的参数，通过obj.user_group.caption调用userGroup表

class Business(models.Model):
    caption = models.CharField(max_length=64)
class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    b = models.ForeignKey("Business",to_field="id",default=1,on_delete=models.CASCADE)
class Application(models.Model):
    name = models.CharField(max_length=32)#应用名  WEB,DB,CACHE,PROXY...
    r = models.ManyToManyField("Host")#获取hostname通过  for i in obj.r.all===>i.hostname
# class APP(models.Model):
#     host = models.ForeignKey("Host",to_field="id",on_delete=models.CASCADE)#host_id
#     app = models.ForeignKey("Application",to_field="id",on_delete=models.CASCADE)#caption_id

class pagetest(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
