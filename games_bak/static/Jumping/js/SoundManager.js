var SoundManager = function( game, on ){
	this.game = game;

	this.button = this.game.add.audio( 'button' );
	this.jump = this.game.add.audio( 'jump' );
	this.hit = this.game.add.audio( 'hit' );
	this.got = this.game.add.audio( 'got' );

    this.mute = !on;
};

var p = SoundManager.prototype;

p.switchSound = function( on ){
	this.mute = !on;
	if( this.theme ){
		if( on ){
			this.theme.resume();
		}else{
			this.theme.pause();
		}
	}
};

p.playTheme = function() {
	if( !this.theme.isPlaying )
		this.theme.play('',0,1,true);
	if( this.mute )
		this.theme.pause();
};

p.playJump = function() {
	if( !this.mute )
		this.jump.play('', 0);
};

p.playGot = function() {
	if( !this.mute )
		this.got.play('',0,0.6);
};

p.playHit = function() {
	if( !this.mute )
		this.hit.play();
};

p.playButton = function() {
	if( !this.mute )
		this.button.play();
};