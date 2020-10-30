from as_ikea import as_ikea, mapper


def test_abelev_remains():
    ikea_name = as_ikea("Abelev")
    assert ikea_name.startswith("V")
    assert ikea_name[2] == "l"
    assert ikea_name[4] == "b"


def test_abelev_at_least_one_letter_changed():
    ikea_name = as_ikea("Abelev")
    flag = False
    all_letters = [x for key in mapper.keys() for x in mapper[key]]
    for letter in [ikea_name[1], ikea_name[3], ikea_name[5]]:
        if letter in all_letters:
            flag = True                
    assert flag
    
def test_uppercase():
    assert as_ikea("AAA")