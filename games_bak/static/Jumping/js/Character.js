Character = function ( game, x, y) {
    Phaser.Sprite.call(this, game, x, y, 'run' );
    game.add.existing(this);

    this.fps = 32;

    this.animations.add('run',[0,1,2,3,4,5,6,7,8,9,10,11,12,13]);
    this.animations.add('salto',[14,14]);
    this.animations.add('fall',[15,15]);
    this.animations.add('kill',[3]);
    this.play( 'run', this.fps, true );
    this.anchor.set(0.6,0.5);
    this.scale.set(0.6,0.6);

    // var gr = this.game.add.graphics(0,0);
    // gr.beginFill( 0xFFFFFF);
    // gr.drawRect(0,0,scaleValue(20),scaleValue(20));
    // gr.endFill();
    // gr.boundsPadding = 0;

    // this.loadTexture( gr.generateTexture() );
    // this.anchor.set(0.5,0.5);
    // this.tint = 0x000000;

    // gr.destroy();

    this.getScore = new Phaser.Signal();

    this.game.physics.enable(this, Phaser.Physics.ARCADE);
    this.body.setSize( scaleValue(24), scaleValue(50), scaleValue(0), scaleValue(5));

    this.tween = this.game.add.tween( this );

    this.speed = scaleValue(180);
    this.gravity = scaleValue(45);

    this.jumpForce = 0;
    this.jumpNum = 0;

    this.active = true;
    this.isPause = false
    this.inBegin = true;
};

Character.prototype = Object.create(Phaser.Sprite.prototype);
Character.prototype.constructor = Character;

var p = Character.prototype;

p.update = function() {
    if( this.isPause )
        return;

    if( this.jumpForce > 0){
        this.jumpForce -= scaleValue(10);
        if( this.jumpForce < 0 ){
            this.jumpForce = 0;
        }
    }

	this.body.velocity.y += this.gravity - this.jumpForce;

	if( this.active && !this.inBegin ){
		this.body.velocity.x = this.speed;
    }

};

p.jump = function() {
    if( this.inBegin ){
        this.inBegin = false;
        this.game.gui.hideTutorial();
    }

    if( this.isPause )
        return;

	if( !this.active || this.jumpNum >= 2)
		return;

    this.play('salto', 1, true);
    this.game.sndManager.playJump();
	this.jumpNum++;

	this.fly();

    this.body.velocity.y = 0;
    this.jumpForce = scaleValue(150);

    var target = 360;
    if( this.angle > 0 )
        target = 720;
    this.tween._parent = 0;
    this.tween._lastChild = 0;
    this.tween.onComplete.add( this.flip, this );
    this.tween.to( {angle:target}, 600, Phaser.Easing.Sinusoidal.Out, true );
};

p.flip = function() {
    this.angle = 0;
    if( !this.animations.getAnimation('run').isPlaying 
        && !this.animations.getAnimation('kill').isPlaying){
        this.play( 'fall' );
    }
};

p.grounded = function() {
    if( this.jumpNum != 0 && this.x > scaleValue(500)){
        this.getScore.dispatch();
        this.game.sndManager.playGot();
    }
	this.jumpNum = 0;
    this.play('run', this.fps, true);
};

p.fly = function() {

};

p.hit = function() {
    this.tween.stop();
    this.play('kill', 1, true);
    this.angle = -70;
    this.game.sndManager.playHit();
	this.active = false;
	this.body.velocity.y = scaleValue(50);
	this.body.velocity.x = -scaleValue(130);
	this.game.camera.follow( null );
};

p.pause = function() {
    this.animations.paused = true;
    this.isPause = true;
    this.body.enable = false;
    if( this.tween.isRunning )
        this.tween.pause();
};

p.resume = function() {
    this.animations.paused = false;
    this.isPause = false;
    this.body.enable = true;
    if( this.tween.isRunning )
        this.tween.resume();
};
