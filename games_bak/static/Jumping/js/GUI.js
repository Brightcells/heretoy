GUI = function (game) {
    this.game = game;
    Phaser.Group.call(this, game);

    this.fixedToCamera = true;

    this.callPause = new Phaser.Signal();
    this.callResume = new Phaser.Signal();
    this.callRestart = new Phaser.Signal();


    this.tutorial = this.game.add.group();
    this.tutorial.x += scaleValue(20);
    this.add( this.tutorial );
    var pic = this.tutorial.create( scaleValue(50), scaleValue(100), 'sprites', 'Tutor' );
    var style_tut = {font:scaleValue(26) + "px Arial", fill:0x000000, align:'left'};
    var text1 = this.game.add.text( scaleValue(80), scaleValue(230), GetPlatformAction( this.game.device.desktop, lang), style_tut, this.tutorial );
    var text2 = this.game.add.text( scaleValue(160), scaleValue(140), GetPlatformAction( this.game.device.desktop, lang), style_tut, this.tutorial );

    this.init_inGameUI();
    this.init_pauseMenu();
    this.init_gameOver();
};

GUI.prototype = Object.create(Phaser.Group.prototype);
GUI.prototype.constructor = GUI;

var p = GUI.prototype;

p.init_inGameUI = function() {
	this.buttonPause = new PopButton( this.game, scaleValue(30), scaleValue(30), 'sprites', 'buttonPause', this );
	this.buttonPause.events.onInputUp.add( this.showPause, this );

	var style_score = {font:"Bold " + scaleValue(26) + "px Arial", fill:0x000000, align:'right'};
	this.labelScore = this.game.add.text(scaleValue(310), scaleValue(10), '0', style_score, this );
	this.labelScore.anchor.set( 1, 0 );
};

p.init_pauseMenu = function() {
	this.pauseBack = this.game.add.graphics( 0, 0 )
	this.add( this.pauseBack );
	this.pauseBack.beginFill( 0xffffff, 0.7 ); 
	this.pauseBack.drawRect( 0, 0, this.game.width, this.game.height );
	this.pauseBack.endFill();

	this.pauseButtonResume = new PopButton( this.game,this.game.width/2, this.game.height/2, 'sprites', 'buttonPlay', this  );
	this.pauseButtonResume.events.onInputUp.add( this.hidePause, this );

	this.pauseButtonMore = new PopButton( this.game,this.game.width/2 - scaleValue(80), this.game.height/2, 'sprites', 'buttonMore', this  );
	this.pauseButtonMore.events.onInputUp.add( this.gotoSite, this );

	this.pauseButtonSound = new PopButton( this.game,this.game.width/2 + scaleValue(80), this.game.height/2, 'sprites', 'buttonSoundOn', this  );
	this.pauseButtonSound.events.onInputUp.add( this.switchSound, this );

	if( JSON.parse(localStorage["Jumper.sound"]) ){
        this.pauseButtonSound.loadTexture( 'sprites', 'buttonSoundOn');
    }
    else{
        this.pauseButtonSound.loadTexture( 'sprites', 'buttonSoundOff');
    }

    this.pauseBack.visible = false;
    this.pauseButtonMore.visible = false;
    this.pauseButtonResume.visible = false;
    this.pauseButtonSound.visible = false;
};

