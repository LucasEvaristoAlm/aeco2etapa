# Consultor de Carreiras em TI
### Sistema Especialista Baseado em Regras com Motor Experta e Interface Streamlit

Trabalho prático da disciplina de Inteligência Artificial do curso de Ciência da Computação da UNIPAC Barbacena.

---

## 1. Descricao do Projeto

O sistema consiste em um classificador vocacional baseado em regras de producao (SE-ENTAO) que avalia o perfil de um usuario e recomenda uma entre 10 trilhas profissionais de Tecnologia da Informacao.

A solucao utiliza encadeamento para frente (forward chaining) implementado com a biblioteca Experta. A inferencia opera sobre os fatos coletados em um questionario estruturado, deduz indicadores intermediarios, aplica regras de pontuacao ponderada, resolve ambiguidades entre perfis semelhantes e seleciona deterministicamente a trilha mais adequada, fornecendo a justificativa por meio do historico das regras disparadas.

---

## 2. Escopo das 10 Trilhas Profissionais

O sistema avalia e diferencia as seguintes 10 trilhas:

| ID | Trilha | Escopo de Atuacao |
|---|---|---|
| `backend` | Desenvolvimento Back-end | Logica de negocio em servidores, construcao de APIs RESTful/GraphQL e persistencia em bancos de dados relacionais e NoSQL. |
| `frontend` | Desenvolvimento Front-end & UI/UX | Desenvolvimento de interfaces web, usabilidade, acessibilidade e consumo de servicos via frameworks reativos. |
| `ciencia_dados` | Ciencia de Dados e Machine Learning | Analise exploratoria, inferencia estatistica, modelagem preditiva e treino de algoritmos de aprendizado de maquina. |
| `engenharia_dados` | Engenharia de Dados | Construcao de pipelines de extracao e carga (ETL/ELT), arquitetura de Data Lakes e sustentacao de dados em larga escala. |
| `ciberseguranca` | Ciberseguranca (Security / Pentesting) | Analise de vulnerabilidades, auditoria de seguranca, testes de invasao, criptografia aplicada e defesa de redes. |
| `devops` | DevOps & SRE | Automacao de esteiras de integracao e entrega continua (CI/CD), orquestracao de conteineres e confiabilidade de sistemas. |
| `cloud` | Computacao em Nuvem (Cloud Architecture) | Planejamento, migracao e dimensionamento de infraestruturas distribuidas em provedores como AWS, Azure e GCP. |
| `mobile` | Desenvolvimento Mobile | Construcao de aplicativos para dispositivos moveis (Android e iOS) em ambientes nativos ou multiplataforma. |
| `qa` | Engenharia de Qualidade e Testes (QA) | Planejamento e execucao de suites de testes automatizados (unitarios, integracao e ponta a ponta), prevencao de regressoes e analise de conformidade. |
| `gestao_produtos` | Gestao de Produtos (Product Management) | Definicao de estrategia de produto, priorizacao de backlog, alinhamento com stakeholders e aplicacao de metodologias ageis. |

---

## 3. Arquitetura e Fluxo de Inferencia

O projeto foi dividido em modulos independentes para desacoplar a interface grafica do motor de inferencia:

```
consultor-carreiras-ti/
├── README.md                   # Documentacao tecnica do projeto
├── requirements.txt            # Dependencias do ambiente
├── .gitignore                  # Arquivos desconsiderados pelo Git
├── app.py                      # Interface grafica em Streamlit
├── docs/
│   └── matriz_decisao.md       # Matriz de regras e condicoes de ativacao
├── src/
│   ├── __init__.py             # Inicializacao do pacote com import do patch
│   ├── compat.py               # Compatibilidade da Experta com Python 3.10+
│   ├── facts.py                # Definicao das classes de fatos (Fact)
│   ├── trilhas.py              # Catalogo de metadados das trilhas
│   ├── questions.py            # Definicao das perguntas e opcoes da entrevista
│   ├── knowledge_base.py       # KnowledgeEngine contendo as 38 regras @Rule
│   └── engine_runner.py        # Ponto de entrada da inferencia e validacao de dados
└── tests/
    ├── __init__.py
    ├── test_personas.py        # Testes automatizados com 10 personas
    └── test_regras.py          # Testes de cobertura de regras, desambiguacao e fallback
```

### Estrutura da Base de Conhecimento em Camadas

A inferencia ocorre em 5 etapas sequenciais organizadas por niveis de prioridade (salience):

