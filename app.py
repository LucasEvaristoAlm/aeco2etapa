"""Interface Web do Sistema Especialista: Consultor Inteligente de Carreiras em TI.

Desenvolvido com Streamlit, utilizando o motor de inferência Experta.
Atividade Acadêmica de Inteligência Artificial — Ciência da Computação, UNIPAC Barbacena.
"""

import streamlit as st
import src.compat  # noqa: F401
from src.questions import PERGUNTAS, DIMENSOES_OBRIGATORIAS
from src.engine_runner import recomendar, validar_respostas

# Configuração da página Streamlit
st.set_page_config(
    page_title="Consultor Inteligente de Carreiras em TI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilização CSS personalizada para visual moderno e profissional
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 2.2rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }

    .main-title {
        color: #f8fafc;
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.025em;
        margin-bottom: 0.5rem;
    }

    .main-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .academic-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.15);
        border: 1px solid rgba(56, 189, 248, 0.35);
        color: #38bdf8;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }

    .result-card {
        background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
        border: 2px solid #38bdf8;
        border-radius: 20px;
        padding: 2.2rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 30px -10px rgba(56, 189, 248, 0.2);
    }

    .track-badge {
        background: #38bdf8;
        color: #0f172a;
        font-weight: 800;
        font-size: 0.85rem;
        padding: 0.3rem 0.9rem;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .rule-box {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid #334155;
        border-left: 4px solid #38bdf8;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.85rem;
    }

    .tech-pill {
        display: inline-block;
        background: rgba(148, 163, 184, 0.15);
        border: 1px solid rgba(148, 163, 184, 0.25);
        color: #e2e8f0;
        padding: 0.25rem 0.75rem;
        border-radius: 6px;
        font-size: 0.82rem;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
        font-weight: 500;
    }

    .stButton>button {
        border-radius: 10px;
        font-weight: 700;
        padding: 0.65rem 1.75rem;
        transition: all 0.2s ease-in-out;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inicialização do estado de sessão
if "respostas" not in st.session_state:
    st.session_state["respostas"] = {}

if "resultado" not in st.session_state:
    st.session_state["resultado"] = None


def reiniciar_entrevista():
    """Limpa as respostas e os resultados armazenados na sessão."""
    st.session_state["respostas"] = {}
    st.session_state["resultado"] = None
    st.rerun()


# Cabeçalho Principal
st.markdown(
    """
    <div class="main-header">
        <div class="main-title">🧭 Consultor Inteligente de Carreiras em TI</div>
        <div class="main-subtitle">
            Sistema Especialista Baseado em Regras com motor de inferência <b>Experta (Forward Chaining)</b>.<br>
            Entrevista dinâmica diagnóstica para identificação precisa do seu perfil vocacional entre 10 trilhas profissionais.
        </div>
        <div class="academic-badge">
            🎓 Inteligência Artificial • Ciência da Computação • UNIPAC Barbacena
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Barra lateral informativa
with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/feathericons/feather/master/icons/cpu.svg",
        width=54,
    )
    st.markdown("### ⚙️ Detalhes do Motor")
    st.markdown(
        """
        - **Motor de Regras:** `Experta 1.9.4`
        - **Estratégia:** Encadeamento para Frente (*Forward Chaining*)
        - **Base de Conhecimento:** 38 Regras `@Rule` ativas
        - **Trilhas Mapeadas:** 10 trilhas formais
        - **Desambiguação:** DS × DE, Back × Cloud × DevOps, Front × Mobile, QA e Produto.
        """
    )
    st.divider()

    st.markdown("### 📋 Escopo das 10 Trilhas")
    st.markdown(
        """
        1. ⚙️ Back-end
        2. 🎨 Front-end & UI/UX
        3. 🧠 Ciência de Dados & ML
        4. 🚰 Engenharia de Dados
        5. 🛡️ Cibersegurança
        6. 🚀 DevOps & SRE
        7. ☁️ Computação em Nuvem
        8. 📱 Desenvolvimento Mobile
        9. 🧪 Engenharia de QA & Testes
        10. 📊 Gestão de Produtos (PM)
        """
    )
    st.divider()

    if st.button("🔄 Reiniciar / Nova Consulta", use_container_width=True):
        reiniciar_entrevista()


# Se já temos resultado calculado, exibe o diagnóstico e as justificativas
if st.session_state["resultado"] is not None:
    res = st.session_state["resultado"]
    trilha = res["trilha_dados"]

    st.markdown(
        f"""
        <div class="result-card">
            <span class="track-badge">Trilha Recomendada com Maior Afinidade</span>
            <h1 style="color: #f8fafc; margin-top: 0.8rem; margin-bottom: 0.5rem;">
                {trilha['icone']} {res['trilha_nome']}
            </h1>
            <p style="color: #38bdf8; font-size: 1.15rem; font-weight: 500; margin-bottom: 1.2rem;">
                {trilha['resumo']}
            </p>
            <p style="color: #cbd5e1; font-size: 1.02rem; line-height: 1.7; margin-bottom: 1.5rem;">
                {trilha['descricao']}
            </p>
            <div style="margin-bottom: 1rem;">
                <b style="color: #94a3b8; font-size: 0.9rem; text-transform: uppercase;">Tecnologias Recomendadas para Iniciar:</b><br>
                <div style="margin-top: 0.5rem;">
                    {''.join([f'<span class="tech-pill">{tech}</span>' for tech in trilha['tecnologias_chave']])}
                </div>
            </div>
            <div>
                <b style="color: #94a3b8; font-size: 0.9rem; text-transform: uppercase;">Soft Skills Relevantes:</b><br>
                <div style="margin-top: 0.5rem;">
                    {''.join([f'<span class="tech-pill" style="border-color: #38bdf8;">{skill}</span>' for skill in trilha['soft_skills']])}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_just, col_rank = st.columns([6, 4])

    with col_just:
        st.subheader("🔍 Justificativa Transparente (Regras Disparadas)")
        st.caption(
            "O motor de inferência SE-ENTÃO registrou a ativação das seguintes regras lógicas durante o ciclo de forward chaining:"
        )

        if res.get("is_fallback"):
            st.warning(
                "⚠️ **Aviso de Fallback Ativado:** Suas respostas indicaram perfil indeciso ou iniciante amplo. "
                "O motor acionou a regra padrão recomendando Desenvolvimento Back-end como alicerce fundamental de lógica e dados."
            )

        for regra in res["regras_disparadas"]:
            pontos_badge = f"+{regra['pontos']} pts" if regra["pontos"] > 0 else "Indicador lógico"
            st.markdown(
                f"""
                <div class="rule-box">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
                        <b style="color: #38bdf8; font-size: 0.95rem;">[{regra['id']}] {regra['nome']}</b>
                        <span style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; font-size: 0.78rem; font-weight: 700; padding: 0.2rem 0.6rem; border-radius: 4px;">{pontos_badge}</span>
                    </div>
                    <div style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.5;">
                        {regra['justificativa']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_rank:
        st.subheader("📊 Ranking Geral de Afinidade")
        st.caption("Pontuações acumuladas nas 10 trilhas profissionais:")

        for i, item in enumerate(res["ranking"]):
            progresso = min(1.0, item["pontos"] / 120.0) if item["pontos"] > 0 else 0.02
            pos = f"#{i+1}"
            cor_pos = "#38bdf8" if i == 0 else "#94a3b8"

            st.markdown(
                f"""
                <div style="margin-bottom: 0.6rem; padding: 0.5rem; border-radius: 8px; background: rgba(30, 41, 59, 0.4);">
                    <div style="display: flex; justify-content: space-between; font-size: 0.9rem; margin-bottom: 0.25rem;">
                        <span style="font-weight: 600; color: #f1f5f9;">
                            <span style="color: {cor_pos}; font-weight: 800;">{pos}</span> {item['icone']} {item['nome']}
                        </span>
                        <span style="font-weight: 700; color: {cor_pos};">{item['pontos']} pts</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(progresso)

    st.markdown("---")
    st.button("📝 Refazer a Entrevista", on_click=reiniciar_entrevista, type="primary")

else:
    # Renderização da Entrevista Diagnóstica
    st.info(
        "💡 **Instruções:** Responda às perguntas abaixo com base nas suas preferências atuais. "
        "As 4 primeiras dimensões são essenciais; as demais complementam o diagnóstico para eliminar ambiguidades."
    )

    with st.form("form_entrevista"):
        respostas_temp = {}

        # Agrupamento das perguntas por categoria
        categorias = {}
        for p in PERGUNTAS:
            cat = p["categoria"]
            categorias.setdefault(cat, []).append(p)

        for cat_nome, perguntas_cat in categorias.items():
            st.markdown(f"#### 📌 {cat_nome}")

            for p in perguntas_cat:
                p_id = p["id"]
                titulo = p["titulo"] + (" *" if p.get("obrigatoria") else "")
                opcoes = p["opcoes"]
                rotulos = [op["rotulo"] for op in opcoes]
                valores = [op["valor"] for op in opcoes]

                # Determina índice selecionado previamente se houver
                valor_atual = st.session_state["respostas"].get(p_id, valores[0])
                idx_default = valores.index(valor_atual) if valor_atual in valores else 0

                escolha = st.radio(
                    label=titulo,
                    options=rotulos,
                    index=idx_default,
                    help=p["ajuda"],
                    key=f"field_{p_id}",
                )

                # Mapeia rótulo de volta para o valor canônico
                escolha_idx = rotulos.index(escolha)
                respostas_temp[p_id] = valores[escolha_idx]

            st.write("")

        col_btn1, col_btn2 = st.columns([3, 7])
        with col_btn1:
            submetido = st.form_submit_button(
                "🚀 Obter Recomendação de Carreira",
                type="primary",
                use_container_width=True,
            )

        if submetido:
            # Validação das respostas obrigatórias
            ausentes = validar_respostas(respostas_temp)
            if ausentes:
                st.error(
                    f"Por favor, responda a todas as dimensões obrigatórias: {', '.join(ausentes)}."
                )
            else:
                st.session_state["respostas"] = respostas_temp
                with st.spinner("Motor Experta processando encadeamento para frente..."):
                    resultado = recomendar(respostas_temp)
                    st.session_state["resultado"] = resultado
                st.rerun()
