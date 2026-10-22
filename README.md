# 🧭 Consultor Inteligente de Carreiras em TI
### Sistema Especialista Baseado em Regras com Motor Experta (Forward Chaining) e Interface Streamlit

> **Atividade Acadêmica:** Inteligência Artificial — Ciência da Computação, UNIPAC Barbacena.

---

## 📌 1. Visão Geral do Projeto

O **Consultor Inteligente de Carreiras em TI** é um sistema especialista fundamentado em regras de produção (SE-ENTÃO) projetado para orientar estudantes e profissionais na escolha da trilha de carreira ideal no vasto mercado de Tecnologia da Informação.

Através de uma **entrevista diagnóstica dinâmica**, o sistema coleta dados sobre afinidade matemática, preferências de rotina diária, ecossistema tecnológico e tipo de entrega de valor preferida. Utilizando um motor de inferência por **encadeamento para frente (*forward chaining*)**, a base de conhecimento processa fatos, gera indicadores intermediários, aplica regras de pontuação cruzada e desambiguação e conclui **exatamente uma recomendação primária**, acompanhada de justificativa transparente (regras disparadas) e ranking completo.

---

## 🎯 2. Escopo: As 10 Trilhas Mapeadas

O sistema diferencia e avalia com precisão as seguintes 10 trilhas profissionais:

| # | Trilha Profissional | Foco e Responsabilidades |
|---|---|---|
| 1 | **⚙️ Desenvolvimento Back-end** | Lógica de servidores, APIs RESTful/GraphQL, regras de negócio e bancos de dados relacionais/NoSQL. |
| 2 | **🎨 Desenvolvimento Front-end & UI/UX** | Interfaces web responsivas, experiência do usuário (UX), acessibilidade e frameworks reativos modernos. |
| 3 | **🧠 Ciência de Dados e Machine Learning** | Estatística inferencial, modelagem preditiva, análise de dados e algoritmos de Inteligência Artificial. |
| 4 | **🚰 Engenharia de Dados** | Arquitetura de dados em larga escala, pipelines de ingestão (ETL/ELT), Data Lakes e data warehouses. |
| 5 | **🛡️ Cibersegurança (Security / Pentesting)** | Defesa cibernética, análise de vulnerabilidades, ethical hacking, criptografia e proteção de redes. |
| 6 | **🚀 DevOps & SRE** | Automação operacional, integração e entrega contínua (CI/CD), contêineres (Docker/K8s) e alta disponibilidade. |
| 7 | **☁️ Computação em Nuvem (Cloud Architecture)** | Planejamento, migração e governança de infraestruturas escaláveis e distribuídas em nuvem (AWS/Azure/GCP). |
| 8 | **📱 Desenvolvimento Mobile** | Ecossistema de dispositivos móveis com desenvolvimento nativo (Kotlin/Swift) ou multiplataforma (Flutter/React Native). |
| 9 | **🧪 Engenharia de Qualidade e Testes (QA)** | Testes automatizados (E2E, integração, carga), prevenção de falhas e garantia de conformidade de software. |
| 10 | **📊 Gestão de Produtos (Product Management)** | Ponte entre negócios, design e desenvolvimento, metodologias ágeis (Scrum/Kanban) e priorização estratégica. |

---

## 🏗️ 3. Arquitetura do Sistema e Estratégia de Inferência

O projeto foi estruturado seguindo os princípios de modularidade, separação estrita de responsabilidades (SOLID) e ausência de lógica de decisão na camada de interface gráfica (`app.py`).

```
consultor-carreiras-ti/
├── README.md                   # Documentação completa e guia de execução
├── requirements.txt            # Dependências com versões estritamente fixadas
├── .gitignore                  # Arquivos ignorados pelo controle de versão Git
├── app.py                      # Interface Web moderna em Streamlit (apenas UI + chamadas)
├── docs/
│   └── matriz_decisao.md       # Fase 1: Matriz formal de regras e condições SE-ENTÃO
├── src/
│   ├── __init__.py             # Inicialização do pacote com patch automático
│   ├── compat.py               # Patch essencial de compatibilidade do Experta em Python 3.10+
│   ├── facts.py                # Fatos Experta: PerfilUsuario, Indicador, Pontuacao, Recomendacao
│   ├── trilhas.py              # Catálogo oficial e metadados das 10 trilhas
│   ├── questions.py            # Catálogo estruturado de perguntas (fonte única para UI e testes)
│   ├── knowledge_base.py       # KnowledgeEngine com 38 regras @Rule em camadas
│   └── engine_runner.py        # Interface desacoplada: recomendar(respostas) -> resultado
└── tests/
    ├── __init__.py
    ├── test_personas.py        # Suíte de validação com 10 personas completas (uma por trilha)
    └── test_regras.py          # Testes de contagem de regras, desambiguações e fallback
```

