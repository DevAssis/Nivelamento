from soma import soma


def test_soma_de_dois_numeros():
    resultado = soma(2, 3)

    assert resultado == 5
