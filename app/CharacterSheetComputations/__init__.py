
import math
import re

def parse_equation(input:str) -> list :
    r = re.compile('([()+-/*D])')
    parsed_list = r.split(input)
    parsed_list = [i for i in parsed_list if i != '']
    return parsed_list

def roll_strength(d6_1: int, d6_2: int, d6_3: int) -> int:
    """Roll for Character Strength Stat. Equation is 3d6*5.
    
    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6
        d6_3 (int): third D6

    Returns:
        int: Character Strength Stat result.
    """
    
    return (d6_1 + d6_2 + d6_3)*5

def roll_dexterity(d6_1: int, d6_2: int, d6_3: int) -> int:
    """Roll for Character Dexterity Stat. Equation is 3d6*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6
        d6_3 (int): third D6

    Returns:
        int: Character Dexterity Stat result.
    """
    return (d6_1 + d6_2 + d6_3)*5

def roll_constitution(d6_1: int, d6_2: int, d6_3: int) -> int:
    """Roll for Character Constitution Stat. Equation is 3d6*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6
        d6_3 (int): third D6

    Returns:
        int: Character Constitution Stat result.
    """
    return (d6_1 + d6_2 + d6_3)*5

def roll_appearance(d6_1: int, d6_2: int, d6_3: int) -> int:
    """Roll for Character Appearance Stat. Equation is 3d6*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6
        d6_3 (int): third D6

    Returns:
        int: Character Appearance Stat result.
    """
    return (d6_1 + d6_2 + d6_3)*5

def roll_power(d6_1: int, d6_2: int, d6_3: int) -> int:
    """Roll for Character Power Stat. Equation is 3d6*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6
        d6_3 (int): third D6

    Returns:
        int: Character Power Stat result.
    """
    return (d6_1 + d6_2 + d6_3)*5

def roll_size(d6_1: int, d6_2: int) -> int:
    """Roll for Character Size Stat. Equation is (2d6+6)*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6

    Returns:
        int: Character Size Stat result.
    """
    return ((d6_1 + d6_2)+6)*5

def roll_education(d6_1: int, d6_2: int) -> int:
    """Roll for Character Education Stat. Equation is (2d6+6)*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6

    Returns:
        int: Character Education Stat result.
    """
    return ((d6_1 + d6_2)+6)*5

def roll_intelligence(d6_1: int, d6_2: int) -> int:
    """Roll for Character Intelligence Stat. Equation is (2d6+6)*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6

    Returns:
        int: Character Intelligence Stat result.
    """
    return ((d6_1 + d6_2)+6)*5

def roll_luck(d6_1: int, d6_2: int, d6_3: int) -> int:
    """Roll for Character Luck Stat. Equation is 3d6*5.

    Args:
        d6_1 (int): first D6
        d6_2 (int): second D6
        d6_3 (int): third D6

    Returns:
        int: Character Luck Stat result.
    """
    return (d6_1 + d6_2 + d6_3)*5

def compute_max_hp(constitution: int, size: int) -> int:
    """Character health points. Computed via round_down((con + siz)/10).

    Args:
        constitution (int): constitution stat
        size (int): size stat

    Returns:
        int: Health Points value
    """
    return math.floor((constitution + size) / 10)

def compute_max_sanity(mythos: int) -> int:
    """Maximum sanity. Computed via 99-mythos.

    Args:
        mythos (int): mythos knowledge

    Returns:
        int: Maximum Sanity value
    """
    return 99-mythos

def compute_max_mp(power: int) -> int:
    """Maximum Magic Points. Computed via POW/5.

    Args:
        power (int): power stat

    Returns:
        int: Maximum Magic Points value
    """
    return power/5

def compute_move_rate(dexterity: int, size: int, strength: int, age: int) -> int:
    """Move Rate. This value is usually 7-9. Computed by comparing dexterity, strength and size then scaled by age.

    Args:
        dexterity (int): dexterity stat
        size (int): size stat
        strength (int): strength stat
        age (int): character age

    Returns:
        int: This is the move rate per turn of the character.
    """
    if dexterity < size and strength < size:
        return 7 - max(math.floor(age / 10) - 3, 0)
    elif strength > size and dexterity > size:
        return 9 - max(math.floor(age / 10) - 3, 0)
    else:
        return 8 - max(math.floor(age / 10) - 3, 0)
    
def compute_damage_bonus(strength: int, size: int) -> str:
    """Damage Bonus Modifier. This is computed based on strength and size and is scaled based on a map of dice rolls.

    Args:
        strength (int): strength stat
        size (int): size stat

    Returns:
        str: This is the damage bonus modifier string.
    """
    damage_bonus_comp  = strength + size
    match damage_bonus_comp:
        case damage_bonus_comp if 0 < damage_bonus_comp <= 2:
            return "-2"
        case damage_bonus_comp if 2 < damage_bonus_comp <= 65:
            return "-1"
        case damage_bonus_comp if 65 < damage_bonus_comp <= 85:
            return "0"
        case damage_bonus_comp if 85 < damage_bonus_comp <= 125:
            return "+1D4"
        case damage_bonus_comp if 125 < damage_bonus_comp <= 165:
            return "+1D6"
        case damage_bonus_comp if 165 < damage_bonus_comp <= 205:
            return "+2D6"
        case damage_bonus_comp if 205 < damage_bonus_comp <= 285:
            return "+3D6"
        case damage_bonus_comp if 285 < damage_bonus_comp <= 365:
            return "+4D6"
        case damage_bonus_comp if 365 < damage_bonus_comp <= 445:
            return "+5D6"
    
def compute_build_mod(strength: int, size: int) -> str:
    """Build Modifier. This is computed based on strength and size and is scaled based on a map of modifiers.

    Args:
        strength (int): strength stat
        size (int): size stat

    Returns:
        str: This is the build modifier string.
    """
    build_comp  = strength + size
    match build_comp:
        case build_comp if 0 < build_comp <= 2:
            return "-2"
        case build_comp if 2 < build_comp <= 65:
            return "-1"
        case build_comp if 65 < build_comp <= 85:
            return "0"
        case build_comp if 85 < build_comp <= 125:
            return "+1"
        case build_comp if 125 < build_comp <= 165:
            return "+2"
        case build_comp if 165 < build_comp <= 205:
            return "+3"
        case build_comp if 205 < build_comp <= 285:
            return "+4"
        case build_comp if 285 < build_comp <= 365:
            return "+5"
        case build_comp if 365 < build_comp <= 445:
            return "+6"
    
def compute_dodge(dexterity: int) -> int:
    """Dodge Stat. This is computed by round_down(DEX/2).

    Args:
        dexterity (int): dexterity stat

    Returns:
        int: This determines the dodge stat of your character
    """
    return math.floor(dexterity/2)

def compute_occupation_skill_points(education: int) -> int:
    """Occupation Skill Points. Spend this on job skills. Computation is EDU*4.

    Args:
        education (int): education stat

    Returns:
        int: Occupation Skill Points to spend on Job Skills.
    """
    return education * 4

def compute_hobby_skill_points(intelligence: int) -> int:
    """Hobby Skill Points. Spend this on hobby and miscellaneous skills. Computation is INT*2.

    Args:
        intelligence (int): intelligence stat

    Returns:
        int: Hobby Skill Points to spend on hobby or miscellaneous skills.
    """
    return intelligence * 2