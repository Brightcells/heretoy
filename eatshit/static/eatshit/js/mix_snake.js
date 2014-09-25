var el = document.body,
    hammer = Hammer(el, {
        drag: true,
        drag_block_horizontal: true,
        drag_min_distance: 5,
        hold: false,
        release: true,
        swipe: false,
        tap: false,
        touch: false,
        transform: false
    });

function Black(money, card) {
    this.x = money;
    this.y = card;
}

function n97() {
    var initX = Math.floor(widthNum/2);
    var initY = Math.floor(heightNum/2);
    var SIZE = 20;

    this.nokia6700 = new Array();
    this.nokia5230 = new Array();

    this.direction = 0;
    this.targetX = 0;
    this.targetY = 0;
    this.manager = null;

    this.setObserver = function(obs) {
        this.manager = obs;
    }

    this.init = function() {
        this.nokia5230.length = 0;
        this.nokia6700.length = 0;

        for(i = 0; i <= widthNum + 1; i++ ) {
            this.nokia5230[i] = new Array();
        }
        for (i = 0; i <= widthNum + 1; i++) {
            this.nokia5230[i][0] = 1;
            this.nokia5230[widthNum + 1][i] = 1;
            this.nokia5230[0][i] = 1;
            this.nokia5230[i][heightNum + 1] = 1;
        }
        /*for (i = 5; i <= initX; i++) {*/
        /*for (i = 5; i < initX; i++) {
            var point = new Black(i, initY);
            this.addBlack(point);
        }*/

        var point = new Black(initX, initY);
        this.addPhoto(point);

        this.direction = 3;
        this.productFood();
    }

    this.move = function() {
        //alert(this);
        var head = this.getHead();
        var point = new Black(head.x, head.y);
        var pre_head = new Black(head.x, head.y);

        switch (this.direction) {
            case 1:
                point.x-- ;
                break;
            case 2:
                point.y--;
                break;
            case 3:
                point.x++;
                break;
            case 4:
                point.y++;
                break;
        }
        this.process(point, pre_head);
    }

    this.turn = function(code) {
        var head = this.getHead();
        var point = new Black(head.x, head.y);
        var pre_head = new Black(head.x, head.y);

        switch(code - 36){
            case 1:
                if(this.direction == 1 || this.direction == 3)
                    return;
                point.x--;
                break;
            case 2:
                if(this.direction == 2 || this.direction == 4)
                    return;
                point.y--;
                break;
            case 3:
                if(this.direction == 1 || this.direction == 3)
                    return;
                point.x++;
                break;
            case 4:
                if(this.direction == 2 || this.direction == 4)
                    return;
                point.y++;
                break;
        }
        this.direction = code - 36;
        this.process(point, pre_head);
    }

    this.process = function(point, pre_head){
        if (this.ifDie(point)) {
            /*alert("Game Over");*/
            this.manager.stopGame();
            return;
        }

        if (this.eatable(point)) {
            this.manager.removeBlack(point);
            this.addPhoto(point);
            this.manager.drawBlack(pre_head);
            this.manager.addScore();
            this.productFood();
        }
        else {
            this.addPhoto(point);
            this.manager.drawBlack(pre_head);
            this.delTailBlack();
        }
    }

    this.ifDie = function(point) {
        return this.nokia5230[point.x][point.y] == 1;
    }

    this.getHead = function() {
        return this.nokia6700[0];
    }

    this.getTail = function() {
        return this.nokia6700[this.nokia6700.length - 1];
    }

    this.eatable = function(head) {
        return (head.x == this.targetX && head.y == this.targetY);
    }

    this.addBlack = function(point) {
        this.nokia5230[point.x][point.y] = 1;
        this.nokia6700.unshift(point);
        this.manager.drawBlack(point);
    }

    this.addPhoto = function(point) {
        this.nokia5230[point.x][point.y] = 1;
        this.nokia6700.unshift(point);
        this.manager.drawPhoto(point);
    }

    this.delTailBlack = function() {
        var point = this.nokia6700.pop();
        this.nokia5230[point.x][point.y] = 0;
        this.manager.removeBlack(point);
    }

    this.productFood = function() {
        do {
            var x = Math.ceil(Math.random() * 100 % widthNum);
            var y = Math.ceil(Math.random() * 100 % heightNum);
        }
        while (this.nokia5230[x][y] == 1)
        this.targetX = x;
        this.targetY = y;
        this.manager.drawFood(x,y);
    }
}

