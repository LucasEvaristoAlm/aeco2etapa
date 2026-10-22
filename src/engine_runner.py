"""Módulo executor da inferência do Sistema Especialista.

Fornece a interface desacoplada recomendador(respostas) -> resultado
para consumo direto pela interface Streamlit e pela suíte de testes automatizados.
"""

from typing import Dict, Any, List
from src.compat import *  # noqa: F401, F403
from src.facts import PerfilUsuario
from src.knowledge_base import ConsultorCarreirasEngine
from src.questions import DIMENSOES_OBRIGATORIAS


def validar_respostas(respostas: Dict[str, Any]) -> List[str]:
    """Valida se as dimensões obrigatórias da entrevista foram fornecidas.

    Retorna uma lista de nomes de campos ausentes, se houver.
    """
    ausentes = []
    for dim in DIMENSOES_OBRIGATORIAS:
        if dim not in respostas or respostas[dim] is None or respostas[dim] == "":
            ausentes.append(dim)
    return ausentes


def recomendar(respostas: Dict[str, Any]) -> Dict[str, Any]:
    """Executa o ciclo completo de inferência forward chaining no Experta.

    Args:
        respostas: Dicionário contendo as respostas do usuário para as 10 perguntas.

    Returns:
        Dicionário estruturado com:
        - trilha_id: ID da trilha recomendada (ex: 'ciencia_dados')
        - trilha_nome: Nome oficial da trilha
        - trilha_dados: Metadados detalhados (descrição, tecnologias, soft skills)
        - pontuacao: Pontuação total atingida pela trilha vencedora
        - ranking: Lista ordenada com as 10 trilhas e respectivas pontuações
        - regras_disparadas: Lista cronológica de todas as regras disparadas
        - motivos_principais: Regras específicas que justificam a trilha vencedora
        - indicadores: Indicadores intermediários gerados
        - is_fallback: Booleano indicando se acionou regra de fallback
    """
    engine = ConsultorCarreirasEngine()
    engine.reset()

    # Mapeamento e preservacao dos campos informados
    sanitized: Dict[str, Any] = {
        "matematica": respostas.get("matematica"),
        "atuacao": respostas.get("atuacao"),
        "linguagem": respostas.get("linguagem"),
        "entrega": respostas.get("entrega"),
        "plataforma": respostas.get("plataforma"),
        "interesse_ia": respostas.get("interesse_ia"),
        "foco_dados": respostas.get("foco_dados"),
        "habilidades_gestao": respostas.get("habilidades_gestao"),
        "rigor_qualidade": respostas.get("rigor_qualidade"),
        "interesse_automacao": respostas.get("interesse_automacao"),
    }

    # Declara o fato PerfilUsuario e dispara o ciclo de encadeamento para frente
    engine.declare(PerfilUsuario(**sanitized))
    engine.run()

    resultado = engine.recomendacao_final
    if resultado is None:
        # Salvaguarda final caso o engine termine sem disparar decisão (não esperado)
        from src.trilhas import TRILHAS, ORDEM_CANONICA
        resultado = {
            "trilha_id": "backend",
            "trilha_nome": TRILHAS["backend"]["nome"],
            "trilha_dados": TRILHAS["backend"],
            "pontuacao": 0.0,
            "ranking": [
                {
                    "id": t,
                    "nome": TRILHAS[t]["nome"],
                    "pontos": 0.0,
                    "icone": TRILHAS[t]["icone"],
                    "resumo": TRILHAS[t]["resumo"],
                }
                for t in ORDEM_CANONICA
            ],
            "regras_disparadas": engine.regras_disparadas,
            "motivos_principais": engine.regras_disparadas,
            "indicadores": engine.indicadores_gerados,
            "is_fallback": True,
        }

    resultado["indicadores"] = engine.indicadores_gerados
    return resultado
