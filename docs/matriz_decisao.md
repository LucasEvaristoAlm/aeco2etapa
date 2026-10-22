# Matriz de Decisão do Sistema Especialista: Consultor de Carreiras em TI

Este documento formaliza a engenharia de conhecimento do sistema especialista, mapeando as características capturadas na entrevista dinâmica, os indicadores intermediários inferidos e as regras de produção (SE-ENTÃO) que pontuam e desambiguam as 10 trilhas profissionais de TI.

---

## 1. Visão Geral das 10 Trilhas

| ID Trilha | Nome Oficial | Foco Principal | Sinais Fortes de Ativação |
|---|---|---|---|
| `backend` | **Desenvolvimento Back-end** | Lógica de servidores, APIs RESTful/GraphQL, regras de negócio e bancos de dados. | Atuação com APIs e algoritmos lógicos; linguagem Java/C#/Python; foco na lógica invisível; plataforma web/servidores. |
| `frontend` | **Desenvolvimento Front-end & UI/UX** | Interfaces web responsivas, experiência do usuário (UX), design visual e frameworks reativos. | Atuação com layouts visuais e telas; linguagem JavaScript/TypeScript; valor no produto nas mãos do usuário; plataforma Web. |
| `ciencia_dados` | **Ciência de Dados e Machine Learning** | Estatística avançada, modelagem preditiva, análise de dados e algoritmos de Inteligência Artificial. | Matemática Alta; análise de dados brutos; linguagem Python; interesse explícito em IA/estatística; foco em extrair hipóteses e treinar modelos. |
| `engenharia_dados` | **Engenharia de Dados** | Arquitetura de dados, pipelines de ingestão e transformação (ETL/ELT), Data Lakes e armazéns analíticos. | Atuação com pipelines de dados; linguagem SQL/Python/Linux; foco em infraestrutura de dados em massa; foco em ETL em vez de modelagem preditiva pura. |
| `ciberseguranca` | **Cibersegurança (Security / Pentesting)** | Defesa cibernética, análise de vulnerabilidades, ethical hacking, criptografia e segurança de redes. | Atuação com proteção contra ataques; linguagem Linux/Redes/Bash; valor na blindagem contra invasores; rigor investigativo e defensivo elevado. |
| `devops` | **DevOps & SRE** | Automação operacional, cultura CI/CD, conteinerização (Docker/K8s) e alta confiabilidade de sistemas. | Atuação com deploy automatizado e CI/CD; interesse alto em Docker/Kubernetes/Terraform; linguagem Linux/Bash; valor na velocidade e estabilidade da entrega contínua. |
| `cloud` | **Computação em Nuvem (Cloud Architecture)** | Planejamento, migração, governança e dimensionamento de infraestruturas escaláveis em nuvem (AWS/Azure/GCP). | Atuação com planejamento de ambientes em nuvem; plataforma Ambientes de Nuvem; valor em arquitetura escalável e resiliente; Linux/Redes ou Java/C#. |
| `mobile` | **Desenvolvimento Mobile** | Aplicativos nativos e multiplataforma para smartphones e tablets (Android, iOS, Flutter, React Native). | Plataforma Dispositivos Móveis; atuação com apps de celular; linguagem Dart/Kotlin/Swift ou JavaScript; valor na experiência móvel fluida. |
| `qa` | **Engenharia de Qualidade e Testes (QA)** | Testes automatizados (E2E, unitários, integração), confiabilidade de software e garantia de conformidade. | Atuação com testes e qualidade; rigor crítico/elevado contra bugs; valor na ausência de falhas e conformidade com requisitos; Python/Java/JS. |
| `gestao_produtos` | **Gestão de Produtos (Product Management)** | Ponte entre negócios, design e engenharia; priorização de backlog, estratégia de mercado e metodologias ágeis. | Habilidades de gestão e pessoas Altas; atuação com definição de produto e backlog; valor no sucesso do negócio e satisfação de stakeholders. |

---

## 2. Perguntas da Entrevista e Domínio de Valores

1. **Afinidade Matemática e Estatística (`matematica`)**:
   - `Alta`, `Média`, `Baixa`
