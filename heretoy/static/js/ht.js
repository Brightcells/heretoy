!function(e){
    e.getRandomNum = function(Min, Max) {return (Min + Math.round(Math.random() * (Max - Min)));}

    e.htWords = ['非常好', '干得漂亮', '帅呆了', '哇塞', 'I服U', '天才诞生了'];
    e.getWord = function() {return e.htWords[Math.floor(Math.random() * e.htWords.length)];}

    e.htData = {"appId": "", "imgUrl" : "http://heretoy.com/static/html5games/img/heretoy_logo.png", "link" : "http://heretoy.com/", "desc" : "HereToy，口袋社交小游戏中心。百款游戏，每天更新，无需下载，点开即玩；玩过的游戏自动保存，无网络也可再玩；不仅可以跟微信好友玩，还可以跟其他社交圈好友玩；", "title" : "口袋社交小游戏中心"};
    e.init = function(data, flag) {
        for(d in data) {
            if(d in e.htData) e.htData[d] = data[d];
        }
        if(flag) e.share();
    }
    e.change = function(key, value, flag) {
        if(key in e.htData) e.htData[key] = value; 
        if(flag) e.share();
    }
    e.share = function() {jsonData=JSON.stringify(e.htData); e.parent.postMessage(jsonData, '*'); console.log(jsonData);}

    // load.js, put it here for speed.
    function asyncLoadScript(a){return function(b,c){var d=document.createElement("script");d.type="text/javascript",d.src=a,d.onload=b,d.onerror=c,d.onreadystatechange=function(){var a=this.readyState;if(a==="loaded"||a==="complete")d.onreadystatechange=null,b()},head.insertBefore(d,head.firstChild)}}(function(a){a=a||{};var b={},c,d;c=function(a,d,e){var f=a.halt=!1;a.error=function(a){throw a},a.next=function(c){c&&(f=!1);if(!a.halt&&d&&d.length){var e=d.shift(),g=e.shift();f=!0;try{b[g].apply(a,[e,e.length,g])}catch(h){a.error(h)}}return a};for(var g in b){if(typeof a[g]=="function")continue;(function(e){a[e]=function(){var g=Array.prototype.slice.call(arguments);if(e==="onError"){if(d)return b.onError.apply(a,[g,g.length]),a;var h={};return b.onError.apply(h,[g,g.length]),c(h,null,"onError")}return g.unshift(e),d?(a.then=a[e],d.push(g),f?a:a.next()):c({},[g],e)}})(g)}return e&&(a.then=a[e]),a.call=function(b,c){c.unshift(b),d.unshift(c),a.next(!0)},a.next()},d=a.addMethod=function(d){var e=Array.prototype.slice.call(arguments),f=e.pop();for(var g=0,h=e.length;g<h;g++)typeof e[g]=="string"&&(b[e[g]]=f);--h||(b["then"+d.substr(0,1).toUpperCase()+d.substr(1)]=f),c(a)},d("chain",function(a){var b=this,c=function(){if(!b.halt){if(!a.length)return b.next(!0);try{null!=a.shift().call(b,c,b.error)&&c()}catch(d){b.error(d)}}};c()}),d("run",function(a,b){var c=this,d=function(){c.halt||--b||c.next(!0)},e=function(a){c.error(a)};for(var f=0,g=b;!c.halt&&f<g;f++)null!=a[f].call(c,d,e)&&d()}),d("defer",function(a){var b=this;setTimeout(function(){b.next(!0)},a.shift())}),d("onError",function(a,b){var c=this;this.error=function(d){c.halt=!0;for(var e=0;e<b;e++)a[e].call(c,d)}})})(this);var head=document.getElementsByTagName("head")[0]||document.documentElement;addMethod("load",function(a,b){for(var c=[],d=0;d<b;d++)(function(b){c.push(asyncLoadScript(a[b]))})(d);this.call("run",c)})
    
    var weixin_api = "http://heretoy.com/static/js/weixin-api.min.js",
        wx = "http://heretoy.com/static/js/wx.min.js",
        yx = "http://heretoy.com/static/js/yx.min.js"; 
    load(weixin_api).thenRun(function() {
        load(wx);
    });
    load(yx).thenRun(function() {
    })
}(window);