### Inferência Forward Chaining em 5 Camadas

```
[ Entrevista Diagnóstica ]
           │
           ▼
[ Camada 1: Fato de Entrada: PerfilUsuario(...) ]
           │
           ▼
[ Camada 2: Indicadores Intermediários: Indicador(tipo=...) ] (Salience: 10)
           │
           ▼
[ Camada 3: Regras Cruzadas de Pontuação por Trilha ] (Salience: 0)
           │
           ▼
[ Camada 4: Regras de Desambiguação Crítica ] (Salience: 20)
           │
           ▼
[ Camada 5: Decisão Final Determinística e Fallback ] (Salience: -50 e -100)
           │
           ▼
[ Recomendacao Final + Ranking + Justificativa ]
```

1. **Camada 1 — Fatos de Entrada:** Injeção das respostas do questionário via `PerfilUsuario(...)`.
2. **Camada 2 — Indicadores Intermediários (`salience=10`):** Dedução de fatos derivados (ex: `perfil_matematico_ia`, `perfil_infra_automacao`, `perfil_defesa_cibernetica`, etc.).
3. **Camada 3 — Regras Cruzadas de Pontuação (`salience=0`):** Combinação de respostas e indicadores com operadores lógicos (`AND`, `OR`, `MATCH`, `TEST`, `L`), acumulando pontuações ponderadas.
4. **Camada 4 — Desambiguações Críticas (`salience=20`):** Regras de desempate refinado para fronteiras comuns:
   - **Ciência de Dados × Engenharia de Dados:** Diferenciação por interesse explícito em IA e matemática alta vs. foco em pipelines e ETL.
   - **Front-end × Mobile:** Diferenciação pela plataforma Web vs. celular.
   - **Back-end × Cloud × DevOps:** Separação entre código de APIs, governança em nuvem e automação CI/CD.
   - **Cibersegurança × Infraestrutura:** Diferenciação pela mentalidade de ataque defensivo e auditoria.
   - **QA × Back-end:** Separação entre foco em novas funcionalidades vs. cobertura e prevenção cirúrgica de falhas.
   - **Gestão de Produtos × Front-end:** Separação entre codificação de telas vs. articulação com pessoas e mercado.
5. **Camada 5 — Decisão Final e Fallback (`salience <= -50`):** Escolhe exatamente uma trilha vencedora, desempata deterministicamente pela ordem do catálogo oficial e aplica regra de *fallback* amigável caso o usuário apresente perfil totalmente indeciso.

---

## ⚙️ 4. O Patch de Compatibilidade do Experta (Python 3.10+)

A biblioteca `experta` (versão 1.9.4) foi concebida na vigência de versões anteriores do Python e referencia classes abstratas diretamente a partir do módulo `collections` (em especial via sua dependência `frozendict`). No Python 3.10 e Python 3.12, estas classes foram transferidas definitivamente para `collections.abc`, provocando erros do tipo `AttributeError: module 'collections' has no attribute 'Mapping'`.