2. **Preferência de Atuação Diária (`atuacao`)**:
   - `backend_api`: Escrever lógica de regras de negócio e APIs robustas
   - `frontend_ui`: Criar layouts visuais e interfaces interativas
   - `ciencia_dados_analise`: Analisar dados brutos e criar modelos preditivos
   - `engenharia_dados_etl`: Construir pipelines de ingestão e arquitetura de dados (ETL/ELT)
   - `seguranca_defesa`: Identificar vulnerabilidades e proteger sistemas contra ataques
   - `devops_ci_cd`: Automatizar deploys, pipelines de CI/CD e monitorar confiabilidade
   - `cloud_infra`: Planejar e estruturar ambientes de servidores e serviços em nuvem
   - `mobile_apps`: Desenvolver aplicativos para smartphones e tablets
   - `qa_testes`: Criar planos de testes automatizados e assegurar conformidade
   - `gestao_produto`: Definir estratégia de produto, priorizar backlog e alinhar equipes
3. **Linguagem / Tecnologia de Maior Afinidade (`linguagem`)**:
   - `python`: Python
   - `javascript`: JavaScript / TypeScript
   - `linux_redes`: Linux / Redes / Bash
   - `java_csharp`: Java / C#
   - `sql`: SQL / Bancos de Dados
   - `dart_mobile`: Dart / Kotlin / Swift
   - `iniciante`: Nenhuma / Iniciante
4. **Tipo de Entrega de Valor Preferida (`entrega`)**:
   - `produto_visual`: O produto final diretamente nas mãos do usuário (telas e usabilidade)
   - `logica_invisivel`: A lógica invisível, processamento robusto e APIs estáveis
   - `insights_modelos`: Descobertas estatísticas, gráficos analíticos e modelos preditivos
   - `infra_dados`: A infraestrutura que move grandes volumes de dados confiavelmente
   - `blindagem_seguranca`: A blindagem e garantia de que ninguém conseguirá invadir o sistema
   - `deploy_confiavel`: A velocidade e segurança com que o código chega em produção sem quedas
   - `escalabilidade_nuvem`: A arquitetura escalável e resiliente hospedada na nuvem (AWS/Azure/GCP)
   - `experiencia_mobile`: A experiência na palma da mão com apps rápidos e fluidos
   - `software_sem_bugs`: A certeza de que o software não tem bugs e cumpre todos os requisitos
   - `impacto_negocio`: O sucesso do negócio, impacto no mercado e satisfação dos stakeholders
5. **Plataforma-Alvo Preferida (`plataforma`)**:
   - `web`: Web (Navegadores)
   - `mobile`: Dispositivos Móveis (Android / iOS)
   - `servidores`: Servidores, Terminais e Infraestrutura
   - `nuvem`: Ambientes de Nuvem e Contêineres
   - `dados_negocio`: Não importa / Foco em Dados e Negócio
6. **Interesse em Inteligência Artificial e Modelagem Preditiva (`interesse_ia`)**:
   - `sim`: Sim (Alto interesse em estatística, redes neurais e algoritmos preditivos)
   - `nao`: Não (Prefiro focar em engenharia de software tradicional, infraestrutura ou produtos)
7. **Foco na Manipulação de Dados (`foco_dados`)**:
   - `modelagem_insights`: Extrair conclusões, hipóteses estatísticas e treinar modelos preditivos
   - `pipelines_infra`: Construir pipelines (ETL/ELT), data lakes e arquitetura de dados em massa
   - `nenhum`: Não tenho foco específico em dados massivos
8. **Gosto por Lidar com Pessoas, Negócios e Metodologias Ágeis (`habilidades_gestao`)**:
   - `alta`: Alto (Gosto de comunicação, liderança de produto e visão de mercado)
   - `media`: Médio (Gosto de colaborar em time, mas prefiro foco técnico)
   - `baixa`: Baixo (Prefiro focar puramente em código, infraestrutura ou análise técnica)
