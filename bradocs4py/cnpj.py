# -*- coding: utf-8 -*-

import re

from itertools import chain
from random import randint

from .documentoidentificacao import DocumentoIdentificacao

class Cnpj(DocumentoIdentificacao):
	"""docstring for Cnpj"""

	def __init__(self, arg): # type: (str)
		super().__init__(arg)

	def __str__(self):
		"""
		Will format an adequately formatted numbers-only CNPJ string, adding in standard formatting visual
		aid symbols for display.
		If CNPJ string is shorten that 14 digits or contains non-digits characters, returns the raw value
		CNPJ string unformatted.
		"""

		if self.rawValue == None: return str()

		x = self.rawValue

		if not x.isdigit() or len(x) != 14 or len(set(x)) == 1: return self.rawValue

		return '{}.{}.{}/{}-{}'.format(x[:2], x[2:5], x[5:8], x[8:12], x[12:])

	@property
	def isValid(self):
		"""
		Returns whether or not the verifying checksum digits of the given `cnpj` match it's base number.
		Input should be a digit string of proper length.
		"""
		return ValidadorCnpj.validar(self)




class ValidadorCnpj(object):
	"""docstring for ValidadorCnpj"""

	def __validarCnpj(self, arg): # type: (cnpj) -> bool
		return self.__validarStr(arg.rawValue)

	def __validarStr(self, arg): # type: (str) -> bool
		if arg == None:
			return False

		p = re.compile('[^0-9]')
		x = p.sub('', arg)

		if len(x) != 14 or len(set(x)) == 1: return False

		return all(self.__hashDigit(x, i + 13) == int(v) for i, v in enumerate(x[12:]))


	def __hashDigit(self, cnpj, position): # type: (str, int) -> int
		"""
		Will compute the given `position` checksum digit for the `cnpj` input. The input needs to contain
		all elements previous to `position` else computation will yield the wrong result.
		"""

		weighten = chain(range(position - 8, 1, -1), range(9, 1, -1))
		val = sum(int(digit) * weight for digit, weight in zip(cnpj, weighten)) % 11

		return 0 if val < 2 else 11 - val

	@staticmethod
	def validar(arg): # type: (CNPJ) -> bool or  type: (str) -> bool
		v = ValidadorCnpj()

		if type(arg) == Cnpj: return v.__validarCnpj(arg)

		if type(arg) == str: return v.__validarStr(arg)

		return False



class GeradorCnpj(object):

	def __hashdigit(self, cnpj, position):
		"""
		Will compute the given `position` checksum digit for the `cnpj` input. The input needs to contain
		all elements previous to `position` else computation will yield the wrong result.
		"""

		weighten = chain(range(position - 8, 1, -1), range(9, 1, -1))
		val = sum(int(digit) * weight for digit, weight in zip(cnpj, weighten)) % 11

		return 0 if val < 2 else 11 - val

	def __checksum(self, basenum):
		"""
		Will compute the checksum digits for a given CNPJ base number. `basenum` needs to be a digit-string
		of adequate length.
		"""

		digitos = str(self.__hashdigit(basenum, 13))
		digitos += str(self.__hashdigit(basenum + digitos, 14))

		return digitos

	@staticmethod
	def gerar(branch = 1): # type: (int) -> Cnpj
		"""
		Generates a random valid CNPJ digit string. An optional branch number parameter can be given,
		it defaults to 1.
		"""

		branch %= 10000
		branch += int(branch == 0)
		branch = str(branch).zfill(4)
		base = str(randint(0, 99999999)).zfill(8) + branch

		while len(set(base)) == 1: base = str(randint(0, 99999999)).zfill(8) + branch

		gerador = GeradorCnpj()

		return Cnpj(base + gerador.__checksum(base))
