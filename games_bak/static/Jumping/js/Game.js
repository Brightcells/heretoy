 /*

Digitboard = function (game, value) {
    this.game = game;
    Phaser.Group.call(this, game);
};

Digitboard.prototype = Object.create(Phaser.Group.prototype);
Digitboard.prototype.constructor = Digitboard;

var p = Digitboard.prototype;


--------


FallBill = function (game, cache) {

    Phaser.Sprite.call(this, game, x, y, 'art', 'FallBill');
    game.add.existing(this);
};

FallBill.prototype = Object.create(Phaser.Sprite.prototype);
FallBill.prototype.constructor = FallBill;

var p = FallBill.prototype;


*/

TheTower.Game = function (game) {

    this.game;      //  a reference to the currently running game
    this.add;       //  used to add sprites, text, groups, etc
    this.camera;    //  a reference to the game camera
    this.cache;     //  the game cache
    this.input;     //  the global input manager (you can access this.input.keyboard, this.input.mouse, as well from it)
    this.load;      //  for preloading assets
    this.math;      //  lots of useful common math operations
    this.sound;     //  the sound manager - add a sound, play one, set-up markers, etc
    this.stage;     //  the game stage
    this.time;      //  the clock
    this.tweens;    //  the tween manager
    this.world;     //  the game world
    this.particles; //  the particle manager
    this.physics;   //  the physics manager
    this.rnd;       //  the repeatable random number generator

};

