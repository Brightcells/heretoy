document.addEventListener('YixinJSBridgeReady', function onBridgeReady() {
    YixinJSBridge.on('menu:share:appmessage', function (argv) {
        YixinJSBridge.invoke('sendAppMessage', { 
            "img_url": htData.imgUrl,
            "img_width": "640",
            "img_height": "640",
            "link": htData.link,
            "desc": htData.desc,
            "title": htData.title
        }, function (res) {
        }); 
    });
    YixinJSBridge.on('menu:share:timeline', function (argv) {
        YixinJSBridge.invoke('shareTimeline', { 
            "img_url": htData.imgUrl,
            "img_width": "640",
            "img_height": "640",
            "link": htData.url,
            "desc": htData.desc,
            "title": htData.title
        }, function (res) {
        }); 
    });
    YixinJSBridge.on('menu:share:weibo', function (argv) {
        YixinJSBridge.invoke('shareWeibo', { 
            "img_url": htData.imgUrl,
            "img_width": "640",
            "img_height": "640",
            "link": htData.url,
            "desc": htData.desc,
            "title": htData.title
        }, function (res) {
        }); 
    });
}); 
