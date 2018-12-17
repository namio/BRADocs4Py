# -*- coding: utf-8 -*-

import re

from datetime import datetime
from itertools import chain
from random import randint

from .cnpj import GeradorCnpj, ValidadorCnpj
from .documentoidentificacao import DocumentoIdentificacao

class ChaveAcessoNFe(DocumentoIdentificacao):
	"""docstring for ChaveAcessoNFe"""

	def __init__(self, arg): # type: (str)
		super().__init__(arg)

	def __str__(self):
		"""
		Will format an adequately formatted numbers-only ChaveAcessoNFe string, adding in standard formatting visual
		aid symbols for display.
		If ChaveAcessoNFe is None, returns an empty string; otherwise, if ChaveAcessoNFe string is shorten that 11 digits or
		contains non-digits characters, returns the raw value that represents the instance of invalid CPF
		string unformatted.
		"""

		if self.rawValue == None: return str()

		x = self.rawValue

		if not x.isdigit() or len(x) != 44 or len(set(x)) == 1:
			return self.rawValue

		return '{} {} {} {} {} {} {} {} {} {} {}'.format(x[:4], x[4:8], x[8:12], x[12:16], x[16:20], x[20:24], x[24:28], x[28:32], x[32:36], x[36:40], x[40:44])

	@property
	def isValid(self):
		"""
		Returns whether or not the verifying checksum digits of the given `cpf` match it's base number.
		Input should be a digit string of proper length.
		"""
		return ValidadorChaveAcessoNFe.validar(self)



class ValidadorChaveAcessoNFe(object):
	"""
	Valida uma instância de ChaveAcessoNFe ou uma cadeia de caracteres (string) que representa uma Chave de Acesso de uma NF-e
	"""

	def __call__(self, value):
		return ValidadorChaveAcessoNFe.validar(value)

	@staticmethod
	def validar(arg):  # type: (ChaveAcessoNFe) -> bool or  type: (str) -> bool

		def __hashDigit(chave):
			pesos = chain(range(4,1,-1), list(range(9,1,-1))*5)

			val = sum(int(digito) * peso for digito, peso in zip(chave, pesos)) % 11

			return 0 if val < 2 else 11 - val

		if type(arg) != ChaveAcessoNFe and type(arg) != str and type(arg) != int:
			raise TypeError('%s não corresponde a um tipo válido para uma ChaveAcessoNFe' & type(arg).__name__)

		p = re.compile('[^0-9]')
		x = p.sub('', str(arg)) if type(arg) == str or type(arg) == int else p.sub('', arg.rawValue)

		if len(x) != 44 or len(set(x)) == 1:
			return False

		# 23 1811 06850713000120 55 001 001766829 1 11103011 2

		p = re.compile(r'^1[1-7]|2[1-9]|3([1-3]|5)|4[1-3]|5[0-3]$')

		if not p.match(str(x)[:2]):
			"""
			O primeiro par de dígitos da chave deve corresponder ao código, segundo o IBGE, de uma das Unidades
			Federativas do Brasil.
			"""
			return False

		if int(x[4:6]) not in range(1,13):
			"""
			O terceiro par de dígitos deve corresponder ao valor de um dos meses do ano
			"""
			return False

		if datetime.strptime(x[2:6], '%y%m').year > datetime.now().year:
			"""
			O ano de emissão do documento fiscal deve ser anterior ao ano em curso
			"""
			return False

		if datetime.strptime(x[2:6], '%y%m').month > datetime.now().month:
			"""
			O mês de emissão do documento fiscal deve ser anterior ao mês em curso
			"""
			return False

		if not ValidadorCnpj.validar(x[6:20]):
			"""
			Os 14 próximos caracteres numéricos devem corresponder a um CNPJ válido
			"""
			return False

		if __hashDigit(x) != int(x[43]):
			"""
			O dígito verificador calculado para a chave da NF-e deve corresponder ao informado
			"""
			return False

		return True

validarChaveAcessoNFe = ValidadorChaveAcessoNFe()