TheTower.Game.prototype = {

    init: function ( ) {
    },

    create: function () {
        //SG_Hooks.start();

        this.game.time.advancedTiming = true;
        //this.game.scale.startFullScreen();
        this.game.stage.backgroundColor = 0xFFFFFF;

        //this.game.sndManager.playTheme();

        this.game.world.setBounds( 0, 0, scaleValue(10000), this.game.height );
        this.game.physics.startSystem(Phaser.Physics.ARCADE);


        this.colors = [
            0xFF9800,
            0x70B85D,
            0x01B0F0,
            0x00A388,
            0xFF6138
        ];
        this.colors = this.shuffle( this.colors );

        this.level = this.game.add.group();
        this.level.enableBody = true;
        this.level.physicsBodyType = Phaser.Physics.ARCADE;

        this.grounds = [];
        this.obstacles = [];

        // groud
        var gr = this.game.add.graphics(0,0);
        gr.beginFill( this.pickColor() );
        gr.drawRect(0,0,scaleValue(420),scaleValue(146));
        gr.endFill();
        gr.boundsPadding = 0;

        var g = this.level.create( 0, scaleValue(480-146), gr.generateTexture() );
        gr.destroy();
        this.grounds.push( g );

        this.level.setAll('body.immovable', true);


        // char
        this.char = new Character( this.game, scaleValue(50), scaleValue(312) );
        this.char.getScore.add( this.getScore, this );

        this.game.camera.follow( this.char );
        this.game.camera.deadzone = new Phaser.Rectangle( 0, 0, scaleValue(60), this.game.height);

        this.clickProxy = this.game.add.sprite( 0, 0 );
        this.clickProxy.scale.set( this.game.width/this.clickProxy.width, this.game.height/this.clickProxy.height );
        this.clickProxy.inputEnabled = true;
        this.clickProxy.events.onInputDown.add( this.char.jump, this.char );
        this.clickProxy.fixedToCamera = true;

        this.game.gui = new GUI( this.game );
        this.game.gui.callPause.add( this.pause, this );
        this.game.gui.callResume.add( this.resume, this );
        this.game.gui.callRestart.add( this.restart, this );
        this.game.gui.buttonShare.events.onInputDown.add( this.gotoTwitter, this );
        this.game.gui.buttonMore.events.onInputDown.add( this.gotoSite, this );

        this.score = 0;
    },

    pickColor: function() {
        var res = this.colors[0];
        this.colors.push( this.colors.shift() );
        return res;
    },

    shuffle: function(o){ //v1.0
        for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
        return o;
    },

    update: function() {
        if( this.char.active ){
            // Ð¿Ñ€Ð¾Ð²ÐµÑ€Ð¸Ð¼ ÐºÐ¾Ð»Ð»Ð°Ð¹Ð´ Ñ Ð·ÐµÐ¼Ð»ÐµÐ¹
            for( var i = 0; i < Math.max( 2, this.grounds.length); i++ ){
                this.game.physics.arcade.collide( this.char, this.grounds[i], this.grounded, null, this);
            }

            for( var i = 0; i < Math.max( 4, this.obstacles.length); i++ ){
                this.game.physics.arcade.collide( this.char, this.obstacles[i], this.hited, null, this);
            }
           // this.game.physics.arcade.collide( this.char, this.level, this.grounded, null, this);
        }

        // remove offscreen ground
        if( this.grounds[0].x + this.grounds[0].width < this.game.camera.x ){
            this.grounds[0].destroy();
            this.grounds.shift();
        }

        // remove offscreen obstacles
        if( this.obstacles.length > 0 && this.obstacles[0].x + this.obstacles[0].width < this.game.camera.x ) {
            this.obstacles[0].destroy();
            this.obstacles[1].destroy();
            this.obstacles.splice(0,2);
        }

        // generate new
        var lastIndex = this.grounds.length-1;
        var posX = this.grounds[lastIndex].x + this.grounds[lastIndex].width;
        if( posX < this.game.camera.x+this.game.camera.width ){
            this.makeNewPart( posX );
        }

        if( this.char.active && this.char.y >= this.game.height ){
            this.char.active= false;
            this.game.gui.showGameOver( this.score );
        }

    },

    makeNewPart: function( fromX ) {
        var dist = scaleValue( this.game.rnd.integerInRange(140, 230) );
        var objs = new Column( this.game, this.level, fromX + dist, this.pickColor() );
        objs[0].body.immovable = true;
        objs[1].body.immovable = true;
        objs[2].body.immovable = true;
        this.grounds.push( objs[2] );
        this.obstacles.push( objs[0], objs[1] );
    },

    getScore: function() {
        this.score++;
        this.game.gui.setScore( this.score );
    },

    restart: function() {
        this.game.state.start( 'Game' );
    },

    pause: function() {
        this.char.pause();
    },

    resume: function() {
        this.char.resume();
    },

    grounded: function() {
        this.char.grounded();
    },

    hited: function () {
        if( this.char.active ){
            this.char.hit();

            var self = this;
            setTimeout(function() { self.game.gui.showGameOver( self.score ); }, 800 );
        }
    },

    gotoSite: function() {
        //window.open("http://m.softgames.de", "_blank");
        SG.redirectToPortal();
    },

    gotoTwitter: function() {
        window.open("http://twitter.com/softgames", "_blank");
    },

    render: function() {
        // game.debug.body(this.char);
        // this.obstacles.forEach(function(item){
        //     game.debug.body( item );
        // }, this);
        //game.debug.text( "fps: "+(game.time.fps || '--'), scaleValue(250), scaleValue(460), "#00ff00", scaleValue(20) + "px Arial"); 
        //game.debug.text( "Ground: " + this.grounds.length, scaleValue(200), scaleValue(430), "#ff0000", scaleValue(20) + "px Arial"); 
        //game.debug.text( "Obstacles: " + this.obstacles.length, scaleValue(200), scaleValue(400), "#ff0000", scaleValue(20) + "px Arial"); 
        //this.game.debug.geom( new Phaser.Rectangle( this.circle.x - this.game.input.zoneSize/2, this.circle.y - this.game.input.zoneSize/2, this.game.input.zoneSize, this.game.input.zoneSize), 'rgba(255,56,0,0.3)' ) ;
        //game.debug.text( this.distance, scaleValue(10), scaleValue(30), "#0000ff", scaleValue(20) + "px Arial"); 
    }

};