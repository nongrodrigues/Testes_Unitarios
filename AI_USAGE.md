# Relatório de Transparência — Uso de IA

## 1. Ferramentas Utilizadas
- **IA:** DeepSeek (DeepSeek AI) — modelo DeepSeek Chat (via chat.deepseek.com)
- **IDE:** Visual Studio Code
- **Gerenciador de Dependências:** `uv` (Python 3.14.8)
- **Framework de Testes:** Pytest 9.1.1 + pytest-cov 7.1.0

## 2. Como a IA foi empregada

A Inteligência Artificial foi utilizada como **copiloto técnico**,
nunca como fonte única de verdade. Seu uso se concentrou em três frentes:

- **Especificação de Requisitos (PRD.md):** apoio na estruturação inicial
  das regras de negócio determinísticas do sistema de classificação 16+
  para *Neon Genesis Evangelion* (BR01 – BR04).
- **Implementação do Domínio (SUT — `src/testes_unitarios/neon.py`):**
  auxílio na escrita do código Python com tipagem estática (*Type Hints*)
  e tratamento defensivo de exceções (`ValueError` e `TypeError`).
- **Suíte de Testes (`tests/test_neon.py`):** geração orientada de casos
  parametrizados aplicando as técnicas de **Particionamento de Equivalência
  (EP)**, **Análise do Valor Limite (BVA)** e **Error Guessing**, além do
  padrão AAA (Arrange, Act, Assert).

## 3. Auditoria e Validação Humana

Todo o conteúdo gerado com apoio de IA passou por **revisão humana rigorosa**:

1. **Revisão crítica linha a linha** do SUT e da suíte de testes,
   verificando conformidade com o PRD e com PEP 8.
2. **Execução local via `uv`** dos comandos:
   ```bash
   uv run pytest -v
   uv run pytest --cov=app --cov-branch --cov-report=term-missing