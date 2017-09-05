#coding=utf-8
from django.shortcuts import render,redirect
from hashlib import sha1
from models import *
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail,EmailMultiAlternatives
from df_user.Token import *
from django.template import Context,loader,RequestContext
import sms
def register(request):
    context = {'title':'用户注册'}
    return render(request,'df_user/register.html')


def register_handle(request):

    error_msg = None
    if request.method == "GET":
        phone_number = request.GET.get("mobile_phone_number")
        print phone_number
        if phone_number is not None:
            if sms.send_message(phone_number):
                return render(request,'df_user/register.html')
            else:
                error_msg = "获取验证码失败"

    elif request.method == "POST":

        post = request.POST
        #进行短信验证
        phone_number = post.get('phone')
        code = post.get('code')
        if code == '':
            error_msg = '请输入验证码'
        elif sms.verify(phone_number,code):
            #如果短信验证成功则
            uname = post.get('user_name')
            uemail = post.get('email')
            upwd = post.get('pwd')
            upwd2 = post.get('cpwd')

            #判断两次密码是否相同
            if upwd!=upwd2:
                return redirect('/user/register/')

            #对密码进行加密
            s1 = sha1()
            s1.update(upwd)
            upwd3 = s1.hexdigest()
            #创建对象
            user = UserInfo()
            user.uname = uname
            user.upwd = upwd3
            user.uemail = uemail
            user.is_active = False
            user.save()

            #做邮箱验证准备
            global token_confirm
            token = token_confirm.generate_validate_token(uname)
            url = '/'.join([django_settings.DOMAIN, 'user/activate', token])

            # print url
            # print isinstance(url,unicode)
            # message = "\n".join([u'{0},欢迎注册CCLSOL实验室的溯源网站'.format(uname), u'请访问该链接，完成用户验证:', url])
            # send_mail(u'注册用户信息', message, '375001904@qq.com', [uemail], fail_silently=False)
            # return HttpResponse(u'请登录到注册邮箱中验证用户，有效期为1个小时')

            subject = u'注册用户信息'
            from_email = '375001904@qq.com'
            to = [uemail]
            text_content = u'欢迎注册CCLSOL实验室的溯源网站,请访问该链接，完成用户验证:'
            email_template_name = 'df_user/activeuser.html'
            t = loader.get_template(email_template_name)
            context = {'url':url}
            html_content = t.render(context)
            msg = EmailMultiAlternatives(subject,text_content,from_email,to)
            msg.attach_alternative(html_content,"text/html")
            msg.send()
            return HttpResponse(u'请登录到注册邮箱中验证用户，有效期为1个小时')
            # subject = u'注册用户信息'
            # from_email = '375001904@qq.com'
            # to = [uemail]
            # text_content = u'欢迎注册CCLSOL实验室的溯源网站,请访问该链接，完成用户验证:'
            # html_content =
            # msg = EmailMultiAlternatives(subject,text_content,from_email,to)
            # msg.attach_alternative(html_content,"text/html")
            # msg.send()
            # return HttpResponse(u'请登录到注册邮箱中验证用户，有效期为1个小时')

            #return redirect('/user/login/')
            #u'验证成功，请进行<a href=\"' + unicode(django_settings.DOMAIN) + u'/login\">登录</a>操作'
        else:
            error_msg = "您输入的验证码有误，请查证后再输入"
        context = {'error_msg':error_msg}
    return render(request,'df_user/register.html',context)



#激活用户的注册
def activeuser(request, token):
    try:
        username = token_confirm.confirm_validate_token(token)

    except:
        username = token_confirm.remove_validate_token(token)
        users = UserInfo.objects.filter(uname=username)
        for user in users:
           user.delete()
        return HttpResponse( u'对不起，验证链接已经过期，请重新<a href=\"' + unicode(django_settings.DOMAIN) + u'/login\">注册</a>')
    try:
        user = UserInfo.objects.get(uname=username)
    except UserInfo.DoesNotExist:
        return HttpResponse(u"对不起，您所验证的用户不存在，请重新注册")
    user.is_active = True
    user.save()
    #message = u'验证成功，请进行<a href=\"' + unicode(django_settings.DOMAIN) + u'/user/login/\" target="_blank">登录</a>操作'
    message = u'验证成功，请进行<a href=http://localhost:8000/user/login/ target="_blank">登录</a>操作'
    return HttpResponse(message)


def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})


def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

def login_handle(request):
    #接收请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    #根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)#如果查的到则返回内容，查不到返回[]
    #判断：如果未查询到则用户名错，如果查到则判断密码是否正确，正确则转到用户中心
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/shouye/index/')
            #url = request.COOKIES.get('/','/')
            #red = HttpResponseRedirect(url)
            #print url
            #成功后删除转向地址，防止以后直接登录造成的转向
            #red.set_cookie('url','/',max_age=-1)#设置max_age=-1表示cookie立马过期
            #记住用户名
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] =users[0].uname
            return red
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
        return render(request, 'df_user/login.html')

# def index(request):
#     return render(request,'df_shouye/index.html')