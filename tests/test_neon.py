import pytest

from testes_unitarios.neon import ClassificadorEva


@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3, pesos, esperado",
    [
        (10.0, 10.0, 10.0, (1.0, 1.0, 1.0), 10.0),
        (0.0, 0.0, 0.0, (1.0, 1.0, 1.0), 0.0),
        (5.0, 5.0, 5.0, (1.0, 1.0, 1.0), 5.0),
        (7.0, 8.0, 9.0, (2.0, 3.0, 5.0), 8.3),
        (6.9, 6.9, 6.9, (2.0, 3.0, 5.0), 6.9),
        (7.0, 7.0, 7.0, (2.0, 3.0, 5.0), 7.0),
    ],
)
def test_calcular_indice_maturidade_sucesso(n1, n2, n3, pesos, esperado):
    resultado = ClassificadorEva.calcular_indice_maturidade(n1, n2, n3, pesos)
    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3, esperado",
    [
        (7.0, 7.0, 7.0, "Acesso Liberado (16+)"),
        (7.1, 7.1, 7.1, "Acesso Liberado (16+)"),
        (6.9, 6.9, 6.9, "Acesso com Supervisão"),
        (4.0, 4.0, 4.0, "Acesso com Supervisão"),
        (4.1, 4.1, 4.1, "Acesso com Supervisão"),
        (3.9, 3.9, 3.9, "Acesso Bloqueado"),
        (10.0, 10.0, 10.0, "Acesso Liberado (16+)"),
        (0.0, 0.0, 0.0, "Acesso Bloqueado"),
    ],
)
def test_determinar_acesso_limites(n1, n2, n3, esperado):
    indice = ClassificadorEva.calcular_indice_maturidade(n1, n2, n3)
    acesso = ClassificadorEva.determinar_acesso(indice)
    assert acesso == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3",
    [
        (-0.1, 5.0, 5.0),
        (10.1, 5.0, 5.0),
        (5.0, -1.0, 5.0),
        (5.0, 11.0, 5.0),
        (5.0, 5.0, -0.01),
        (5.0, 5.0, 10.01),
    ],
)
def test_error_guessing_pontuacoes_fora_do_intervalo(n1, n2, n3):
    with pytest.raises(ValueError):
        ClassificadorEva.calcular_indice_maturidade(n1, n2, n3)


@pytest.mark.unit
@pytest.mark.parametrize(
    "n1, n2, n3",
    [
        ("10", 5.0, 5.0),
        (5.0, None, 5.0),
        (5.0, 5.0, [5.0]),
        (True, 5.0, 5.0),
    ],
)
def test_error_guessing_tipos_invalidos(n1, n2, n3):
    with pytest.raises(TypeError):
        ClassificadorEva.calcular_indice_maturidade(n1, n2, n3)


@pytest.mark.unit
def test_error_guessing_pesos_negativos():
    with pytest.raises(ValueError):
        ClassificadorEva.calcular_indice_maturidade(
            5.0, 5.0, 5.0, pesos=(-1.0, -1.0, -1.0)
        )


@pytest.mark.unit
def test_error_guessing_pesos_soma_zero():
    with pytest.raises(ValueError):
        ClassificadorEva.calcular_indice_maturidade(
            5.0, 5.0, 5.0, pesos=(0.0, 0.0, 0.0)
        )


@pytest.mark.unit
@pytest.mark.parametrize("indice_invalido", [-0.1, 10.1])
def test_error_guessing_indice_fora_intervalo(indice_invalido):
    with pytest.raises(ValueError):
        ClassificadorEva.determinar_acesso(indice_invalido)


@pytest.mark.unit
@pytest.mark.parametrize("indice_invalido", ["7.0", None, True])
def test_error_guessing_indice_tipo_invalido(indice_invalido):
    with pytest.raises(TypeError):
        ClassificadorEva.determinar_acesso(indice_invalido)


@pytest.mark.unit
@pytest.mark.parametrize(
    "idade, esperado",
    [
        (15, "Não pode assistir"),
        (16, "Pode assistir"),
        (17, "Pode assistir"),
        (0, "Não pode assistir"),
        (100, "Pode assistir"),
    ],
)
def test_verificar_idade_limites(idade, esperado):
    resultado = ClassificadorEva.verificar_idade(idade)
    assert resultado == esperado


@pytest.mark.unit
@pytest.mark.parametrize("idade_invalida", [-1, -100])
def test_error_guessing_idade_negativa(idade_invalida):
    with pytest.raises(ValueError):
        ClassificadorEva.verificar_idade(idade_invalida)


@pytest.mark.unit
@pytest.mark.parametrize("idade_invalida", ["16", None, 16.5, True])
def test_error_guessing_idade_tipo_invalido(idade_invalida):
    with pytest.raises(TypeError):
        ClassificadorEva.verificar_idade(idade_invalida)