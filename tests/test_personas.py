"""Suíte de validação do Sistema Especialista com 10 Personas de Teste.

Cobre 100% das 10 trilhas profissionais de TI exigidas pelo edital.
Cada teste valida:
(a) Recomendação exata da trilha esperada;
(b) Justificativa rica e não vazia (regras disparadas e motivos em português);
(c) Unicidade da recomendação final e coerência no ranking geral.
"""

import pytest
import src.compat  # noqa: F401
from src.engine_runner import recomendar


PERSONAS = [
    # 1. Perfil Analítico / Machine Learning
    (
        "Persona 1: Marina (Cientista de Dados & ML)",
        {
            "matematica": "Alta",
            "atuacao": "ciencia_dados_analise",
            "linguagem": "python",
            "entrega": "insights_modelos",
            "plataforma": "dados_negocio",
            "interesse_ia": "sim",
            "foco_dados": "modelagem_insights",
            "habilidades_gestao": "baixa",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "nao",
        },
        "ciencia_dados",
    ),
    # 2. Perfil Defesa e Ethical Hacking
    (
        "Persona 2: Lucas (Analista de Cibersegurança)",
        {
            "matematica": "Média",
            "atuacao": "seguranca_defesa",
            "linguagem": "linux_redes",
            "entrega": "blindagem_seguranca",
            "plataforma": "servidores",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "baixa",
            "rigor_qualidade": "defensivo_seguranca",
            "interesse_automacao": "nao",
        },
        "ciberseguranca",
    ),
    # 3. Perfil Visual e Experiência do Usuário
    (
        "Persona 3: Camila (Engenheira Front-end & UI/UX)",
        {
            "matematica": "Baixa",
            "atuacao": "frontend_ui",
            "linguagem": "javascript",
            "entrega": "produto_visual",
            "plataforma": "web",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "media",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "nao",
        },
        "frontend",
    ),
    # 4. Perfil Negócios e Liderança de Produto
    (
        "Persona 4: Rodrigo (Product Manager)",
        {
            "matematica": "Média",
            "atuacao": "gestao_produto",
            "linguagem": "iniciante",
            "entrega": "impacto_negocio",
            "plataforma": "dados_negocio",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "alta",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "nao",
        },
        "gestao_produtos",
    ),
    # 5. Perfil Back-end Corporativo e APIs
    (
        "Persona 5: Bruno (Desenvolvedor Back-end)",
        {
            "matematica": "Média",
            "atuacao": "backend_api",
            "linguagem": "java_csharp",
            "entrega": "logica_invisivel",
            "plataforma": "servidores",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "baixa",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "nao",
        },
        "backend",
    ),
    # 6. Perfil Pipelines e Infra de Dados
    (
        "Persona 6: Beatriz (Engenheira de Dados)",
        {
            "matematica": "Média",
            "atuacao": "engenharia_dados_etl",
            "linguagem": "sql",
            "entrega": "infra_dados",
            "plataforma": "servidores",
            "interesse_ia": "nao",
            "foco_dados": "pipelines_infra",
            "habilidades_gestao": "baixa",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "nao",
        },
        "engenharia_dados",
    ),
    # 7. Perfil Automação CI/CD e Contêineres
    (
        "Persona 7: Thiago (Engenheiro DevOps & SRE)",
        {
            "matematica": "Baixa",
            "atuacao": "devops_ci_cd",
            "linguagem": "linux_redes",
            "entrega": "deploy_confiavel",
            "plataforma": "nuvem",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "media",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "sim",
        },
        "devops",
    ),
    # 8. Perfil Infraestrutura Elástica em Nuvem
    (
        "Persona 8: Gabriel (Arquiteto de Nuvem / Cloud)",
        {
            "matematica": "Média",
            "atuacao": "cloud_infra",
            "linguagem": "linux_redes",
            "entrega": "escalabilidade_nuvem",
            "plataforma": "nuvem",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "media",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "nao",
        },
        "cloud",
    ),
    # 9. Perfil Aplicativos Móveis Nativos
    (
        "Persona 9: Juliana (Desenvolvedora Mobile)",
        {
            "matematica": "Baixa",
            "atuacao": "mobile_apps",
            "linguagem": "dart_mobile",
            "entrega": "experiencia_mobile",
            "plataforma": "mobile",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "baixa",
            "rigor_qualidade": "equilibrado",
            "interesse_automacao": "nao",
        },
        "mobile",
    ),
    # 10. Perfil Prevenção de Falhas e Automação de Testes
    (
        "Persona 10: Felipe (Engenheiro de QA / Testes)",
        {
            "matematica": "Média",
            "atuacao": "qa_testes",
            "linguagem": "python",
            "entrega": "software_sem_bugs",
            "plataforma": "web",
            "interesse_ia": "nao",
            "foco_dados": "nenhum",
            "habilidades_gestao": "media",
            "rigor_qualidade": "critico_bugs",
            "interesse_automacao": "nao",
        },
        "qa",
    ),
]


@pytest.mark.parametrize("nome_persona,respostas,trilha_esperada", PERSONAS)
def test_validacao_persona(nome_persona, respostas, trilha_esperada):
    """Executa a inferência para a persona e valida a trilha recomendada e justificativa."""
    resultado = recomendar(respostas)

    # (a) Trilha recomendada deve ser exatamente a esperada
    assert resultado["trilha_id"] == trilha_esperada, (
        f"Falha na {nome_persona}: Esperado '{trilha_esperada}', mas obteve '{resultado['trilha_id']}'"
    )

    # (b) Justificativa rica e não vazia
    assert len(resultado["regras_disparadas"]) > 0, (
        f"{nome_persona} deveria ter registrado regras disparadas"
    )
    for regra in resultado["regras_disparadas"]:
        assert "nome" in regra and len(regra["nome"]) > 0
        assert "justificativa" in regra and len(regra["justificativa"]) > 0

    # (c) Pontuação positiva e consistência de ranking
    assert resultado["pontuacao"] > 0
    assert len(resultado["ranking"]) == 10
    assert resultado["ranking"][0]["id"] == trilha_esperada
    assert resultado["is_fallback"] is False
