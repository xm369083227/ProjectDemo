from django.db import models

# Create your models here.

#���������

# class UserGroup(models.Model):
#     uid = models.AutoField(primary_key=True)#�Լ�д��������attoFieldָ�����ֶ�
#     caption = models.CharField(max_length=64,unique=True)#unique�����Ψһ������
#     ctime = models.DateTimeField(auto_now_add=True,null=True)#nullָ�Ƿ����Ϊ��,�Ժ��޸�ʱ����ֶε�ʱ�䲻�ٸı�
#     mtime = models.DateTimeField(auto_now=True,null=True)#auto_nowָ�޸�ʱ�Զ�����ʱ��
#
# class UserInfo(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     email = models.CharField(max_length=20,null=True)
#     user_group = models.ForeignKey("UserGroup",to_field="uid",default=1,on_delete=models.CASCADE)
#     #���������ʽ��on_delete��django2.0�����Ĳ�����ͨ��obj.user_group.caption����userGroup��

class Business(models.Model):
    caption = models.CharField(max_length=64)
class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    b = models.ForeignKey("Business",to_field="id",default=1,on_delete=models.CASCADE)
class Application(models.Model):
    name = models.CharField(max_length=32)#Ӧ����  WEB,DB,CACHE,PROXY...
    r = models.ManyToManyField("Host")#��ȡhostnameͨ��  for i in obj.r.all===>i.hostname
# class APP(models.Model):
#     host = models.ForeignKey("Host",to_field="id",on_delete=models.CASCADE)#host_id
#     app = models.ForeignKey("Application",to_field="id",on_delete=models.CASCADE)#caption_id

class pagetest(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=32)
