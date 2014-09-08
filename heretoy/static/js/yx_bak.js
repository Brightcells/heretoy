YixinJSBridge.on('menu:share:appmessage', function (argv) {
alert("test");
    YixinJSBridge.invoke('sendAppMessage', { 
        "img_url": wxData.imgUrl,
        "img_width": "640",
        "img_height": "640",
        "link": wxData.url,
        "desc": wxData.desc,
        "title": wxData.title
    }, function (res) {
    }); 
});
YixinJSBridge.on('menu:share:timeline', function (argv) {
alert("test");
    YixinJSBridge.invoke('shareTimeline', { 
        "img_url": wxData.imgUrl,
        "img_width": "640",
        "img_height": "640",
        "link": wxData.url,
        "desc": wxData.desc,
        "title": wxData.title
    }, function (res) {
    }); 
});
YixinJSBridge.on('menu:share:weibo', function (argv) {
alert("test");
    YixinJSBridge.invoke('shareWeibo', { 
        "img_url": wxData.imgUrl,
        "img_width": "640",
        "img_height": "640",
        "link": wxData.url,
        "desc": wxData.desc,
        "title": wxData.title
    }, function (res) {
    }); 
});
