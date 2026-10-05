from __future__ import annotations

IDADE_MINIMA_EVA: int = 16

class ClassificadorEva:

    @staticmethod
    def calcular_indice_maturidade(
        n1: float,
        n2: float,
        n3: float,
        pesos: tuple[float, float, float] = (2.0, 3.0, 5.0),
    ) -> float:
        for i, nota in enumerate([n1, n2, n3], start=1):
            if not isinstance(nota, (int, float)) or isinstance(nota, bool):
                raise TypeError(f"A pontuação {i} deve ser um número.")
            if not (0.0 <= nota <= 10.0):
                raise ValueError(
                    f"A pontuação {i} deve estar entre 0.0 e 10.0."
                )

        p1, p2, p3 = pesos
        soma_pesos = p1 + p2 + p3
        if soma_pesos <= 0:
            raise ValueError("A soma dos pesos deve ser maior que zero.")

        indice = (n1 * p1 + n2 * p2 + n3 * p3) / soma_pesos
        return round(indice, 2)

    @staticmethod
    def determinar_acesso(indice: float) -> str:
        if not isinstance(indice, (int, float)) or isinstance(indice, bool):
            raise TypeError("O índice deve ser um número.")
        if not (0.0 <= indice <= 10.0):
            raise ValueError("O índice deve estar entre 0.0 e 10.0.")

        if indice >= 7.0:
            return "Acesso Liberado (16+)"
        elif indice >= 4.0:
            return "Acesso com Supervisão"
        else:
            return "Acesso Bloqueado"

    @staticmethod
    def verificar_idade(idade: int) -> str:
        if not isinstance(idade, int) or isinstance(idade, bool):
            raise TypeError("A idade deve ser um número inteiro.")
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")

        return "Pode assistir" if idade >= IDADE_MINIMA_EVA else "Não pode assistir"