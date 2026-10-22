"""Catalogo oficial de metadados das 10 trilhas profissionais de TI."""

from typing import Dict, Any

TRILHAS: Dict[str, Dict[str, Any]] = {
    "backend": {
        "id": "backend",
        "nome": "Desenvolvimento Back-end",
        "icone": "",
        "resumo": "Logica de servidores, construcao de APIs, regras de negocio e bancos de dados.",
        "descricao": (
            "O profissional de Back-end projeta e desenvolve a arquitetura de servicos de aplicacoes corporativas. "
            "E responsavel pela persistencia em bancos de dados relacionais e NoSQL, autenticacao segura, "
            "processamento de alto desempenho, regras de negocio e integracao por APIs RESTful e GraphQL."
        ),
        "tecnologias_chave": ["Java / Spring Boot", "Python / FastAPI", "Node.js", "C# / .NET", "PostgreSQL", "Redis", "Docker"],
        "soft_skills": ["Pensamento logico estruturado", "Padroes arquiteturais", "Resolucao analitica de problemas"],
    },
    "frontend": {
        "id": "frontend",
        "nome": "Desenvolvimento Front-end & UI/UX",
        "icone": "",
        "resumo": "Interfaces web responsivas, experiencia do usuario (UX) e frameworks modernos.",
        "descricao": (
            "O desenvolvedor Front-end implementa componentes visuais interativos, acessiveis e otimizados. "
            "Atua na camada cliente utilizando frameworks reativos, tecnicas de otimizacao de renderizacao "
            "e integracao com servicos web."
        ),
        "tecnologias_chave": ["JavaScript / TypeScript", "React", "Vue.js / Next.js", "Tailwind CSS / Sass", "Figma", "HTML5 Semantico"],
        "soft_skills": ["Usabilidade e acessibilidade", "Atencao a detalhes visuais", "Empatia com o usuario"],
    },
    "ciencia_dados": {
        "id": "ciencia_dados",
        "nome": "Ciencia de Dados e Machine Learning",
        "icone": "",
        "resumo": "Estatistica, modelagem preditiva, analise de dados e inteligencia artificial.",
        "descricao": (
            "O Cientista de Dados aplica metodos estatisticos e algoritmos de Machine Learning e Deep Learning "
            "para identificar padroes quantitativos em grandes volumes de informacao e gerar modelos preditivos."
        ),
        "tecnologias_chave": ["Python (NumPy, Pandas, Scikit-learn)", "PyTorch / TensorFlow", "Jupyter", "SQL Avancado", "Estatistica Descritiva e Inferencial"],
        "soft_skills": ["Raciocinio dedutivo e quantitativo", "Curiosidade analitica", "Comunicacao tecnica de resultados"],
    },
    "engenharia_dados": {
        "id": "engenharia_dados",
        "nome": "Engenharia de Dados",
        "icone": "",
        "resumo": "Arquitetura de dados, construcao de pipelines (ETL/ELT) e infraestrutura para Data Lakes.",
        "descricao": (
            "O Engenheiro de Dados projeta e mantem fluxos de ingestao, processamento e transformacao de grandes "
            "volumes de informacoes. Desenvolve a arquitetura de armazenamento analitico para alimentar sistemas de analise e BI."
        ),
        "tecnologias_chave": ["Apache Spark", "Airflow / Prefect", "Kafka", "SQL & NoSQL", "dbt", "Snowflake / BigQuery", "AWS S3 / Data Lake"],
        "soft_skills": ["Pensamento sistemico de fluxo", "Governanca de dados", "Escalabilidade e monitoramento"],
    },
    "ciberseguranca": {
        "id": "ciberseguranca",
        "nome": "Ciberseguranca (Security / Pentesting)",
        "icone": "",
        "resumo": "Defesa cibernetica, analise de vulnerabilidades, criptografia e seguranca de redes.",
        "descricao": (
            "O especialista em Ciberseguranca atua na protecao de infraestruturas e aplicacoes. "
            "Realiza testes de intrusao (pentest), auditorias de codigo, analise de vulnerabilidades e resposta a incidentes de seguranca."
        ),
        "tecnologias_chave": ["Linux & Kali", "Wireshark / Nmap", "Burp Suite", "Protocolos de Rede (TCP/IP)", "Criptografia", "OWASP Top 10"],
        "soft_skills": ["Pensamento investigativo", "Etica profissional", "Gestao de risco e conformidade"],
    },
    "devops": {
        "id": "devops",
        "nome": "DevOps & SRE",
        "icone": "",
        "resumo": "Automacao operacional, integracao e entrega continua (CI/CD), conteineres e confiabilidade de sistemas.",
        "descricao": (
            "O engenheiro DevOps/SRE integra desenvolvimento e operacoes por meio da automacao de esteiras "
            "de entrega continua (CI/CD), orquestracao de conteineres, infraestrutura como codigo (IaC) e monitoramento de disponibilidade."
        ),
        "tecnologias_chave": ["Docker", "Kubernetes", "GitHub Actions / GitLab CI", "Terraform", "Ansible", "Prometheus / Grafana", "Bash / Python"],
        "soft_skills": ["Cultura de automacao", "Gestao de incidentes", "Resiliencia operacional"],
    },
    "cloud": {
        "id": "cloud",
        "nome": "Computacao em Nuvem (Cloud Architecture)",
        "icone": "",
        "resumo": "Planejamento, migracao e gestao de infraestruturas escalaveis em nuvem (AWS/Azure/GCP).",
        "descricao": (
            "O Arquiteto Cloud planeja solucoes de infraestrutura distribuidas e escalaveis. "
            "Define modelos de alta disponibilidade, planos de recuperacao de desastres, gestao de custos computacionais (FinOps) e arquiteturas serverless."
        ),
        "tecnologias_chave": ["AWS (EC2, S3, Lambda, VPC)", "Microsoft Azure", "Google Cloud Platform", "Terraform", "FinOps", "Arquiteturas Serverless"],
        "soft_skills": ["Visao estrategica de arquitetura", "Negociacao tecnica", "Analise de custo-beneficio"],
    },
    "mobile": {
        "id": "mobile",
        "nome": "Desenvolvimento Mobile",
        "icone": "",
        "resumo": "Ecossistema de dispositivos moveis com desenvolvimento nativo ou multiplataforma.",
        "descricao": (
            "O desenvolvedor Mobile cria aplicacoes para smartphones e tablets. "
            "Gerencia ciclos de vida de aplicativos, consumo de bateria, gerenciamento de memoria e integracao com sensores de hardware."
        ),
        "tecnologias_chave": ["Flutter / Dart", "React Native", "Kotlin (Android)", "Swift (iOS)", "Mobile UX", "SQLite / Realm"],
        "soft_skills": ["Atencao a restricoes de hardware", "Diretrizes de design mobile", "Foco em estabilidade"],
    },
    "qa": {
        "id": "qa",
        "nome": "Engenharia de Qualidade e Testes (QA)",
        "icone": "",
        "resumo": "Testes automatizados, confiabilidade de software e garantia de conformidade.",
        "descricao": (
            "O Engenheiro de Qualidade projeta e executa suites de testes automatizados (unitarios, integracao, E2E e carga). "
            "Garante a conformidade dos requisitos de software e previne a introducao de regressoes no produto."
        ),
        "tecnologias_chave": ["Cypress / Playwright", "Selenium", "Postman / Newman", "Pytest / JUnit", "JMeter", "CI/CD para testes"],
        "soft_skills": ["Rigor analitico", "Pensamento critico de borda", "Comunicacao assertiva"],
    },
    "gestao_produtos": {
        "id": "gestao_produtos",
        "nome": "Gestao de Produtos (Product Management)",
        "icone": "",
        "resumo": "Ponte entre negocios, design e desenvolvimento, metodologias ageis e priorizacao de backlog.",
        "descricao": (
            "O Product Manager define a visao e o roadmap de produto com base nas necessidades de negocio e clientes. "
            "Prioriza backlogs de funcionalidades, estabelece metricas de impacto (OKRs) e conduz cerimonias em equipes ageis."
        ),
        "tecnologias_chave": ["Scrum / Kanban", "Jira / Linear", "Product Discovery", "Mapeamento de Jornada", "Metricas de Produto", "OKRs"],
        "soft_skills": ["Lideranca por influencia", "Negociacao e alinhamento", "Visao analitica de negocio"],
    },
}

ORDEM_CANONICA = [
    "backend",
    "frontend",
    "ciencia_dados",
    "engenharia_dados",
    "ciberseguranca",
    "devops",
    "cloud",
    "mobile",
    "qa",
    "gestao_produtos",
]


def obter_trilha(trilha_id: str) -> Dict[str, Any]:
    """Retorna os metadados de uma trilha pelo ID com fallback seguro."""
    return TRILHAS.get(trilha_id, TRILHAS["backend"])