9. **Perfil de Detalhismo com Testes, Bugs e Segurança (`rigor_qualidade`)**:
   - `critico_bugs`: Crítico / Elevado (Adoro caçar bugs, validar cenários extremos e garantir estabilidade)
   - `defensivo_seguranca`: Defensivo / Investigativo (Foco em quebrar sistemas para achar brechas de segurança)
   - `equilibrado`: Equilibrado / Padrão de desenvolvimento ágil
10. **Interesse em Automação de Infraestrutura e CI/CD (`interesse_automacao`)**:
    - `sim`: Sim (Fascinado por Docker, Kubernetes, Terraform e automação de deploys)
    - `nao`: Não (Prefiro focar em desenvolvimento de aplicações, dados ou regras de negócio)

---

## 3. Matriz de Regras do Sistema Especialista

### Camada 2 — Regras de Geração de Indicadores Intermediários

| ID Regra | Condição de Ativação | Indicador Gerado | Justificativa |
|---|---|---|---|
| `IND_01` | `matematica == "Alta"` E `interesse_ia == "sim"` | `Indicador(tipo="perfil_matematico_ia")` | Forte aptidão para abordagens analíticas e modelos preditivos baseados em estatística. |
| `IND_02` | `atuacao in ["devops_ci_cd", "cloud_infra"]` OU `interesse_automacao == "sim"` | `Indicador(tipo="perfil_infra_automacao")` | Afinidade natural com operações, escalabilidade e infraestrutura como código. |
| `IND_03` | `atuacao in ["frontend_ui", "mobile_apps"]` OU `entrega in ["produto_visual", "experiencia_mobile"]` | `Indicador(tipo="perfil_experiencia_usuario")` | Foco primordial na experiência direta do usuário e componentes de interface. |
| `IND_04` | `habilidades_gestao == "alta"` E `entrega == "impacto_negocio"` | `Indicador(tipo="perfil_negocio_lideranca")` | Orientação marcante para visão de produto, mercado e articulação com stakeholders. |
| `IND_05` | `rigor_qualidade == "defensivo_seguranca"` OU `atuacao == "seguranca_defesa"` | `Indicador(tipo="perfil_defesa_cibernetica")` | Mentalidade focada em identificar pontos de falha, auditoria e blindagem de ativos. |
| `IND_06` | `rigor_qualidade == "critico_bugs"` OU `atuacao == "qa_testes"` | `Indicador(tipo="perfil_qualidade_assegurada")` | Perfil minucioso direcionado a metodologias de teste, cobertura de código e conformidade. |

---

### Camada 3 — Regras Cruzadas de Pontuação por Trilha

