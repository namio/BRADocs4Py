# -*- coding: utf-8 -*-

import re

from itertools import chain
from random import randint

from . import validadoresie
from . import __SIGLAS_ESTADOS_BRASILEIROS__ as __siglas__
from .documentoidentificacao import DocumentoIdentificacao

class InscricaoEstadual(DocumentoIdentificacao):
	"""docstring for InscricaoEdtadual"""
	def __init__(self, arg, siglaUF): # type: (str, str)
		super(InscricaoEstadual, self).__init__(arg)
		self._siglaUF = siglaUF

	def __repr__(self):
		return "<{0}.{1}({2}, {3!r})>".format(self.__class__.__module__, self.__class__.__name__, self.rawValue, self.UF)

	def __str__(self):
		if self._siglaUF == None or self.rawValue == None: return str()

		x = self.rawValue

		if self._siglaUF == 'AC':
			if len(x) != 13: return self.rawValue

			return '{}.{}.{}/{}-{}'.format(x[:2], x[2:5], x[5:8], x[8:11], x[11:])

		if self._siglaUF == 'AL':
			return self.rawValue

		if self._siglaUF == 'AP':
			return self.rawValue

		if self._siglaUF == 'AM':
			if len(x) != 9: return self.rawValue

			return '{}.{}.{}-{}'.format(x[:2], x[2:5], x[5:8], x[8:])

		if self._siglaUF == 'BA':
			if len(x) == 8:
				return '{}-{}'.format(x[:6], x[6:])
			if len(x) == 9:
				return '{}-{}'.format(x[:7], x[7:])

			return self.rawValue

		if self._siglaUF == 'CE':
			if len(x) != 9: return self.rawValue

			return '{}-{}'.format(x[:8], x[8:])

		if self._siglaUF == 'DF':
			if len(x) != 13: return self.rawValue

			return '{}-{}'.format(x[:11], x[11:])

		if self._siglaUF == 'ES':
			if len(x) != 9: return self.rawValue

			return '{}-{}'.format(x[:8], x[8:])

		if self._siglaUF == 'GO':
			if len(x) != 9: return self.rawValue

			return '{}.{}.{}-{}'.format(x[:2], x[2:5], x[5:8], x[8:])

		if self._siglaUF == 'MA':
			if len(x) != 9: return self.rawValue

			return '{}-{}'.format(x[:8], x[8:])

		if self._siglaUF == 'MT':
			if len(x) != 11: return self.rawValue

			return '{}-{}'.format(x[:10], x[10:])

		if self._siglaUF == 'MS':
			if len(x) != 9: return self.rawValue

			return '{}-{}'.format(x[:8], x[8:])

		if self._siglaUF == 'MG':
			if len(x) != 13: return self.rawValue

			return '{}.{}.{}/{}'.format(x[:3], x[3:6], x[6:9], x[9:])

		if self._siglaUF == 'PA':
			if len(x) != 9: return self.rawValue

			return '{}-{}-{}'.format(x[:2], x[2:8], x[8:])

		if self._siglaUF == 'PB':
			if len(x) != 9: return self.rawValue

			return '{}.{}'.format(x[:8], x[8:])

		if self._siglaUF == 'PR':
			if len(x) != 10: return self.rawValue

			return '{}.{}-{}'.format(x[:3], x[3:8], x[8:])

		if self._siglaUF == 'PE':
			if len(x) != 9: return self.rawValue

			return'{}-{}'.format(x[:7], x[7:])

		if self._siglaUF == 'PI':
			if len(x) != 9: return self.rawValue

			return '{}-{}'.format(x[:8], x[8:])

		if self._siglaUF == 'RJ':
			if len(x) != 8: return self.rawValue

			return '{}.{}.{}-{}'.format(x[:2], x[2:5], x[5:7], x[7:])

		if self._siglaUF == 'RN':
			if len(x) == 9:
				return '{}.{}.{}-{}'.format(x[:2], x[2:5], x[5:8], x[8:])

			if len(x) == 10:
				return '{}.{}.{}.{}-{}'.format(x[:2], x[2], x[3:6], x[6:9], x[9:])

			return self.rawValue

		if self._siglaUF == 'RS':
			if len(x) != 10: return self.rawValue

			return '{}/{}'.format(x[:3], x[3:])

		if self._siglaUF == 'RO':
			if len(x) == 9:
				return '{}.{}-{}'.format(x[:3], x[3:8], x[8:])

			if len(x) == 14:
				return '{}-{}'.format(x[:13], x[13:])

			return self.rawValue

		if self._siglaUF == 'RR':
			if len(x) != 9:
				return self.rawValue

			return '{}-{}'.format(x[:8], x[8:])

		if self._siglaUF == 'SC':
			if len(x) != 9: return self.rawValue

			return '{}.{}.{}'.format(x[:3], x[3:6], x[6:])

		if self._siglaUF == 'SP':
			if len(x) == 12:
				return '{}.{}.{}.{}'.format(x[:3], x[3:6], x[6:9], x[9:])

			if len(x) == 13:
				if x[0] != 'P':
					return self.rawValue

				return '{}-{}.{}/{}'.format(x[0], x[1:9], x[9], x[10:])

			return self.rawValue

		if self._siglaUF == 'SE':
			if len(x) != 9: return self.rawValue

			return '{}-{}'.format(x[:8], x[8:])

		if self._siglaUF == 'TO':
			if len(x) != 11: return self.rawValue

			return '{}-{}'.format(x[:10], x[10:])

		return self.rawValue

	@property
	def isValid(self):
		return ValidadorInscricaoEstadual.validar(self)

	@property
	def UF(self):
		return self._siglaUF



class ValidadorInscricaoEstadual(object):
	"""
	docstring for ValidadorInscricaoEstadual
	"""

	validadores = validadoresie

	@staticmethod
	def validar(inscricaoEstadual):
		return ValidadorInscricaoEstadual.validarStr(inscricaoEstadual.rawValue, inscricaoEstadual.UF)

	@staticmethod
	def validarStr(inscricaoStr, siglaUF):
		if inscricaoStr == None or siglaUF == None:
			return False

		if not siglaUF.upper() in __siglas__:
			return False

		v = ValidadorInscricaoEstadual()

		classeValidador = getattr(v.__class__.validadores, 'Validador' + siglaUF.upper())

		return classeValidador.validar(inscricaoStr)


















