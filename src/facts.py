"""Definição das classes Fact da base de conhecimento Experta."""

from src.compat import *  # noqa: F401, F403
from experta import Fact


class PerfilUsuario(Fact):
    """Fato primário que encapsula as respostas fornecidas pelo usuário na entrevista."""
    pass


class Indicador(Fact):
    """Fato intermediário (Camada 2) deduzido a partir da combinação de respostas do usuário."""
    pass


class Pontuacao(Fact):
    """Fato de pontuação atribuída a uma trilha específica por uma regra de produção."""
    pass


class RegraDisparada(Fact):
    """Fato que registra a ativação formal de uma regra SE-ENTÃO no motor."""
    pass


class Recomendacao(Fact):
    """Fato terminal (Camada 5) contendo a trilha final recomendada e o relatório de motivos."""
    pass