p.init_gameOver = function() {
	this.overBack = this.game.add.graphics( 0, 0 )
	this.add( this.overBack );
	this.overBack.beginFill( 0xffffff ); 
	this.overBack.drawRect( 0, 0, this.game.width, this.game.height );
	this.overBack.endFill();


	var style_big = {font:"Bold " + scaleValue(36) + "px Arial", fill:0x000000, align:'center'};
	this.labelGameOver = this.game.add.text(this.game.width/2, scaleValue(60), Lang[lang][0], style_big, this );
	this.labelGameOver.anchor.set( 0.5, 0 );

	this.overBorder = this.create( this.game.width/2, scaleValue(110), 'sprites', 'gameOverBorder');
	this.overBorder.anchor.set( 0.5, 0 );

    this.medal = this.create( scaleValue(178), scaleValue(151));
    this.medal.scale.set( 1.1, 1.1);

	var style_label = {font:scaleValue(18) + "px Arial", fill:0x000000, align:'left'};
	var style_value = {font: "Bold "+scaleValue(18) + "px Arial", fill:0x000000, align:'left'};

	this.labelResult = this.game.add.text(scaleValue(70), scaleValue(125), Lang[lang][1], style_label, this );
	this.labelResultValue = this.game.add.text(scaleValue(70), this.labelResult.y + scaleValue(22), '0', style_value, this );

	this.labelBest = this.game.add.text(scaleValue(70), scaleValue(176), Lang[lang][2], style_label, this );
	this.labelBestValue = this.game.add.text(scaleValue(70), this.labelBest.y + scaleValue(22), '0', style_value, this );

	this.labelReward = this.game.add.text(scaleValue(211), scaleValue(125), Lang[lang][3], style_label, this );
	this.labelReward.anchor.set( 0.5, 0 );

    this.backRecord = this.create( 0, this.labelBestValue.y, 'sprites', 'New' );
    var style_record = {font:scaleValue(12) + "px Arial", fill:'#ffffff', align:'left'};
    this.recordLabel = this.game.add.text( 0,0,Lang[lang][7], style_record, this);

	this.buttonAgain = new ColorButton( this.game, this.game.width/2, scaleValue(270), scaleValue(180), scaleValue(40), scaleValue(20), '#5acf63', this, Lang[lang][4]);
	this.buttonShare = new ColorButton( this.game, this.game.width/2, scaleValue(320), scaleValue(180), scaleValue(40), scaleValue(20), '#4198de', this, Lang[lang][5]);
	this.buttonMore = new ColorButton( this.game, this.game.width/2, scaleValue(370), scaleValue(180), scaleValue(40), scaleValue(20), '#9f53d6', this, Lang[lang][6]);

	this.buttonAgain.events.onInputUp.add( this.callRestart.dispatch, this );

	this.overBorder.visible = false;
	this.overBack.visible = false;
	this.labelGameOver.visible = false;
	this.labelReward.visible = false;
	this.labelResult.visible = false;
	this.labelResultValue.visible = false;
	this.labelBest.visible = false;
	this.labelBestValue.visible = false;
	this.buttonAgain.visible = false;
	this.buttonShare.visible = false;
    this.buttonMore.visible = false;
	this.medal.visible = false;
    this.backRecord.visible = false;
    this.recordLabel.visible = false;
};

p.hideTutorial = function() {
    var tween  = this.game.add.tween( this.tutorial );
    tween.onComplete.add( function(){ this.destroy(true) }, this.tutorial );
    tween.to( {alpha:0}, 500, Phaser.Easing.Linear.None, true );
};

p.setScore = function( value ){
	this.labelScore.setText( value );
};

p.showPause = function() {
	this.callPause.dispatch();
	this.pauseBack.visible = true;
	this.pauseButtonMore.visible = true;
    this.pauseButtonResume.visible = true;
    this.pauseButtonSound.visible = true;
};

p.hidePause = function() {
	this.callResume.dispatch();
	this.pauseBack.visible = false;
	this.pauseButtonMore.visible = false;
    this.pauseButtonResume.visible = false;
    this.pauseButtonSound.visible = false;
};