| ID Regra | Condições (Respostas e Indicadores) | Trilha Beneficiada | Pontos | Justificativa |
|---|---|---|---|---|
| `R_BACKEND_CORE` | `atuacao == "backend_api"` E `entrega == "logica_invisivel"` | `backend` | +40 | Alinhamento central com construção de APIs e regras de negócio no servidor. |
| `R_BACKEND_TECH` | `linguagem in ["java_csharp", "python"]` E `plataforma in ["web", "servidores"]` | `backend` | +25 | Domínio de pilhas tecnológicas canônicas para serviços de back-end. |
| `R_FRONTEND_CORE` | `atuacao == "frontend_ui"` E `entrega == "produto_visual"` | `frontend` | +40 | Vocação evidente para criação de interfaces interativas e usabilidade web. |
| `R_FRONTEND_TECH` | `linguagem == "javascript"` E `plataforma == "web"` | `frontend` | +30 | Sintonia direta com o ecossistema Web moderno (JavaScript/TypeScript e frameworks reativos). |
| `R_DATA_SCIENCE_CORE` | `Indicador("perfil_matematico_ia")` E `foco_dados == "modelagem_insights"` | `ciencia_dados` | +45 | Combinação essencial de matemática alta, curiosidade analítica e apetite por machine learning. |
| `R_DATA_SCIENCE_PYTHON` | `atuacao == "ciencia_dados_analise"` E `linguagem == "python"` | `ciencia_dados` | +30 | Emprego da linguagem padrão para ciência de dados e experimentação de modelos preditivos. |
| `R_DATA_ENG_CORE` | `atuacao == "engenharia_dados_etl"` E `foco_dados == "pipelines_infra"` | `engenharia_dados` | +45 | Foco direcionado à arquitetura de fluxos de dados, pipelines distribuídos e ETL/ELT. |
| `R_DATA_ENG_TECH` | `linguagem in ["sql", "python", "linux_redes"]` E `entrega == "infra_dados"` | `engenharia_dados` | +30 | Aliança de modelagem em banco relacional/não-relacional com sustentação de data lakes massivos. |
| `R_SECURITY_CORE` | `Indicador("perfil_defesa_cibernetica")` E `entrega == "blindagem_seguranca"` | `ciberseguranca` | +45 | Vocação prioritária para resguardo de dados críticos, conformidade e contramedidas a ataques. |
| `R_SECURITY_TECH` | `linguagem == "linux_redes"` E `plataforma in ["servidores", "nuvem"]` | `ciberseguranca` | +30 | Base técnica indispensável em protocolos de rede, sistemas operacionais e anatomia de invasões. |
| `R_DEVOPS_CORE` | `atuacao == "devops_ci_cd"` E `entrega == "deploy_confiavel"` | `devops` | +45 | Domínio da esteira de integração e entrega contínua garantindo previsibilidade aos deploys. |
| `R_DEVOPS_AUTOMATION` | `interesse_automacao == "sim"` E `linguagem in ["linux_redes", "python"]` | `devops` | +30 | Paixão por automação de tarefas operacionais, orquestração de contêineres e scripts de infraestrutura. |
| `R_CLOUD_CORE` | `atuacao == "cloud_infra"` E `entrega == "escalabilidade_nuvem"` | `cloud` | +45 | Visão arquitetural orientada a elasticidade, redundância e serviços gerenciados em provedores de nuvem. |
| `R_CLOUD_PLATFORM` | `plataforma == "nuvem"` E `linguagem in ["linux_redes", "java_csharp", "python"]` | `cloud` | +25 | Conexão estreita com dimensionamento de instâncias, VPCs e serviços de computação em nuvem. |
| `R_MOBILE_CORE` | `atuacao == "mobile_apps"` E `plataforma == "mobile"` | `mobile` | +45 | Dedicação exclusiva ao ciclo de vida e particularidades de aplicativos móveis. |
| `R_MOBILE_TECH` | `linguagem in ["dart_mobile", "javascript"]` E `entrega == "experiencia_mobile"` | `mobile` | +35 | Uso de ferramentas especializadas para dispositivos móveis (Flutter, Kotlin, Swift ou React Native). |
| `R_QA_CORE` | `Indicador("perfil_qualidade_assegurada")` E `entrega == "software_sem_bugs"` | `qa` | +45 | Compromisso intransigente com conformidade de requisitos, critérios de aceite e estabilidade. |
| `R_QA_TECH` | `atuacao == "qa_testes"` E `linguagem in ["python", "javascript", "java_csharp"]` | `qa` | +30 | Capacidade de implementar automação de testes de ponta a ponta e pipelines de validação contínua. |
| `R_PRODUCT_CORE` | `Indicador("perfil_negocio_lideranca")` E `atuacao == "gestao_produto"` | `gestao_produtos` | +45 | Aptidão central para liderança funcional, alinhamento de roadmap e visão holística de valor. |
| `R_PRODUCT_STRATEGY`| `habilidades_gestao == "alta"` E `entrega == "impacto_negocio"` | `gestao_produtos` | +30 | Foco estratégico em indicadores de negócio (KPIs/OKRs) e conexão entre time técnico e mercado. |

---

### Camada 4 — Regras de Desambiguação Crítica

Regras projetadas com prioridade (`salience=20`) para desempatar e separar áreas de fronteira comuns na tecnologia:

