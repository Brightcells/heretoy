function cookieHelper() {
	this.readCookie = function(callback) {
		callback(this.getCookie("gs"));
	}

	this.writeCookie = function(game) {
		var d = new Date();
		d.setTime(d.getTime() + (300*24*60*60*1000));
		var expires = "expires="+d.toGMTString();
		var toWrite = "gs=" + 
			game.currentClicks + " " +
			game.bestLevel + " " +
			game.clicksForBest + " " +
			game.totalClicks + " " +
			game.level + " " +
			game.isFirstGame + " " +
			game.gb.board.toString() + 
			"; "+ expires;
		document.cookie = toWrite;
		// console.log(document.cookie);
	}

	this.getCookie = function(cname) {
	    var name = cname + "=";
	    var ca = document.cookie.split(';');
	    for(var i=0; i<ca.length; i++) {
	        var c = ca[i];
	        while (c.charAt(0)==' ') c = c.substring(1);
	        if (c.indexOf(name) != -1) return c.substring(name.length,c.length);
	    }
	    return "";
	}
}

function styleHelper() {
	this.setGridSize = function(level) {
		var margin = this.getMargin(level)
		var res = ($('.container').width() - margin * level) / (level);
		$('.gamesquare').css('margin-right', margin);
		$('.gamesquare').css('width', res);
		$('.gamesquare').css('height', res);
		$('.gamerow').css('height', res);
		$('.gamerow').css('margin-right', margin * (-1));
		$('.gamerow').css('margin-bottom', margin);
		$('.board').css('padding', margin);
		$('.board').css('padding-bottom', 0);
	}

	this.getMargin = function(level) {
		if (level <= 6) return 7.5;
		if (level > 15) return 2.5;
		return 20 - level;
	}
}

function cheesyWordGetter() {
	this.words = ['非常好', '干得漂亮', '帅呆了', '哇塞', 'I服U', '天才诞生了'];

	this.getWord = function() {
		return this.words[Math.floor(Math.random()*this.words.length)];
	}
}

function Game() {
	var self = this;

	// Local game state variables
	this.currentClicks = 0;
	this.bestLevel = 1;
	this.clicksForBest = 0;
	this.totalClicks = 0;
	this.level = 1;
	this.isFirstGame = 1;
        this.share_info = '';
        this.rank = "";
        this.title = "不服来战！";

	// Objects that help facilitate the game
	this.gb;
	this.sh = new styleHelper();
	this.cookh = new cookieHelper();
	this.cwg = new cheesyWordGetter();

	this.processClick = function(w, h) {
		this.gb.processClick(w, h);
		this.currentClicks++;
		this.totalClicks++;
		this.updateCounts();
		if (this.gb.isGameWin()) {
			this.gameEnd(function(){
				self.cookh.writeCookie(self);
			});
		} else {
			self.cookh.writeCookie(self);
		}
	}

	this.beginGame = function() {
		var res;
		this.cookh.readCookie(function(csv){
			res = csv;
			if (res != "") {
				var state = res.split(" ");
				self.currentClicks = parseInt(state[0]);
				self.bestLevel = parseInt(state[1]);
				self.clicksForBest = parseInt(state[2]);
				self.totalClicks = parseInt(state[3]);
				self.level = parseInt(state[4]);
				self.isFirstGame = parseInt(state[5]);
			}
			if (self.isFirstGame == 1) {
				$('#instructions').modal('show');
				self.isFirstGame = 0;
			}
			self.setupLevel();
		});
		
	}

	this.gameEnd = function(callback) {
		this.level++;
		if (this.level == this.bestLevel && this.currentClicks < this.clicksForBest) {
			this.clicksForBest = this.currentClicks;
		} 
		if (this.level > this.bestLevel) {
			this.clicksForBest = this.currentClicks;
			this.bestLevel = this.level;
		}
		this.resetGame();
		callback();
	}

	this.resetGame = function() {
	        change('desc', this.share_info, true);
                var conf = confirm(this.share_info);
                if(conf == true) self.setupLevel();
	}

	this.setupLevel = function() {
		this.gb = new GameBoard(this.level, this.level);
		$('.board').html("");
		this.gb.populate();
		self.gb.renderBoard();
		self.sh.setGridSize(this.level);
		self.updateCounts();
		self.applyBindings();
	}

	this.updateCounts = function() {
		$(".currLevel").html("当前级别: <b>" + this.level + "</b>");
		$(".score").html("当前点击次数: <b>" + this.currentClicks +"</b>");
		$(".best").html("历史最高级别: <b>" + this.bestLevel + "</b> (" + this.clicksForBest + " clicks)");
		$(".total").html("总计点击次数: <b>" + this.totalClicks + "</b>");

		if(this.level == 1) {this.rank = 1;}
		else if(this.level == 2) {this.rank = getRandomNum(1, 3);}
		else if(this.level == 3) {this.rank = getRandomNum(4, 10);}
		else if(this.level == 4) {this.rank = getRandomNum(11, 20);}
		else if(this.level == 5) {this.rank = getRandomNum(21, 40); this.title = "超越有难度！";}
		else if(this.level == 6) {this.rank = getRandomNum(41, 50); this.title = "超越有难度！";}
		else if(this.level == 7) {this.rank = getRandomNum(51, 64); this.title = "已经不好超越！";}
		else if(this.level == 8) {this.rank = getRandomNum(65, 80); this.title = "已经不好超越！";}
		else {this.rank = getRandomNum(81, 99); this.title = "已经不好超越！";}
		this.share_info = "用了" + this.currentClicks + "次点击，完成级别" + this.level + "，击败全球" + this.rank + "%用户，" + this.title;
	}

	this.applyBindings = function() {
		$('.gamesquare').click(function(){
			// Get the other class
			var cname = $(this).context.className.split(" ")[1];
			var coord = cname.substring(5).split("q");
			// console.log("coord " + coord);
			var height = parseInt(coord[1]);
			var width = parseInt(coord[0]);
			self.processClick(width, height);
		});
	}

	this.onNewGameClick = function() {
		this.currentClicks = 0;
		this.level = 1;
		this.setupLevel();
	}

	this.onResetLevelClick = function() {
		this.gb.populate();
		this.gb.renderBoard();
		this.setupLevel();
	}
}

