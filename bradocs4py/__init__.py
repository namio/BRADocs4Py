# -*- coding: utf-8 -*-

__SIGLAS_ESTADOS_BRASILEIROS__ = 'AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RR|RO|RJ|RN|RS|SC|SP|SE|TO'

from .cnpj import Cnpj, ValidadorCnpj, GeradorCnpj
from .cpf import CPF, ValidadorCpf, GeradorCpf
from .inscricaosuframa import InscricaoSuframa, ValidadorSuframa, GeradorSuframa
from .inscricaoestadual import InscricaoEstadual, ValidadorInscricaoEstadual
from .chaveacessonfe import ChaveAcessoNFe, ValidadorChaveAcessoNFe, GeradorChaveAcessoNFe, validarChaveAcessoNFe, gerarChaveAcessoNFe
from .gtin import GTIN, ValidadorGTIN, GeradorGTIN, gerar_gtin, validar_gtin

__version__ = '1.2.2'


