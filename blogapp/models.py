from django.db import models

# Create your models here.
class admin(models.Model):
    hkname=models.CharField(max_length=10)#管理员
    hkpwd=models.CharField(max_length=17)#密码

class blogtxt(models.Model):#文章
    blogid=models.AutoField(primary_key=True)#文章序号
    blogtitle=models.CharField(max_length=20,null=False)#文章标题
    blogcontenta=models.CharField(max_length=255,null=True)#文章内容
    blogcontentb = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentc = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentd = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontente = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentf = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentg = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontenth = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontenti = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentj = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentk = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentl = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentm = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentn = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontento = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentp = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentq = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentr = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontents = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentt = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentu = models.CharField(max_length=255, null=True)  # 文章内容
    blogcontentv = models.CharField(max_length=255, null=True)  # 文章内容
    blogtype=models.CharField(max_length=20,null=False)#文章类型
    bloghref=models.CharField(max_length=255)  #文章地址
    blogimg=models.CharField(max_length=255,null=True)#图片
    blogimga = models.CharField(max_length=255, null=True)  # 图片
    blogimgb = models.CharField(max_length=255, null=True)  # 图片
    blogimgc = models.CharField(max_length=255, null=True)  # 图片
    blogimgd = models.CharField(max_length=255, null=True)  # 图片
    blogimge = models.CharField(max_length=255, null=True)  # 图片
    blogtime=models.CharField(max_length=20,null=False)#发表时间
    blogread=models.IntegerField()#阅读人数
    blogreview=models.IntegerField()#评论数
    blogzan=models.IntegerField()#赞数
    bloglow=models.IntegerField()#low数

class comment(models.Model):
    blogid = models.AutoField(primary_key=True)  # 评论序号
    bloggre=models.CharField(max_length=255)#评论
    blogtype=models.CharField(max_length=5)#分类
    blogtime=models.CharField(max_length=20,null=False)#评论时间

# class
# class inform(models.Model):#公告、通知
#     infotime=models.CharField(max_length=20,null=False)#时间
#     infotxt=models.CharField(max_length=255,null=False)#内容
#     inform

