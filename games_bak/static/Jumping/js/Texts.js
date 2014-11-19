function GetPlatformAction( isDesktop, lang ){
    if( isDesktop )
        return Lang[lang][9];
    else
        return Lang[lang][8];
}

var Lang = {
    'en':
    [
        "Game Over",   
        "Result",
        "Best",
        "Reward",
        "Again",
        "Share",
        "More Games",
        "New",
        "Tap",
        "Click"
    ],

    'ru':
    [
        "Конец Игры",
        "Результат",
        "Лучший",
        "Награда",
        "Снова",
        "Поделиться",
        "Больше Игр",
        "Новый",
        "Тап",
        "Клик"
    ],

    'de':
    [
        'Game Over',
        'Ergebnis',
        'Rekord',
        'Belohnung',
        'Noch einmal',
        'Teilen',
        'Mehr Spiele',
        'Neu',
        'Antippen',
        'Klick'
    ],

    'es':
    [
        'Fin del juego', 
        'Resultado',
        'Mejor',
        'Premio',
        'Otra vez',
        'Compartir',
        'Más juegos',
        'Nuevo',
        'Pulsar',
        'Haz clic'
    ],

    'fr':
    [
        'Terminé',
        'Score',
        'Meilleur',
        'Récompense',
        'Rejouer',
        'Partager',
        'Plus de jeux',
        'Nouveau',
        'Tapez',
        'Cliquez'
    ],

    'it':    
    [
        'Game Over',
        'Risultato',
        'Migliore',
        'Premio',
        'Gioca ancora',
        'Condividi',
        'Altri giochi',
        'Nuovo',
        'Tap',
        'Clic'
    ],

    'pt':    
    [
        'Fim do Jogo',
        'Resultado',
        'Melhor',
        'Prémio',
        'Outra vez',
        'Partilhar',
        'Mais Jogos',
        'Novo',
        'Tocar',
        'Clicar'
    ],

    'tr':
    [
        'Oyun Bitti',
        'Sonuç',
        'En iyi',
        'Ödül',
        'Tekrar',
        'Paylaş',
        'Daha Fazla Oyun',
        'Yeni',
        'Tuşla',
        'Tıkla'
    ] 
};
