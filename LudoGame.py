"""players start on ready space and move to starting position"""

"""player_a_start == 1
player_b_start == 15
player_c_start == 29
player_c_start == 43"""

"""player start pos changed to current pos == 1"""

"""player rolls die and move that number of spaces"""

"""If the player’s two tokens land on the same space on the board, the player will stack the two tokens and move 
them as one piece until they reach the finishing square. When stacked pieces are sent back to their home yard by an 
opponent landing on them, they are no longer stacked. Note that if two tokens are both at the “ready to go” position, 
they are not stacked."""

"""When a token finishes one move, if it lands on a space occupied by an opponent's (other player’s) token, 
the opponent token will be returned (kicked back) to its home yard. The returned token can re-enter into 
play when the owner rolls a 6."""

"""players turn at start pos - 7 or space 50 when player start set to 1"""
"""enter home row"""
"""players end on E"""

class LudoGame():
    """object represents the game as played."""
    pass

    def __init__(self):

        self._players_list = []
        self._turns_list = []
        # self._board = board
        self._players = players
        self._player_by_posiiton = ()
        # self._move_token = move_token
        # self._play_game = play_game


    def get_player_by_position(self):
        """ takes a parameter representing the player’s position as a string and returns the player object.
        For an invalid string parameter, it will return "Player not found!"""
        return self._player_by_position()# return player position as a string and the player-- token or name or Player class info?

    def priority_rule(self, die_roll, player_obj):
        if die_roll == 6:

            if player_obj.get_p_token_pos() == "H" and player_obj.get_token_p_step_count() == -1:
                return "p"
            if player_obj.get_q_token_pos() == "H" and player_obj.get_token_q_step_count() == -1:
                return "q"
        else:
            if player_obj.get_token_p_step_count() + die_roll == 57:
                return "p"
            if player_obj.get_token_q_step_count() + die_roll == 57:
                return "q"
            if player_obj.get_token_p_step_count() == 57 and player_obj.get_token_q_step_count() == 57:
                player_obj.set_player_state("Finished")

        for player in self.players_list:

            if player_obj.get_space_name(player_obj.get_token_q_step_count() + die_roll) == player.get_space_name(player.set_token_q_step_count()):
                return "q"
            if player_obj.get_space_name(player_obj.get_token_p_step_count() + die_roll) == player.get_space_name(player.set_token_p_step_count()):
                return "p"
            if player_obj.get_space_name(player_obj.get_token_p_step_count() + die_roll) == player.get_space_name(player.set_token_q_step_count()):
                return "p"
            if player_obj.get_space_name(player_obj.get_token_q_step_count() + die_roll) == player.get_space_name(player.set_token_p_step_count()):
                return "q"

        if player_obj.get_token_p_step_count() == -1 and player_obj. get_token_q_step_count == -1:
            pass
        if player_obj.get_token_p_step_count() >= 0 and player_obj. get_token_q_step_count == -1:
            return "q"
        if player_obj.get_token_q_step_count() >= 0 and player_obj. get_token_p_step_count == -1:
            return "p"
        if player_obj.get_token_p_step_count() > player_obj. get_token_q_step_count == -1:
            return "q"
        else:
            if player_obj.get_token_p_step_count() < player_obj.get_token_q_step_count == -1:
                return "p"

    def move_token(self, player, token, die_roll):
        """takes three parameters, the player object, the token name (‘p’ or ‘q’) and the steps the
        token will move on the board (int)."""

        if die_roll == 6:

            if player.get_p_token_pos() == "H" and player.get_token_p_step_count() == -1:
                player.set_p_token_pos("R")
                player.set_p_token_step_count(0)
                return
            elif player.get_q_token_pos() == "H" and player.get_token_q_step_count() == -1:
                player.set_q_token_pos("R")
                player.set_q_token_step_count(0)
                return

        if player.get_token_p_step_count() + die_roll == 57:
            player.set_token_p_step_count(57)
            player.set_p_token_pos("E")
            player.set_player_state("Finished")

        if player.get_token_q_step_count() + die_roll == 57:
            player.set_token_q_step_count(57)
            player.set_q_token_pos("E")
            player.set_player_state("Finished")

        if player.get_token_p_step_count() + die_roll == 57 and player.get_token_q_step_count() == 57:
            player.set_token_p_step_count(57)
            player.set_p_token_pos("E")
            player.set_player_state("Finished")

        for player in self._players_list:


        #else:
            if player.get_space_name(player.get_token_q_step_count() + die_roll) == player.get_space_name(player.get_token_q_step_count()):
                player.set_token_q_step_count(player.get_token_q_step_count() + die_roll)
                player.set_token_q_step_count(0)
                player.set_q_token_pos("H")

            if player.get_space_name(player.get_token_p_step_count() + die_roll) == player.get_space_name(player.get_token_p_step_count()):
                player.set_token_p_step_count(player.get_token_p_step_count() + die_roll)
                player.set_token_p_step_count(0)
                player.set_q_token_pos("H")

            if player.get_space_name(player.get_token_p_step_count() + die_roll) == player.get_space_name(player.get_token_q_step_count()):
                player.set_token_q_step_count(player.get_token_p_step_count() + die_roll)
                player.set_token_q_step_count(0)
                player.set_q_token_pos("H")

            if player.get_space_name(player.get_token_q_step_count() + die_roll) == player.get_space_name(player.get_token_p_step_count()):
                player.set_token_q_step_count(player.get_token_q_step_count() + die_roll)
                player.set_token_p_step_count(0)
                player.set_p_token_pos("H")


        if player.get_token_p_step_count() == -1 and player.get_token_q_step_count() == -1:
            pass

            if player.get_token_p_step_count() >= 0 and player.get_token_q_step_count() == -1:
                player.get_token_p_step_count(player.get_token_p_step_count() + die_roll)

            if player.get_token_q_step_count() >= 0 and player.get_token_p_step_count() == -1:
                player.get_token_q_step_count(player.get_token_q_step_count() + die_roll)

            if player.get_token_p_step_count() > 0 and player.get_token_q_step_count() == -1:
                player.get_token_q_step_count(player.get_token_q_step_count() + die_roll)

            else:
                if player.get_token_p_step_count() < 0 and player.get_token_q_step_count() == -1:
                    player.get_token_p_step_count(player.get_token_p_step_count() + die_roll)

    def play_game(self, player_list, turns_list):
        """method takes two parameters, the players list, and the turns list."""

        for player in player_list:
            player = Player(player)
            self._players_list.append(player)

        for turns in turns_list:
            print(turns)
            player_letter = turns[8]
            token_steps = turns[1]
            player = self.get_player_by_position(player_letter)
            token = self.priority_rule(token_steps, player)
            self.move_token(player, token, token_steps)

            moves = []

            for player_letter in self.players_list:
                moves += player_letter.get_p_token_pos() + player_letter. get_q_token_pos()
            print(moves)


