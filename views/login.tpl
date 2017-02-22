<html>
<body>

    <h1> This is a login page </h1>
    <p> River 第一次bottle模版实例 </p>
    <hr />

    <form action="/login" methon="post">
        <b>用户名:</b> <input name="username" type="text"/>
        </br>
        <b>密码&#12288:</b> <input name="password" type="password" />
        </br>
        <input value="登录" type="submit"/></br>
    </form>

    %if message:
        {{message}} </br>
    %end

</body>
</html>

<!--&#32; == 普通的英文半角空格>
<!--&#160; == &nbsp; == &#xA0; == no-break space （普通的英文半角空格但不换行）>
<!--&#12288; == 中文全角空格 （一个中文宽度）>
<!--&#8194; == &ensp; == en空格 （半个中文宽度）>
<!--&#8195; == &emsp; == em空格 （一个中文宽度）>
<!--&#8197; == 四分之一em空格 （四分之一中文宽度）>
