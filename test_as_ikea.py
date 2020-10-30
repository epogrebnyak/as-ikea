from as_ikea import as_ikea, mapper


def test_abelev_remains():
    ikea_name = as_ikea("Abelev")
    assert ikea_name.startswith("V")
    assert ikea_name[2] == "l"


def test_abelev_changes():
    # change - this fails
    assert ikea_name[-1] in mapper["a"]
    assert ikea_name[1] in mapper["e"]
