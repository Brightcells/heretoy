/*
 *Swiper
 */
var theSwiper, windowWidth, windowHeight, resizeWidth, resizeHeight, resizeTop, resizeLeft;
var setting;

function initSwiper() {
    windowWidth = $(window).innerWidth();
    windowHeight = $(window).innerHeight();
    if ((windowWidth / windowHeight) > (640 / 960)) {
        resizeWidth = windowHeight * (640 / 960);
        resizeHeight = windowHeight;
        resizeTop = 0;
        resizeLeft = (windowWidth - resizeWidth) / 2;
    }
    else {
        resizeWidth = windowWidth;
        resizeHeight = windowWidth / (640 / 960);
        resizeTop = (windowHeight - resizeHeight) / 2;
        resizeLeft = 0;
    }
    
    $('.swiper-container').css({
        'width':windowWidth,
        'height':windowHeight
    });
    
    $('.page-container').css({
        'width':resizeWidth,
        'height':resizeHeight,
        'top':resizeTop,
        'left':resizeLeft
    });
    
    $('#page0-bg').css({
        'width': windowHeight,
        'height': windowHeight,
        'left':(windowWidth - windowHeight) / 2
    });
    
    theSwiper = new Swiper('.swiper-container', {
        progress:true,
        mode:'vertical',
        onlyExternal:false,
        onProgressChange: function(swiper) {
            for (var i = 0; i < swiper.slides.length; i++){
                var slide = swiper.slides[i];
                var progress = slide.progress;
                swiper.setTransform(slide, 'translate3d(0px,0,'+(-Math.abs(progress*1500))+'px)');
            }
        },
        onTouchStart:function(swiper) {
            for (var i = 0; i < swiper.slides.length; i++){
                swiper.setTransition(swiper.slides[i], 0);
            }
        },
        onSetWrapperTransition: function(swiper, speed) {
            for (var i = 0; i < swiper.slides.length; i++){
                swiper.setTransition(swiper.slides[i], speed);
            }
        }
    });
}



/*
 *Weixin
 */
function initWeixin() {
    WeixinApi.ready(function(Api) {
        Api.showOptionMenu();
        var wxData = {
            'appId': '',
            'imgUrl': '',
            'link': '',
            'desc': '中国在线答疑应用教育价值分析报告',
            'title': '中国在线答疑应用教育价值分析报告'
        };
        
        var wxCallbacks = {
            ready: function() {},
            cancel: function(resp) {},
            fail: function(resp) {},
            confirm: function(resp) {},
            all: function(resp,shareTo) {}
        };
        
        wxCallbacks = {};
        
        Api.shareToFriend(wxData, wxCallbacks);
        Api.shareToTimeline(wxData, wxCallbacks);
        Api.shareToWeibo(wxData, wxCallbacks);
        Api.generalShare(wxData,wxCallbacks);
    });
}

/*
 *Loaded
 */
$(window).load(function() {
    $('#loading').hide();
    initSwiper();
    initWeixin();
});