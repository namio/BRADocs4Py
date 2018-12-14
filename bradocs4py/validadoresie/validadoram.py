# -*- coding: utf-8 -*-

import re

class ValidadorAM(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado do Amazonas, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_AM.html.
	"""

	def __hashDigit(self, insc):
		pesos = range(9, 1, -1)

		soma = sum(int(digito) * peso for digito, peso in zip(insc, pesos))

		if soma < 11: return 11 - soma

		val = soma % 11

		return 0 if val < 2 else 11 - val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		if len(x) != 9 or len(set(x)) == 1: return False

		v = ValidadorAM()

		return v.__hashDigit(x) == int(x[8])
