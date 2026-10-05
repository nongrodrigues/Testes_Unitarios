# Sistema de Classificação de Idade — Neon Genesis Evangelion (16+)

Trabalho prático da disciplina de **Qualidade e Teste de Software (QTS)**.

Sistema que calcula um índice de maturidade ponderado e determina se uma
pessoa pode assistir *Neon Genesis Evangelion* (classificação indicativa
oficial de **16 anos**), aplicando as regras de negócio **BR01–BR04**
descritas no [`PRD.md`](./PRD.md).

---

## 📋 Pré-requisitos

- **Python 3.12+** (recomendado 3.14.x)
- **[uv](https://docs.astral.sh/uv/)** — gerenciador de dependências e ambientes

### Instalar o `uv` (caso ainda não tenha)

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"