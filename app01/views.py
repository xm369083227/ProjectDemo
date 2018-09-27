#coding:utf8
from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.

def login(request):
    error_msg = ""
    if request.method == "GET":
        return  render(request,"login.html",{"error_msg":error_msg})
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        user_obj = models.UserInfo.objects.filter(username=u,password=p).first()

        if user_obj:
            return redirect("/cmdb/user_info/")
        else:
            error_msg = "请输入正确的用户名密码。。"
            return render(request,"login.html",{"error_msg":error_msg})
    else:
        return redirect("login.html")


def index(request):
    return render(request,"index.html")

#增加功能
def user_info(request):
    if request.method == "GET":
        group_list = models.UserGroup.objects.all()
        user_list = models.UserInfo.objects.all()#返回的是多行数据的对象，需要循环输出
        return render(request,"user_info.html",{"user_list":user_list,"group_list":group_list})
    elif request.method == "POST":#接收前台form表单提交过来的数据
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        #将前台提交过来的数据写入数据库，然后GET方式重定向（相当于刷新页面）
        models.UserInfo.objects.create(username=u,password=p)
        return redirect("/cmdb/user_info/")

#详细页面功能
def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()#返回的是一个列表
    return render(request, "detail.html",{"obj":obj})

#删除功能
def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/cmdb/user_info/")

#编辑功能
def user_edit(request,nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request,"user_edit.html",{"obj":obj})
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        #找到nid对应的这条数据再update
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        #更新完毕后以GET方式刷新user_info页面即可
        return redirect("/cmdb/user_info")
# def orm(request):
#     #增加一条数据
#     #models.UserInfo.objects.create(username="root",password="123")
#     # models.UserInfo.objects.create(username="admin",password="123")
#     # models.UserInfo.objects.create(username="sa",password="123")
#
#     #查看所有数据
#     #result = models.UserInfo.objects.all()
#     #查看一条数据，返回的是一个列表，需要循环输出
#     # result = models.UserInfo.objects.filter(username="admin",password="123").first()
#     # for row in result:
#     #     print(row.id,row.username,row.password)
#
#     #删除一条数据
#     #models.UserInfo.objects.filter(id=5).delete()
#
#     #更新一条数据
#     models.UserInfo.objects.filter(id=1).update(password=666)
#     return HttpResponse("creat successful!")


def cpt(request):
    if request.method == "GET":
        return render(request,"cpt.html")
    elif request.method == "POST":
        cpt = request.POST.get("cpt")
        models.UserGroup.objects.update(caption=cpt)
        return render(request,"cpt.html")
