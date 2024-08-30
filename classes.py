class player:
    def __init__(self, name, maxhp, hp, max_energy, energy, cards, defense, status_effects, is_alive, gold, draw_strength, is_shackled):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.max_energy = max_energy
        self.energy = energy
        self.cards = cards
        self.defense = defense
        self.status_effects = status_effects
        self.is_alive = is_alive
        self.gold = gold
        self.draw_strength = draw_strength

############### CARDS ######################

class cards:
    card_list = []
    attack_card_list = []
    skill_card_list = []
    def __init__(self, name, type, use, cost, desc, effect,playable):
        self.name = name
        self.type = type
        self.use = use
        self.cost = cost
        self.desc = desc
        self.effect = effect
        self.playable = playable

class attack(cards):
    def __init__(self, name, type, use, cost, desc, damage, effect, playable):
        super().__init__(name, type, use, cost, desc, effect, playable)
        self.damage = damage
        cards.attack_card_list.append(self)
        cards.card_list.append(self)

    def attack_enemy(target, card,):
        card.damage -= card.damage - target.defense
        target.defense -= card.damage
        target.hp -= card.damage
        
    def slash(self, card):
        attack.attack_enemy(self.foe,card)
        print(f"Slashed for {card.damage}")
        self.action = f"Slashed the enemy for {6} Damage"

    def bash(self):
        pass
    
class skill(cards):
    def __init__(self, name, type, use,cost, desc, effect, playable):
        super().__init__(name, type, use, cost, desc, effect, playable)
        cards.skill_card_list.append(self)
        cards.card_list.append(self)

    def block(self,card):
        self.me.defense += card.effect

class status_card(cards):
    def __init__(self, name, type, use, cost, desc, effect, playable):
        super().__init__(name, type, use, cost, desc, effect, playable)

##################### STATUS #########################

class status_effect:
    def __init__(self, name, type, use, duration, intensity, stack):
        self.name = name
        self.type = type
        self.use = use
        self.duration = duration
        self.intensity = intensity


class buff(status_effect):
    def __init__(self, name, type, use, duration, intensity, stack):
        super().__init__(name, type, use, duration, intensity, stack) 

class debuff(status_effect):
    def __init__(self, name, type, use, duration, intensity, stack):
        super().__init__(name, type, use, duration, intensity, stack,)
        self.attack = attack
        self.skill = skill

    def update(self):
        i = 1
        while i > 10000:
            print("test")
            i += 1

    def poison(self, self2):
        pass
    
    def shackled(self,status):
        if status in self.me.status_effects:
            for item in self.deck:  # for every item in my deck that is attack type, change to these settings
                if item.type == "Attack":
                    item.playable == 1
                else:
                    pass
