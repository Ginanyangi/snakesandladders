import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

class SnakesandLadders:
    def __init__(self,num_players) :
        self.num_players = num_players
        self.players = [Player(f'Player {i+1}') for i in range (num_players)]
        self.board = {
            #Ladder positions
           5: 14,
           9: 31,
           1: 38,
           21: 42,
           28: 84,
           51: 67,
           72: 91,
           80: 99,
           #Snake positions
           7: 17,
           18: 62,
           34: 54,
           60: 64,
           36: 87,
           73: 92,
           75: 95,
           79: 98,

        }

    def roll_dice(self):
        return random.randint(1,6)    
    
    def move_player(self,player,steps):
        player.position += steps
        if player.position in self.board:
            new_position = self.board[player.position]
            if new_position > player.position:
                print(f'{player.name} climbed a ladder!')
            else:
                print(f'{player.name} got bitten by a snake!')
            player.position = new_position
    
    def check_win(self,player):
        return player.position >= 100
    
    def play_game(self):
        print('Welcome to Snakes and Ladders')
        while True:
            for player in self.players:
                input(f"{player.name}, press Enter to roll the dice...")
                steps = self.roll_dice()
                print(f"{player.name} rolled a {steps}.")
                self.move_player(player,steps)
                if self.check_win(player):
                    print(f"Congratulations, {player.name}! You won!")
                    return
                print(f"{player.name} is now at position {player.position}.")

if __name__ == "__main__":
    num_players = int(input('Enter number of players: '))
    game = SnakesandLadders(num_players)
    game.play_game()