class GeradorChaveAcessoNFe(object):
	"""
	Permite gerar uma Chave de Acesso de uma NF-e, considerando a sua Lei de Formação

	A Chave de Acesso da Nota Fiscal Eletrônica é representada por uma sequência de 44 caracteres numéricos, devendo ser
	composta pelos seguintes campos que se encontram dispersos no Layout da NF-e:

	* UF - Código da UF do emitente do Documento Fiscal (2 caracteres numéricos)
	* AAMM - Ano e mês da emissão da NF-e (4 caracteres numéricos)
	* CNPJ - CNPJ do emitente do Documento Fiscal (14 caracteres numéricos)
	* Modelo - Modelo do Documento Fiscal (2 caracteres numéricos)
	* Série - Série do Documento Fiscal (3 caracteres numéricos)
	* Número - Número do Documento Fiscal (9 caracteres numéricos)
	* Forma Emissão - Forma de emissão do Documento Fiscal (1 caractere numérico)
	* Código Numérico - Código numérico que compõe a Chave de Acesso (8 caracteres numéricos)
	* DV - Dígito verificados (1 caractere numérico)

	O Dígito Verificador irá garantir a integridade da Chave de Acesso, protegendo-a principalmente contra digitações erradas.

	O GeradorChaveAcessoNFe, considera cada conjunto de caracteres numéricos que compõe a chave de acesso de forma independente,
	iso é, os dois primeiros caracteres numéricos não serão gerados aleatoriamente, uma vez que nem todo par de dígitos representam
	uma Unidade da Federação Brasileira, como é o caso do número 30 ou 34 - Não existe, até o momento de lançamento deste
	código, uma UF brasileira com algum desses códigos. De igual forma, a sequência de 14 caracteres que corresponde ao
	CNPJ do emitente, corresponderá a um número de CNPJ válido.
	"""

	def __call__(self, **kwargs):
		return GeradorChaveAcessoNFe.gerar(**kwargs)


	@staticmethod
	def gerar(**kwargs):

		def __hashDigit(chave):
			pesos = chain(range(4,1,-1), list(range(9,1,-1))*5)

			val = sum(int(digito) * peso for digito, peso in zip(chave, pesos)) % 11

			return 0 if val < 2 else 11 - val

		_estados_brasileiros = [11,12,13,14,15,16,17,21,22,23,24,25,26,27,28,29,31,32,33,35,41,42,43,50,51,52,53]
		_formas_emissao = (
			(1, 'Emissão normal (não em contingência)'),
			(2, 'Contingência FS-IA, com impressão do DANFE em formulário de segurança'),
			(3, 'Contingência SCAN (Sistema de Contingência do Ambiente Nacional)'),
			(4, 'Contingência DPEC (Declaração Prévia da Emissão em Contingência)'),
			(5, 'Contingência FS-DA, com impressão do DANFE em formulário de segurança'),
			(6, 'Contingência SVC-AN (SEFAZ Virtual de Contingência do AN)'),
			(7, 'Contingência SVC-RS (SEFAZ Virtual de Contingência do RS);'),
			(9, 'Contingência off-line da NFC-e (as demais opções de contingência são válidas também para a NFC-e)')
		)

		_uf = str(kwargs.pop('UF', _estados_brasileiros[randint(0,26)]))
		_ano = kwargs.pop('anoEmissao', datetime.now().year)
		_mes = kwargs.pop('mesEmissao', datetime.now().month)
		_cnpj = kwargs.pop('cnpjEmitente', GeradorCnpj.gerar().rawValue)
		_modelo = str(kwargs.pop('modelo', 55 + 10 * randint(0,1)))
		_serie = str(kwargs.pop('serie', randint(0,999))).zfill(3)
		_numeroDF = str(kwargs.pop('numero', randint(1,999999999))).zfill(9)
		_formaEmissao = str(kwargs.pop('formaEmissao', _formas_emissao[randint(0,7)][0]))

		branch = randint(0,99)
		branch %= 10000
		branch += int(branch == 0)
		branch = str(branch).zfill(4)

		_codigoNumerico = str(randint(0, 9999)).zfill(4) + branch

		while len(set(_codigoNumerico)) == 1: _codigoNumerico = str(randint(0, 9999)).zfill(4) + branch

		base = "%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nNF)s%(tpEmis)s%(cNF)s"%{
				'uf': _uf,
				'ano': datetime(_ano, _mes, datetime.now().day).strftime('%y'),
				'mes': datetime(_ano, _mes, datetime.now().day).strftime('%m'),
				'cnpj': _cnpj,
				'mod': _modelo,
				'serie': _serie,
				'nNF': _numeroDF,
				'tpEmis': _formaEmissao,
				'cNF': _codigoNumerico
		}

		return ChaveAcessoNFe(base + str(__hashDigit(base)))



gerarChaveAcessoNFe = GeradorChaveAcessoNFe.gerar()




