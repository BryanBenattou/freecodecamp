full_dot = '●'
empty_dot = '○'

character_name = ""

# stats
strength = 0
intelligence = 0
charisma = 0

def create_character(character_name, strength, intelligence, charisma):

    # if character isn't string
    if not isinstance(character_name, str):
        return("The character name should be a string")

    # if character name is longer than 10 characters
    if len(character_name) > 10:
        return("The character name is too long")

    # if character name contains spaces
    if " " in character_name:
        return("The character name should not contain spaces")

    # if one more more stats are not integers
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"

   # strength remainder
    strength_remainder = 10 - strength
    strength_remainder_dot = strength_remainder * empty_dot

    # intelligence remainder
    intelligence_remainder = 10 - intelligence
    intelligence_remainder_dot = intelligence_remainder * empty_dot

    # charisma remainder
    charisma_remainder = 10 - charisma
    charisma_remainder_dot = charisma_remainder * empty_dot     

    # if one or more stats are less than 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    # if one or more stats are more than 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    # if sum of all stats is different than 7
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # function return
    else:
        return f"{character_name}\nSTR {strength * full_dot + strength_remainder_dot}\nINT {intelligence * full_dot + intelligence_remainder_dot}\nCHA {charisma * full_dot + charisma_remainder_dot}"
        

print(create_character("ren", 4, 2, 1))        