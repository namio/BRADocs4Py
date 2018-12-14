# -*- coding: utf-8 -*-

import re

from itertools import chain

class ValidadorPR(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado do Paraná, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_PR.html.
	"""

	def __hashDigit(self, insc, posicao):
		pesos = chain(range(posicao - 6, 1, -1), range(7, 1, -1))

		val = sum(int(digito) * peso for digito, peso in zip(insc, pesos)) % 11

		return 0 if val < 2 else 11 - val

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9]')
		x = p.sub('', numero)

		if len(x) != 10 or len(set(x)) == 1: return False

		v = ValidadorPR()

		return all(v.__hashDigit(x, i + 9) == int(d) for i, d in enumerate(x[8:]))