function Ga1900(canvasId) {
    var WIDTH = 25;
    var WIDTH2 = 25 - 2;
    var canvas = document.getElementById(canvasId);
    var RED = "#f9dd5f";
    var WHITE = "#dedede";
    var GREY = "#ffffff";
    var BLACK = "#000000";
    this.cxt = canvas.getContext("2d");
    var e398 = new n97();
    this.moveHandle = null;
    this.gamePanel = document.getElementById("gamePanel");
    this.scoreLabel =  document.getElementById("score");
    this.maxScoreLabel =  document.getElementById("highestScore");
    this.step = 0;
    this.score = 0;
    this.maxScore = 0;

    if(localStorage.maxScore)
    this.maxScore = localStorage.maxScore;
    this.maxScoreLabel.innerHTML = this.maxScore;

    e398.setObserver(this);

    this.startGame = function(step, username) {
        this.clear();
        e398.init();
        this.score = 0;
        this.scoreLabel.innerHTML = this.score;
        this.gamePanel.onkeydown = onKeyDown;
        this.gamePanel.swipeup = swipeUp;
        this.gamePanel.swiperight = swipeRight;
        this.gamePanel.swipedown = swipeDown;
        this.gamePanel.swipeleft = swipeLeft;
        this.step = parseInt(step);
        this.username = username;
        this.moveHandle = setInterval(move, 500 - 50 * this.step);
        this.countHandle = setInterval(countDown, 1000);
    }
    var move = function() {
        e398.move();
    }
    var _this = this;
    var countDown = function() {
        var left_time = parseInt(document.getElementById("leftTime").innerHTML);
        if(left_time > 0) {
            document.getElementById("leftTime").innerHTML = left_time - 1;
            if(left_time == 40) {
                clearInterval(_this.moveHandle);
                _this.step = 5;
                _this.moveHandle = setInterval(move, 500 - 50 * _this.step);
            } else if(left_time == 20) {
                clearInterval(_this.moveHandle);
                _this.step = 7;
                _this.moveHandle = setInterval(move, 500 - 50 * _this.step);
            }
        } else {
            /*alert("Game Over");*/
            _this.stopGame();
        }
    }
    this.stopGame = function() {
        var rank = '',
            title = '';

        this.pause();
        document.getElementById("control").disabled = true;
        if(this.score == 0) {
            rank = 0;
            title = "吃翔翔大笨蛋";
        } else if(this.score <= 5) {
            rank = GetRandomNum(1, 20);
            title = "吃翔翔小菜鸟";
        } else if(this.score <= 10) {
            rank = GetRandomNum(21, 40);
            title = "吃翔翔小能手";
        } else if(this.score <= 25) {
            rank = GetRandomNum(41, 65);
            title = "吃翔翔小怪兽";
        } else {
            rank = GetRandomNum(66, 98);
            title = "吃翔翔大宗师";
        }
        document.getElementById("shitNum").innerHTML = this.score;
        document.getElementById("rank").innerHTML = rank;
        document.getElementById("title").innerHTML = title;

        document.getElementById("share").style.zIndex = 999;
        
        share_info = this.username + "同学，丧心病狂地吃掉了" + this.score + "坨翔翔，击败了" + rank + "%的翔友，NB闪闪的获得了" + title + "称号！";
        change('desc', share_info, true);

        localStorage.maxScore = this.maxScore;
        //alert(localStorage.maxScore);
    }
    this.pause = function() {
        clearInterval(this.moveHandle);
        clearInterval(this.countHandle);
        this.gamePanel.onkeydown = null;
        this.gamePanel.swipeup = null;
        this.gamePanel.swiperight = null;
        this.gamePanel.swipedown = null;
        this.gamePanel.swipeleft = null;
    }
    this.goon = function() {
        this.gamePanel.onkeydown = onKeyDown;
        this.gamePanel.swipeup = swipeUp;
        this.gamePanel.swiperight = swipeRight;
        this.gamePanel.swipedown = swipeDown;
        this.gamePanel.swipeleft = swipeLeft;
        this.moveHandle = setInterval(move, 500 - 50 * this.step);
        this.countHandle = setInterval(countDown, 1000);
    }
    this.addScore = function() {
        /*this.score += this.step;*/
        this.score += 1;
        this.scoreLabel.innerHTML = this.score;
        if(this.score > this.maxScore){
            this.maxScore = this.score;
            this.maxScoreLabel.innerHTML = this.score;
        }
    }

    var onKeyDown = function(e) {
        if (e.which < 37 || e.which > 40)
            return;
        e398.turn(e.which);
    }
    var swipeUp = hammer.on('dragup', function(ev) {
        e398.turn(38);
    });
    var swipeRight = hammer.on('dragright', function(ev) {
        e398.turn(39);
    });
    var swipeDown = hammer.on('dragdown', function(ev) {
        e398.turn(40);
    });
    var swipeLeft = hammer.on('dragleft', function(ev) {
        e398.turn(37);
    });

    this.removeFood = function(x, y) {
        this.cxt.fillStyle = WHITE;
        this.cxt.fillRect((x - 1) * WIDTH + 1, (y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
    }

    this.drawFood = function(x, y) {
        this.cxt.fillStyle = RED;
        this.cxt.fillRect((x - 1) * WIDTH + 1, (y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
        var img = document.getElementById("shit");
        this.cxt.drawImage(img, (x - 1) * WIDTH + 1, (y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
    }

    this.drawBlack = function(point) {
        this.cxt.fillStyle = BLACK;
        this.cxt.fillRect((point.x - 1) * WIDTH + 1, (point.y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
        var img = document.getElementById("shit");
        this.cxt.drawImage(img, (point.x - 1) * WIDTH + 1, (point.y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
    }

    this.drawPhoto = function(point) {
        this.cxt.fillStyle = BLACK;
        this.cxt.fillRect((point.x - 1) * WIDTH + 1, (point.y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
        var img = document.getElementById("photo");
        this.cxt.drawImage(img, (point.x - 1) * WIDTH + 1, (point.y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
    }

    this.removeBlack = function(point) {
        this.cxt.fillStyle = WHITE;
        this.cxt.fillRect((point.x - 1) * WIDTH + 1, (point.y - 1) * WIDTH + 1, WIDTH2, WIDTH2);
    }

    this.clear = function() {
        this.cxt.fillStyle = GREY;
        this.cxt.fillRect(0, 0, widthNum * WIDTH, heightNum * WIDTH);
        this.cxt.fillStyle = WHITE;
        for(var i=0; i<heightNum; i++){
            for(var j=0; j<widthNum; j++){
                this.cxt.fillRect(j * WIDTH + 1, i * WIDTH + 1, WIDTH2, WIDTH2);
            }
        }
    }
 }
