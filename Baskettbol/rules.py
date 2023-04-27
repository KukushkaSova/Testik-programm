def get_rules_by_location(location, language='en'):
    """Returns the rules of basketball for a given location and language."""
    if location == 'world':
        if language == 'ru':
            return """
            Правила баскетбола:
            1. Команда состоит из 5 игроков.
            2. Цель игры - забросить мяч в корзину противника и не дать ему забросить мяч в вашу корзину.
            3. Игра начинается с центра площадки, где судья бросает мяч между двумя игроками.
            4. Игроки передают мяч друг другу, передвигаясь по площадке, и пытаются забросить мяч в корзину противника.
            5. Игра длится 4 периода по 12 минут каждый.
            """
        else:
            return """
            Basketball rules:
            1. A team consists of 5 players.
            2. The objective of the game is to shoot the ball through the opponent's basket while preventing the opponent from shooting the ball through your own basket.
            3. The game starts with a jump ball at center court, where the referee tosses the ball between two players.
            4. Players pass the ball to each other while moving around the court, attempting to shoot the ball into the opponent's basket.
            5. The game consists of 4 quarters, each lasting 12 minutes.
            """
    elif location == 'usa':
        if language == 'ru':
            return """
            Правила баскетбола в США:
            1. Команда состоит из 5 игроков.
            2. Цель игры - забросить мяч в корзину противника и не дать ему забросить мяч в вашу корзину.
            3. Игра начинается с броска мяча с боковой линии площадки.
            4. Игроки передают мяч друг другу, передвигаясь по площадке, и пытаются забросить мяч в корзину противника.
            5. Игра длится 4 периода по 12 минут каждый.
            """
        else:
            return """
            Basketball rules in the USA:
            1. A team consists of 5 players.
            2. The objective of the game is to shoot the ball through the opponent's basket while preventing the opponent from shooting the ball through your own basket.
            3. The game starts with a throw-in from the sideline.
            4. Players pass the ball to each other while moving around the court, attempting to shoot the ball into the opponent's basket.
            5. The game consists of 4 quarters, each lasting 12 minutes.
            """
    else:
        return "Rules not available for this location."