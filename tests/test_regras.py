"""Testes de integridade da Base de Conhecimento e do Motor de Inferência Experta.

Verifica:
1. Contagem formal de regras @Rule (deve atender/superar o mínimo de 20-25 regras);
2. Cobertura de todas as 10 trilhas profissionais;
3. Testes específicos para desambiguações críticas (DS x DE, etc.);
4. Comportamento determinístico da regra de Fallback para perfil indeciso;
5. Validação de perguntas obrigatórias ausentes.
"""

import inspect
import src.compat  # noqa: F401
from experta import Rule
from src.knowledge_base import ConsultorCarreirasEngine, REGRAS_METADADOS
from src.trilhas import ORDEM_CANONICA
from src.engine_runner import recomendar, validar_respostas


def test_contagem_minima_de_regras():
    """Valida que o KnowledgeEngine possui no mínimo 20 a 25 métodos @Rule."""
    engine = ConsultorCarreirasEngine()
    regras_engine = engine.get_rules()
    total_catalogo = len(REGRAS_METADADOS)

    print(f"\n[INFO] Total de regras no catálogo: {total_catalogo}")
    print(f"[INFO] Total de regras registradas no Engine: {len(regras_engine)}")

    assert total_catalogo >= 25, f"Esperado ao menos 25 regras no catálogo, encontrado {total_catalogo}"
    assert len(regras_engine) >= 20, (
        f"Esperado no mínimo 20 regras no KnowledgeEngine, encontrados {len(regras_engine)}"
    )
    # Valida o número exato planejado
    assert len(regras_engine) == 38, f"Esperado 38 regras no engine, obtido {len(regras_engine)}"


def test_cobertura_das_10_trilhas():
    """Valida se todas as 10 trilhas possuem ao menos duas regras no catálogo."""
    trilhas_cobertas = set()
    for meta in REGRAS_METADADOS.values():
        t = meta.get("trilha")
        if t and t in ORDEM_CANONICA:
            trilhas_cobertas.add(t)

    for trilha in ORDEM_CANONICA:
        assert trilha in trilhas_cobertas, f"A trilha '{trilha}' não possui regras associadas no catálogo"


def test_desambiguacao_critica_ds_vs_de():
    """Teste dedicado para o requisito crítico obrigatório: DS versus DE."""
    # Cenário DS: matemática alta + foco em modelagem preditiva + IA
    perfil_ds = {
        "matematica": "Alta",
        "atuacao": "ciencia_dados_analise",
        "linguagem": "python",
        "entrega": "insights_modelos",
        "foco_dados": "modelagem_insights",
        "interesse_ia": "sim",
    }
    res_ds = recomendar(perfil_ds)
    assert res_ds["trilha_id"] == "ciencia_dados"
    assert any(r["id"] == "DES_DS_VS_DE_DS" for r in res_ds["regras_disparadas"])

    # Cenário DE: foco em pipelines + ETL + ausência de foco em IA
    perfil_de = {
        "matematica": "Média",
        "atuacao": "engenharia_dados_etl",
        "linguagem": "sql",
        "entrega": "infra_dados",
        "foco_dados": "pipelines_infra",
        "interesse_ia": "nao",
    }
    res_de = recomendar(perfil_de)
    assert res_de["trilha_id"] == "engenharia_dados"
    assert any(r["id"] == "DES_DS_VS_DE_DE" for r in res_de["regras_disparadas"])


def test_desambiguacao_front_vs_mobile():
    """Teste de desambiguação entre Front-end Web e Desenvolvimento Mobile."""
    # Front-end Web
    perfil_front = {
        "atuacao": "frontend_ui",
        "plataforma": "web",
        "linguagem": "javascript",
        "entrega": "produto_visual",
    }
    res_front = recomendar(perfil_front)
    assert res_front["trilha_id"] == "frontend"
    assert any(r["id"] == "DES_FRONT_VS_MOBILE_F" for r in res_front["regras_disparadas"])

    # Mobile
    perfil_mobile = {
        "atuacao": "mobile_apps",
        "plataforma": "mobile",
        "linguagem": "dart_mobile",
        "entrega": "experiencia_mobile",
    }
    res_mobile = recomendar(perfil_mobile)
    assert res_mobile["trilha_id"] == "mobile"
    assert any(r["id"] == "DES_FRONT_VS_MOBILE_M" for r in res_mobile["regras_disparadas"])


def test_desambiguacao_devops_cloud_backend():
    """Teste de desambiguação entre DevOps, Cloud e Back-end."""
    # DevOps (automação)
    perfil_devops = {
        "atuacao": "devops_ci_cd",
        "interesse_automacao": "sim",
        "linguagem": "linux_redes",
        "entrega": "deploy_confiavel",
    }
    res_devops = recomendar(perfil_devops)
    assert res_devops["trilha_id"] == "devops"
    assert any(r["id"] == "DES_BACK_CLOUD_DEVOPS_D" for r in res_devops["regras_disparadas"])

    # Cloud (arquitetura em nuvem)
    perfil_cloud = {
        "atuacao": "cloud_infra",
        "plataforma": "nuvem",
        "interesse_automacao": "nao",
        "entrega": "escalabilidade_nuvem",
    }
    res_cloud = recomendar(perfil_cloud)
    assert res_cloud["trilha_id"] == "cloud"
    assert any(r["id"] == "DES_BACK_CLOUD_DEVOPS_C" for r in res_cloud["regras_disparadas"])

    # Back-end (lógica de negócio e APIs)
    perfil_back = {
        "atuacao": "backend_api",
        "entrega": "logica_invisivel",
        "linguagem": "java_csharp",
        "plataforma": "servidores",
    }
    res_back = recomendar(perfil_back)
    assert res_back["trilha_id"] == "backend"
    assert any(r["id"] == "DES_BACK_CLOUD_DEVOPS_B" for r in res_back["regras_disparadas"])


def test_regra_fallback_perfil_indeciso():
    """Valida a ativação determinística da regra de fallback para perfil vago/indeciso."""
    # Respostas neutras ou vazias que não ativam nenhuma regra pontuadora específica
    perfil_vago = {
        "matematica": "Baixa",
        "atuacao": "indeciso",
        "linguagem": "iniciante",
        "entrega": "indeciso",
        "plataforma": "dados_negocio",
        "interesse_ia": "nao",
        "foco_dados": "nenhum",
        "habilidades_gestao": "baixa",
        "rigor_qualidade": "equilibrado",
        "interesse_automacao": "nao",
    }
    res = recomendar(perfil_vago)
    assert res["trilha_id"] == "backend"
    assert res["is_fallback"] is True
    assert any(r["id"] == "R_FALLBACK_INICIANTE" for r in res["regras_disparadas"])


def test_validacao_campos_obrigatorios():
    """Valida a detecção de respostas obrigatórias não preenchidas."""
    incompleto = {"matematica": "Alta"}
    ausentes = validar_respostas(incompleto)
    assert "atuacao" in ausentes
    assert "linguagem" in ausentes
    assert "entrega" in ausentes

    completo = {
        "matematica": "Alta",
        "atuacao": "backend_api",
        "linguagem": "python",
        "entrega": "logica_invisivel",
    }
    ausentes_ok = validar_respostas(completo)
    assert len(ausentes_ok) == 0
