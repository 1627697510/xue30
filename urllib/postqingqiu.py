Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> values = {"username":"1627697510@qq.com","password":"xh177151..."}
>>> data=urllib.urlencode(values)
>>> url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
>>> request=urllib2.Request(url,data)
>>> response=urllib2.urlopen(request)
>>> print response.read()







<html>
  <head>
    <meta charset="utf-8" />
    <meta name="referrer" content="unsafe-url">
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta property="qc:admins" content="24530273213633466654" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>�ʺŵ�¼</title>
    
    
    <link type="text/css" rel="stylesheet" href="/css/bootstrap.css;jsessionid=71FE597B996707315E9F1B2FD60C9CF0.tomcat2" />
    <link type="text/css" rel="stylesheet" href="/css/login.css;jsessionid=71FE597B996707315E9F1B2FD60C9CF0.tomcat2" />
    <link type="text/css" rel="stylesheet" href="/css/weixinqr.css;jsessionid=71FE597B996707315E9F1B2FD60C9CF0.tomcat2" />
    <script src="https://res.wx.qq.com/connect/zh_CN/htmledition/js/wxLogin.js"></script>
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <script>
	var _hmt = _hmt || [];
	(function() {
	  var hm = document.createElement("script");
	  hm.src = "https://hm.baidu.com/hm.js?6bcd52f51e9b3dce32bec4a3997715ac";
	  var s = document.getElementsByTagName("script")[0]; 
	  s.parentNode.insertBefore(hm, s);
	})();
	</script>
  </head>
  <body>
  	<div id="hidebg"></div>
	<div id="hidebox"><div id="close" onClick="hide();"></div><div id="wxqr" class="wxqr"></div></div>
  	<script type="text/javascript">
  		var protocol = window.location.protocol;
  		document.write('<script type="text/javascript" src="' +protocol+ '//csdnimg.cn/pubfooter/js/repoAddr2.js?v=' + Math.random() + '"></'+'script>');
	</script>
	
    <div class="header"></div>
    <div class="main" style="background:url(https://csdnimg.cn/passport/login-bg.png)">
      <div class="container container-custom">
        <div class="row wrap-login">
          <div class="login-banner col-sm-6 col-md-7 col-lg-7 hidden-xs"><a href="http://dwz.cn/6JIiAl" target="_blank"><img src=https://csdnimg.cn/passport/login-banner.png class="img-responsive"></a></div>
          <div class="login-user col-xs-12 col-sm-6 col-md-5 col-lg-5">
            <div class="login-part">
              <h3>�ʺŵ�¼ </h3>
              <div class="user-info">
                <div class="user-pass">
                
                  <form id="fm1" action="/account/login;jsessionid=71FE597B996707315E9F1B2FD60C9CF0.tomcat2?from=http://my.csdn.net/my/mycsdn" method="post">

                    <input id="username" name="username" tabindex="1" placeholder="�����û���/����/�ֻ���" class="user-name" type="text" value=""/>
                    <div class="mobile-auth" style="display:none"><span>���ֻ��Ѱ��˺ţ���ʹ��  </span><a href="" id="mloginurl" class="mobile-btn" >�ֻ���֤���¼</a></div>
                    <input id="password" name="password" tabindex="2" placeholder="��������" class="pass-word" type="password" value="" autocomplete="off"/>
                   
                    
						
						
							<div class="error-mess" style="display:none;">
								<span class="error-icon"></span><span id="error-message"></span>
							</div>
						
					
					
                    <div class="row forget-password">
                    	<span class="col-xs-6 col-sm-6 col-md-6 col-lg-6">
                        	<input type="checkbox" name="rememberMe" id="rememberMe" value="true" class="auto-login" tabindex="4"/>
                        	<label for="rememberMe">�´��Զ���¼</label>
                        </span>
                        <span class="col-xs-6 col-sm-6 col-md-6 col-lg-6 forget tracking-ad" data-mod="popu_26">
                        	<a href="/account/fpwd?action=forgotpassword&service=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn" tabindex="5">��������</a>
                        </span>
                    </div>
                    <!-- �ò������������ÿ����Ҫ��¼���û�����һ����ˮ�š�ֻ������webflow���ŵ���Ч����ˮ�ţ��û��ſ���˵�����Ѿ�������webflow���̡�����û����ˮ�ŵ�����£�webflow����Ϊ�û���û�н���webflow���̣��Ӷ������½���һ��webflow���̣��Ӷ������³��ֵ�¼���档 -->
					<input type="hidden" name="lt" value="LT-578186-r1dERYCScuWxPUJUnfIyowz2dvliwe" />
			 		<input type="hidden" name="execution" value="e1s1" /> 
					<input type="hidden" name="_eventId" value="submit" /> 
					<input class="logging" accesskey="l" value="�� ¼" tabindex="6" type="button" /> 
                    
                  </form>
                </div>
              </div>
              <div class="line"></div>
              <div class="third-part tracking-ad" data-mod="popu_27">
              	<span style="width: 257px;">�������ʺŵ�¼</span>
              	<span><font color="red">  </font></span>
              	<a id="qqAuthorizationUrl" href="https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=100270989&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DQQProvider&state=test" class="qq"></a>
              	
                   	<a id="wechatAuthorizationUrl" href="javascript:void(0)" onClick="show();" class="wechat" target="_parent"></a>
                   	<script src="/js/apps/weixinqr.js;jsessionid=71FE597B996707315E9F1B2FD60C9CF0.tomcat2"></script>
				
              	<a id="sinaAuthorizationUrl" href="https://api.weibo.com/oauth2/authorize?client_id=2601122390&response_type=code&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DSinaWeiboProvider" class="sina"></a>
              	<a id="baiduAuthorizationUrl" href="https://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id=cePqkUpKCBrcnQtARTNPxxQG&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DBaiduProvider" class="baidu"></a>
              	<a id="osChinaAuthorizationUrl" href="https://www.oschina.net/action/oauth2/authorize?response_type=code&client_id=cIh1UuWvSyrYlbe93rM6&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DOsChinaProvider&state=test" class="cc"></a>
              	<a id="githubAuthorizationUrl" href="https://github.com/login/oauth/authorize?client_id=4bceac0b4d39cf045157&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DGitHubProvider" class="github"></a>
              	<a href="javascript:;" class="show_more"></a>
              	
                <div class="register-now"><span>��û��CSDN�ʺţ�</span>
	                <span class="register tracking-ad" data-mod="popu_28">
	                	<a href="/account/mobileregister?action=mobileRegisterGuideView&service=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn">����ע��</a>
	                </span>
               	</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer"></div>
    <script data-main="/js/login-config.js;jsessionid=71FE597B996707315E9F1B2FD60C9CF0.tomcat2" src="/js/libs/require.js;jsessionid=71FE597B996707315E9F1B2FD60C9CF0.tomcat2"></script>
    <script type="text/javascript">
		document.write('<script type="text/javascript" src="//csdnimg.cn/pubfooter/js/publib_footer.js?' + Math.floor(new Date()/120000).toString(36) + '="></'+'script>');
	</script>
  </body>
