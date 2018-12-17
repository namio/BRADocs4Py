# -*- coding: utf-8 -*-

import re

class DocumentoIdentificacao(object):
	"""docstring for DocumentoIdentificacao"""

	__valor = str()

	def __new__(cls, *args, **kwargs):
		if cls == DocumentoIdentificacao:
			raise Exception('Esta classe não pode ser instanciada diretamente!')
		else:
			#return super(DocumentoIdentificacao, cls).__new__(cls, *args, **kwargs)
			return super().__new__(cls)

	def __init__(self, arg):
		self.__valor = self.__sieve(arg)

	def __repr__(self):
		return "<{0}.{1}({2!r})>".format(self.__class__.__module__, self.__class__.__name__, self.rawValue)

	def __str__(self):
		pass

	@property
	def rawValue(self):
		return self.__valor

	def isValid(self):
		return false

	def __sieve(self, input):
		"""
		Filters out CNPJ formatting symbols. Symbols that are not used in the CNPJ formatting are left
		unfiltered on purpose so that if fails other tests, because their presence indicate that the
		input was somehow corrupted.
		"""
		p = re.compile('[ ./-]')

		return p.sub('', str(input)) if input != None else None





