# -*- coding: utf-8 -*-

import re

from itertools import chain, compress

class ValidadorAL(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado do Alagoas, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_AL.html.
	"""

	def __hashDigit(self, insc):
		pesos = range(9, 1, -1)

		val = (10 * sum(int(digito) * peso for digito, peso in zip(insc, pesos))) % 11

		return 0 if val == 10 else val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		p = re.compile('\\b24[03578]{1}\\d{6}\\b')

		if not p.match(x): return False

		v = ValidadorAL()

		return v.__hashDigit(x) == int(x[8])

