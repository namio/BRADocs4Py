# -*- coding: utf-8 -*-

import re

from itertools import chain
from random import choice, randint

from .documentoidentificacao import DocumentoIdentificacao

class InscricaoSuframa(DocumentoIdentificacao):
	"""
	Número de inscrição na Superintendência da Zona Franca de Manaus (SUFRAMA)
	"""

	def __init__(self, arg): # type: (str)
		super(InscricaoSuframa, self).__init__(arg)

	def __str__(self):
		"""
		Will format an adequately formatted numbers-only CPF string, adding in standard formatting visual
		aid symbols for display.
		If CPF is None, returns an empty string; otherwise, if CPF string is shorten that 11 digits or
		contains non-digits characters, returns the raw value that represents the instance of invalid CPF
		string unformatted.
		"""
		if self.rawValue == None: return str()

		x = self.rawValue

		if not x.isdigit() or len(x) != 9 or len(set(x)) == 1:
			return self.rawValue

		return '{}.{}.{}'.format(x[:2], x[2:6], x[6:])

	@property
	def isValid(self):
		"""
		Returns whether or not the verifying checksum digits of the given `cpf` match it's base number.
		Input should be a digit string of proper length.
		"""
		return ValidadorSuframa.validar(self)



class ValidadorSuframa(object):
	"""
	docstring for ValidadorSuframa
	"""

	def __validarInscricaoSuframa(self, arg): # type: (InscricaoSuframa) -> bool
		return self.__validarStr(arg.rawValue)


	def __validarStr(self, arg): # type: (str) -> bool
		if arg == None:
			return False

		p = re.compile('[^0-9]')
		x = p.sub('', arg)

		if len(x) != 9 or len(set(x)) == 1: return False

		p = re.compile('[0126][012].?\\d{4}.?[013][10]\\d')

		if not p.match(x): return False

		return all(self.__hashDigit(x, i + 9) == int(v) for i, v in enumerate(x[8:]))


	def __hashDigit(self, num, position): # type: (str, int) -> int
		"""
		Will compute the given `position` checksum digit for the `cpf` input. The input needs to contain all
		elements previous to `position` else computation will yield the wrong result.
		"""

		val = sum(int(digit) * weight for digit, weight in zip(num, range(position, 1, -1))) % 11

		return 0 if val < 2 else 11 - val


	@staticmethod
	def validar(arg):

		v = ValidadorSuframa()

		if type(arg) == InscricaoSuframa: return v.__validarInscricaoSuframa(arg)

		if type(arg) == str: return v.__validarStr(arg)

		return False



class GeradorSuframa(object):
	"""
	docstring for GeradorSuframa
	"""

	def __hashDigit(self, num, position): # type: (str, int) -> int
		"""
		Will compute the given `position` checksum digit for the `cpf` input. The input needs to contain all
		elements previous to `position` else computation will yield the wrong result.
		"""

		val = sum(int(digit) * weight for digit, weight in zip(num, range(position, 1, -1))) % 11

		return 0 if val < 2 else 11 - val


	def __checksum(self, baseNum): # type: (str) -> str
		"""
		Will compute the checksum digits for a given CPF base number. `basenum` needs to be a digit-string
		of adequate length.
		"""
		return str(self.__hashDigit(baseNum, 9))


	@staticmethod
	def gerar(): # type: () -> InscricaoSuframa
		"""
		Gera aleatoriamente uma inscrição SUFRAMA válida, para fins de testes de softwares em desenvolvimento
		"""

		base = choice(['01','02','10','11','20','60'])
		seq = str(randint(1, 9998)).zfill(4)

		while len(set(seq)) == 1:
			seq = str(randint(1, 9998)).zfill(4)

		base += seq
		base += choice(['01','10','30'])

		g = GeradorSuframa()

		return InscricaoSuframa(base + g.__checksum(base))



