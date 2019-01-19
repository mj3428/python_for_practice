var answerOk=false;
var authType=0;
var brand_id=0;
var curBrand;
var brand_title="";
var brand_img="";
var isweixin=false;
var ischeckcaptcha=false;
var VPath='http://img.10brandchina.com/';
//var VPath='http://localhost/';
function showcaptcha() {
    ischeckcaptcha=false;
    if(brand_id%2)VPath='http://img.10brandchina.com/';else VPath='http://www.10brandchina.com/';
    if(Dd('captchapng').style.display=='none') {
        Dd('captchapng').style.display='';
    }
    if(Dd('captchapng').src.indexOf('loading.gif') != -1) {
        Dd('captchapng').src=VPath+'api/captcha.vote.png.php?authType='+authType+'&rnd='+Math.random();
    }
    if(Dd('captcha').value=='点击显示') {
        Dd('captcha').value='';
    }
    Dd('captcha').className = '';
    //reloadJS('voteJs',VPath+'api\/vote\.js\.php?id='+brand_id+'&rnd='+Math.random());
}
function reloadcaptcha() {
    ischeckcaptcha=false;
    if(brand_id%2)VPath='http://img.10brandchina.com/';else VPath='http://www.10brandchina.com/';
    Dd('captchapng').src = VPath+'api/captcha.vote.png.php?authType='+authType+'&rnd='+Math.random();
    Dd('ccaptcha').innerHTML = '';
    Dd('captcha').value = '';
    //reloadJS('voteJs',VPath+'api\/vote\.js\.php?id='+brand_id+'&rnd='+Math.random());
}
function signUrl(url,queryString)
{
    strs=queryString.split("&");
    strs.sort();
    vals='';
    for (i=0;i<strs.length;i++)
    {
        vals=vals+strs[i].split("=")[1];
    }
    return VPath+url+"?"+queryString+'&sign='+hex_md5(vals);
}
function checkcaptcha(s) {
    if(ischeckcaptcha){return;}else{ischeckcaptcha=true;}
    if(!is_captcha(s))return;
    if(s.length<4)return;
    $.ajax({
    type : "get",
    async:false,
    url : VPath+"api/captcha.check.php?action=captcha_brand&captcha="+s+"&authType="+authType+'&rnd='+Math.random(),
    dataType : "jsonp",
    jsonp: "callbackparam",
    jsonpCallback:"_checkcaptcha",
    success : function(json){
        ischeckcaptcha=false;
       if(json == '0') {
            Dd('ccaptcha').innerHTML = '  <img src="'+SKPath+'image/check_right.gif" align="absmiddle"/>';
        } else {
            Dd('captcha').focus;
            Dd('ccaptcha').innerHTML = '  <img src="'+SKPath+'image/check_error.gif" align="absmiddle"/>';
        }
    },
    error:function(){ischeckcaptcha=false;}
    });
}
function reloadJS(id,newJS)
{
    var oldjs = null; 
    var oldjs = document.getElementById(id); 
    if(oldjs) oldjs.parentNode.removeChild(oldjs); 
    var scriptObj = document.createElement("script"); 
    scriptObj.src = newJS; 
    scriptObj.type = "text/javascript"; 
    scriptObj.id   = id;
    document.body.appendChild(scriptObj);
}
function reloadquestion() {
    answerOk=false;
    $('#questionnext').hide();
    setTimeout(function (){$('#questionnext').show();}, 7000);
    Dd('question').style.display = '';
    Dd('canswer').innerHTML = '';
    Dd('answer').value = '';
    Dd('canswer').innerHTML = '';
    reloadJS('bc_question',VPath+"api/captcha.question.php?action=question&rnd="+Math.random()+".js")
}
function checkanswer() {
    var v=Dd('answer').value;
    if(v.length < 1) {
        Dd('answer').focus; return;
    }
    $.ajax({
    type : "get",
    async:false,
    url : VPath+"api/question.check.php?action=question&answer="+v+"&authType="+authType,
    dataType : "jsonp",
    jsonp: "callbackparam",
    jsonpCallback:"_checkquestion",
    success : function(json){
       if(json == '0') {
            Dd('canswer').innerHTML = '  <img src="'+SKPath+'image/check_right.gif" align="absmiddle"/>';
        } else {
            Dd('answer').focus;
            Dd('canswer').innerHTML = '  <img src="'+SKPath+'image/check_error.gif" align="absmiddle"/>';
        }
    },
    error:function(){}
    });
}
    function toupiao_click(queryString,url) {
            $.ajax({
            type : "get",
            async:false,
            url : signUrl(url,queryString),
            dataType : "jsonp",
            jsonp: "callbackparam",
            jsonpCallback:"_toupiao",
            success : function(json){
            resultArr=json.split(",");
            result=resultArr[0];
            if(result=='ok'){//投票成功
                var piaoNum=resultArr[1];
                curBrand.find("strong").html(piaoNum);
                $(".imgck").remove();               
                $(".tp_title").html('投票成功<br /><a href="'+DTPath+'brand/show-htm-itemid-'+brand_id+'.html" target="_blank"><span class="px14 f_blue">'+brand_title+'：<span class="f_red px14">'+piaoNum+'</span></span></a> <span class="px12 f_gray">'+get_time()+'</span>');
                closeStr='<img class="c_p" src="/skin/default/vote/close.jpg" alt="关闭" />';
                if(bc_userid>0 && userTouPiao>0){
                    prizeid=0;
                    if(resultArr.length>2){
                        prizeid=Number(resultArr[2]);
                        $(".close").html(closeStr+'  <a href="'+DTPath+'prize/start-'+prizeid+'.html" target="_blank"><img src="/skin/default/vote/prize_go.gif" alt="去抽奖" /></a>');
                    }
                    else
                    {
                        $(".close").html(closeStr+'  <a href="'+DTPath+'member/vote.php" target="_blank"><img src="/skin/default/vote/my_toupiao.gif" alt="我的投票" /></a>');
                    }
                }
                else
                {
                    $(".close").html(closeStr);
                }
                $("#_message").css('display','block');
                $(".share_input").find("input").val(bdUrlValue+"&bid="+brand_id);
                if(isweixin)
                {
                    $("#_message").find(".wxsharebox").css('display','block');
                    reloadJS('weixinJs2','\/api\/weixin\/sdk\.php?url='+location.href.split('#')[0].replace(/\&/g, "~"));
                }
                window._bd_share_config = {
                common : {
                    bdText : bdTextValue,   
                    bdDesc : '喜欢就来支持Ta,请为'+brand_title+'品牌投上您的宝贵一票吧!',
                    bdUrl : bdUrlValue+"&bid="+brand_id,    
                    bdPic : brand_img
                },
                share : [{
                    "bdSize" : 16
                }]
                }
                with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?cdnversion='+~(-new Date()/36e5)];
            }
            else if(result=='no'){
                alert("验证码不正确！");
                $("#btnSignCheck"+brand_id).removeAttr('disabled');
                $("#btnSignCheck"+brand_id).css('background','url('+SKPath+'vote/tpbut.gif)');
                if(authType!=3)reloadcaptcha();
            }else if(result=="no2"){
                  show_tip("一天之内只能投一票，请明天再来！");
                }
            else if(result=="no3"){
                  show_tip("5分钟之内只能投一票，请5分钟之后再来！");
                }
            else if(result=="no4"){
                  show_tip("10分钟之内只能投一票，请10分钟之后再来！");
                }
            else if(result=="no5"){
                  show_tip("30分钟之内只能投一票，请30分钟之后再来！");
                }
            else if(result=="no6"){
                  show_tip("投票进入前"+resultArr[1]+"名的品牌资质审核通过后才可以继续投票，资质审核流程:企业填写“资质审核表”（投票窗口上方可自行下载）填写完毕后回传给投票页面右侧的“行业专员”等待审核通过后就可以继续投票。（组委会电话："+toupiaoTel+"  传真：010-80745637）");
                }
            else if(result=="no7"){
                  show_tip("投票失败，可能是投票太频繁所致，请隔30分钟后再投！");
                }
            else if(result=="no8"){
                  show_tip("品牌投票还没有开始或已经结束！");
                }
            else if(result=="m1"){
                  show_tip("不是会员或没有登录！");
                }
            else if(result=="m2"){
                  show_tip("每个会员24小时只能投"+resultArr[1]+"票！");
                }
            else if(result=="m3"){
                  show_tip("会员已被禁用，不能投票！");
                }
            else if(result=="m4"){
                  show_tip("您所使用的网络发生了变化，为了安全，请重新登录后再进行投票!");
                  Go(DTPath+'member/login.php');
                }
            else if(result=="m5"){
                  show_tip("管理员禁止投票！");
                }
            else if(result=="m6"){
                  show_tip("本行业会员禁止投票！");
                }
            else{
                show_tip('投票失败,有可能是投票太频繁所致，请隔30分钟后再投！');
            }
            },
            error:function(){}
            });
    }
    function vote(id,authV){
        brand_id=id;
        curBrand=$("#b"+brand_id);
        brand_title=curBrand.find(".bimg").attr("alt");
        brand_img=curBrand.find(".bimg").attr("src");
        authType=authV;
        $(".imgck").remove();
        $("#b"+id).append('<div class="imgck"></div>');
        if(bc_userid>0 && userTouPiao>0)
        {
            $(".imgck").html('<p><strong class="px15 f_green">喜欢就来支持TA</strong><a href="javascript:guanbi();" class="close">关闭</a></p><p style="width:270px;" class="px14"><strong>会员名：</strong>'+bc_username+'</p><p class="px14 f_red"><strong>品 牌：</strong>'+brand_title+'</p><p class="px14"><strong>时 间：</strong>'+get_time()+'</p><p><img src="'+SKPath+'vote/confirm.png" align="absmiddle" id="btnSignCheck'+id+'" /></p>');
         $("#_message").css('display','none');
         $("#btnSignCheck"+id).click(
           function(){
                $("#btnSignCheck"+id).unbind("click");
                $("#btnSignCheck"+id).attr('src',SKPath+"vote/confirm_wait.png");
               toupiao_click("itemid="+id,'vote/do_m.php');
          });
            return true;
        }
         
        if(authType==3)
        {
            $(".imgck").html( '<p><strong class="px15 f_green">喜欢就来支持TA '+brand_title+'</strong><a href="javascript:guanbi();" class="close">关闭</a></p><p class="top">请根据提示内容回答问题</p><p><input name="answer" id="answer" type="text" size="8" value="" maxlength="10"/><span id="canswer"></span> <span id="question" style="display:none;"><span id="questionstr" class="f_red"></span>  <a href="javascript:reloadquestion();" id="questionnext">[换个问题]</a><br/></p><p><button id="btnSignCheck'+id+'" class="btnSignCheck" type="buttom"></button></p><p></p>');
        reloadquestion();
         $("#_message").css('display','none');
         $("#btnSignCheck"+id).click(
           function(){
                var captcha=Dd('answer').value;         
                $("#btnSignCheck"+id).attr('disabled','disabled');
                this.style.background="url("+SKPath+"vote/tpbut_wait.gif)";
               toupiao_click("itemid="+id+"&captcha="+captcha,'vote/do.php');
          });
        }
        else
        {
            $(".imgck").html( '<p><strong class="px15 f_green">喜欢就来支持TA '+brand_title+'</strong><a href="javascript:guanbi();" class="close">关闭</a></p><p class="top"><strong>请输入验证码</strong>(不区分大小写)</p><p style="width:270px;"><input name="captcha" id="captcha" type="text" size="8" value="点击显示"  maxlength="10"/> <img src="'+SKPath+'image/loading.gif" title="验证码,看不清楚?请点击刷新字母不区分大小写" align="absmiddle" id="captchapng" /><span id="ccaptcha"></span></p><p><button id="btnSignCheck'+id+'" class="btnSignCheck" type="buttom"></button></p><p></p>');
         //reloadcaptcha();
         $("#_message").css('display','none');
         $("#btnSignCheck"+id).click(
           function(){
                var captcha=Dd('captcha').value;            
                $("#btnSignCheck"+id).attr('disabled','disabled');
                this.style.background="url("+SKPath+"vote/tpbut_wait.gif)";
               toupiao_click("itemid="+id+"&captcha="+captcha,'vote/do.php');
            });
         }
    }
    function show_tip(str)
    {
        alert(str);
        $(".imgck").remove();
    }
    function guanbi(){
        $(".imgck").remove();
    }
    function onCopy(obj){ 
        obj.select(); 
        js=obj.createTextRange(); 
        js.execCommand("Copy");
        alert("复制成功！");
    }
    function get_time(){
        var myDate=new Date();
        var year=myDate.getFullYear();
        var month=myDate.getMonth()+1;
        var day=myDate.getDate();
        var h=myDate.getHours();
        var m=myDate.getMinutes();
        var s=myDate.getSeconds();
        return year+"-"+month+"-"+day+" "+h+":"+m+":"+s;
    }
    function shareVoteBrand(){
        $('#share_guide').show();
        if(brand_id>0)
        {
            $('#_message').hide();
            content={title: bdTextValue,desc: '喜欢就来支持Ta,请为'+brand_title+'品牌投上您的宝贵一票吧!',link: bdUrlValue+"&bid="+brand_id,imgUrl: brand_img};
        }
        else
        {
            content={title: bdTextValue,desc: '喜欢就来支持Ta,请为您喜欢的品牌投上您的宝贵一票吧!',link: bdUrlValue,imgUrl: SKPath+'image/sharelogo.gif'};
        }
        wx.onMenuShareAppMessage(content);
        wx.onMenuShareTimeline(content);
    }
    reloadJS('md5',VPath+'file\/script\/md5-min\.js');
    if((UA.indexOf('phone') != -1 || UA.indexOf('mobile') != -1 || UA.indexOf('android') != -1 || UA.indexOf('ipod') != -1) && get_cookie('mobile') != 'pc' && UA.indexOf('ipad') == -1) {
        $('#qrcodeTable').hide();
        if(UA.indexOf('micromessenger') != -1)
        {
            isweixin=true;
            var body = document.documentElement || document.body;
            if(isGecko) body = document.body;
            var ch = body.clientHeight;
            var bsh = body.scrollHeight;
            var bh = parseInt((bsh < ch) ? ch : bsh);
            $("#share_guide").css('height',bh+'px');
            $('#ShareFriends').show();
            reloadJS('weixinJs2','\/api\/weixin\/sdk\.php?url='+location.href.split('#')[0].replace(/\&/g, "~"));
            wx.ready(function () {
                document.querySelector('#ShareFriends').onclick = shareVoteBrand;
                document.querySelector('#ShareAppMessage').onclick = shareVoteBrand;
                document.querySelector('#ShareTimeline').onclick = shareVoteBrand;
            });
        }
    }
