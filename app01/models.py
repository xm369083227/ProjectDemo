from django.db import models

# Create your models here.

#���������

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)#�Լ�д��������attoFieldָ�����ֶ�
    caption = models.CharField(max_length=64,unique=True)#unique�����Ψһ������
    ctime = models.DateTimeField(auto_now_add=True,null=True)#nullָ�Ƿ����Ϊ��,�Ժ��޸�ʱ����ֶε�ʱ�䲻�ٸı�
    mtime = models.DateTimeField(auto_now=True,null=True)#auto_nowָ�޸�ʱ�Զ�����ʱ��

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=20,null=True)
    user_group = models.ForeignKey("UserGroup",to_field="uid",default=1,on_delete=models.CASCADE)
    #���������ʽ��on_delete��django2.0�����Ĳ�����ͨ��obj.user_group.caption����userGroup��