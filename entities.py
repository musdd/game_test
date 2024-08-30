import classes

#### ATTACK ####

slash = classes.attack(name="Slash", type="Attack", use=classes.attack.slash, cost=1, desc=f"Slashes for {6} damage", effect=None, damage=6, playable=True)
bash = classes.attack(name="Bash", type="Attack", use=classes.attack.bash, cost=2, desc=f"Bashes for {4} damage and stuns for 1 turn", effect=None, damage=4, playable=True)

##### SKILL #####

block = classes.skill(name="Block",type="Skill", use=classes.skill.block, cost=1, desc=f"Gains {6} defense", effect=6, playable=True)

######   STATUS CARD  ######

wound = classes.status_card(name="Wound", type="Status_card", use=None, cost=0, desc="Wounded. Loses 1 life if in hand", effect=None, playable=False)

# burn

#####  STATUS #####

#####  BUFFS  #####

## INTENSITY

## DURATION


###### DEBUFFS #######
poison = classes.debuff(name="Poison", type="debuff", use=classes.debuff.poison, duration=None, intensity=None, stack=[])

## DEBUFF DURATION

shackled = classes.debuff(name="Shackled", type="debuff", use=classes.debuff.shackled, duration=3, intensity=None, stack=["duration"])

###### CURSE ######


##### PLAYER #####

char = classes.player(name="Nobody",maxhp=100,hp=100,max_energy=4,energy=4,
            cards=[slash,slash,slash,slash,slash,block,block,block,block,bash,wound,wound],
            defense=0,status_effects=[shackled],is_alive=True, gold=99, draw_strength=5,
            is_shackled=True)
