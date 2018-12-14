# -*- coding: utf-8 -*-

import re

from itertools import chain, compress


class ValidadorSP(object):
	"""
	Realiza a validação de cadeias de caracteres (strings) que representam
	o número da Inscrição Estadual do Estado de São Paulo, conforme regras
	encontradas em http://www.sintegra.gov.br/Cad_Estados/cad_SP.html.
	"""

	def __hashDigit(self, insc, posicao):
		pesos = compress(range(1, posicao + 2, 1), [1,0,1,1,1,1,1,1,0,1]) if posicao == 9 else chain(range(posicao - 9, 1, -1), range(posicao - 2, 1, -1))

		val = sum(int(digito) * peso for digito, peso in zip(insc, pesos)) % 11

		return val if val < 10 else val - 10

	@staticmethod
	def validar(numero):
		if numero == None: return False

		p = re.compile('[^0-9P]')
		x = p.sub('', numero)
		validador = ValidadorSP()

		if len(x) == 12:
			return all(validador.__hashDigit(x, 9 if i == 0 else 12) == int(v) for i, v in enumerate([x[8], x[11]]))

		if len(x) == 13:
			return validador.__hashDigit(x[1:9], 9) == int(x[9])

		return False