p.showGameOver = function( score ) {
	SG_Hooks.gameOver(0, score, null);
	this.overBorder.visible = true;
	this.overBack.visible = true;
	this.labelGameOver.visible = true;
	this.labelReward.visible = true;
	this.labelResult.visible = true;
	this.labelResultValue.visible = true;
	this.labelBest.visible = true;
	this.labelBestValue.visible = true;
	this.buttonAgain.visible = true;
	this.buttonShare.visible = true;
	this.buttonMore.visible = true;
    this.medal.visible = true;

	var best = JSON.parse( localStorage["Jumper.bestScore"] );
	this.labelBestValue.setText( best )
	this.labelResultValue.setText( score );
	if( score > best ) {
		localStorage["Jumper.bestScore"] = score;
        this.labelBestValue.setText( score )

        this.backRecord.visible = true;
        this.recordLabel.visible = true;
        this.backRecord.x = this.labelBestValue.x + this.labelBestValue.width + scaleValue(5);
        this.recordLabel.x = this.backRecord.x + scaleValue(10);
        this.recordLabel.y = this.backRecord.y + scaleValue(2);
    }

    if( score >= 30 )
        this.medal.loadTexture( 'sprites', 'medalGold' );
    else if( score >= 20 )
        this.medal.loadTexture( 'sprites', 'medalSilver' );    
    else if( score >= 10 )
        this.medal.loadTexture( 'sprites', 'medalBronze' );
};

p.switchSound = function() {
	var soundState = JSON.parse(localStorage["Jumper.sound"]);
	soundState = !soundState;
	if( soundState ){
        this.pauseButtonSound.loadTexture( 'sprites', 'buttonSoundOn');
    }
    else{
        this.pauseButtonSound.loadTexture( 'sprites', 'buttonSoundOff');
    }
    localStorage["Jumper.sound"] = soundState;
    this.game.sndManager.switchSound( soundState );
};

p.gotoSite = function() {
	//window.open( 'http://m.softgames.de', '_blank' );
    SG.redirectToPortal();
};



PopButton = function ( game, x, y, list, sprite, group) {
    Phaser.Sprite.call(this, game, x, y, list, sprite );
    game.add.existing(this);

    group.add( this );
    this.anchor.set( 0.5, 0.5 );

    this.inputEnabled = true;
    this.events.onInputDown.add( function() {
    	this.scale.set( 1.1, 1.1 );
    }, this );    
    this.events.onInputUp.add( function() {
    	this.scale.set( 1, 1 );
    	this.game.sndManager.playButton();
    }, this );
};

PopButton.prototype = Object.create(Phaser.Sprite.prototype);
PopButton.prototype.constructor = PopButton;

var p = PopButton.prototype;



ColorButton = function ( game, x, y, width, height, round, color, group, title) {
    Phaser.Sprite.call(this, game, x, y);
    game.add.existing(this);

    group.add( this );
    this.anchor.set( 0.5, 0.5 );

    renderGroup = this.game.add.group();
    texture = this.game.add.renderTexture(width, height, 'button_'+title);

    var x = 0;
    var y = 0;
    var w = width;
    var h = height;
    var r = round;
    var gr_header = this.game.add.bitmapData( w, h );
    gr_header.context.beginPath();
    gr_header.context.moveTo(x+r, y);
    gr_header.context.arcTo(x+w, y,   x+w, y+h, r);
    gr_header.context.arcTo(x+w, y+h, x,   y+h, r);
    gr_header.context.arcTo(x,   y+h, x,   y,   r);
    gr_header.context.arcTo(x,   y,   x+w, y,   r);
    gr_header.context.closePath();
    gr_header.context.fillStyle = color;
    gr_header.context.fill();

    var p = renderGroup.create( 0, 0, gr_header );
    p.anchor.set( 0.5, 0.5 );

    var style = {font:"Bold "+scaleValue(22) + "px Arial", fill:'#ffffff', align:'center'};
    var label = this.game.add.text( 0, 0, title, style, renderGroup);
    label.anchor.set( 0.5, 0.5 );

    texture.renderXY( renderGroup, renderGroup.width/2, renderGroup.height/2);
    renderGroup.destroy( true );

    this.loadTexture(texture);

    this.inputEnabled = true;
    this.events.onInputDown.add( function() {
    	this.scale.set( 1.1, 1.1 );
    }, this );    
    this.events.onInputUp.add( function() {
    	this.scale.set( 1, 1 );
    	this.game.sndManager.playButton();
    }, this );
};

ColorButton.prototype = Object.create(Phaser.Sprite.prototype);
ColorButton.prototype.constructor = ColorButton;

var p = ColorButton.prototype;
