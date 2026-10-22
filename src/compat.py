"""Módulo de compatibilidade para execução da biblioteca Experta em Python 3.10+.

A biblioteca Experta depende de uma versão do frozendict que tenta acessar
classes abstratas diretamente a partir do módulo `collections`.
No Python 3.10 e 3.12, estas classes foram movidas para `collections.abc`.
Este patch reatribui os atributos necessários para manter compatibilidade total.
"""

import collections
import collections.abc

_COMPAT_NAMES = (
    "Mapping",
    "MutableMapping",
    "Sequence",
    "MutableSequence",
    "Iterable",
    "Callable",
    "Container",
    "Hashable",
    "Sized",
    "Set",
    "MutableSet",
)

for _name in _COMPAT_NAMES:
    if not hasattr(collections, _name) and hasattr(collections.abc, _name):
        setattr(collections, _name, getattr(collections.abc, _name))
