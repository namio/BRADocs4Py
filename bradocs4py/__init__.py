# -*- coding: utf-8 -*-

__SIGLAS_ESTADOS_BRASILEIROS__ = 'AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RR|RO|RJ|RN|RS|SC|SP|SE|TO'

from .cnpj import Cnpj, ValidadorCnpj, GeradorCnpj
from .cpf import CPF, ValidadorCpf, GeradorCpf
from .inscricaosuframa import InscricaoSuframa, ValidadorSuframa, GeradorSuframa
from .inscricaoestadual import InscricaoEstadual, ValidadorInscricaoEstadual

__version__ = '1.0.0'


