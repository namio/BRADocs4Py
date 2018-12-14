# -*- coding: utf-8 -*-

import re

class ValidadorPA(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado do Pará, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_PA.html.
	"""

	def __hashDigit(self, insc):
		pesos = range(9, 1, -1)

		val = sum(int(digito) * peso for digito, peso in zip(insc, pesos)) % 11

		return 0 if val < 2 else 11 - val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		p = re.compile('\\b15\\d{7}\\b')

		if not p.match(x): return False

		v = ValidadorPA()

		return v.__hashDigit(x) == int(x[8])