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
        keyboardControl:true,
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
        },
        onSlideChangeEnd:function(swiper) {
            if (swiper.activeIndex == 0) {
                resetPage(1);
                showPage(0);
                $('#swiper-tip').show();
            }
            // else if(swiper.activeIndex == 8) {
            //     resetPage(7);
            //     resetPage(9);
            //     showPage(8);
            //     $('#swiper-tip').show();
            // }
             else if(swiper.activeIndex == 13) {
                $('#swiper-tip').hide();
            }
            else {
                resetPage(swiper.activeIndex - 1);
                resetPage(swiper.activeIndex + 1);
                showPage(swiper.activeIndex);
                $('#swiper-tip').show();
            }
        }
    });
}

function resetPage(id) {
    $('#page' + id + '_part1').hide();
    $('#page' + id + '_part2').hide();
    $('#page' + id + '_part3').hide();
    $('#page' + id + '_part4').hide();
    $('#page' + id + '_part5').hide();
    $('#page' + id + '_part6').hide();
    $('#page' + id + '_part7').hide();
}

function showPage(id) {
    // if (id == 0) {
       
    // }
    switch(id) {
        case 0:
        $('#page0-bg').removeClass().addClass('zoom');
        resetPage(1);
        break;

        case 1: 
        $('#page1_part1').removeClass().addClass('animated tada').one('webkitAnimationEnd animationend', function() {
            $('#page1_part2').removeClass().addClass('animated lightSpeedIn').show(); 
            $('#page1_part3').removeClass().addClass('animated lightSpeedIn').show();            
        });
        $('#page1_part1').show();
        break;

        case 2: 
        $('#page2_part1').removeClass().addClass('animated fadeInRightBig').one('webkitAnimationEnd animationend', function() {
            
            $('#page2_part2').removeClass().addClass('animated fadeInRight').one("webkitAnimationEnd animationend",function(){
                $('#page2_part3').removeClass().addClass('animated fadeInRight').one("webkitAnimationEnd animationend",function () {
                    $('#page2_part4').removeClass().addClass('animated fadeInRight').one("webkitAnimationEnd animationend", function() {
                        $('#page2_part5').removeClass().addClass('animated fadeInRight').show();            
                    }).show();
                }).show();
            }).show(); 
        });
        $('#page2_part1').show();
        break;

        case 3: 
        $('#page3_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page3_part2').removeClass().addClass('animated flipInX').show(); 
        });
        $('#page3_part3').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page3_part4').removeClass().addClass('animated flipInX').show(); 
        });
        $('#page3_part1').show();
        $('#page3_part3').show();
        break;

        case 4: 
        $('#page4_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page4_part2').removeClass().addClass('animated flipInX').show(); 
        });
        $('#page4_part3').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page4_part4').removeClass().addClass('animated flipInX').show(); 
        });
        $('#page4_part1').show();
        $('#page4_part3').show();
        break;

        case 5:
        $('#page5_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page5_part2').removeClass().addClass('animated pulse').one('webkitAnimationEnd animationend', function(){
                $('#page5_part3').removeClass().addClass('animated fadeInRight').show();            
          }).show(); 
        });
        $('#page5_part1').show();

        break;

        case 6:
        $('#page6_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page6_part2').removeClass().addClass('animated pulse').one('webkitAnimationEnd animationend', function(){
                $('#page6_part3').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend',function() {
                    $("#page6_part4").removeClass().addClass("animated fadeInRight").show();
                    $("#page6_part5").removeClass().addClass("animated fadeInRight").show();
                    $("#page6_part6").removeClass().addClass("animated fadeInRight").show(); 
                }).show();            
          }).show(); 
        });
        $('#page6_part1').show();
        break;

        case 7: 
        $('#page7_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page7_part2').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function(){
                 $('#page7_part3').removeClass().addClass('animated fadeInRight').show();
          }).show(); 
        });
        $('#page7_part1').show();
        break;

        case 8: 
        $('#page8_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page8_part2').removeClass().addClass('animated bounceInDown').one('webkitAnimationEnd animationend', function(){
                 $('#page8_part3').removeClass().addClass('animated bounceInUp').show();
          }).show(); 
        });
        $('#page8_part1').show();
        break;

        case 9:
        $('#page9_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page9_part2').removeClass().addClass('animated flipInX').show(); 
        });
        $('#page9_part3').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page9_part4').removeClass().addClass('animated flipInX').show(); 
        });
        $('#page9_part1').show();
        $('#page9_part3').show();
        break;

        case 10: 
        $('#page10_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page10_part2').removeClass().addClass('animated bounceInDown').one('webkitAnimationEnd animationend', function(){
                 $('#page10_part3').removeClass().addClass('animated fadeInRight').one("webkitAnimationEnd animationend",function() {                
                     $('#page10_part4').removeClass().addClass('animated bounceInDown').show();
                 }).show();
          }).show(); 
        });
        $('#page10_part1').show();
        break;

        case 11: 
        $('#page11_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page11_part2').removeClass().addClass('animated bounceInDown').one('webkitAnimationEnd animationend', function(){
                 $('#page11_part3').removeClass().addClass('animated fadeInRight').one("webkitAnimationEnd animationend",function() {                
                     $('#page11_part4').removeClass().addClass('animated bounceInDown').show();
                 }).show();
          }).show(); 
        });
        $('#page11_part1').show();
        break;
        case 12: 
        $('#page12_part1').removeClass().addClass('animated fadeInRight').one('webkitAnimationEnd animationend', function() {
            $('#page12_part2').removeClass().addClass('animated bounceInDown').one('webkitAnimationEnd animationend', function(){
                 $('#page12_part3').removeClass().addClass('animated bounceInUp').show();
          }).show(); 
        });
        $('#page12_part1').show();
        break;
    }
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
    showPage(0)
});