Para sanar este comportamento sem alterar a essência da biblioteca original, foi desenvolvido o módulo [`src/compat.py`](file:///home/fycer/Documentos/AECO/src/compat.py), que deve ser importado **antes de qualquer importação da biblioteca `experta`**:

```python
import collections
import collections.abc

for _name in ("Mapping", "MutableMapping", "Sequence", "MutableSequence", "Iterable", "Callable", "Container", "Hashable", "Sized", "Set", "MutableSet"):
    if not hasattr(collections, _name) and hasattr(collections.abc, _name):
        setattr(collections, _name, getattr(collections.abc, _name))
```

---

## 🚀 5. Requisitos e Guia de Instalação

### Pré-requisitos
- **Python 3.10 ou superior** (testado e homologado no Python 3.12.3).
- Gerenciador de pacotes `pip` e utilitário `venv`.

### Passo a Passo

1. **Clone o repositório ou acesse o diretório do projeto:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd consultor-carreiras-ti
   ```

2. **Crie e ative o ambiente virtual:**
   - **No Linux/macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **No Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - **No Windows (Prompt de Comando):**
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate.bat
     ```

3. **Instale as dependências fixadas:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 6. Como Executar a Aplicação Web

Com o ambiente virtual ativado, inicie o servidor Streamlit:

```bash
streamlit run app.py
```

A interface abrirá automaticamente no seu navegador padrão no endereço:
`http://localhost:8501`

---

## 🧪 7. Como Executar a Suíte de Testes Automatizados

Para executar os testes unitários e de integração com cobertura das 10 personas e das regras:

```bash
pytest -v -s
```

### Resultados da Validação com Personas de Teste

Todas as 10 personas foram validadas com 100% de precisão na primeira inferência:

| Persona | Perfil Chave | Trilha Esperada | Trilha Obtida | Status |
|---|---|---|---|---|
| **Persona 1 (Marina)** | Matemática Alta, análise de dados, Python, modelos preditivos, interesse em IA | Ciência de Dados e ML | `ciencia_dados` | ✅ Aprovado |
| **Persona 2 (Lucas)** | Linux/Redes, defesa contra invasões, ethical hacking, rigor defensivo | Cibersegurança | `ciberseguranca` | ✅ Aprovado |
| **Persona 3 (Camila)** | JavaScript, interfaces web reativas, produto visual ao usuário | Front-end & UI/UX | `frontend` | ✅ Aprovado |
| **Persona 4 (Rodrigo)** | Gestão de produto, alta habilidade com pessoas e negócios, impacto de mercado | Gestão de Produtos | `gestao_produtos` | ✅ Aprovado |
| **Persona 5 (Bruno)** | Java/C#, regras de negócio corporativas, APIs de backend e servidores | Desenvolvimento Back-end | `backend` | ✅ Aprovado |
| **Persona 6 (Beatriz)** | SQL, pipelines de ETL/ELT, sustentação de Data Lakes em massa | Engenharia de Dados | `engenharia_dados` | ✅ Aprovado |
| **Persona 7 (Thiago)** | Linux, automação CI/CD, esteiras de deploy contínuo, contêineres | DevOps & SRE | `devops` | ✅ Aprovado |
| **Persona 8 (Gabriel)** | Ambientes em nuvem pública (AWS), arquitetura escalável e resiliente | Computação em Nuvem | `cloud` | ✅ Aprovado |
| **Persona 9 (Juliana)** | Dart/Flutter, ecossistema móvel, experiência fluida no smartphone | Desenvolvimento Mobile | `mobile` | ✅ Aprovado |
| **Persona 10 (Felipe)** | Automação de testes, rigor cirúrgico contra bugs, garantia de conformidade | Engenharia de QA & Testes | `qa` | ✅ Aprovado |

---

## 📊 8. Contagem Formal de Regras

- **Regras de Indicadores Intermediários:** 6 regras
- **Regras Cruzadas de Pontuação por Trilha:** 20 regras (2 por trilha)
- **Regras de Desambiguação Crítica:** 10 regras
- **Regras de Decisão Final e Fallback:** 2 regras
- **Total no `KnowledgeEngine`:** **38 regras `@Rule`** (cumprindo e superando amplamente o requisito de 20–25 regras).

---

## 📦 9. Histórico Sugerido de Commits Git

```bash
git init
git add .gitignore
git commit -m "chore: inicializacao do repositorio e configuracao do .gitignore"

git add docs/matriz_decisao.md
git commit -m "feat: fase 1 - matriz de decisao e engenharia de conhecimento formalizada"

git add src/
git commit -m "feat: fase 2 - base de conhecimento experta com 38 regras e patch de compatibilidade"

git add app.py
git commit -m "feat: fase 3 - interface web interativa em streamlit desacoplada da inferencia"

git add tests/
git commit -m "test: fase 4 - validacao automatizada com 10 personas e integridade do motor"

git add README.md requirements.txt
git commit -m "docs: fase 5 - documentacao completa e dependencias fixadas para entrega"
```
