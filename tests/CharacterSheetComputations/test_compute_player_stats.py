from app.CharacterSheetComputations import compute_build_mod, compute_damage_bonus, compute_dodge, compute_hobby_skill_points, compute_max_hp, compute_max_mp, compute_max_sanity, compute_move_rate, compute_occupation_skill_points, roll_appearance, roll_constitution, roll_dexterity, roll_education, roll_intelligence, roll_luck, roll_power, roll_size, roll_strength


def test_strength_roll():
    assert 0 < roll_strength() < 100
    
def test_dexterity_roll():
    assert 0 < roll_dexterity() < 100

def test_constitution_roll():
    assert 0 < roll_constitution() < 100

def test_appearance_roll():
    assert 0 < roll_appearance() < 100

def test_power_roll():
    assert 0 < roll_power() < 100
    
def test_size_roll():
    assert 0 < roll_size() < 100
    
def test_education_roll():
    assert 0 < roll_education() < 100
    
def test_intelligence_roll():
    assert 0 < roll_intelligence() < 100
    
def test_luck_roll():
    assert 0 < roll_luck() < 100

def test_compute_max_hp():
    assert 5 == compute_max_hp(35,15)
    
def test_compute_max_sanity():
    assert 87 == compute_max_sanity(12)

def test_compute_max_mp():
    assert 13 == compute_max_mp(65)

def test_compute_move_rate():
    assert 7 == compute_move_rate(40,50,40,20)
    assert 9 == compute_move_rate(70,50,70,20)
    assert 8 == compute_move_rate(70,60,50,20)
    assert 6 == compute_move_rate(60,50,60,60)
    
def test_compute_damage_bonus():
    assert "-2" == compute_damage_bonus(1,1)
    assert "-1" == compute_damage_bonus(30,30)
    assert "0" == compute_damage_bonus(40,42)
    assert "+1D4" == compute_damage_bonus(51,40)
    assert "+1D6" == compute_damage_bonus(82,80)
    assert "+2D6" == compute_damage_bonus(100,103)
    assert "+3D6" == compute_damage_bonus(160,120)
    assert "+4D6" == compute_damage_bonus(153,160)
    assert "+5D6" == compute_damage_bonus(200,210)
    
def test_compute_build_mod():
    assert "-2" == compute_build_mod(1,1)
    assert "-1" == compute_build_mod(30,30)
    assert "0" == compute_build_mod(40,42)
    assert "+1" == compute_build_mod(51,40)
    assert "+2" == compute_build_mod(82,80)
    assert "+3" == compute_build_mod(100,103)
    assert "+4" == compute_build_mod(160,120)
    assert "+5" == compute_build_mod(153,160)
    assert "+6" == compute_build_mod(200,210)

def test_compute_dodge():
    assert 45 == compute_dodge(90)

def test_compute_occupation_skill_points():
    assert 360 == compute_occupation_skill_points(90)
    
def test_compute_hobby_skill_points():
    assert 80 == compute_hobby_skill_points(40)