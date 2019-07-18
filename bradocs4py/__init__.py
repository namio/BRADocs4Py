# -*- coding: utf-8 -*-

__SIGLAS_ESTADOS_BRASILEIROS__ = 'AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RR|RO|RJ|RN|RS|SC|SP|SE|TO'

from .cnpj import Cnpj, ValidadorCnpj, GeradorCnpj, validar_cnpj
from .cpf import CPF, ValidadorCpf, GeradorCpf, validar_cpf
from .inscricaosuframa import InscricaoSuframa, ValidadorSuframa, GeradorSuframa, validar_inscricao_suframa
from .inscricaoestadual import InscricaoEstadual, ValidadorInscricaoEstadual
from .chaveacessonfe import ChaveAcessoNFe, ValidadorChaveAcessoNFe, GeradorChaveAcessoNFe, validarChaveAcessoNFe, gerarChaveAcessoNFe
from .gtin import GTIN, ValidadorGTIN, GeradorGTIN, gerar_gtin, validar_gtin

__version__ = '1.3.0'


