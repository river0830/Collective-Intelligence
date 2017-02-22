<!DOCTYPE html>
<html>
<!--Head-->
<head>
    <meta charset="utf-8" />
    <title>用户登陆</title>
</head>
<body>

    <h1> This is a login page </h1>
    <p> River 第一次bottle模版实例 </p>
    <hr />

    <form action="" method="post">
        <div class="loginbox-textbox">
            <b>用户名:</b><input type="text" class="form-control" name="username" placeholder="帐号" />
        </div>
        <div class="loginbox-textbox">
            <b>密码&#12288:</b><input type="password" class="form-control" name="password" placeholder="密码" />
        </div>

        <div class="loginbox-submit">
            <input type="submit" class="btn btn-primary btn-block" value="登陆">
        </div>
        % if message:
        <div class="loginbox-signup">
            <font color="red">{{message}}</font>
        </div>
        % end
    </form>

</body>
</html>

<!--&#32; == 普通的英文半角空格>
<!--&#160; == &nbsp; == &#xA0; == no-break space （普通的英文半角空格但不换行）>
<!--&#12288; == 中文全角空格 （一个中文宽度）>
<!--&#8194; == &ensp; == en空格 （半个中文宽度）>
<!--&#8195; == &emsp; == em空格 （一个中文宽度）>
<!--&#8197; == 四分之一em空格 （四分之一中文宽度）>
