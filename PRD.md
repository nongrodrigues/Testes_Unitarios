# Product Requirements Document (PRD)
## Sistema de Classificação de Idade — Neon Genesis Evangelion

### 1. Visão Geral
Sistema que determina se uma pessoa pode assistir Neon Genesis Evangelion
(classificação: 16 anos) com base em um índice de maturidade ponderado.

### 2. Regras de Negócio

#### BR01: Validação de Intervalo das Pontuações
- N1, N2, N3 ∈ [0.0, 10.0]
- Fora do intervalo → ValueError | Tipo inválido → TypeError

#### BR02: Pesos das Avaliações
- Pesos padrão: (2.0, 3.0, 5.0)
- Soma dos pesos deve ser > 0 → senão ValueError

#### BR03: Índice de Maturidade Ponderado
- Fórmula: (N1·2 + N2·3 + N3·5) / 10
- Arredondado para 2 casas decimais

#### BR04: Classificação de Acesso
- Acesso Liberado (16+):  índice ≥ 7.0
- Acesso com Supervisão:  4.0 ≤ índice < 7.0
- Acesso Bloqueado:       índice < 4.0