1. **Camada 1 (Fatos de Entrada):** Os dados preenchidos no questionario sao encapsulados na instancia de `PerfilUsuario(...)` e declarados na memoria de trabalho.
2. **Camada 2 (Indicadores Intermediarios, salience=10):** Regras avaliam combinacoes de atributos e declaram fatos intermediarios (`Indicador`), reduzindo acoplamento e facilitando a reutilizacao de premissas logicas.
3. **Camada 3 (Regras de Pontuacao por Trilha, salience=0):** Regras cruzadas combinam indicadores e respostas diretas para atribuir pontos as trilhas correspondentes. Cada trilha possui ao menos duas regras associadas.
4. **Camada 4 (Desambiguacao Critica, salience=20):** Regras com prioridade mais alta atuam especificamente para resolver sobreposicoes entre trilhas com caracteristicas proximas:
   - Ciencia de Dados vs. Engenharia de Dados (diferencia pelo objetivo de modelagem preditiva e nivel de matematica versus construcao de pipelines de ETL e SQL);
   - Front-end vs. Mobile (diferencia pela plataforma web versus celular);
   - Back-end vs. Cloud vs. DevOps (diferencia foco em regras de negocio/APIs versus arquitetura em nuvem versus esteiras de deploy CI/CD);
   - Ciberseguranca vs. Infraestrutura (diferencia mentalidade investigativa de ameacas versus operacao);
   - QA vs. Back-end (diferencia rotina de testes sistematicos versus desenvolvimento de novas funcoes);
   - Gestao de Produtos vs. Front-end (diferencia articulacao de negocio/pessoas versus implementacao de interfaces).
5. **Camada 5 (Decisao e Fallback, salience=-50 e -100):** Com salience negativa, consolida a pontuacao final. Em caso de empate, utiliza a ordem de precedencia definida no catalogo. Caso o questionario seja submetido sem combinacoes conclusivas, a regra de fallback atribui a trilha de Back-end com justificativa documentada.

---

## 4. Nota de Compatibilidade da Biblioteca Experta (Python 3.10+)

A biblioteca `experta` (versao 1.9.4) acessa classes abstratas diretamente pelo modulo `collections`. A partir do Python 3.10 (e confirmado no Python 3.12), essas classes foram movidas para `collections.abc`, o que gera erro de `AttributeError` em tempo de execucao.

Para contornar essa incompatibilidade sem modificar os fontes internos do pacote, o modulo `src/compat.py` reatribui os identificadores necessarios antes de qualquer importacao do motor:

```python
import collections
import collections.abc

for name in ("Mapping", "MutableMapping", "Sequence", "MutableSequence", "Iterable", "Callable", "Container", "Hashable", "Sized", "Set", "MutableSet"):
    if not hasattr(collections, name) and hasattr(collections.abc, name):
        setattr(collections, name, getattr(collections.abc, name))
```

O arquivo `src/__init__.py` importa esse modulo automaticamente, garantindo que o patch esteja sempre ativo nas rotinas de inferencia, testes e aplicacao web.

---

## 5. Requisitos e Instalacao

### Requisitos
- Python 3.10 ou superior (ambiente validado no Python 3.12.3)
- Gerenciador de pacotes pip

### Procedimento

1. Clonar ou descompactar o repositorio e navegar ate a raiz do projeto:
   ```bash
   cd consultor-carreiras-ti
   ```

2. Criar e ativar o ambiente virtual:
   - Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - Windows (CMD):
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate.bat
     ```

3. Instalar os pacotes necessarios:
   ```bash
   pip install -r requirements.txt
   ```

---

## 6. Execucao da Aplicacao

Com o ambiente virtual ativado, executar:

```bash
streamlit run app.py
```

O servidor local ficara disponivel em `http://localhost:8501`.

---

## 7. Execucao dos Testes Automatizados

Os testes estao implementados em pytest e cobrem tanto a integridade da base de regras quanto a avaliacao de personas representativas para cada uma das 10 trilhas:

```bash
pytest -v -s
```

### Personas Validadas nos Testes

| Persona | Perfil Resumido | Trilha Esperada | Trilha Obtida | Resultado |
|---|---|---|---|---|
| Marina | Matematica alta, foco em estatistica e modelos preditivos, Python | Ciencia de Dados e ML | ciencia_dados | Aprovado |
| Lucas | Redes, Linux, analise de vulnerabilidades e defesa contra ataques | Ciberseguranca | ciberseguranca | Aprovado |
| Camila | Criacao de layouts visuais, usabilidade e JavaScript em ambiente web | Front-end & UI/UX | frontend | Aprovado |
| Rodrigo | Habilidades interpessoais altas, priorizacao de backlog e estrategia | Gestao de Produtos | gestao_produtos | Aprovado |
| Bruno | Logica de servico, APIs e bancos de dados em Java/C# | Desenvolvimento Back-end | backend | Aprovado |
| Beatriz | Construcao de pipelines ETL, SQL e infraestrutura de Data Lakes | Engenharia de Dados | engenharia_dados | Aprovado |
| Thiago | Automacao operacional, esteiras CI/CD, conteineres e Linux | DevOps & SRE | devops | Aprovado |
| Gabriel | Dimensionamento de servicos em nuvem pública (AWS), resiliencia | Computacao em Nuvem | cloud | Aprovado |
| Juliana | Construcao de aplicativos moveis em Dart/Flutter | Desenvolvimento Mobile | mobile | Aprovado |
| Felipe | Rigor com cenarios extremos, testes automatizados e prevencao de falhas | Engenharia de QA & Testes | qa | Aprovado |

---

## 8. Resumo da Base de Regras

- Regras de Indicadores (Camada 2): 6
- Regras de Pontuacao Direta (Camada 3): 20 (2 regras por trilha)
- Regras de Desambiguacao (Camada 4): 10
- Regras de Conclusao e Fallback (Camada 5): 2
- **Total de metodos @Rule:** 38 regras implementadas em `ConsultorCarreirasEngine`.
