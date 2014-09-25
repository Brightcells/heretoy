!function(e){
    var s={},
        a="*",
        o={},
        n={
            title:function(e){return parent.postMessage({type:"title",data:e},a),console.log("title: %s",e),this},
            desc:function(e){return parent.postMessage({type:"desc",data:e},a),console.log("desc: %s",e),this},
            icon:function(e){return parent.postMessage({type:"icon",data:e},a),console.log("icon: %s",e),this},
            param:function(e){var t="?";return Object.keys(e).forEach(function(s,a){a>0&&(t+="&"),t+=s+"="+e[s]}),parent.postMessage({type:"param",data:t},a),console.log("param: %s",t),this},
            trigger:function(){return parent.postMessage({type:"trigger"},a),console.log("triggered "),this},
            popup:function(){this.trigger()},onshared:function(e){var t=o.shared=o.shared||[];return t.push(e),parent.postMessage({type:"onshared"},a),this}
        };
    s.share=function(e){return e&&n.title(e),n},
    s.uishare=function(e,o){return parent.postMessage({type:"showui",message:e,playagain:o},a),console.log("showui ",t),n},
    s.score=function(e){parent.postMessage({type:"score",data:e},a),console.log("score ",e)},
    s.status=function(e){parent.postMessage({type:"status",data:e},a),console.log("status %s",e)},
    s.more=function(){parent.postMessage({type:"more",data:null},a),console.log("更多游戏")},
    s.about=function(){parent.postMessage({type:"about",data:null},a),console.log("关于我们")},
    s.showad=function(e){parent.postMessage({type:"showad",data:e},a),console.log("showad %s",JSON.stringify(e))},
    window.addEventListener("message",function(e){var t=e.data.type;switch(t){case"playagain":e.data.playagain.call(null);break;case"shared":o.shared&&o.shared.length&&o.shared.forEach(function(e){e.call(null)}),console.log("shared")}}),
    e.eg=s
}(window);

function getRandomNum(Min, Max) {
    return (Min + Math.round(Math.random() * (Max - Min)));
}

