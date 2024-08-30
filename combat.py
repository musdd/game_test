import os
import random
import entities
import classes as cl

#################################
# ENEMY PLACEHOLDER
class enemy:
    def __init__(self, name, maxhp, hp, defense, intent):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.defense = defense
        self.intent = intent

bot = enemy(name="bot", maxhp=100,hp=100, defense=0,intent=[entities.slash, entities.bash])

#######################################

class combat:
    def __init__(self, me, foe):
        self.me = me
        self.foe = foe
        self.turn_list = [me, foe]
        self.is_turn = True
        self.turn_counter = 0
        self.hand = []
        self.deck = entities.char.cards[:]
        self.discard_pile = []
        self.combat_log = []
        self.action = " "

    def display_fight(self):
            os.system("cls")
            print(f"╔═══════════════════════════════════════════════════════════════════════════════════════╗")
            print(f"║   TURN: {self.turn_counter}                                                                                  ")
            print(f"║                                                                                       ")
            print(f"║                                                                                 ")
            print(f"║ [ {self.me.name.upper()} ] ❤️  : {self.me.maxhp}/{self.me.hp}  | 🛡️  : {self.me.defense}  | 🌟 : {self.me.energy}                                                         ")
            print(f"║                                                                                ")
            print(f"║ ENEMIES                                                                                  ")
            print(f"║ [1] [ CULTIST(placeholder) ] ❤️  : {self.foe.hp}  | 🛡️  : {self.foe.defense} | ATTACKS FOR 6                                                                          ")
            print(f"║                                                                                       ")
            print(f"║                                                                                        ")
            print(f"║                                                                            ")
            print(f"╠═══════════════════════════════════════════════════════════════════════════════════════╣")
            print(f"║ [ E ] END TURN | [ Q ] USE POTION | [ W ] RELICS | [ T ] DISCARD PILE | [ R ]  HELP   ║")
            print(f"║ [ G ]   HELP   |                                                                      ║")
            print("╚═══════════════════════════════════════════════════════════════════════════════════════╝")


###############  CARDS LOGIC  ####################

    def start_turn(self):
        for turn in self.turn_list:
            if turn == self.me and self.is_turn == True:
                self.turn_counter += 1
                self.draw_cards()
                self.me.energy = self.me.max_energy
                self.turn_manager()
            else:
                self.enemy_turn()

    def draw_cards(self, num=entities.char.draw_strength):
        for _ in range(num):
            if not self.deck: # if there are no cards in deck, reshuffle the deck, then get a card.
                self.reshuffle_deck()
                card = self.deck.pop()
                self.hand.append(card)
            else:
                if self.turn_counter == 1: # shuffles the deck if first turn
                    self.reshuffle_deck()
                card = self.deck.pop(0) # gets the first index of the deck
                self.hand.append(card) # appends to the player hand

    #shuffles or reshuffles deck 
    def reshuffle_deck(self):
        random.shuffle(self.deck)
        if not self.deck:
            self.deck.extend(self.discard_pile) # all discard_pile items are transfered to the player deck.
            self.discard_pile.clear() # clears the discard pile

    def play_card(self,card):
        if card.cost > self.me.energy:
            pass
        elif card.playable == False:
            pass
        else:
            card.use(self, card)
            self.me.energy -= card.cost
            card = self.hand.pop(self.hand.index(card))
            self.discard_pile.append(card)

#############     GAME STATE     ################

    def is_dead(self):
        if self.me.hp >= 0:
            self.me.is_alive = False

    def apply_effect(self):
        pass

    def turn_manager(self):
        if "Defend" in self.me.status_effects: # Checks if an effect is in the list.
            pass   
        else:
            self.me.defense = 0

###########################################

        # TODO: Changing the logic of status effects.
 #       for status in self.me.status_effects: # checks for status effects on the play effects list
 #           cll = cl.debuff
#            cll.status.update()

  #          if status.duration == 0: # if duration is less or = than 0, remove that from the list.
  #              self.me.status_effects.remove(status)
        
        self.my_turn()

    def end_turn(self):
        self.turn_list.pop(self)
        self.turn_list.append(self)

#############         COMBAT         ###################



#############         GAME      #####################

    def my_turn(self):
        # put enemy intent here first
        # self.intent()
        while self.is_turn and self.hand and self.me.energy >= 0:
            self.is_dead()
            self.display_fight()

            for item_num, item in enumerate(self.hand): 
                status = None
                if item.playable == False:
                    status = "X"
                elif self.me.energy < item.cost:
                    status = "X"
                else:
                    status = item_num + 1
                print(f" [ { status } ] {item.name}   ({item.cost})    ({item.desc})") 

            # print(f"[ {"X" if self.me.energy < item.cost or item.type == "status_card" else item_num + 1} ] {item.name}       ({item.desc})")   
            print("═════════════════════════════════════════════════════════════════════════════════════════")
            try:
                choice = input("Please choose an operation.\n>: ")
                if choice in {"E", "e"}: # puts the unused cards back to deck
                    self.deck.extend(self.hand)
                    self.hand.clear()
                    self.is_turn = False
                    self.start_turn()
                else:
                    choice = int(choice)
                    event = self.hand[choice - 1]
            except ValueError:
                pass
            except IndexError:
                pass
            else:
                self.play_card(event)
                os.system("cls")
        else:
            self.is_turn = False
            self.start_turn()

    def enemy_turn(self):
        self.is_turn = True
        self.start_turn()

combat_nice = combat(entities.char,bot)
combat_nice.start_turn()