class Player():
    """object represents the player who plays the game at a certain position"""

    def __init__(self, position, start_space, end_space, p_token_pos, q_token_pos, player_state, token_steps, player_list, player_letter):

        self._position = position #player "A", "B", "C", "D"
        self._start_space = start_space #"H" home
        self._end_space = end_space #"E" end
        self._p_token_pos = p_token_pos  #current pos
        self._q_token_pos = q_token_pos #current pos
        self._player_state = player_state # won and done or still playing
        self._token_steps = token_steps  #moves
        self._player_list = player_list
        self._player_letter = player_letter

        self._token = ["p", "q"]
        self._position = position
        if position == "A":
            self._start_space = 1
            self._end_space = 50
        if position == "B":
            self._start_space = 15
            self._end_space = 8
        if position == "C":
            self._start_space = 29
            self._end_space = 22
        if position == "D":
            self._start_space = 43
            self._end_space = 36
        else:
            self._position = position

    def get_position(self):
        return self._position

    def get_player_list(self):
        return self._player_list

    def set_player_list(self, player_list):
        self._player_list = player_list

    def get_start_space(self):
        return self._start_space

    def get_p_token_pos(self):
        return self._p_token_pos

    def get_q_token_pos(self):
        return self._q_token_pos

    def set_p_token_pos(self, p_token_pos):
        self._p_token_pos = p_token_pos

    def set_q_token_pos(self, q_token_pos):
        self._q_token_pos = q_token_pos

    def get_player_state(self):
        return self._player_state

    def set_player_state(self, _player_state):
        self._player_state = _player_state

    def get_completed(self):
        """takes no parameters and returns True or False if the player has finished or not finished the game"""
        if self._player_state == "playing":
            return False
        if self._player_state == "finished":
            return True

    def get_token_p_step_count(self):
        """takes no parameters and returns the total steps the token p has taken on the board"""
        return self.get_token_p_step_count(int())

    def get_token_q_step_count(self):
        """takes no parameters and returns the total steps the token q has taken on the board"""
        return self.get_token_q_step_count(int())

    def set_token_p_step_count(self, p_step_count):
        self.set_token_p_step_count = p_step_count

    def set_token_q_step_count(self, q_step_count):
        self.set_token_q_step_count = q_step_count

    def get_space_name(self, total_steps):
        """takes as a parameter the total steps of the token and returns the name of the space the token has
        landed on the board as a string."""
        if total_steps < -1 or total_steps >= 58:
            return "invalid"
        if total_steps == -1:
            return "H"
        if total_steps == 0:
            return "R"
        if total_steps == 1:
            return self._start_space
        if total_steps == 57:
            return "E"
        if 50 < total_steps <= 56:
            return self._position + str(total_steps - 50)
        if 0 < total_steps <57:
            mod = (total_steps + self._start_space) % 56
            return str(mod)


# players = ['A', 'B']
# turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
# game = LudoGame()
# current_tokens_space = game.play_game(players, turns)
# player_A = game.get_player_by_position('A')
# print(player_A.get_completed())
# print(player_A.get_token_p_step_count())
# print(current_tokens_space)
# player_B = game.get_player_by_position('B')
# print(player_B.get_space_name(55))

# And the output will be:
# False
# 28
# [‘28’, ‘28’, ‘21’, ‘H’]
# B5