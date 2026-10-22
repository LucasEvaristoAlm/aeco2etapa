"""Interface Web do Sistema Especialista: Consultor de Carreiras em TI.

Desenvolvido com Streamlit, utilizando o motor de inferencia Experta.
Atividade Academica de Inteligencia Artificial — Ciencia da Computacao, UNIPAC Barbacena.
"""

import sys
import streamlit as st
from streamlit.runtime import exists

# Se for executado diretamente com 'python app.py', inicia o servidor Streamlit automaticamente
if not exists():
    from streamlit.web import cli as stcli
    sys.argv = ["streamlit", "run", sys.argv[0]]
    sys.exit(stcli.main())

import src.compat  # noqa: F401
from src.questions import PERGUNTAS, DIMENSOES_OBRIGATORIAS
from src.engine_runner import recomendar, validar_respostas

# Configuracao da pagina Streamlit
st.set_page_config(
    page_title="Consultor de Carreiras em TI",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilizacao CSS profissional, sobria e moderna
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .main-header {
        background-color: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 8px;
        padding: 1.8rem 2rem;
        margin-bottom: 1.5rem;
    }

    .main-title {
        color: #f8fafc;
        font-size: 1.85rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 0.35rem;
    }

    .main-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        line-height: 1.5;
        margin-bottom: 0.85rem;
    }

    .academic-badge {
        display: inline-block;
        background: #1e293b;
        border: 1px solid #334155;
        color: #94a3b8;
        padding: 0.25rem 0.65rem;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 500;
    }

    .result-card {
        background: #0f172a;
        border: 1px solid #0284c7;
        border-radius: 8px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
    }

    .track-badge {
        background: #0284c7;
        color: #ffffff;
        font-weight: 600;
        font-size: 0.78rem;
        padding: 0.2rem 0.65rem;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .rule-box {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-left: 3px solid #0284c7;
        border-radius: 4px;
        padding: 0.85rem 1rem;
        margin-bottom: 0.75rem;
    }

    .tech-pill {
        display: inline-block;
        background: #1e293b;
        border: 1px solid #334155;
        color: #e2e8f0;
        padding: 0.2rem 0.6rem;
        border-radius: 4px;
        font-size: 0.8rem;
        margin-right: 0.35rem;
        margin-bottom: 0.35rem;
        font-weight: 500;
    }

    .stButton>button {
        border-radius: 6px;
        font-weight: 600;
        padding: 0.5rem 1.25rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inicializacao do estado de sessao
if "respostas" not in st.session_state:
    st.session_state["respostas"] = {}

if "resultado" not in st.session_state:
    st.session_state["resultado"] = None


def reiniciar_entrevista():
    """Limpa as respostas e os resultados armazenados na sessao."""
    st.session_state["respostas"] = {}
    st.session_state["resultado"] = None
    for p in PERGUNTAS:
        k = f"field_{p['id']}"
        if k in st.session_state:
            del st.session_state[k]
    st.rerun()


# Cabecalho Principal
st.markdown(
    """
    <div class="main-header">
        <div class="main-title">Consultor de Carreiras em TI</div>
        <div class="main-subtitle">
            Sistema Especialista Baseado em Regras com motor de inferencia Experta (Forward Chaining).<br>
            Questionario estruturado para recomendacao tecnica entre 10 trilhas profissionais.
        </div>
        <div class="academic-badge">
            Inteligencia Artificial | Ciencia da Computacao | UNIPAC Barbacena
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Barra lateral informativa
with st.sidebar:
    st.markdown("### Detalhes do Sistema")
    st.markdown(
        """
        - **Motor de Regras:** Experta 1.9.4
        - **Estrategia:** Encadeamento para Frente (Forward Chaining)
        - **Base de Conhecimento:** 38 Regras ativas
        - **Trilhas Catalogadas:** 10
        - **Desambiguacoes:** DS x DE, Back x Cloud x DevOps, Front x Mobile, QA e Produto.
        """
    )
    st.divider()

    st.markdown("### Trilhas Avaliadas")
    st.markdown(
        """
        1. Desenvolvimento Back-end
        2. Desenvolvimento Front-end & UI/UX
        3. Ciencia de Dados e ML
        4. Engenharia de Dados
        5. Ciberseguranca
        6. DevOps & SRE
        7. Computacao em Nuvem
        8. Desenvolvimento Mobile
        9. Engenharia de QA & Testes
        10. Gestao de Produtos (PM)
        """
    )
    st.divider()

    if st.button("Nova Consulta", use_container_width=True):
        reiniciar_entrevista()


# Se ja temos resultado calculado, exibe o diagnostico e as justificativas
if st.session_state["resultado"] is not None:
    res = st.session_state["resultado"]
    trilha = res["trilha_dados"]

    st.markdown(
        f"""
        <div class="result-card">
            <span class="track-badge">Trilha Recomendada</span>
            <h2 style="color: #f8fafc; margin-top: 0.75rem; margin-bottom: 0.35rem;">
                {res['trilha_nome']}
            </h2>
            <p style="color: #38bdf8; font-size: 1rem; font-weight: 500; margin-bottom: 1rem;">
                {trilha['resumo']}
            </p>
            <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.25rem;">
                {trilha['descricao']}
            </p>
            <div style="margin-bottom: 0.85rem;">
                <b style="color: #94a3b8; font-size: 0.82rem; text-transform: uppercase;">Tecnologias Recomendadas:</b><br>
                <div style="margin-top: 0.4rem;">
                    {''.join([f'<span class="tech-pill">{tech}</span>' for tech in trilha['tecnologias_chave']])}
                </div>
            </div>
            <div>
                <b style="color: #94a3b8; font-size: 0.82rem; text-transform: uppercase;">Competencias Relevantes:</b><br>
                <div style="margin-top: 0.4rem;">
                    {''.join([f'<span class="tech-pill">{skill}</span>' for skill in trilha['soft_skills']])}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_just, col_rank = st.columns([6, 4])

    with col_just:
        st.subheader("Justificativa da Decisao (Regras Disparadas)")
        st.caption(
            "Regras de producao ativadas durante o ciclo de inferencia:"
        )

        if res.get("is_fallback"):
            st.warning(
                "Aviso de Fallback: Respostas sem convergencia especifica. "
                "O motor acionou a regra padrao recomendando Desenvolvimento Back-end como base fundamental de logica e dados."
            )

        for regra in res["regras_disparadas"]:
            pontos_badge = f"+{regra['pontos']} pts" if regra["pontos"] > 0 else "Indicador"
            st.markdown(
                f"""
                <div class="rule-box">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
                        <b style="color: #38bdf8; font-size: 0.9rem;">[{regra['id']}] {regra['nome']}</b>
                        <span style="background: #1e293b; color: #94a3b8; font-size: 0.75rem; font-weight: 600; padding: 0.15rem 0.5rem; border-radius: 3px;">{pontos_badge}</span>
                    </div>
                    <div style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.45;">
                        {regra['justificativa']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_rank:
        st.subheader("Classificacao Geral")
        st.caption("Pontuacao acumulada nas 10 trilhas:")

        for i, item in enumerate(res["ranking"]):
            progresso = min(1.0, item["pontos"] / 120.0) if item["pontos"] > 0 else 0.02
            pos = f"#{i+1}"
            cor_pos = "#38bdf8" if i == 0 else "#94a3b8"

            st.markdown(
                f"""
                <div style="margin-bottom: 0.5rem; padding: 0.4rem 0.6rem; border-radius: 4px; background: #0f172a; border: 1px solid #1e293b;">
                    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 0.2rem;">
                        <span style="font-weight: 500; color: #f1f5f9;">
                            <span style="color: {cor_pos}; font-weight: 700;">{pos}</span> {item['nome']}
                        </span>
                        <span style="font-weight: 600; color: {cor_pos};">{item['pontos']} pts</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(progresso)

    st.markdown("---")
    st.button("Refazer Entrevista", on_click=reiniciar_entrevista, type="primary")

else:
    # Renderizacao do Questionario Diagnostico
    st.caption(
        "Selecione as opcoes que melhor representam seu perfil. "
        "As primeiras quatro dimensoes sao obrigatorias; as questoes complementares auxiliam na desambiguacao."
    )

    with st.form("form_entrevista"):
        respostas_temp = {}

        # Agrupamento das perguntas por categoria
        categorias = {}
        for p in PERGUNTAS:
            cat = p["categoria"]
            categorias.setdefault(cat, []).append(p)

        for cat_nome, perguntas_cat in categorias.items():
            st.markdown(f"#### {cat_nome}")

            for p in perguntas_cat:
                p_id = p["id"]
                titulo = p["titulo"] + (" *" if p.get("obrigatoria") else "")
                opcoes = p["opcoes"]
                rotulos = [op["rotulo"] for op in opcoes]
                valores = [op["valor"] for op in opcoes]

                # Determina indice selecionado previamente se houver (padrao None = desmarcado)
                valor_atual = st.session_state["respostas"].get(p_id, None)
                idx_default = (
                    valores.index(valor_atual)
                    if (valor_atual is not None and valor_atual in valores)
                    else None
                )

                escolha = st.radio(
                    label=titulo,
                    options=rotulos,
                    index=idx_default,
                    help=p["ajuda"],
                    key=f"field_{p_id}",
                )

                # Mapeia rotulo de volta para o valor canonico
                if escolha is not None:
                    escolha_idx = rotulos.index(escolha)
                    respostas_temp[p_id] = valores[escolha_idx]
                else:
                    respostas_temp[p_id] = None

            st.write("")

        col_btn1, col_btn2 = st.columns([3, 7])
        with col_btn1:
            submetido = st.form_submit_button(
                "Submeter Perfil",
                type="primary",
                use_container_width=True,
            )

        if submetido:
            # Validacao das respostas obrigatorias
            ausentes = validar_respostas(respostas_temp)
            if ausentes:
                nomes_ausentes = [
                    next((p["titulo"] for p in PERGUNTAS if p["id"] == a), a)
                    for a in ausentes
                ]
                st.error(
                    f"Por favor, responda as dimensoes obrigatorias: {', '.join(nomes_ausentes)}."
                )
            else:
                st.session_state["respostas"] = respostas_temp
                with st.spinner("Processando inferencia..."):
                    resultado = recomendar(respostas_temp)
                    st.session_state["resultado"] = resultado
                st.rerun()
