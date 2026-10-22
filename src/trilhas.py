"""Catálogo oficial de metadados das 10 trilhas profissionais de TI."""

from typing import Dict, Any

TRILHAS: Dict[str, Dict[str, Any]] = {
    "backend": {
        "id": "backend",
        "nome": "Desenvolvimento Back-end",
        "icone": "⚙️",
        "resumo": "Lógica de servidores, construção de APIs, regras de negócio e bancos de dados.",
        "descricao": (
            "O profissional de Back-end projeta e desenvolve a espinha dorsal de aplicações web e corporativas. "
            "É responsável pela persistência em bancos de dados relacionais e NoSQL, autenticação segura, "
            "alta performance de processamento, regras de negócio complexas e integração via APIs RESTful e GraphQL."
        ),
        "tecnologias_chave": ["Java / Spring Boot", "Python / FastAPI", "Node.js", "C# / .NET", "PostgreSQL", "Redis", "Docker"],
        "soft_skills": ["Pensamento lógico estruturado", "Atenção a padrões arquiteturais", "Resolução sistemática de problemas"],
    },
    "frontend": {
        "id": "frontend",
        "nome": "Desenvolvimento Front-end & UI/UX",
        "icone": "🎨",
        "resumo": "Interfaces web responsivas, experiência do usuário (UX) e frameworks reativos modernos.",
        "descricao": (
            "O engenheiro Front-end transforma protótipos de design em experiências digitais interativas, acessíveis e rápidas. "
            "Trabalha diretamente na camada visível ao cliente final, dominando frameworks reativos modernos, "
            "otimização de renderização (Core Web Vitals), animações fluidas e integração eficiente com APIs."
        ),
        "tecnologias_chave": ["JavaScript / TypeScript", "React", "Vue.js / Next.js", "Tailwind CSS / Sass", "Figma", "HTML5 Semântico"],
        "soft_skills": ["Empatia com o usuário final", "Olhar estético e espacial apurado", "Atenção a detalhes visuais"],
    },
    "ciencia_dados": {
        "id": "ciencia_dados",
        "nome": "Ciência de Dados e Machine Learning",
        "icone": "🧠",
        "resumo": "Estatística, modelagem preditiva, análise de grandes massas de dados e inteligência artificial.",
        "descricao": (
            "O Cientista de Dados aplica rigor matemático, métodos estatísticos e algoritmos de Machine Learning e Deep Learning "
            "para descobrir padrões ocultos em dados brutos e prever comportamentos futuros. "
            "Atua na fronteira da Inteligência Artificial gerando insights acionáveis e treinando modelos de alta precisão."
        ),
        "tecnologias_chave": ["Python (NumPy, Pandas, Scikit-learn)", "PyTorch / TensorFlow", "Jupyter", "SQL Avançado", "Estatística Descritiva e Inferencial"],
        "soft_skills": ["Curiosidade científica e analítica", "Raciocínio dedutivo", "Comunicação de conclusões quantitativas"],
    },
    "engenharia_dados": {
        "id": "engenharia_dados",
        "nome": "Engenharia de Dados",
        "icone": "🚰",
        "resumo": "Arquitetura de dados, construção de pipelines (ETL/ELT) e infraestrutura para Data Lakes.",
        "descricao": (
            "O Engenheiro de Dados constrói e mantém os sistemas de encanamento de alta escala que transportam, "
            "higienizam e disponibilizam petabytes de informações de forma confiável. "
            "Projeta arquiteturas analíticas robustas, integrando múltiplos sistemas para alimentar Cientistas de Dados e Analistas de BI."
        ),
        "tecnologias_chave": ["Apache Spark", "Airflow / Prefect", "Kafka", "SQL & NoSQL", "dbt", "Snowflake / BigQuery", "AWS S3 / Data Lake"],
        "soft_skills": ["Pensamento sistêmico de fluxo", "Rigor com governança e integridade", "Preocupação com escalabilidade contínua"],
    },
    "ciberseguranca": {
        "id": "ciberseguranca",
        "nome": "Cibersegurança (Security / Pentesting)",
        "icone": "🛡️",
        "resumo": "Defesa cibernética, análise de vulnerabilidades, criptografia, redes seguras e ethical hacking.",
        "descricao": (
            "O especialista em Cibersegurança atua como o escudo digital de organizações. "
            "Identifica vulnerabilidades ativamente através de simulações de ataques (pentest / Red Team) e desenvolve "
            "estratégias rigorosas de defesa e mitigação de incidentes (Blue Team), aplicando criptografia e auditorias contínuas."
        ),
        "tecnologias_chave": ["Linux Avançado & Kali", "Wireshark / Nmap", "Burp Suite", "Protocolos de Rede (TCP/IP)", "Criptografia", "OWASP Top 10"],
        "soft_skills": ["Pensamento defensivo e investigativo", "Ética profissional inabalável", "Calma sob pressão em incidentes"],
    },
    "devops": {
        "id": "devops",
        "nome": "DevOps & SRE",
        "icone": "🚀",
        "resumo": "Automação de processos, integração e entrega contínua (CI/CD), contêineres e confiabilidade de sistemas.",
        "descricao": (
            "O engenheiro DevOps/SRE une os mundos de desenvolvimento de software e operações. "
            "Sua missão é criar esteiras automatizadas de entrega rápida e segura de código (CI/CD), "
            "gerenciar orquestração em contêineres, implementar infraestrutura como código (IaC) e garantir uptime e resiliência máxima."
        ),
        "tecnologias_chave": ["Docker", "Kubernetes", "GitHub Actions / GitLab CI", "Terraform", "Ansible", "Prometheus / Grafana", "Bash / Python"],
        "soft_skills": ["Cultura de automação implacável", "Proatividade na mitigação de atritos", "Resiliência operacional"],
    },
    "cloud": {
        "id": "cloud",
        "nome": "Computação em Nuvem (Cloud Architecture)",
        "icone": "☁️",
        "resumo": "Planejamento, migração e gestão de infraestruturas escaláveis e distribuídas em nuvem (AWS/Azure/GCP).",
        "descricao": (
            "O Arquiteto Cloud desenha soluções globais de infraestrutura corporativa na nuvem. "
            "Define estratégias de alta disponibilidade, disaster recovery, redução de custos computacionais (FinOps) "
            "e migração de sistemas legados para ambientes serverless e microsserviços distribuídos."
        ),
        "tecnologias_chave": ["AWS (EC2, S3, Lambda, VPC)", "Microsoft Azure", "Google Cloud Platform", "Terraform", "FinOps", "Arquiteturas Serverless"],
        "soft_skills": ["Visão estratégica de arquitetura", "Capacidade de negociação técnica", "Gestão de risco tecnológico"],
    },
    "mobile": {
        "id": "mobile",
        "nome": "Desenvolvimento Mobile",
        "icone": "📱",
        "resumo": "Ecossistema de dispositivos móveis com desenvolvimento nativo ou multiplataforma reativo.",
        "descricao": (
            "O desenvolvedor Mobile cria aplicativos para a experiência na palma da mão em smartphones e wearables. "
            "Domina particularidades de ciclos de vida de apps em segundo plano, otimização extrema de memória e bateria, "
            "funcionalidades de hardware (câmera, sensores, GPS) e publicação nas lojas App Store e Google Play."
        ),
        "tecnologias_chave": ["Flutter / Dart", "React Native", "Kotlin (Android Nativo)", "Swift (iOS Nativo)", "Mobile UX", "SQLite / Realm"],
        "soft_skills": ["Sensibilidade à fluidez e toque", "Atenção às limitações de hardware móvel", "Respeito a diretrizes Apple/Google"],
    },
    "qa": {
        "id": "qa",
        "nome": "Engenharia de Qualidade e Testes (QA)",
        "icone": "🧪",
        "resumo": "Testes automatizados, confiabilidade de software, prevenção de defeitos e processos de qualidade.",
        "descricao": (
            "O Engenheiro de Qualidade (QA/SDET) é o guardião dos padrões de excelência de um produto de software. "
            "Desenvolve suítes completas de testes automatizados (unitários, de integração, E2E e testes de carga), "
            "validando cenários de borda e garantindo que novas funcionalidades não quebrem o comportamento esperado do sistema."
        ),
        "tecnologias_chave": ["Cypress / Playwright", "Selenium", "Postman / Newman", "Pytest / JUnit", "JMeter (Testes de Carga)", "CI/CD para testes"],
        "soft_skills": ["Atenção cirúrgica aos detalhes", "Pensamento analítico de quebra de regras", "Comunicação assertiva e construtiva"],
    },
    "gestao_produtos": {
        "id": "gestao_produtos",
        "nome": "Gestão de Produtos (Product Management)",
        "icone": "📊",
        "resumo": "Ponte entre negócios, design e desenvolvimento, metodologias ágeis e priorização estratégica.",
        "descricao": (
            "O Product Manager (PM) lidera pelo convencimento, conectando a estratégia corporativa com as necessidades dos clientes "
            "e a capacidade de entrega técnica da engenharia. "
            "Define visões de produto, prioriza backlogs de funcionalidades com base em valor de negócio, define métricas de impacto (OKRs) e lidera cerimônias ágeis."
        ),
        "tecnologias_chave": ["Scrum / Kanban / Ágil", "Jira / Linear", "Product Discovery", "Mapeamento de Jornada", "Análise de Métricas (Amplitude, Mixpanel)", "OKRs"],
        "soft_skills": ["Liderança influenciadora e interpessoal", "Negociação e diplomacia", "Visão holística de negócio"],
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
