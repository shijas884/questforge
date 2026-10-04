from domain.character import Character


def run_special_round(attacker:Character, defender:Character) -> None:
    #works for ANY Character subclass - this is polymoriphism in action
    attacker.special_ability(defender)

def total_party_damage(party:Character,target:Character)-> None:
    for member in party:
      member.attack(target)

    