function GameBoard (wd, hi) {
	// wide and high are 0 indexed
	this.high = hi - 1;
	this.wide = wd - 1;

	this.count = 0;

	// This board is accessed wide first then high
	//    0 | 1 | 2 | 3 | ....
    //  - - - - - - - - - - - -
   	//  0   |   |   |   | 
	//  - - - - - - - - - - - -
	//  1   |   |[2][1]
	//  -
	//  2
	//  :
	//  :
	//
	this.board = new Array(wd);
	for (var i = 0; i <= this.wide; i++) {
		this.board[i] = new Array(hi);
	}

	this.renderBoard = function() {
		var s = "";
		for (var j = 0; j <= this.high; j++) {
			s += "<div class='gamerow'>";
			for (var i = 0; i <= this.wide; i++) {
				s += "<div class='gamesquare coord" + i + "q" + j + "'></div>";
				// console.log(this.board[i][j]);
			}
			s += "</div>";
		}
		$('.board').html(s);


		for (var i = 0; i <= this.wide; i++) {
			for (var j = 0; j <= this.high; j++) {
				this.processCLickView(i, j);
			}
		}
	}

	this.processClick = function(w, h) {
		// find the proper range for inversion
		var lowx = w - 1;
		var highx = w + 1;
		var lowy = h - 1;
		var highy = h + 1;

		// Test for edge cases and change the bounds accordingly
		if (w == 0) lowx = 0;
		if (w == this.wide) highx = this.wide;
		if (h == 0) lowy = 0;
		if (h == this.high) highy = this.high;

		// invert all in proper vertical range
		for (var i = lowy; i <= highy; i++) {
			// if (i == h) continue;
			if (this.board[w][i] == 0) {
				this.board[w][i] = 1;
				this.count++;
			} else {
				this.board[w][i] = 0;
				this.count--;
			}
			this.processCLickView(w, i);
		}

		// invert all in proper horizontal range
		for (var i = lowx; i <= highx; i++) {
			if (i == w) continue;
			if (this.board[i][h] == 0) {
				this.board[i][h] = 1;
				this.count++;
			} else {
				this.board[i][h] = 0;
				this.count--;
			}
			this.processCLickView(i, h);
		}
	}

	// For a single tile finds the corresponding DOM element 
	// and inverts the color
	this.processCLickView = function(w, h) {
		var coord = ".coord" + w + "q" + h;
		// console.log(coord);
		if (this.board[w][h] == 0) {
			$(coord).css("background-color", "#E6AB5E");
		} else {
			$(coord).css("background-color", "#5C90FF");
		}
	}

	// Populate the game board with 0s and 1s randomly
	this.populate = function() {
		for (var i = 0; i <= this.wide; i++) {
			for (var j = 0; j <= this.high; j++) {
				this.board[i][j] = 0;
			}
		}
	}

	this.isGameWin = function() {
		return this.count == (this.wide + 1) * (this.high + 1);
	}

	/*this.parseGameBoard = function(csv, callback) {
		var res = csv.split(",");
		//console.log(res.length);
		for (var i = 0; i < res.length; i++) {
			console.log(Math.floor(i/(this.high+1)) + "," + i % (this.high+1));
			this.board[Math.floor(i / (this.high+1))][i % (this.high+1)] = parseInt(res[i]);
		}
		callback();
	}*/
}
