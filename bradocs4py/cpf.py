# -*- coding: utf-8 -*-

import re

from itertools import chain
from random import randint

from .documentoidentificacao import DocumentoIdentificacao

class CPF(DocumentoIdentificacao):
	"""docstring for CPF"""

	def __init__(self, arg): # type: (str)
		super().__init__(arg)

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

		if not x.isdigit() or len(x) != 11 or len(set(x)) == 1:
			return self.rawValue

		return '{}.{}.{}-{}'.format(x[:3], x[3:6], x[6:9], x[9:])

	@property
	def isValid(self):
		"""
		Returns whether or not the verifying checksum digits of the given `cpf` match it's base number.
		Input should be a digit string of proper length.
		"""
		return ValidadorCpf.validar(self)



class ValidadorCpf(object):

	def __validarCpf(self, arg):  # type: (CPF) -> bool
		return self.__validarStr(arg.rawValue)

	def __validarStr(self, arg):  # type: (str) -> bool

		if arg == None:
			return False

		p = re.compile('[^0-9]')
		x = p.sub('', arg)

		if len(x) != 11 or len(set(x)) == 1: return False

		return all(self.__hashdigit(x, i + 10) == int(v) for i, v in enumerate(x[9:]))


	def __hashdigit(self, cpf, position):  # type: (str, int) -> int
		"""
		Will compute the given `position` checksum digit for the `cpf` input. The input needs to contain all
		elements previous to `position` else computation will yield the wrong result.
		"""

		val = sum(int(digit) * weight for digit, weight in zip(cpf, range(position, 1, -1))) % 11

		return 0 if val < 2 else 11 - val

	@staticmethod
	def validar(arg):  # type: (CPF) -> bool or  type: (str) -> bool
		v = ValidadorCpf()

		if type(arg) == CPF: return v.__validarCpf(arg)

		if type(arg) == str: return v.__validarStr(arg)

		return False



class GeradorCpf(object):
	"""docstring for GeradorCpf"""

	def __hashDigit(self, cpf, position): # type: (str, int) -> int
		"""
		Will compute the given `position` checksum digit for the `cpf` input. The input needs to contain
		all elements previous to `position` else computation will yield the wrong result.
		"""

		val = sum(int(digit) * weight for digit, weight in zip(cpf, range(position, 1, -1))) % 11

		return 0 if val < 2 else 11 - val

	def __checksum(self, basenum): # type: (str) -> str
		"""
		Will compute the checksum digits for a given CPF base number. `basenum` needs to be a digit-string
		of adequate length.
		"""
		digits = str(self.__hashDigit(basenum, 10))
		digits += str(self.__hashDigit(basenum + digits, 11))

		return digits

	@staticmethod
	def gerar(): # type: () -> CPF
		"""
		Generates a random valid CPF
		"""
		base = str(randint(1, 999999998)).zfill(9)

		while len(set(base)) == 1: base = str(randint(1, 999999998)).zfill(9)

		gerador = GeradorCpf()

		return CPF(base + gerador.__checksum(base))
