Column = function( game, group, x, color ) {
    var configs = [
        [240, 144],
        [216, 168],
        [192, 192],
        [168, 216],
        [144, 240]
    ];


    var width = scaleValue( game.rnd.integerInRange(80, 170) );
    var part = game.rnd.integerInRange(0, 4);

	this.game = game;
	var height_1 = configs[part][0];
	var height_2 = configs[part][1];

    var gr = this.game.add.graphics(0,0);
    gr.beginFill( color);
    gr.drawRect(0,0,width,scaleValue(height_1));
    gr.endFill();
    gr.boundsPadding = 0;
	var obstacle_1 = group.create( x, 0, gr.generateTexture() );
	gr.destroy();

	var gr = this.game.add.graphics(0,0);
    gr.beginFill( color);
    gr.drawRect(0,0,width,scaleValue(height_2+10));
    gr.endFill();
    gr.boundsPadding = 0;
	var obstacle_2 = group.create( x, scaleValue(480 - height_2+10), gr.generateTexture() );
	gr.destroy();


	var gr = this.game.add.graphics(0,0);
    gr.beginFill( color);
    gr.drawRect(0,0,width,scaleValue(10));
    gr.endFill();
    gr.boundsPadding = 0;
	var ground = group.create( x, scaleValue(480 - height_2), gr.generateTexture() );
	gr.destroy();

	return [ obstacle_1, obstacle_2, ground ];
};