</html>
>>> values={}
>>> values['username']='1627697510@qq.com'
>>> values['password']='xh177151...'
>>> data=urllib.urlencode(values)
>>> url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
>>> request = urllib2.Request(url,data)
>>> response = urllib2.urlopen(request)
>>> print response.read()







<html>
  <head>
    <meta charset="utf-8" />
    <meta name="referrer" content="unsafe-url">
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta property="qc:admins" content="24530273213633466654" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>�ʺŵ�¼</title>
    
    
    <link type="text/css" rel="stylesheet" href="/css/bootstrap.css;jsessionid=C793B784180AD050EE5DD2C36AAABD44.tomcat2" />
    <link type="text/css" rel="stylesheet" href="/css/login.css;jsessionid=C793B784180AD050EE5DD2C36AAABD44.tomcat2" />
    <link type="text/css" rel="stylesheet" href="/css/weixinqr.css;jsessionid=C793B784180AD050EE5DD2C36AAABD44.tomcat2" />
    <script src="https://res.wx.qq.com/connect/zh_CN/htmledition/js/wxLogin.js"></script>
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <script>
	var _hmt = _hmt || [];
	(function() {
	  var hm = document.createElement("script");
	  hm.src = "https://hm.baidu.com/hm.js?6bcd52f51e9b3dce32bec4a3997715ac";
	  var s = document.getElementsByTagName("script")[0]; 
	  s.parentNode.insertBefore(hm, s);
	})();
	</script>
  </head>
  <body>
  	<div id="hidebg"></div>
	<div id="hidebox"><div id="close" onClick="hide();"></div><div id="wxqr" class="wxqr"></div></div>
  	<script type="text/javascript">
  		var protocol = window.location.protocol;
  		document.write('<script type="text/javascript" src="' +protocol+ '//csdnimg.cn/pubfooter/js/repoAddr2.js?v=' + Math.random() + '"></'+'script>');
	</script>
	
    <div class="header"></div>
    <div class="main" style="background:url(https://csdnimg.cn/passport/login-bg.png)">
      <div class="container container-custom">
        <div class="row wrap-login">
          <div class="login-banner col-sm-6 col-md-7 col-lg-7 hidden-xs"><a href="http://dwz.cn/6JIiAl" target="_blank"><img src=https://csdnimg.cn/passport/login-banner.png class="img-responsive"></a></div>
          <div class="login-user col-xs-12 col-sm-6 col-md-5 col-lg-5">
            <div class="login-part">
              <h3>�ʺŵ�¼ </h3>
              <div class="user-info">
                <div class="user-pass">
                
                  <form id="fm1" action="/account/login;jsessionid=C793B784180AD050EE5DD2C36AAABD44.tomcat2?from=http://my.csdn.net/my/mycsdn" method="post">

                    <input id="username" name="username" tabindex="1" placeholder="�����û���/����/�ֻ���" class="user-name" type="text" value=""/>
                    <div class="mobile-auth" style="display:none"><span>���ֻ��Ѱ��˺ţ���ʹ��  </span><a href="" id="mloginurl" class="mobile-btn" >�ֻ���֤���¼</a></div>
                    <input id="password" name="password" tabindex="2" placeholder="��������" class="pass-word" type="password" value="" autocomplete="off"/>
                   
                    
						
						
							<div class="error-mess" style="display:none;">
								<span class="error-icon"></span><span id="error-message"></span>
							</div>
						
					
					
                    <div class="row forget-password">
                    	<span class="col-xs-6 col-sm-6 col-md-6 col-lg-6">
                        	<input type="checkbox" name="rememberMe" id="rememberMe" value="true" class="auto-login" tabindex="4"/>
                        	<label for="rememberMe">�´��Զ���¼</label>
                        </span>
                        <span class="col-xs-6 col-sm-6 col-md-6 col-lg-6 forget tracking-ad" data-mod="popu_26">
                        	<a href="/account/fpwd?action=forgotpassword&service=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn" tabindex="5">��������</a>
                        </span>
                    </div>
                    <!-- �ò������������ÿ����Ҫ��¼���û�����һ����ˮ�š�ֻ������webflow���ŵ���Ч����ˮ�ţ��û��ſ���˵�����Ѿ�������webflow���̡�����û����ˮ�ŵ�����£�webflow����Ϊ�û���û�н���webflow���̣��Ӷ������½���һ��webflow���̣��Ӷ������³��ֵ�¼���档 -->
					<input type="hidden" name="lt" value="LT-578886-4KsX00TDBKv5hGvTJlttYJXyksdo2s" />
			 		<input type="hidden" name="execution" value="e1s1" /> 
					<input type="hidden" name="_eventId" value="submit" /> 
					<input class="logging" accesskey="l" value="�� ¼" tabindex="6" type="button" /> 
                    
                  </form>
                </div>
              </div>
              <div class="line"></div>
              <div class="third-part tracking-ad" data-mod="popu_27">
              	<span style="width: 257px;">�������ʺŵ�¼</span>
              	<span><font color="red">  </font></span>
              	<a id="qqAuthorizationUrl" href="https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=100270989&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DQQProvider&state=test" class="qq"></a>
              	
                   	<a id="wechatAuthorizationUrl" href="javascript:void(0)" onClick="show();" class="wechat" target="_parent"></a>
                   	<script src="/js/apps/weixinqr.js;jsessionid=C793B784180AD050EE5DD2C36AAABD44.tomcat2"></script>
				
              	<a id="sinaAuthorizationUrl" href="https://api.weibo.com/oauth2/authorize?client_id=2601122390&response_type=code&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DSinaWeiboProvider" class="sina"></a>
              	<a id="baiduAuthorizationUrl" href="https://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id=cePqkUpKCBrcnQtARTNPxxQG&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DBaiduProvider" class="baidu"></a>
              	<a id="osChinaAuthorizationUrl" href="https://www.oschina.net/action/oauth2/authorize?response_type=code&client_id=cIh1UuWvSyrYlbe93rM6&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DOsChinaProvider&state=test" class="cc"></a>
              	<a id="githubAuthorizationUrl" href="https://github.com/login/oauth/authorize?client_id=4bceac0b4d39cf045157&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Faccount%2Flogin%3Foauth_provider%3DGitHubProvider" class="github"></a>
              	<a href="javascript:;" class="show_more"></a>
              	
                <div class="register-now"><span>��û��CSDN�ʺţ�</span>
	                <span class="register tracking-ad" data-mod="popu_28">
	                	<a href="/account/mobileregister?action=mobileRegisterGuideView&service=http%3A%2F%2Fmy.csdn.net%2Fmy%2Fmycsdn">����ע��</a>
	                </span>
               	</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer"></div>
    <script data-main="/js/login-config.js;jsessionid=C793B784180AD050EE5DD2C36AAABD44.tomcat2" src="/js/libs/require.js;jsessionid=C793B784180AD050EE5DD2C36AAABD44.tomcat2"></script>
    <script type="text/javascript">
		document.write('<script type="text/javascript" src="//csdnimg.cn/pubfooter/js/publib_footer.js?' + Math.floor(new Date()/120000).toString(36) + '="></'+'script>');
	</script>
  </body>
</html>
>>> 