document.addEventListener('YixinJSBridgeReady', function onBridgeReady() {
    YixinJSBridge.on('menu:share:appmessage', function (argv) {
        YixinJSBridge.invoke('sendAppMessage', { 
            "img_url": wxData.imgUrl,
            "img_width": "640",
            "img_height": "640",
            "link": wxData.link,
            "desc": wxData.desc,
            "title": wxData.title
        }, function (res) {
        }); 
    });
    YixinJSBridge.on('menu:share:timeline', function (argv) {
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
}); 
