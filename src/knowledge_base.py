"""Base de Conhecimento e Motor de Inferência Experta.

Implementa o KnowledgeEngine com 38 regras SE-ENTÃO estruturadas em camadas
de encadeamento para frente (forward chaining):
- Camada 2: Dedução de indicadores intermediários
- Camada 3: Pontuação cruzada por trilha
- Camada 4: Regras de desambiguação crítica
- Camada 5: Decisão final determinística e fallback
"""

from typing import Dict, List, Any, Optional
from src.compat import *  # noqa: F401, F403
from experta import KnowledgeEngine, Rule, AND, OR, NOT, TEST, MATCH, L
from src.facts import PerfilUsuario, Indicador, Pontuacao, RegraDisparada, Recomendacao
from src.trilhas import ORDEM_CANONICA, TRILHAS

# Catálogo descritivo e metadados oficiais de cada regra para justificativa legível
REGRAS_METADADOS: Dict[str, Dict[str, Any]] = {
    # Camada 2: Indicadores
    "IND_01": {
        "nome": "Indicador: Perfil Analítico e IA",
        "camada": "Indicadores",
        "justificativa": "Matemática avançada combinada com interesse explícito em Inteligência Artificial deduz forte aptidão analítica.",
    },
    "IND_02": {
        "nome": "Indicador: Perfil de Infraestrutura e Automação",
        "camada": "Indicadores",
        "justificativa": "Interesse marcante em automação, contêineres ou rotinas operacionais deduz vocação para sustentação de sistemas.",
    },
    "IND_03": {
        "nome": "Indicador: Perfil de Experiência do Usuário (UI/UX)",
        "camada": "Indicadores",
        "justificativa": "Preferência por interfaces visuais ou produtos entregues diretamente ao usuário final deduz vocação para experiência interativa.",
    },
    "IND_04": {
        "nome": "Indicador: Perfil de Negócios e Liderança",
        "camada": "Indicadores",
        "justificativa": "Alta habilidade interpessoal somada à busca por impacto no negócio deduz forte orientação para liderança de produtos.",
    },
    "IND_05": {
        "nome": "Indicador: Perfil de Defesa e Segurança Cibernética",
        "camada": "Indicadores",
        "justificativa": "Mentalidade investigativa e defensiva voltada a vulnerabilidades deduz perfil nato de proteção cibernética.",
    },
    "IND_06": {
        "nome": "Indicador: Perfil de Qualidade e Prevenção de Falhas",
        "camada": "Indicadores",
        "justificativa": "Rigor metódico com detalhes e detecção proativa de bugs deduz perfil voltado a testes e confiabilidade de software.",
    },
    # Camada 3: Pontuação por trilha
    "R_BACKEND_CORE": {
        "nome": "Back-end: Núcleo de Lógica e APIs",
        "camada": "Trilha",
        "trilha": "backend",
        "pontos": 40,
        "justificativa": "Atuação centrada em regras de negócio e APIs combinada com preferência pela lógica invisível no servidor.",
    },
    "R_BACKEND_TECH": {
        "nome": "Back-end: Pilha Tecnológica de Servidor",
        "camada": "Trilha",
        "trilha": "backend",
        "pontos": 25,
        "justificativa": "Afinidade com linguagens consolidadas de servidor (Java, C# ou Python) operando em ambientes web e servidores.",
    },
    "R_FRONTEND_CORE": {
        "nome": "Front-end: Núcleo Visual e Interatividade",
        "camada": "Trilha",
        "trilha": "frontend",
        "pontos": 40,
        "justificativa": "Atuação dedicada a layouts e interfaces com foco na entrega do produto visual interativo ao usuário.",
    },
    "R_FRONTEND_TECH": {
        "nome": "Front-end: Ecossistema Web Moderno",
        "camada": "Trilha",
        "trilha": "frontend",
        "pontos": 30,
        "justificativa": "Domínio da tríade e ecossistema Web (JavaScript/TypeScript, frameworks reativos e plataforma Web).",
    },
    "R_DATA_SCIENCE_CORE": {
        "nome": "Ciência de Dados: Núcleo Analítico e Modelagem",
        "camada": "Trilha",
        "trilha": "ciencia_dados",
        "pontos": 45,
        "justificativa": "Perfil matemático com foco na extração de conclusões, hipóteses estatísticas e treino de modelos de Machine Learning.",
    },
    "R_DATA_SCIENCE_PYTHON": {
        "nome": "Ciência de Dados: Linguagem Python e Análise",
        "camada": "Trilha",
        "trilha": "ciencia_dados",
        "pontos": 30,
        "justificativa": "Atuação com análise de dados brutos utilizando a principal linguagem e ecossistema do ecossistema de Data Science.",
    },
    "R_DATA_ENG_CORE": {
        "nome": "Engenharia de Dados: Núcleo de Pipelines e ETL",
        "camada": "Trilha",
        "trilha": "engenharia_dados",
        "pontos": 45,
        "justificativa": "Foco prioritário na construção de fluxos de dados em larga escala, pipelines de ETL/ELT e Data Lakes.",
    },
    "R_DATA_ENG_TECH": {
        "nome": "Engenharia de Dados: Tecnologias e Infraestrutura de Dados",
        "camada": "Trilha",
        "trilha": "engenharia_dados",
        "pontos": 30,
        "justificativa": "Afinidade com SQL, Linux e sustentação confiável de infraestruturas que movimentam grandes volumes de dados.",
    },
    "R_SECURITY_CORE": {
        "nome": "Cibersegurança: Núcleo de Proteção e Blindagem",
        "camada": "Trilha",
        "trilha": "ciberseguranca",
        "pontos": 45,
        "justificativa": "Vocação defensiva comprovada e desejo primordial de garantir blindagem do sistema contra invasões.",
    },
    "R_SECURITY_TECH": {
        "nome": "Cibersegurança: Fundamentos em Linux e Redes",
        "camada": "Trilha",
        "trilha": "ciberseguranca",
        "pontos": 30,
        "justificativa": "Domínio de redes e sistemas operacionais Linux em servidores e nuvem, base indispensável para auditoria e ethical hacking.",
    },
    "R_DEVOPS_CORE": {
        "nome": "DevOps: Núcleo de CI/CD e Disponibilidade",
        "camada": "Trilha",
        "trilha": "devops",
        "pontos": 45,
        "justificativa": "Foco prioritário em automatizar a esteira de entrega contínua (CI/CD) com máxima confiabilidade em produção.",
    },
    "R_DEVOPS_AUTOMATION": {
        "nome": "DevOps: Automação e Ferramental de Infra",
        "camada": "Trilha",
        "trilha": "devops",
        "pontos": 30,
        "justificativa": "Entusiasmo por contêineres e automação de operações utilizando Linux, Shell Script ou scripts Python.",
    },
    "R_CLOUD_CORE": {
        "nome": "Cloud: Arquitetura e Escalabilidade Global",
        "camada": "Trilha",
        "trilha": "cloud",
        "pontos": 45,
        "justificativa": "Planejamento estrutural de ambientes em nuvem buscando arquiteturas elásticas, escaláveis e resilientes.",
    },
    "R_CLOUD_PLATFORM": {
        "nome": "Cloud: Ambientes de Provedores em Nuvem",
        "camada": "Trilha",
        "trilha": "cloud",
        "pontos": 25,
        "justificativa": "Preferência expressa por operar em provedores de nuvem pública (AWS/Azure/GCP) com linguagens de backend/infra.",
    },
    "R_MOBILE_CORE": {
        "nome": "Mobile: Desenvolvimento para Dispositivos Móveis",
        "camada": "Trilha",
        "trilha": "mobile",
        "pontos": 45,
        "justificativa": "Atuação especializada na construção de aplicativos nativos ou multiplataforma voltados exclusivamente para smartphones.",
    },
    "R_MOBILE_TECH": {
        "nome": "Mobile: Pilha e Experiência no Celular",
        "camada": "Trilha",
        "trilha": "mobile",
        "pontos": 35,
        "justificativa": "Domínio de tecnologias móveis (Dart/Flutter, Kotlin, Swift ou React Native) com foco na experiência fluida na palma da mão.",
    },
    "R_QA_CORE": {
        "nome": "QA: Prevenção de Falhas e Software Sem Bugs",
        "camada": "Trilha",
        "trilha": "qa",
        "pontos": 45,
        "justificativa": "Perfil minucioso focado na garantia irrestrita de conformidade, qualidade e eliminação de falhas críticas de software.",
    },
    "R_QA_TECH": {
        "nome": "QA: Automação de Suítes de Testes",
        "camada": "Trilha",
        "trilha": "qa",
        "pontos": 30,
        "justificativa": "Atuação prática com rotinas e ferramentas de testes automatizados com linguagens modernas de programação.",
    },
    "R_PRODUCT_CORE": {
        "nome": "Gestão de Produtos: Estratégia e Backlog",
        "camada": "Trilha",
        "trilha": "gestao_produtos",
        "pontos": 45,
        "justificativa": "Perfil de liderança interpessoal focado em definir visão de produto, gerenciar roadmap e alinhar equipes multifuncionais.",
    },
    "R_PRODUCT_STRATEGY": {
        "nome": "Gestão de Produtos: Impacto de Negócio e Stakeholders",
        "camada": "Trilha",
        "trilha": "gestao_produtos",
        "pontos": 30,
        "justificativa": "Habilidade destacada em lidar com pessoas, negócios e métricas orientadas ao sucesso de mercado do produto.",
    },
    # Camada 4: Desambiguações Críticas
    "DES_DS_VS_DE_DS": {
        "nome": "Desambiguação: Ciência de Dados sobre Engenharia",
        "camada": "Desambiguação",
        "trilha": "ciencia_dados",
        "pontos": 35,
        "justificativa": "Diferencial de Ciência de Dados: alta matemática, modelagem preditiva e interesse direto em IA superam a infraestrutura de dados.",
    },
    "DES_DS_VS_DE_DE": {
        "nome": "Desambiguação: Engenharia de Dados sobre Ciência",
        "camada": "Desambiguação",
        "trilha": "engenharia_dados",
        "pontos": 35,
        "justificativa": "Diferencial de Engenharia de Dados: prioridade clara para construção de pipelines e data lakes sobre a modelagem preditiva.",
    },
    "DES_FRONT_VS_MOBILE_M": {
        "nome": "Desambiguação: Mobile sobre Front-end Web",
        "camada": "Desambiguação",
        "trilha": "mobile",
        "pontos": 30,
        "justificativa": "Foco exclusivo em ecossistema mobile e apps para smartphones supera o desenvolvimento para navegadores web.",
    },
    "DES_FRONT_VS_MOBILE_F": {
        "nome": "Desambiguação: Front-end Web sobre Mobile",
        "camada": "Desambiguação",
        "trilha": "frontend",
        "pontos": 30,
        "justificativa": "Foco na plataforma Web de navegadores supera os requisitos de desenvolvimento nativo para smartphones.",
    },
    "DES_BACK_CLOUD_DEVOPS_D": {
        "nome": "Desambiguação: DevOps sobre Cloud e Back-end",
        "camada": "Desambiguação",
        "trilha": "devops",
        "pontos": 30,
        "justificativa": "Foco contundente em automação contínua de esteiras (CI/CD) sobressai sobre arquitetura em nuvem e código de APIs.",
    },
    "DES_BACK_CLOUD_DEVOPS_C": {
        "nome": "Desambiguação: Cloud sobre DevOps e Back-end",
        "camada": "Desambiguação",
        "trilha": "cloud",
        "pontos": 30,
        "justificativa": "Foco primordial na arquitetura de nuvem pública e governança escalável sobressai sobre automação de deploys e APIs.",
    },
    "DES_BACK_CLOUD_DEVOPS_B": {
        "nome": "Desambiguação: Back-end sobre Cloud e DevOps",
        "camada": "Desambiguação",
        "trilha": "backend",
        "pontos": 30,
        "justificativa": "Foco na escrita de lógica de negócio e APIs sobressai sobre sustentação operacional e infraestrutura em nuvem.",
    },
    "DES_SEC_VS_INFRA_S": {
        "nome": "Desambiguação: Cibersegurança sobre Infraestrutura",
        "camada": "Desambiguação",
        "trilha": "ciberseguranca",
        "pontos": 35,
        "justificativa": "Mentalidade investigativa e de ethical hacking supera a rotina padrão de provisionamento de servidores e nuvem.",
    },
    "DES_QA_VS_BACK_Q": {
        "nome": "Desambiguação: QA sobre Desenvolvimento Back-end",
        "camada": "Desambiguação",
        "trilha": "qa",
        "pontos": 35,
        "justificativa": "Compromisso metódico com detecção de falhas e automação de testes supera o desenvolvimento tradicional de novas APIs.",
    },
    "DES_PROD_VS_FRONT_P": {
        "nome": "Desambiguação: Produto sobre Front-end e Design",
        "camada": "Desambiguação",
        "trilha": "gestao_produtos",
        "pontos": 35,
        "justificativa": "Orientação para estratégia de negócios, métricas e pessoas sobressai sobre a implementação técnica de layouts visuais.",
    },
    # Camada 5: Finalização e Fallback
    "R_DECISAO_FINAL": {
        "nome": "Conclusão Diagnóstica do Sistema Especialista",
        "camada": "Decisão Final",
        "justificativa": "Consolidação de pontuações ponderadas por inferência forward chaining com desempate determinístico.",
    },
    "R_FALLBACK_INICIANTE": {
        "nome": "Recomendação Fundamental de Entrada (Fallback)",
        "camada": "Decisão Final",
        "trilha": "backend",
        "pontos": 10,
        "justificativa": "Para perfis indecisos ou iniciantes, o Desenvolvimento Back-end fornece a melhor base de lógica e bancos de dados.",
    },
}