| ID Regra | Cenário de Ambiguidade | Condições Específicas | Decisão / Trilha Favorecida | Pontos | Justificativa |
|---|---|---|---|---|---|
| `DES_DS_VS_DE_DS` | **DS × DE** | Interesse em IA = `sim` E Matemática = `Alta` E Foco = `modelagem_insights` | `ciencia_dados` | +35 | Desambiguação DS: aprofundamento estatístico e objetivo de modelagem preditiva sobrepõem-se à engenharia de dados. |
| `DES_DS_VS_DE_DE` | **DS × DE** | Foco = `pipelines_infra` E Atuação = `engenharia_dados_etl` E Interesse em IA != `sim` | `engenharia_dados` | +35 | Desambiguação DE: prioridade para construção de infraestrutura e pipelines de ETL, diferenciando-se da modelagem preditiva. |
| `DES_FRONT_VS_MOBILE_M` | **Front-end × Mobile** | Plataforma = `mobile` E Atuação = `mobile_apps` | `mobile` | +30 | Desambiguação Mobile: foco declarado em telas móveis e ecossistemas iOS/Android supera a web tradicional. |
| `DES_FRONT_VS_MOBILE_F` | **Front-end × Mobile** | Plataforma = `web` E Atuação = `frontend_ui` | `frontend` | +30 | Desambiguação Front: foco direcionado a navegadores e ecossistema web moderno supera o desenvolvimento de apps nativos. |
| `DES_BACK_CLOUD_DEVOPS_D` | **Back-end × Cloud × DevOps** | Interesse em automação = `sim` E Atuação = `devops_ci_cd` | `devops` | +30 | Desambiguação DevOps: paixão por automação e CI/CD sobressai sobre a arquitetura pura e o desenvolvimento de regras de negócio. |
| `DES_BACK_CLOUD_DEVOPS_C` | **Back-end × Cloud × DevOps** | Plataforma = `nuvem` E Atuação = `cloud_infra` E Interesse em automação != `sim` | `cloud` | +30 | Desambiguação Cloud: planejamento e sustentação de serviços globais em nuvem sobressaem sobre pipelines de código. |
| `DES_BACK_CLOUD_DEVOPS_B` | **Back-end × Cloud × DevOps** | Atuação = `backend_api` E Entrega = `logica_invisivel` | `backend` | +30 | Desambiguação Back-end: concentração no código de regras de negócio e APIs supera o foco em infraestrutura e operações. |
| `DES_SEC_VS_INFRA_S` | **Segurança × DevOps/Cloud** | Rigor qualidade = `defensivo_seguranca` E Atuação = `seguranca_defesa` | `ciberseguranca` | +35 | Desambiguação Segurança: mentalidade orientada a pentest, ameaças e vulnerabilidades distingue-se da sustentação de infraestrutura. |
| `DES_QA_VS_BACK_Q` | **QA × Back-end** | Rigor qualidade = `critico_bugs` E Atuação = `qa_testes` | `qa` | +35 | Desambiguação QA: obstinação por cobertura de testes e prevenção de falhas sobrepõe-se à criação de novas funcionalidades de backend. |
| `DES_PROD_VS_FRONT_P` | **Produto × Front-end/UX** | Habilidades gestão = `alta` E Atuação = `gestao_produto` | `gestao_produtos` | +35 | Desambiguação Produto: ênfase em estratégia, métricas e pessoas sobrepõe-se à codificação visual de interfaces. |

---

### Camada 5 — Regras de Finalização e Fallback

| ID Regra | Salience | Condição | Ação | Justificativa |
|---|---|---|---|---|
| `R_DECISAO_FINAL` | `-50` | Pontuação calculada para as trilhas | Identifica a trilha com maior pontuação (desempate determinístico pela ordem canônica de catálogo) | Seleciona e declara `Recomendacao(trilha=..., pontuacao=..., ranking=..., motivos=[...])`. |
| `R_FALLBACK_INICIANTE`| `-100` | Nenhuma regra acumulou pontuação (todas opções nulas/indecisas) | Atribui pontuação à trilha `backend` como trilha-mãe fundamental | Fornece orientação segura como base fundamental de lógica para quem está iniciando e indeciso. |

---

## 4. Total de Regras Planejadas no KnowledgeEngine

- Indicadores intermediários: **6 regras**
- Pontuação cruzada de trilhas: **20 regras**
- Desambiguação crítica: **10 regras**
- Finalização e Fallback: **2 regras**
- **Total:** **38 regras lógicas `@Rule`**, garantindo cobertura completa das 10 trilhas e margem robusta acima do requisito de 20–25 regras.
