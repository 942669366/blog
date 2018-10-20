from django.shortcuts import render
from blogapp.models import blogtxt,comment,admin
from django.core.paginator import Paginator
from django.http import HttpResponse
import time
# Create your views here.
def blog(request,pagenum):#进入博客主页面
    bl = blogtxt.objects.filter()
    # nua=blogtxt.objects.filter(blogtype=0)
    # nub=blogtxt.objects.filter(blogtype=1)
    # nuc=blogtxt.objects.filter(blogtype=2)
    # nud=blogtxt.objects.filter(blogtype=3)
    come=[]
    for bli in bl:
        pid=bli.blogid
        come.append(len(comment.objects.filter(blogtype=pid)))
    tong=len(blogtxt.objects.filter(blogtype=0))
    pjc=len(blogtxt.objects.filter(blogtype=1))
    pweb=len(blogtxt.objects.filter(blogtype=2))
    ppa=len(blogtxt.objects.filter(blogtype=3))
    pi=Paginator(bl,3)
    pnums=pi.num_pages
    page=pi.page(pagenum)
    pnum=page.number
    sslist=page.object_list
    # come=comment.objects.filter(blogtype=pid)
    return render(request,'blog.html',{"bl":bl,"sslist":sslist,"pnum":pnum,"pnums":pnums,"come":come,"tong":tong,"pjc":pjc,"pweb":pweb,"ppa":ppa})

def news(request,num):#进入博客文章主体
    bl=blogtxt.objects.filter(blogid=num)
    pl=comment.objects.filter(blogtype=num)
    come=[]
    come.append(len(pl))
    # for bll in bl:
    #     blogid=bll.blogid
    #     title=bll.blogtitle#标题
    #     bloga=bll.blogcontenta#内容a
    #     blogb=bll.blogcontentb#内容b
    #     blogc=bll.blogcontentc#内容c
    #     hre=bll.bloghref#网址
    #     image=bll.blogimg#图片
    #     tim=bll.blogtime#发表时间
    #     read=bll.blogread#阅读人数
    #     view=bll.blogreview#评论人数
    #     zan=bll.blogzan#赞数
    #     low=bll.bloglow#low数
    # for pll in pl:
    #     gra=pll.bloggre#评论

    return render(request,'news.html',{"bl":bl,"pl":pl,"come":come})

# def admins(request):#进入管理员系统
#     bl = blogtxt.objects.filter()
#     return render(request, 'admins.html', {"bl":bl})

def add(request):#添加博客按钮
    return render(request,'addlogin.html')

def addlogin(request):
    ad = admin.objects.get(id=1)
    name = request.POST.get("user")
    password = request.POST.get("password")
    if name == ad.hkname and str(password) == str(ad.hkpwd):
        return render(request, "add.html")
    else:
        return HttpResponse("error")

def addblog(request):#添加博客
    tim=time.strftime("%Y/%m/%d %H:%M:%S")#时间
    title=request.POST.get("title")#标题
    type=request.POST.get("type")#博客类型
    test=request.POST.get("test")#博客内容
    if len(test)<250:
        testa=test[0:250]
        testb=testc=testd =teste = testf =testg =testh =testi =testj =testk =testl =testm =testn =testo =testp=testq =testr =tests =testt =testu =testv =""
        if len(test)>249 and len(test)<750:
            testa = test[0:250]
            testb = test[250:500]
            testc = test[500:750]
            testd = teste = testf = testg = testh = testi = testj = testk = testl = testm = testn = testo = testp =testq= testr = tests = testt = testu = testv = ""
            if len(test)>249 and len(test)<9751:
                testa=test[0:250]
                testb=test[250:500]
                testc=test[500:750]
                testd = test[1000:1250]
                teste = test[1250:1500]
                testf = test[1750:2000]
                testg = test[2250:2500]
                testh = test[2750:3000]
                testi = test[3250:3500]
                testj = test[3750:4000]
                testk = test[4250:4500]
                testl = test[4750:5000]
                testm = test[5250:5500]
                testn = test[5750:6000]
                testo = test[6250:6500]
                testp = test[6750:7000]
                testq = test[7250:7500]
                testr = test[7750:8000]
                tests = test[8250:8500]
                testt = test[8750:9000]
                testu = test[9250:9500]
                testv = test[9500:9750]
    blogtxt(blogtitle=title,blogtime=tim,blogread=0,blogreview=0,blogzan=0,bloglow=0,blogcontenta=testa,
            blogcontentb=testb,blogcontentc=testc,blogcontentd=testd,blogcontente=teste,blogcontentf=testf,
            blogcontentg=testg,blogcontenth=testh,blogcontenti=testi,blogcontentj=testj,blogcontentk=testk,
            blogcontentl=testl,blogcontentm=testm,blogcontentn=testn,blogcontento=testo,blogcontentp=testp,
            blogcontentq=testq,blogcontentr=testr,blogcontents=tests,blogcontentt=testt,blogcontentu=testu,
            blogcontentv=testv,
            blogtype=type).save()
    return render(request, 'add.html')

def dele(request,blogid):
    bl = blogtxt.objects.filter(blogid=blogid)
    bl.delete()
    return render(request,"admins.html")
def addzan(request,num):#增加zan数
    bl = blogtxt.objects.filter(blogid=num)
    for bll in bl:
        zan = bll.blogzan+1  # 赞数
    bl.update(blogzan=zan)
    return HttpResponse(zan)

def addlow(request,num):#增加low数
    bl = blogtxt.objects.filter(blogid=num)
    for bll in bl:
        low = bll.bloglow+1  # low数
    bl.update(bloglow=low)
    return HttpResponse(low)

def addpin(request,nums):#添加评论
    gra=request.POST.get('txt')
    tim = time.strftime("%Y/%m/%d %H:%M:%S")
    comment(bloggre=gra,blogtype=nums,blogtime=tim).save()
    da=""
    return HttpResponse(da)

def comeon(request):
    return render(request,"login.html")

def comecheck(request):
    bl = blogtxt.objects.filter()
    ad=admin.objects.get(id=1)
    name=request.POST.get("user")
    password=request.POST.get("password")
    if name==ad.hkname and str(password)==str(ad.hkpwd):
        return render(request, "admins.html", {"bl":bl})
    else:
        return HttpResponse("error")

