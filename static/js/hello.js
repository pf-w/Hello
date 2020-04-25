// 文字禁止选中
var content_div = document.getElementById("content");
content_div.onselectstart = function () {
    return false;
};

var hello_span = document.getElementById("hello");
var hello_a = hello_span.children[0];
hello_a.onclick = function () {
    request_color();
};

function request_color() {
    options = {
        method: "GET",
        url: "/color",
        params: {"is_json": 1},
        success: function (data) {
            let res = JSON.parse(data);
            let angle = res.data.angle;
            let color_0 = res.data.colors[0];
            let color_1 = res.data.colors[1];
            hello_a.style.backgroundImage = 'linear-gradient(' + angle + 'deg, ' + color_0 + ', ' + color_1 + ')';
        }
    };
    ajax_func(options);
}

function ajax_func(options) {
    // 创建ajax对象
    var xhr = null;
    if (window.XMLHttpRequest) {
        xhr = new XMLHttpRequest();
    } else if (window.ActiveObject) {      //兼容IE6以下版本
        xhr = new ActiveXobject('Microsoft.XMLHTTP');
    }

    // 接收-第三步; 存有处理服务器响应的函数，每当 readyState 改变时，onreadystatechange 函数就会被执行。
    xhr.onreadystatechange = function (e) {
        // readyState存有服务器响应的状态信息, 4说明请求已完成
        if (xhr.readyState === 4) {
            if (xhr.status === 200)
                options.success && options.success(xhr.responseText);
            else
                options.error && options.error(status);
        }
    };
    //连接和发送-第二步
    if (options.method === 'GET') {
        if (options.params) {
            var param = "?";
            for (const k in options.params)
                param += k + "=" + options.params[k] + "&";

        }
        xhr.open(options.method, options.url + param.replace(/&$/, ""), true);
        xhr.send();
    } else if (options.method === 'POST') {
        xhr.open(options.method, options.url, true);
        //设置表单提交时的内容类型
        // xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(options.params);
    }
}