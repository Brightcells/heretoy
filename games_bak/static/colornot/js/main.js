var colorMap = [
	{"name": "绿", "color": "#66FF00"},
	{"name": "白色", "color": "#FFFFFF"},
	{"name": "蓝色", "color": "#0047AB"},
	{"name": "黄色", "color": "#FFFF00"},
	{"name": "紫色", "color": "#7400A1"},
	{"name": "灰色", "color": "#999999"},
	{"name": "橙色", "color": "#FF7300"},
	{"name": "古铜色", "color": "#B87333"},
	{"name": "青色", "color": "#00FFFF"},
	{"name": "粉红色", "color": "#FFC0CB"},

];

var gtimer = false;
var gsame = false;
var gscore = 0;
var gbest = 0;

// 本地存储
function save(item, value) {
	if(window['localStorage'] && window['localStorage']['setItem']) {
		localStorage.setItem(item, value);
	}
}

// 获取本地存储
function color_load(item) {
	if(window['localStorage'] && window['localStorage']['getItem']) {
		return localStorage.getItem(item);
	}
}

function GetId(id) {
	if(GetId.cache[id]) {
		return GetId.cache[id];
	} else {
		GetId.cache[id] = document.getElementById(id);
		return GetId.cache[id];
	}
}
GetId.cache = {};

function setNewColor() {
	var length = colorMap.length;
	var name = 0;
	var color = 0;

	length = Math.min(length, 4*Math.ceil(gscore/10));

	gsame = Math.random() < 0.4;
	if(gsame) {
		name = color = Math.floor(Math.random()*length);
	} else {
		name = Math.floor(Math.random()*length);
		color = Math.floor(Math.random()*length);
		if(name === color) {
			gsame = true;
		}
	}

	if(gtimer)
		gtimer.stop();

	var waitTime = 0;
	if(gscore === 0) {
		waitTime = 5000;
	} else if(gscore < 4) {
		waitTime = 2200;
	} else if(gscore <= 10) {
		waitTime = 1800 - gscore * 50;
	} else if(gscore <= 25) {
		waitTime = 1300 - (gscore-10) * 20;
	} else {
		waitTime = 800 - (gscore-25) * 12;
	}


	var rotateTick = new Clock(100, 10, function(per) {
		GetId('color-tag').style['webkitTransform'] = 'rotateY(' + (per*90) + 'deg)';
		GetId('process').style['webkitTransform'] = 'rotateX(' + (per*90) + 'deg)';
		if(per >= 1) {
			GetId('color-tag').style['webkitTransform'] = 'rotateY(-90deg)';
			GetId('process-inner').style.width = '0px';
			GetId('color-tag').innerText = colorMap[name]['name'];
			GetId('color-tag').style.color = colorMap[color]['color'];
			GetId('process-inner').style.background = colorMap[color]['color'];
			var rotateBackTick = new Clock(150, 10, function(per) {
				GetId('color-tag').style['webkitTransform'] = 'rotateY(' + (per*90 - 90) + 'deg)';
				GetId('process').style['webkitTransform'] = 'rotateX(' + (per*90 - 90) + 'deg)';
				if(per >= 1) {
					resetTick(waitTime, 20);
				}
			});

			rotateBackTick.start();
		}
	});

	rotateTick.start();
}

function gameOver() {
	if(gtimer) {
		gtimer.stop();
	}
	GetId('cover').style.background = '';
	GetId('cover').style.display = '';
	GetId('cover-score').innerText = gscore;
	GetId('cover-best-score').innerText = 'BEST: ' + gbest;

        var rank = 0;
        if(gscore == 0) {
            rank = 0;
        } else if(gscore <= 5) {
            rank = getRandomNum(1, 20);
        } else if(gscore <= 10) {
            rank = getRandomNum(21, 40);
        } else if(gscore <= 25) {
            rank = getRandomNum(41, 65);
        } else {
            rank = getRandomNum(66, 98);
        }
        change('desc', "丧心病狂地获得" + gscore + "分，击败了" + rank + "%的朋友!", true);

	var tick = new Clock(300, 10, function(per) {
		if('webkitFilter' in document.body.style) {
			GetId('play').style.webkitFilter = 'blur(' + Math.floor(per*15) + 'px)';
			GetId('cover').style.background = 'rgba(255,255,255,' + (0.5*per) + ')';
		} else {
			GetId('cover').style.background = 'rgba(200,200,200,' + (0.92*per) + ')';
		}
	});
	tick.start();
}


function Clock(total, tick, callback) {
	this.begin = new Date();
	this.total = total;
	this.flag = true;

	var self = this;

	function clock() {
		if(!self.flag) return;
		var now = new Date();
		var per = (now - self.begin) / self.total;
		if(per < 1) {
			callback(per);
			setTimeout(clock, tick)
		} else {
			callback(1);
		}
	}

	this.start = clock;
	this.stop = function(){
		self.flag = false;
	};
}

function resetTick(totalTime, step) {
	if(gtimer) {
		gtimer.stop();
	}

	gtimer = new Clock(totalTime, step, function (per) {
		GetId('process-inner').style.width = per*100 + '%';
		if(per >= 1) {
			gameOver();
			// setNewColor();
		}
	});
	gtimer.start();
}

function select(flag) {
	if(flag === gsame) {
		gscore++;

		if(gscore > gbest) {
			save('color-not.best', gscore);
			GetId('b-score').innerText = gscore;
			gbest = gscore;
		}
		GetId('current-score').innerText = gscore;
		setNewColor();
	} else {
		gameOver();
	}
}


window.onload = function () {
	if(!/webkit/ig.test(navigator.userAgent)) {
		alert('抱歉，在您的设备或浏览器上可能不能做到完美展现。');
	}
	var clickEvent = 'click';
	if(/iphone|android/ig.test(navigator.userAgent)) {
		clickEvent = 'touchstart';
	}
	document.body.addEventListener('touchmove', function (e) {
		e.preventDefault();
	}, false);

	GetId('btn-no').addEventListener(clickEvent, function(e){
		select(false);
	}, false);

	GetId('btn-yes').addEventListener(clickEvent, function(e){
		select(true);
	}, false);

	GetId('btn-again').addEventListener(clickEvent, function(e){
		var tick = new Clock(300, 10, function(per) {
			GetId('play').style.webkitFilter = 'blur(' + Math.floor(15-per*15) + 'px)';
			GetId('cover').style.background = 'rgba(255,255,255,' + (0.5-0.5*per) + ')';
			if(per >= 1) {
				GetId('cover').style.display = 'none';
				gscore = 0;
				setNewColor();
			}
		});
		tick.start();
	})

	gbest = parseInt(color_load('color-not.best')) || 0;
	GetId('b-score').innerText = gbest;

	setNewColor();
}
