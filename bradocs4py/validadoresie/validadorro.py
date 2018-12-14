# -*- coding: utf-8 -*-

import re

from itertools import chain

class ValidadorRO(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado de Rondônia, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_RO.html.
	"""

	def __hashDigit(self, insc):
		pesos = chain(range(len(insc) - 8, 1, -1), range(9, 1, -1))

		val = sum(int(digito) * peso for digito, peso in zip(insc, pesos)) % 11

		return 0 if val < 2 else 11 - val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		# Contempla a alteração realiozada a partir de 01/08/2000
		if len(x) == 9: x = x[3:].zfill(14)

		if len(x) != 14 or len(set(x)) == 1: return False

		v = ValidadorRO()

		return v.__hashDigit(x) == int(x[13])
