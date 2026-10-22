"""Catálogo único e estruturado das perguntas da entrevista diagnóstica.

Serve como fonte da verdade compartilhada para a interface Streamlit e suíte de testes.
"""

from typing import List, Dict, Any

PERGUNTAS: List[Dict[str, Any]] = [
    {
        "id": "matematica",
        "categoria": "Dimensões Essenciais",
        "obrigatoria": True,
        "titulo": "1. Afinidade Matemática e Estatística",
        "ajuda": "Indique seu nível de conforto com cálculos, fórmulas, álgebra linear e probabilidade.",
        "opcoes": [
            {
                "valor": "Alta",
                "rotulo": "Alta — Gosto muito de modelos estatísticos, probabilidades e formulações matemáticas",
            },
            {
                "valor": "Média",
                "rotulo": "Média — Lógica formal e álgebra básica me atendem bem para programar",
            },
            {
                "valor": "Baixa",
                "rotulo": "Baixa — Prefiro atividades intuitivas, visuais ou de organização prática",
            },
        ],
    },
    {
        "id": "atuacao",
        "categoria": "Dimensões Essenciais",
        "obrigatoria": True,
        "titulo": "2. Preferência de Atuação Diária",
        "ajuda": "Qual tipo de desafio técnico mais te entusiasma na rotina de trabalho?",
        "opcoes": [
            {
                "valor": "backend_api",
                "rotulo": "Escrever regras de negócio, algoritmos lógicos e construir APIs robustas",
            },
            {
                "valor": "frontend_ui",
                "rotulo": "Criar layouts visuais, interfaces reativas e aprimorar a experiência do usuário (UX)",
            },
            {
                "valor": "ciencia_dados_analise",
                "rotulo": "Analisar dados brutos, encontrar padrões estatísticos e treinar modelos preditivos de IA",
            },
            {
                "valor": "engenharia_dados_etl",
                "rotulo": "Construir pipelines de ingestão de dados em larga escala (ETL/ELT) e Data Lakes",
            },
            {
                "valor": "seguranca_defesa",
                "rotulo": "Auditar vulnerabilidades, proteger contra ataques e simular invasões éticas",
            },
            {
                "valor": "devops_ci_cd",
                "rotulo": "Automatizar deploys contínuos (CI/CD), contêineres e garantir disponibilidade de sistemas",
            },
            {
                "valor": "cloud_infra",
                "rotulo": "Planejar e arquitetar servidores escaláveis, resiliência e redes em provedores de nuvem (AWS/Azure/GCP)",
            },
            {
                "valor": "mobile_apps",
                "rotulo": "Construir aplicativos fluidos e dinâmicos para smartphones e tablets",
            },
            {
                "valor": "qa_testes",
                "rotulo": "Desenvolver testes automatizados rigorosos para caçar bugs e garantir software sem falhas",
            },
            {
                "valor": "gestao_produto",
                "rotulo": "Definir visão estratégica de produto, priorizar backlog e liderar pelo alinhamento de equipes",
            },
        ],
    },
    {
        "id": "linguagem",
        "categoria": "Dimensões Essenciais",
        "obrigatoria": True,
        "titulo": "3. Linguagem ou Ferramenta de Maior Afinidade Atual",
        "ajuda": "Qual ecossistema tecnológico você se sente mais confiante ou tem maior interesse em dominar?",
        "opcoes": [
            {
                "valor": "python",
                "rotulo": "Python (análise de dados, scripts, IA, APIs modernas)",
            },
            {
                "valor": "javascript",
                "rotulo": "JavaScript / TypeScript (navegadores, React, Node.js, apps)",
            },
            {
                "valor": "linux_redes",
                "rotulo": "Linux, Shell Script / Bash, Redes e Ferramentas de Terminal",
            },
            {
                "valor": "java_csharp",
                "rotulo": "Java ou C# / .NET (orientação a objetos corporativa, robustez e microsserviços)",
            },
            {
                "valor": "sql",
                "rotulo": "SQL / Bancos de Dados Relacionais e NoSQL",
            },
            {
                "valor": "dart_mobile",
                "rotulo": "Dart (Flutter), Kotlin (Android) ou Swift (iOS)",
            },
            {
                "valor": "iniciante",
                "rotulo": "Nenhuma / Iniciante (ainda estou definindo meu ponto de partida)",
            },
        ],
    },
    {
        "id": "entrega",
        "categoria": "Dimensões Essenciais",
        "obrigatoria": True,
        "titulo": "4. Tipo de Entrega de Valor Preferida",
        "ajuda": "O que te dá maior sensação de realização ao ver um projeto concluído?",
        "opcoes": [
            {
                "valor": "produto_visual",
                "rotulo": "O produto final interativo visível na tela e usado diretamente pelas pessoas",
            },
            {
                "valor": "logica_invisivel",
                "rotulo": "A lógica invisível nos bastidores: processamento ágil, APIs estáveis e dados bem guardados",
            },
            {
                "valor": "insights_modelos",
                "rotulo": "Descobertas quantitativas, previsões estatísticas e inteligência que guia decisões",
            },
            {
                "valor": "infra_dados",
                "rotulo": "A infraestrutura invisível que transporta bilhões de dados com segurança e pontualidade",
            },
            {
                "valor": "blindagem_seguranca",
                "rotulo": "A certeza comprovada de que a organização e seus usuários estão seguros contra invasões",
            },
            {
                "valor": "deploy_confiavel",
                "rotulo": "A velocidade com que novos códigos chegam a produção sem qualquer indisponibilidade",
            },
            {
                "valor": "escalabilidade_nuvem",
                "rotulo": "A arquitetura em nuvem resiliente que aguenta picos massivos de tráfego sem engasgar",
            },
            {
                "valor": "experiencia_mobile",
                "rotulo": "A conveniência e fluidez de uma experiência de alto nível no celular",
            },
            {
                "valor": "software_sem_bugs",
                "rotulo": "A garantia de qualidade com zero falhas críticas e máxima confiabilidade de execução",
            },
            {
                "valor": "impacto_negocio",
                "rotulo": "O atingimento de metas corporativas, geração de receita e resolução de dores do cliente",
            },
        ],
    },
    {
        "id": "plataforma",
        "categoria": "Preferências de Ambiente e Plataforma",
        "obrigatoria": False,
        "titulo": "5. Plataforma-Alvo Preferida",
        "ajuda": "Em qual meio de execução você prefere ver seu trabalho operando?",
        "opcoes": [
            {"valor": "web", "rotulo": "Web (navegadores desktop e mobile)"},
            {"valor": "mobile", "rotulo": "Dispositivos Móveis (Android / iOS)"},
            {"valor": "servidores", "rotulo": "Servidores de Aplicação e Terminais de Infraestrutura"},
            {"valor": "nuvem", "rotulo": "Ambientes de Nuvem Pública (AWS, Google Cloud, Azure)"},
            {"valor": "dados_negocio", "rotulo": "Agnóstico à plataforma / Foco em Dados e Negócio"},
        ],
    },
    {
        "id": "interesse_ia",
        "categoria": "Especialização em Inteligência Artificial e Dados",
        "obrigatoria": False,
        "titulo": "6. Interesse em Inteligência Artificial e Modelagem Preditiva",
        "ajuda": "Você tem desejo genuíno de trabalhar diretamente com treinamento de algoritmos de Machine Learning?",
        "opcoes": [
            {
                "valor": "sim",
                "rotulo": "Sim — Tenho grande interesse em redes neurais, estatística avançada e IA generativa",
            },
            {
                "valor": "nao",
                "rotulo": "Não — Prefiro software tradicional, infraestrutura, automação ou gestão",
            },
        ],
    },
    {
        "id": "foco_dados",
        "categoria": "Especialização em Inteligência Artificial e Dados",
        "obrigatoria": False,
        "titulo": "7. Foco na Manipulação de Grandes Massas de Dados",
        "ajuda": "Se você fosse trabalhar com dados, qual seria sua inclinação primária?",
        "opcoes": [
            {
                "valor": "modelagem_insights",
                "rotulo": "Extrair conclusões analíticas, levantar hipóteses e treinar modelos preditivos",
            },
            {
                "valor": "pipelines_infra",
                "rotulo": "Construir pipelines de ETL/ELT, Data Lakes e arquitetura de distribuição de dados em massa",
            },
            {
                "valor": "nenhum",
                "rotulo": "Não tenho interesse primário em trabalhar focado em grandes massas de dados",
            },
        ],
    },
    {
        "id": "habilidades_gestao",
        "categoria": "Habilidades Interpessoais e Visão de Negócio",
        "obrigatoria": False,
        "titulo": "8. Afinidade com Pessoas, Negócios e Metodologias Ágeis",
        "ajuda": "Qual seu grau de interesse em reuniões com stakeholders, análise de métricas de mercado e facilitação ágil?",
        "opcoes": [
            {
                "valor": "alta",
                "rotulo": "Alto — Adoro articular com pessoas de diferentes áreas, entender mercado e liderar pelo exemplo",
            },
            {
                "valor": "media",
                "rotulo": "Médio — Gosto de trabalhar em time ágil, mas prefiro manter foco prioritário na técnica",
            },
            {
                "valor": "baixa",
                "rotulo": "Baixo — Prefiro máxima concentração técnica individual e o mínimo de burocracia de reuniões",
            },
        ],
    },
    {
        "id": "rigor_qualidade",
        "categoria": "Mentalidade de Confiabilidade e Segurança",
        "obrigatoria": False,
        "titulo": "9. Rigor com Detalhes, Testes e Prevenção de Falhas",
        "ajuda": "Qual postura mental mais se aproxima do seu estilo em um projeto de software?",
        "opcoes": [
            {
                "valor": "critico_bugs",
                "rotulo": "Crítico e metódico — Gosto de pensar nos casos extremos, validar fluxos e garantir cobertura de testes",
            },
            {
                "valor": "defensivo_seguranca",
                "rotulo": "Defensivo e investigativo — Gosto de analisar vulnerabilidades e pensar como um invasor para blindar o sistema",
            },
            {
                "valor": "equilibrado",
                "rotulo": "Equilibrado — Foco no desenvolvimento ágil com testes básicos suficientes",
            },
        ],
    },
    {
        "id": "interesse_automacao",
        "categoria": "Operações e Automação",
        "obrigatoria": False,
        "titulo": "10. Interesse em Automação Operacional, Contêineres e CI/CD",
        "ajuda": "Você se atrai por ferramentas como Docker, Kubernetes, Terraform e automação de servidores?",
        "opcoes": [
            {
                "valor": "sim",
                "rotulo": "Sim — Fascinado por automatizar esteiras, orquestrar contêineres e infraestrutura como código",
            },
            {
                "valor": "nao",
                "rotulo": "Não — Prefiro focar em código de produto, regras de negócio ou modelos de dados",
            },
        ],
    },
]

MAPA_PERGUNTAS: Dict[str, Dict[str, Any]] = {p["id"]: p for p in PERGUNTAS}
DIMENSOES_OBRIGATORIAS = [p["id"] for p in PERGUNTAS if p.get("obrigatoria")]
