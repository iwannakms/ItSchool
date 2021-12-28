import random

cards = ["2 черви", "3 черви", "4 черви", "5 черви", "6 черви", "7 черви", "8 черви", "9 черви", "10 черви"
         "валет черви", "дама черви", "король черви", "туз черви"
         "2 буби", "3 буби", "4 буби", "5 буби", "6 буби", "7 буби", "8 буби", "9 буби", "10 буби",
         "валет буби", "дама буби", "король буби", "туз буби",
         "2 пики", "3 пики", "4 пики", "5 пики", "6 пики", "7 пики", "8 пики", "9 пики", "10 пики",
         "валет пики", "дама пики", "король пики", "туз пики",
         "2 крести", "3 крести", "4 крести", "5 крести", "6 крести", "7 крести", "8 крести", "9 крести", "10 крести",
         "валет крести", "дама крести", "король перксти", "туз крести"]


def distribution(player, dealer):
    for i in range(1):
        player.append(cards[random.randint(0, 51)])

    for j in range(1):
        dealer.append(cards[random.randint(0, 51)])


def add_card(player=None, dealer=None):
    if player:
        player.append(cards[random.randint(0, 49)])
    elif dealer:
        dealer.append(cards[random.randint(0, 49)])


def show_hands(player, dealer):
    for card in player:
        print(card)

    print(dealer[0])
    print("********")


def final(player, dealer):
    print("\nВаша рука\n")
    for card in player:
        print(card)

    print("\nРука дилера\n")
    for card in dealer:
        print(card)


def convert_card_to_int(player=None, dealer=None):
    if player:
        for card in player:
            cut = len(card)
            for symbol in card:
                if symbol.isdigit():
                    continue
                cut -= 1
            return int(card[:cut])
    elif dealer:
        for card in dealer:
            cut = len(card)
            for symbol in card:
                if symbol.isdigit():
                    continue
                cut -= 1
            return int(card[:cut])


def sum_of_scores(player, dealer, score_of_player=0, score_of_dealer=0):
    score_of_player += convert_card_to_int(player)
    score_of_dealer += convert_card_to_int(None, dealer)


def game_over(score_of_player, score_of_dealer, spot_parameter, rate_parameter):
    if score_of_player > 21:
        spot_parameter -= rate_parameter
        print("Вы проиграли, у вас перебор очков:", score_of_player)
        print("Вы просрали", rate_parameter, "$.")
    elif score_of_player > score_of_dealer or score_of_dealer > 21:
        spot_parameter += rate * 2
        print("Поздравляем, вы выйграли!!!")
        print("Ваше очко:", score_of_player,
              "\nОчко дилера:", score_of_dealer,
              "\nВаш выйгрыш:", rate_parameter * 2, "$.")
    elif score_of_player == score_of_dealer:
        print("Ничья.\nВаше очко:", score_of_player,
              "\nОчко дилера:", score_of_dealer,
              "\nВы забираете свои", rate, "$.")
    elif score_of_player < score_of_dealer <= 21:
        spot_parameter -= rate_parameter
        print("Вы проиграли.\nВаше очко:", score_of_player,
              "\nОчко дилера:", score_of_dealer,
              "\nВы просрали:", rate_parameter, "$.")


player_hand = []
dealer_hand = []
spot = 200
restart = 0

print("Добро пожаловать в наше казино \"ЗАЛУПИНО\"")
while True:
    player_score, dealer_score = 0, 0
    print("Делаем ставки, у вас", spot, "$.")
    rate = int(input("Ваша ставка >>> "))
    if rate > spot:
        "У вас недостаточно средсв для совершения такой ставки.\nПовторите действие."
        continue

    print("Ставки приняты. Раздача карт.")
    distribution(player_hand, dealer_hand)
    show_hands(player_hand, dealer_hand)
    sum_of_scores(player_hand, dealer_hand, player_score, dealer_score)

    while player_score < 21:
        add = int(input("\nХотите добрать карты? (да - 1  :  нет - 2) >>> "))
        if add == 1:
            add_card(player_hand)
            show_hands(player_hand, dealer_hand)
            sum_of_scores(player_hand, dealer_hand, player_score, dealer_score)
            if player_score > 21:
                game_over(player_score, dealer_score, spot, rate)
                restart_game = int(input("Хотите сыграть еще раз? (1 - да  :  2 - нет) >>> "))
                if restart_game == 1:
                    restart = 1
                else:
                    print("Рады были вас видеть. До скорой встечи!")
                    restart = 0
        else:
            break

    if restart:
        continue

    while dealer_score <= 16:
        add_card(None, dealer_hand)
        sum_of_scores(player_hand, dealer_hand, player_score, dealer_score)

    final(player_hand, dealer_hand)
    game_over(player_score, dealer_score, spot, rate)
    if spot <= 0:
        print("Ебаный рот этого казио, блять!!!")

    restart = int(input("Хотите сыграть еще раз? (1 - да  :  2 - нет) >>> "))
    if not restart:
        print("Рады были вас видеть. До скорой встечи!")
        break
