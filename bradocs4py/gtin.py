# -*- coding: utf-8 -*-

import re

from itertools import chain
from random import randint
from enum import IntEnum

from .documentoidentificacao import DocumentoIdentificacao

class GTIN(DocumentoIdentificacao):
	"""
	Representa um Número Global do Item Comercial - Global Trade Item Number (GTIN)

	O GTIN é um identificador para itens comerciais desenvolvido e controlado pela GS1, antiga EAN/UCC. Os GTINs,
	anteriormente chamados de códigos EAN, são atribuídos para qualquer item (produto ou serviço) que pode ser
	precificado, pedido ou faturado em qualquer ponto da cadeia de suprimentos. O GTIN é utilizado para recuperar
	informação pré-definida e abrange desde as matérias primas até produtos acabados. GTIN é um termo “guarda-chuva”
	para descrever toda a família de identificação das estruturas de dados GS1 para itens comerciais (produtos e serviços).
	Os GTINs podem ter o tamanho de 8, 12, 13 ou 14 dígitos e podem ser construídos utilizando qualquer uma das quatro
	estruturas de numeração dependendo da aplicação. O GTIN-8 é codificado no código de barras EAN-8. O GTIN-12 é mais
	utilizado no código de barras UPC-A, o GTIN-13 é codificado no EAN-13 e o GTIN-14 no ITF-14.
	"""

	def __init__(self, arg):
		super().__init__(arg)

	def __str__(self):
		"""
		Retorna uma cadeia de caracteres (string) numéricos que representa o valor de uma instância de GTIN devidamente formatado.
		If GTIN for vazio, retorna uma string vazia.
		Caso o valor passado para criação de uma instância de GTIN contenha caracteres não esperados, ou tenha um tamanho
		inadequado para o padrão aceitável de um GTIN, retorna o valor bruto, passado no ato de criação da instância,
		sem qualquer formatação aplicada.
		"""
		if self.rawValue == None: return str()

		return self.rawValue


	def __repr__(self):

		if self.rawValue and self.rawValue.isdigit() and len(self.rawValue) in (8, 12, 13, 14):
			return "<{0}.{1}(GTIN-{2} {3!r})>".format(self.__class__.__module__, self.__class__.__name__, len(self.rawValue), self.rawValue)

		return super().__repr__()

	@property
	def isValid(self):
		return ValidadorGTIN.validar(self)



class ValidadorGTIN(object):
	"""
	Valida uma instância de GTIN ou uma cadeia de caracteres que representa um número de GTIN.
	"""

	def __call__(self, value):
		return ValidadorGTIN.validar(value)

	@staticmethod
	def validar(arg):
		def __hashDigit(gtin):
			posicao = len(gtin) - 1
			pesos = list('31'*int((len(gtin)-1)/2) + '3') if len(gtin) % 2 == 0 else list('13'*int((len(gtin)-1)/2))

			val = sum(int(digito) * int(peso) for digito, peso in zip(gtin[:posicao], pesos))

			return -((-val)//10)*10 - val

		if type(arg) != GTIN and type(arg) != str and type(arg) != int:
			raise TypeError('%s não corresponde a um tipo válido para uma GTIN' & type(arg).__name__)

		p = re.compile('[^0-9]')
		x = p.sub('', str(arg)) if type(arg) == str or type(arg) == int else p.sub('', arg.rawValue)

		if len(x) not in (8, 12, 13, 14):
			return False

		return __hashDigit(x) == int(x[len(x)-1])

validar_gtin = ValidadorGTIN()

class GeradorGTIN(object):
	"""
	Permite gerar um Global Trade Item Number (GTIN) válida.

	O GTIN é um identificador para itens comerciais desenvolvido e controlado pela GS1, antiga EAN/UCC. Os GTINs,
	anteriormente chamados de códigos EAN, são atribuídos para qualquer item (produto ou serviço) que pode ser
	precificado, pedido ou faturado em qualquer ponto da cadeia de suprimentos. O GTIN é utilizado para recuperar
	informação pré-definida e abrange desde as matérias primas até produtos acabados. GTIN é um termo “guarda-chuva”
	para descrever toda a família de identificação das estruturas de dados GS1 para itens comerciais (produtos e serviços).
	Os GTINs podem ter o tamanho de 8, 12, 13 ou 14 dígitos e podem ser construídos utilizando qualquer uma das quatro
	estruturas de numeração dependendo da aplicação. O GTIN-8 é codificado no código de barras EAN-8. O GTIN-12 é mais
	utilizado no código de barras UPC-A, o GTIN-13 é codificado no EAN-13 e o GTIN-14 no ITF-14.

	IMPORTANTE: Este gerador de GTIN tem como intenção ajudar estudantes, programadores, analistas e testadores de sistemas
	computacionais a gerar GTINs válidas. Normalmente necessárias parar testar seus softwares em desenvolvimento.
	A má utilização dos dados aqui gerados é de total responsabilidade do usuário.
	Os números são gerados de forma aleatória, respeitando as regras de criação de um GTIN.
	"""

	class TipoGTIN(IntEnum):
		GTIN8 = 8
		GTIN12 = 12
		GTIN13 = 13
		GTIN14 = 14

	def __call__(self, tipo=TipoGTIN.GTIN8):
		return GeradorGTIN.gerar(tipo)

	@staticmethod
	def gerar(tipo = TipoGTIN.GTIN8):
		def __hashDigit(base):
			pesos = list('31'*int(len(base)/2) + '3') if (len(base) + 1) % 2 == 0 else list('13'*int(len(base)/2))

			val = sum(int(digito) * int(peso) for digito, peso in zip(base, pesos))

			return -((-val)//10)*10 - val

		base = str(randint(1, int('9'*(tipo.value-2) + '8'))).zfill(tipo.value - 1)

		return GTIN(base + str(__hashDigit(base)))


gerar_gtin = GeradorGTIN()