class ConsultorCarreirasEngine(KnowledgeEngine):
    """Motor de Inferência Baseado em Regras para Orientação Vocacional em TI."""

    def __init__(self):
        super().__init__()
        self.pontuacoes: Dict[str, float] = {t: 0.0 for t in ORDEM_CANONICA}
        self.regras_disparadas: List[Dict[str, Any]] = []
        self.indicadores_gerados: List[str] = []
        self.recomendacao_final: Optional[Dict[str, Any]] = None

    def _pontuar(self, regra_id: str, trilha: str, pontos: float):
        """Registra a pontuação acumulada e o histórico auditável da regra disparada."""
        meta = REGRAS_METADADOS.get(regra_id, {})
        self.pontuacoes[trilha] = self.pontuacoes.get(trilha, 0.0) + pontos
        self.regras_disparadas.append(
            {
                "id": regra_id,
                "nome": meta.get("nome", regra_id),
                "camada": meta.get("camada", "Geral"),
                "trilha": trilha,
                "pontos": pontos,
                "justificativa": meta.get("justificativa", ""),
            }
        )

    # =========================================================================
    # CAMADA 2 — REGRAS DE INDICADORES INTERMEDIÁRIOS (Salience = 10)
    # =========================================================================

    @Rule(
        PerfilUsuario(matematica="Alta", interesse_ia="sim"),
        NOT(Indicador(tipo="perfil_matematico_ia")),
        salience=10,
    )
    def regra_ind_01_matematica_ia(self):
        """Deduz afinidade avançada com modelagem estatística e IA."""
        self.indicadores_gerados.append("perfil_matematico_ia")
        self.declare(Indicador(tipo="perfil_matematico_ia"))
        self.regras_disparadas.append(
            {
                "id": "IND_01",
                "nome": REGRAS_METADADOS["IND_01"]["nome"],
                "camada": "Indicadores",
                "trilha": "ciencia_dados",
                "pontos": 0,
                "justificativa": REGRAS_METADADOS["IND_01"]["justificativa"],
            }
        )

    @Rule(
        PerfilUsuario(atuacao=MATCH.at, interesse_automacao=MATCH.ia),
        TEST(lambda at, ia: at in ["devops_ci_cd", "cloud_infra"] or ia == "sim"),
        NOT(Indicador(tipo="perfil_infra_automacao")),
        salience=10,
    )
    def regra_ind_02_infra_automacao(self):
        """Deduz vocação para operações, contêineres e infraestrutura."""
        self.indicadores_gerados.append("perfil_infra_automacao")
        self.declare(Indicador(tipo="perfil_infra_automacao"))
        self.regras_disparadas.append(
            {
                "id": "IND_02",
                "nome": REGRAS_METADADOS["IND_02"]["nome"],
                "camada": "Indicadores",
                "trilha": "devops/cloud",
                "pontos": 0,
                "justificativa": REGRAS_METADADOS["IND_02"]["justificativa"],
            }
        )

    @Rule(
        PerfilUsuario(atuacao=MATCH.at, entrega=MATCH.en),
        TEST(lambda at, en: at in ["frontend_ui", "mobile_apps"] or en in ["produto_visual", "experiencia_mobile"]),
        NOT(Indicador(tipo="perfil_experiencia_usuario")),
        salience=10,
    )
    def regra_ind_03_experiencia_usuario(self):
        """Deduz afinidade direta com interfaces e interação humana."""
        self.indicadores_gerados.append("perfil_experiencia_usuario")
        self.declare(Indicador(tipo="perfil_experiencia_usuario"))
        self.regras_disparadas.append(
            {
                "id": "IND_03",
                "nome": REGRAS_METADADOS["IND_03"]["nome"],
                "camada": "Indicadores",
                "trilha": "frontend/mobile",
                "pontos": 0,
                "justificativa": REGRAS_METADADOS["IND_03"]["justificativa"],
            }
        )

    @Rule(
        PerfilUsuario(habilidades_gestao="alta", entrega="impacto_negocio"),
        NOT(Indicador(tipo="perfil_negocio_lideranca")),
        salience=10,
    )
    def regra_ind_04_negocio_lideranca(self):
        """Deduz vocação para liderança funcional e visão corporativa."""
        self.indicadores_gerados.append("perfil_negocio_lideranca")
        self.declare(Indicador(tipo="perfil_negocio_lideranca"))
        self.regras_disparadas.append(
            {
                "id": "IND_04",
                "nome": REGRAS_METADADOS["IND_04"]["nome"],
                "camada": "Indicadores",
                "trilha": "gestao_produtos",
                "pontos": 0,
                "justificativa": REGRAS_METADADOS["IND_04"]["justificativa"],
            }
        )

    @Rule(
        PerfilUsuario(rigor_qualidade=MATCH.rq, atuacao=MATCH.at),
        TEST(lambda rq, at: rq == "defensivo_seguranca" or at == "seguranca_defesa"),
        NOT(Indicador(tipo="perfil_defesa_cibernetica")),
        salience=10,
    )
    def regra_ind_05_defesa_cibernetica(self):
        """Deduz mentalidade focada em proteção de ativos e ethical hacking."""
        self.indicadores_gerados.append("perfil_defesa_cibernetica")
        self.declare(Indicador(tipo="perfil_defesa_cibernetica"))
        self.regras_disparadas.append(
            {
                "id": "IND_05",
                "nome": REGRAS_METADADOS["IND_05"]["nome"],
                "camada": "Indicadores",
                "trilha": "ciberseguranca",
                "pontos": 0,
                "justificativa": REGRAS_METADADOS["IND_05"]["justificativa"],
            }
        )

    @Rule(
        PerfilUsuario(rigor_qualidade=MATCH.rq, atuacao=MATCH.at),
        TEST(lambda rq, at: rq == "critico_bugs" or at == "qa_testes"),
        NOT(Indicador(tipo="perfil_qualidade_assegurada")),
        salience=10,
    )
    def regra_ind_06_qualidade_assegurada(self):
        """Deduz mentalidade cirúrgica focada em prevenção e detecção de bugs."""
        self.indicadores_gerados.append("perfil_qualidade_assegurada")
        self.declare(Indicador(tipo="perfil_qualidade_assegurada"))
        self.regras_disparadas.append(
            {
                "id": "IND_06",
                "nome": REGRAS_METADADOS["IND_06"]["nome"],
                "camada": "Indicadores",
                "trilha": "qa",
                "pontos": 0,
                "justificativa": REGRAS_METADADOS["IND_06"]["justificativa"],
            }
        )

    # =========================================================================
    # CAMADA 3 — REGRAS CRUZADAS DE PONTUAÇÃO POR TRILHA (Salience = 0)
    # =========================================================================

    # 1. Desenvolvimento Back-end
    @Rule(
        PerfilUsuario(atuacao="backend_api", entrega="logica_invisivel"),
        salience=0,
    )
    def r_backend_core(self):
        self._pontuar("R_BACKEND_CORE", "backend", 40.0)

    @Rule(
        PerfilUsuario(linguagem=MATCH.lg, plataforma=MATCH.pl),
        TEST(lambda lg, pl: lg in ["java_csharp", "python"] and pl in ["web", "servidores"]),
        salience=0,
    )
    def r_backend_tech(self):
        self._pontuar("R_BACKEND_TECH", "backend", 25.0)

    # 2. Desenvolvimento Front-end & UI/UX
    @Rule(
        PerfilUsuario(atuacao="frontend_ui", entrega="produto_visual"),
        salience=0,
    )
    def r_frontend_core(self):
        self._pontuar("R_FRONTEND_CORE", "frontend", 40.0)

    @Rule(
        PerfilUsuario(linguagem="javascript", plataforma="web"),
        salience=0,
    )
    def r_frontend_tech(self):
        self._pontuar("R_FRONTEND_TECH", "frontend", 30.0)

    # 3. Ciência de Dados e Machine Learning
    @Rule(
        Indicador(tipo="perfil_matematico_ia"),
        PerfilUsuario(foco_dados="modelagem_insights"),
        salience=0,
    )
    def r_data_science_core(self):
        self._pontuar("R_DATA_SCIENCE_CORE", "ciencia_dados", 45.0)

    @Rule(
        PerfilUsuario(atuacao="ciencia_dados_analise", linguagem="python"),
        salience=0,
    )
    def r_data_science_python(self):
        self._pontuar("R_DATA_SCIENCE_PYTHON", "ciencia_dados", 30.0)

    # 4. Engenharia de Dados
    @Rule(
        PerfilUsuario(atuacao="engenharia_dados_etl", foco_dados="pipelines_infra"),
        salience=0,
    )
    def r_data_eng_core(self):
        self._pontuar("R_DATA_ENG_CORE", "engenharia_dados", 45.0)

    @Rule(
        PerfilUsuario(linguagem=MATCH.lg, entrega="infra_dados"),
        TEST(lambda lg: lg in ["sql", "python", "linux_redes"]),
        salience=0,
    )
    def r_data_eng_tech(self):
        self._pontuar("R_DATA_ENG_TECH", "engenharia_dados", 30.0)

    # 5. Cibersegurança (Security / Pentesting)
    @Rule(
        Indicador(tipo="perfil_defesa_cibernetica"),
        PerfilUsuario(entrega="blindagem_seguranca"),
        salience=0,
    )
    def r_security_core(self):
        self._pontuar("R_SECURITY_CORE", "ciberseguranca", 45.0)

    @Rule(
        PerfilUsuario(linguagem="linux_redes", plataforma=MATCH.pl),
        TEST(lambda pl: pl in ["servidores", "nuvem"]),
        salience=0,
    )
    def r_security_tech(self):
        self._pontuar("R_SECURITY_TECH", "ciberseguranca", 30.0)

    # 6. DevOps & SRE
    @Rule(
        PerfilUsuario(atuacao="devops_ci_cd", entrega="deploy_confiavel"),
        salience=0,
    )
    def r_devops_core(self):
        self._pontuar("R_DEVOPS_CORE", "devops", 45.0)

    @Rule(
        PerfilUsuario(interesse_automacao="sim", linguagem=MATCH.lg),
        TEST(lambda lg: lg in ["linux_redes", "python"]),
        salience=0,
    )
    def r_devops_automation(self):
        self._pontuar("R_DEVOPS_AUTOMATION", "devops", 30.0)

    # 7. Computação em Nuvem (Cloud Architecture)
    @Rule(
        PerfilUsuario(atuacao="cloud_infra", entrega="escalabilidade_nuvem"),
        salience=0,
    )
    def r_cloud_core(self):
        self._pontuar("R_CLOUD_CORE", "cloud", 45.0)

    @Rule(
        PerfilUsuario(plataforma="nuvem", linguagem=MATCH.lg),
        TEST(lambda lg: lg in ["linux_redes", "java_csharp", "python"]),
        salience=0,
    )
    def r_cloud_platform(self):
        self._pontuar("R_CLOUD_PLATFORM", "cloud", 25.0)

    # 8. Desenvolvimento Mobile
    @Rule(
        PerfilUsuario(atuacao="mobile_apps", plataforma="mobile"),
        salience=0,
    )
    def r_mobile_core(self):
        self._pontuar("R_MOBILE_CORE", "mobile", 45.0)

    @Rule(
        PerfilUsuario(linguagem=MATCH.lg, entrega="experiencia_mobile"),
        TEST(lambda lg: lg in ["dart_mobile", "javascript"]),
        salience=0,
    )
    def r_mobile_tech(self):
        self._pontuar("R_MOBILE_TECH", "mobile", 35.0)

    # 9. Engenharia de Qualidade e Testes (QA)
    @Rule(
        Indicador(tipo="perfil_qualidade_assegurada"),
        PerfilUsuario(entrega="software_sem_bugs"),
        salience=0,
    )
    def r_qa_core(self):
        self._pontuar("R_QA_CORE", "qa", 45.0)

    @Rule(
        PerfilUsuario(atuacao="qa_testes", linguagem=MATCH.lg),
        TEST(lambda lg: lg in ["python", "javascript", "java_csharp"]),
        salience=0,
    )
    def r_qa_tech(self):
        self._pontuar("R_QA_TECH", "qa", 30.0)

    # 10. Gestão de Produtos (Product Management)
    @Rule(
        Indicador(tipo="perfil_negocio_lideranca"),
        PerfilUsuario(atuacao="gestao_produto"),
        salience=0,
    )
    def r_product_core(self):
        self._pontuar("R_PRODUCT_CORE", "gestao_produtos", 45.0)

    @Rule(
        PerfilUsuario(habilidades_gestao="alta", entrega="impacto_negocio"),
        salience=0,
    )
    def r_product_strategy(self):
        self._pontuar("R_PRODUCT_STRATEGY", "gestao_produtos", 30.0)

    # =========================================================================
    # CAMADA 4 — REGRAS DE DESAMBIGUAÇÃO CRÍTICA (Salience = 20)
    # =========================================================================

    @Rule(
        PerfilUsuario(interesse_ia="sim", matematica="Alta", foco_dados="modelagem_insights"),
        salience=20,
    )
    def des_ds_vs_de_ds(self):
        """Desambiguação DS x DE: Favorece Ciência de Dados se houver alta matemática e modelagem."""
        self._pontuar("DES_DS_VS_DE_DS", "ciencia_dados", 35.0)

    @Rule(
        PerfilUsuario(foco_dados="pipelines_infra", atuacao="engenharia_dados_etl", interesse_ia=MATCH.ia),
        TEST(lambda ia: ia != "sim"),
        salience=20,
    )
    def des_ds_vs_de_de(self):
        """Desambiguação DS x DE: Favorece Engenharia de Dados com pipelines e ausência de foco em IA pura."""
        self._pontuar("DES_DS_VS_DE_DE", "engenharia_dados", 35.0)

    @Rule(
        PerfilUsuario(plataforma="mobile", atuacao="mobile_apps"),
        salience=20,
    )
    def des_front_vs_mobile_mobile(self):
        """Desambiguação Front x Mobile: Favorece Mobile quando a plataforma é celular nativo."""
        self._pontuar("DES_FRONT_VS_MOBILE_M", "mobile", 30.0)

    @Rule(
        PerfilUsuario(plataforma="web", atuacao="frontend_ui"),
        salience=20,
    )
    def des_front_vs_mobile_front(self):
        """Desambiguação Front x Mobile: Favorece Front-end quando a plataforma prioritária é Web."""
        self._pontuar("DES_FRONT_VS_MOBILE_F", "frontend", 30.0)

    @Rule(
        PerfilUsuario(interesse_automacao="sim", atuacao="devops_ci_cd"),
        salience=20,
    )
    def des_back_cloud_devops_devops(self):
        """Desambiguação Back x Cloud x DevOps: Favorece DevOps por esteiras de deploy e CI/CD."""
        self._pontuar("DES_BACK_CLOUD_DEVOPS_D", "devops", 30.0)

    @Rule(
        PerfilUsuario(plataforma="nuvem", atuacao="cloud_infra", interesse_automacao=MATCH.ia),
        TEST(lambda ia: ia != "sim"),
        salience=20,
    )
    def des_back_cloud_devops_cloud(self):
        """Desambiguação Back x Cloud x DevOps: Favorece Cloud por arquitetura em nuvem global."""
        self._pontuar("DES_BACK_CLOUD_DEVOPS_C", "cloud", 30.0)

    @Rule(
        PerfilUsuario(atuacao="backend_api", entrega="logica_invisivel"),
        salience=20,
    )
    def des_back_cloud_devops_backend(self):
        """Desambiguação Back x Cloud x DevOps: Favorece Back-end por lógica invisível de negócio."""
        self._pontuar("DES_BACK_CLOUD_DEVOPS_B", "backend", 30.0)

    @Rule(
        PerfilUsuario(rigor_qualidade="defensivo_seguranca", atuacao="seguranca_defesa"),
        salience=20,
    )
    def des_sec_vs_infra_seguranca(self):
        """Desambiguação Segurança x Infraestrutura: Favorece Cibersegurança por perfil defensivo."""
        self._pontuar("DES_SEC_VS_INFRA_S", "ciberseguranca", 35.0)

    @Rule(
        PerfilUsuario(rigor_qualidade="critico_bugs", atuacao="qa_testes"),
        salience=20,
    )
    def des_qa_vs_back_qa(self):
        """Desambiguação QA x Back-end: Favorece QA por rigor de qualidade e testes contínuos."""
        self._pontuar("DES_QA_VS_BACK_Q", "qa", 35.0)

    @Rule(
        PerfilUsuario(habilidades_gestao="alta", atuacao="gestao_produto"),
        salience=20,
    )
    def des_prod_vs_front_produto(self):
        """Desambiguação Produto x Front/UX: Favorece Produto por visão gerencial e pessoas."""
        self._pontuar("DES_PROD_VS_FRONT_P", "gestao_produtos", 35.0)

    # =========================================================================
    # CAMADA 5 — DECISÃO FINAL E FALLBACK (Salience <= -50)
    # =========================================================================

    @Rule(
        salience=-50,
    )
    def regra_final_selecao_recomendacao(self):
        """Consolida as pontuações e extrai deterministicamente a trilha vencedora."""
        maior_pontuacao = max(self.pontuacoes.values()) if self.pontuacoes else 0.0

        if maior_pontuacao > 0:
            # Desempate determinístico pela ORDEM_CANONICA
            trilha_vencedora = next(
                t for t in ORDEM_CANONICA if self.pontuacoes[t] == maior_pontuacao
            )
            ranking = [
                {
                    "id": t,
                    "nome": TRILHAS[t]["nome"],
                    "pontos": self.pontuacoes[t],
                    "icone": TRILHAS[t]["icone"],
                    "resumo": TRILHAS[t]["resumo"],
                }
                for t in sorted(
                    ORDEM_CANONICA,
                    key=lambda t: (-self.pontuacoes[t], ORDEM_CANONICA.index(t)),
                )
            ]

            regras_especificas = [
                r for r in self.regras_disparadas
                if r.get("trilha") == trilha_vencedora or r.get("camada") == "Indicadores"
            ]

            self.recomendacao_final = {
                "trilha_id": trilha_vencedora,
                "trilha_nome": TRILHAS[trilha_vencedora]["nome"],
                "trilha_dados": TRILHAS[trilha_vencedora],
                "pontuacao": maior_pontuacao,
                "ranking": ranking,
                "regras_disparadas": self.regras_disparadas,
                "motivos_principais": regras_especificas,
                "is_fallback": False,
            }
            self.declare(
                Recomendacao(
                    trilha=trilha_vencedora,
                    pontos=maior_pontuacao,
                    ranking=ranking,
                )
            )

    @Rule(
        salience=-100,
    )
    def regra_final_fallback_iniciante(self):
        """Fallback caso nenhuma regra tenha acumulado pontos (perfil vago/iniciante)."""
        if self.recomendacao_final is None or max(self.pontuacoes.values()) == 0.0:
            trilha_fallback = "backend"
            self._pontuar("R_FALLBACK_INICIANTE", trilha_fallback, 10.0)

            ranking = [
                {
                    "id": t,
                    "nome": TRILHAS[t]["nome"],
                    "pontos": self.pontuacoes[t],
                    "icone": TRILHAS[t]["icone"],
                    "resumo": TRILHAS[t]["resumo"],
                }
                for t in sorted(
                    ORDEM_CANONICA,
                    key=lambda t: (-self.pontuacoes[t], ORDEM_CANONICA.index(t)),
                )
            ]

            self.recomendacao_final = {
                "trilha_id": trilha_fallback,
                "trilha_nome": TRILHAS[trilha_fallback]["nome"],
                "trilha_dados": TRILHAS[trilha_fallback],
                "pontuacao": 10.0,
                "ranking": ranking,
                "regras_disparadas": self.regras_disparadas,
                "motivos_principais": self.regras_disparadas,
                "is_fallback": True,
            }
            self.declare(
                Recomendacao(
                    trilha=trilha_fallback,
                    pontos=10.0,
                    ranking=ranking,
                )
            )
