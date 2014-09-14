// Bindings go here


$(document).ready(function(){
	var game = new Game();
	game.beginGame();

	$('.reset').click(function(){
		// $('#restartLevel').modal('show');
                var conf = confirm("再来一次！");
                if(conf == true) {
                    game.onResetLevelClick();
                }
	});

	$('.newgame').click(function(){
		// $('#newGame').modal('show');
                var conf = confirm("从头来过！");
                if(conf == true) {
                    game.onNewGameClick();
                }
	});

	$('#resetLevelConfirm').click(function(){
		game.onResetLevelClick();
	});

	$('#newGameConfirm').click(function(){
		game.onNewGameClick();
	});

	$('.instruct').click(function(){
		$('#instructions').modal('show');
	})
});
