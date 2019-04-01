[![PyPI](https://img.shields.io/pypi/v/BRADocs4Py.svg)](https://pypi.org/project/bradocs4py/)
[![GitHub top language](https://img.shields.io/github/languages/top/namio/BRADocs4Py.svg)](https://github.com/namio/BRADocs4Py.git)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/BRADocs4Py.svg)](https://pypi.org/project/bradocs4py/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/BRADocs4Py.svg)](https://pypi.org/project/bradocs4py/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/BRADocs4Py.svg)](https://pypi.org/project/bradocs4py/)
[![GitHub](https://img.shields.io/github/license/namio/BRADocs4Py.svg)](https://github.com/namio/BRADocs4Py/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/namio/BRADocs4PY.svg)](https://github.com/namio/BRADocs4Py.git)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/namio)

# BRADocs4Py

BRADocs4Py é uma biblioteca que visa fornecer componentes para trabalhar com tipos de dados específicos da realidade brasileira.

Esta biblioteca surgiu mediante a necessidade de se ter tipos específicos que possibilitem lidar com documentos de identificação próprios do Brasil, como é o caso do Cadastro de Pessoa Física (CPF) e do Cadastro Nacional de Pessoa Jurídica (CNPJ).

Além de conter classes que representam o modelo computacional dos principais documentos brasileiros, esta biblioteca também disponibiliza classes que permitem a validação e a geração de números válidos para estes documentos; sendo estas últimas disponibilizadas exclusivamente para fins de testes computacionais.

> This software is coded and documented in portuguese only as it is intended to be used to generate the necessary files for the brazilian government regarding to digital bookkeeping.

## Requisitos

  * python

## Como instalar

    $ pip install bradocs4py

## Objetivos do Projeto

A ideia inicial do projeto e unificar em uma única biblioteca módulos que permitam representar computacionalmente e validar documentos brasileiros - inicialmente CPF e CNPJ, além de permitir a geração de números válidos para estes documentos.

## Compatibilidade do Projeto

O projeto inicialmente suportará apenas Python 3.6.5+.

Outras linguagens de programação poderão ter versões especificas conforme minha disponibilidade de tempo.

## Status do Projeto

O projeto está em fase inicial de desenvolvimento.

| Módulo                              |  Situação       |
|:------------------------------------|:---------------:|
| [DocumentoIdentificacao](#di)       |Funcional        |
| [CPF](#cpf)                         |Funcional        |
| [ValidadorCpf](#vcpf)               |Funcional        |
| [GeradorCpf](#gcpf)                 |Funcional        |
| [Cnpj](#cnpj)                       |Funcional        |
| [ValidadorCnpj](#vcnpj)             |Funcional        |
| [GeradorCnpj](#gcnpj)               |Funcional        |
| [InscricaoEstadual](#ie)            |Funcional        |
| [ValidadorInscricaoEstadual](#vie)  |Funcional        |
| [GeradorInscricaoEstadual](#gie)    |Não implementado |
| [InscricaoSuframa](#is)             |Funcional        |
| [ValidadorSuframa](#vs)             |Funcional        |
| [GeradorSuframa](#gs)               |Funcional        |
| [ChaveAcessoNFe](#chave)            |Funcional        |
| [ValidadorChaveAcessoNFe](#vchave)  |Funcional        |
| [GeradorChaveAcessoNFe](#gchave)    |Funcional        |
| [GTIN](#gtin)                       |Funcional        |
| [ValidadorGTIN](#vgtin)             |Funcional        |
| [GeradorGTIN](#ggtin)               |Funcional        |


### <a name="di"></a> DocumentoIdentificacao

Classe abstrata, não podendo ser instanciada diretamente, serve como base para todas as classes que representam um documento de identificação ou qualquer outro documento brasileiro que necessite de validação.

### <a name="cpf"></a> CPF

Classe usada para representar em código Pyhton um _Cadastro de Pessoa Física_ (CPF); permitindo representá-lo textualmente, com a devida formatação e identificar a sua validade.

#### Utilização

    >>> cpf = CPF('52513127765')
    >>> cpf
    '525.131.277-65'

    >>> cpf.isValid
    True

    >>> cpf.rawValue
    52513127765

    >>> cpf = CPF('abcdefghijk')
    >>> cpf.isValid
    False

    >>> print(cpf)
    abcdefghijk

    >>> print(cpf.rawValue)
    abcdefghijk

> Independente do conteúdo passado ao se criar uma instância de CPF, **sempre** obter-se-á uma instância deste. Caberá consultar a propriedade __isValid__ de uma instância de CPF para verificar se esta é válida ou não.

> A representação textual de uma instância de CPF só será exibida caso esta instância contenha um número válido de CPF; ao contrário será exibida a _string_ utilizada para criá-la.

> Para obter a _string_ utilizada ao instanciar um CPF, basta acessar a propriedade **rawValue** da instância criada.

### <a name="vcpf"></a> ValidadorCpf

Classe responsável por validar uma instância de CPF ou uma _string_ contendo a representação numérica de um CPF.

#### Utilização

    >>> cpf = CPF('abcdefghijk')
    >>> ValidadorCpf.validar(cpf)
    False

    >>> ValidadorCpf.validar('123.456.789-00')
    False

    Foi criado um CPF válido, porém foi digitado um caractere de separação diferente dos caracteres esperados (.-/ ). Mesmo assim, o validador informa tratar-se de um CPF correto
    >>> cpf = CPF('508,697,212-40')
    >>> ValidadorCpf.validar(cpf)
    True

### <a name="gcpf"></a> GeradorCpf

Classe responsável por gerar aleatoriamente um CPF válido.

#### Utilização

    >>> cpf = GeradorCpf.gerar()
    >>> cpf.isValid
    True

### <a name="cnpj"></a> Cnpj

Classe usada para representar em código Pyhton um _Cadastro Nacional de Pessoa Jurídica_ (CNPJ); permitindo representá-lo textualmente, com a devida formatação e identificar a sua validade.

#### Utilização

	>>> cnpj = Cnpj('abcdefghijklmn')
	>>> cnpj.isValid
	False

	>>> cnpj = Cnpj('12345678901234')
	>>> cnpj.isValid
	False

	>>> cnpj = Cnpj('19.658.147/0001-0O')
	>>> cnpj.isValid
	False

	>>> cnpj = Cnpj('19.658.147/0001-00')
	>>> cnpj.isValid
	True

> Independente do conteúdo passado ao se criar uma instância de CNPJ, **sempre** obter-se-á uma instância deste. Caberá consultar a propriedade __isValid__ de uma instância de CNPJ para verificar se esta é válida ou não.

> A representação textual de uma instância de CNPJ só será exibida caso esta instância contenha um número válido de CNPJ; ao contrário será exibida a _string_ utilizada para criá-la.

> Para obter a _string_ utilizada ao instanciar um CNPJ, basta acessar a propriedade **rawValue** da instância criada.

### <a name="vcnpj"></a> ValidadorCnpj

Classe responsável por validar uma instância de CNPJ ou uma _string_ contendo a representação numérica de um CNPJ.

#### Utilização

	>>> cnpj = Cnpj('abcdefghijklmn')
	>>> ValidadorCnpj.validar(cnpj)
	False

	>>> cnpj = Cnpj('19.658.147/0001-0O')
	>>>ValidadorCnpj.validar(cnpj)
	False

	>>> ValidadorCnpj.validar('12345678901234')
	False

	>>> cnpj = Cnpj('34  633 423,0001/60')
	>>> ValidadorCnpj.validar(cnpj)
	True

	>>> ValidadorCnpj.validar('05.692.744/0001-38')
	True

### <a name="gcnpj"></a> GeradorCnpj

Classe responsável por gerar aleatoriamente um CNPJ válido.

#### Utilização

    >>> cnpj = GeradorCnpj.gerar()
    >>> cnpj.isValid
    True

### <a name="is"></a> InscricaoSuframa

Representa o número de inscrição na Superintendência da Zona Franca de Manaus (SUFRAMA)

> A SUFRAMA mantém controle sobre as empresas com insentivo fiscal, identificando-as através do número de _Inscrição SUFRAMA_.

A composição deste indicador é: _SS.NNNN.LLD_, onde:

**SS** representa o __código do setor de atividade__ da empresa, conforme exemplo abaixo:

| Código  | Descrição                   |
| :----:  | :---------------------------|
| 01 e 02 | Cooperativa                 |
| 10 e 11 | Comércio                    |
| 20      | Indústria com projeto pleno |
| 60      | Serviços                    |

**NNNN** número sequencial

**LL** representa o código da licalidade da Unidade Administrativa da Suframa que habilitou a empresa, conforme exemplo abaixo:


| Código | Descrição   |
| :----: | :-----------|
|   01   | Manaus      |
|   10   | Boa Vista   |
|   30   | Porto Velho |

**D** dígito verificador

#### Validação

* Campo numérico com 9 posições (incluindo o dígito verificador).
* Pode iniciar por 0 (zero), mas não pode iniciar por 00.
* Dígito verificador calculado por [__módulo 11__](https://pt.wikipedia.org/wiki/D%C3%ADgito_verificador#Módulo_11 "Método de cálculo do dígito verificador usando Módulo 11"), pesos 2 a 9.

#### Utilização

    >>> x = InscricaoSuframa('01.1234.129')
    >>> x.rawValue
    '011234129'
    >>> print(x)
    01.1234.129
    >>> x.isValid
    False

    >>> x = InscricaoSuframa('101580100')
    >>> x.rawValue
    '101580100'
    >>> print(x)
    10.1580.100
    >>> x.isValid
    True

    >>> x = InscricaoSuframa('1015801OO')
    >>> x.rawValue
    '1015801OO'
    >>> print(x)
    1015801OO
    >>> x.isValid
    False

### <a name="vs"></a> ValidadorSuframa

Valida uma instância de InscricaoSuframa ou uma _string_ contendo a representação numérica de uma Inscrição Suframa.

#### Utilização

    # Validação de uma _string_ representando uma Inscrição Suframa:
    >>> ValidadorSuframa.validar('101580100')
    True

    # Validação de uma _string_ representando uma Inscrição Suframa inválida (contendo caracteres não numéricos):
    >>> ValidadorSuframa.validar('1015801OO')
    False

    # Validação de uma instância de InscriçãoSuframa:
    >>> x = InscricaoSuframa('01.1234.129')
    >>> ValidadorSuframa.validar(x)
    False

### <a name="gs"></a> GeradorSuframa

Gera aleatoriamente uma Inscrição Suframa válida

    >>> x = GeradorSuframa.gerar()
    >>> x.isValid
    True

> **IMPORTANTE**: O __GeradorSuframa__ tem por objetivo ajudar estudantes, programadores, analistas de sistemas e testadores de código a gerar Inscrições Suframa válidas visando auxiliar as rotinas de testes de softwares em desenvolvimento.

> A má utilização dos dados gerados pelo __GeradorSuframa__ é de **total responsabilidade do usuário** desta biblioteca.

> As inscrições são geradas de forma aleatória, respeitando as leis de formação estabelecidas pela SUFRAMA.

### <a name="ie"></a> InscricaoEstadual

Representa, em código Pyhton, uma _Inscrição Estadual_ (IE), ou o registro do contribuinte no cadastro do ICMS mantido pela Receita Estadual; permitindo representá-lo textualmente, com a devida formatação e identificar a sua validade.

#### Utilização

    >>> ie = InscricaoEstadual('613.855.219.926', 'SP')
    >>> ie.isValid
    True
    >>> ie.rawValue
    '613855219926'
    >>> ie.UF
    'SP'
    >>> print(ie)
    613.855.219.926

### <a name="vie"></a> ValidadorInscricaoEstadual

Valida a consistência de uma instância de InscricaoEstadual ou uma _string_ contendo a representação numérica de uma Inscrição Estadual para uma determinada Unidade da Federação, informada juntamente com a representação numérica da IE a qual se deseja validar.

> A validação da Inscrição Estadual para cada Unidade da Federação brasileira, leva em consideração o disposto no [__Convênio 57/59__](http://www.sintegra.gov.br/conv_5795.html "ConvênioICMS 57/59"), como também as orientações e especificidades contidas na página [Conferências de Inscrições Estaduais](http://www.sintegra.gov.br/insc_est.html "Conferência de Inscrições Estaduais") do SINTEGRA.

#### Utilização

    >>> ie = InscricaoEstadual('613.855.219.926', 'SP')
    >>> ValidadorInscricaoEstadual.validar(ie)
    True

    >>> ValidadorInscricaoEstadual.validarStr('207653461', 'RN')
    True
    >>> ValidadorInscricaoEstadual.validarStr('209564598', 'TO')
    False

> **NOTA**: Caso não se deseje utilizar o __ValidadorInscricaoEstadual__, pode-se utilizar o validador específico para uma determinada Unidade da Federação.
<p>Cada Unidade da Federação brasileira possui o seu próprio validador, definido por: **Validador**XX, onde _XX_ deve ser substituído pela sigla da Unidade da Federação desejada.</p>
<p>O Exemplo a seguir mostra como utilizar somente o validador específico para o Ceará, visando validar uma Inscrição Estadual deste Estado:</p>

    >>> from bradocs4py.validadoresie import ValidadorCE
    >>> ValidadorCE.validar('1234567')
    False
    >>> ValidadorCE.validar('50374156-6')
    True

> **IMPORTANTE**: Ao contrário de ValidadorInscricaoEstadual, os validadores específicos de cada UF validam somente uma cadeia de caracteres (_string_) contendo o número representativo da Inscrição Estadual a ser validada.

### <a name="chave"></a> ChaveAcessoNFe

Representa a **Chave de Acesso** de uma Nota Fiscal Eletrônica.

#### <a name="lfchave"></a> Lei de formação de uma Chave de Acesso de NF-e
A Chave de Acesso da Nota Fiscal Eletrônica é representada por uma sequência de 44 caracteres numéricos, devendo ser composta pelos seguintes campos que se encontram dispersos no Layout da NF-e:

* UF - Código da UF do emitente do Documento Fiscal
* AAMM - Ano e mês da emissão da NF-e
* CNPJ - CNPJ do emitente do Documento Fiscal
* Modelo - Modelo do Documento Fiscal
* Série - Série do Documento Fiscal
* Número - Número do Documento Fiscal
* Forma Emissão - Forma de emissão do Documento Fiscal
* Código Numérico - Código numérico que compõe a Chave de Acesso
* DV - Dígito verificados

| Código    |  UF  | AAMM | CNPJ | Modelo | Série | Número | Forma Emissão | Código Numérico |  DV  |
| :--------:|:----:|:----:|:----:|:------:|:-----:|:------:|:-------------:|:---------------:|:----:|
|Quantidade de caracteres |02    |04    |14    |02      |03     |09      |01             |08               |01    |


#### Utilização

    >>> ca = ChaveAcessoNFe('23 1811 06850713000120 55 001 001766829 1 11103011 2')
    >>> ca
    <BRADocs4Py.bradocs4py.chaveacessonfe.ChaveAcessoNFe('23181106850713000120550010017668291111030112')>
    >>> print(ca)
    2318 1106 8507 1300 0120 5500 1001 7668 2911 1103 0112
    >>> ca.rawValue
    '23181106850713000120550010017668291111030112'
    >>> ca.isValid
    True

### <a name="vchave"></a> ValidadorChaveAcessoNFe

Valida a consistência e a integridade de uma instância de [ChaveAcessoNFe](#chave) ou uma _string_ contendo a representação numérica de uma Chave de Acesso, através do cálculo de seu _dígito verificador_.

> O **Dígito Verificador** (DV) visa garantir a integridade da Chave de Acesso, protegendo-a principalmente contra digitações erradas.

#### Utilização

    >>> chave = ChaveAcessoNFe(35181298957205000164667451830925015791400679)
    >>> validarChaveAcessoNFe(chave)
    True
    >>> ValidadorChaveAcessoNFe.validar(52060433009911002506550120000007800267301615)
    True
    >>> ValidadorChaveAcessoNFe.validar('52060433009911002506550120000007800267301615')
    True
    >>> ValidadorChaveAcessoNFe.validar('52060433009911002506550120000007800267301625')
    False

    ou

    >>> validarChaveAcessoNFe(52060433009911002506550120000007800267301615)
    True
    >>> validarChaveAcessoNFe('52060433009911002506550120000007800267301615')
    True
    >>> validarChaveAcessoNFe('52060433009911002506550120000007800267301625')
    False
    >>> validarChaveAcessoNFe(chave)
    True


#### <a name="dvchave"></a> Cálculo do dígito verificador

O dígito verificador da chave de acesso da NF-e é baseado em um cálculo do módulo 11. O módulo 11 de um número é calculado multiplicando-se cada algarismo pela sequência de multiplicadores 2,3,4,5,6,7,8,9,2,3, ..., posicionados da direita para a esquerda.

A somatória dos resultados das ponderações dos algarismos é dividida por 11 e o DV (dígito verificador) será a diferença entre o divisor (11) e o resto da divisão:

DV = 11 - (resto da divisão)

> Quando o resto da divisão for 0 (zero) ou 1 (um), o DV deverá ser igual a 0 (zero).

Exemplo: consideremos a seguinte chave de acesso: _52060433009911002506550120000007800267301615_

Isolando o _dígito verificador_, temos: _5206043300991100250655012000000780026730161_

|**Chave** | 5 | 2 | 0 | 6 | 0 | 4 | 3 | 3 | 0 | 0 | 9 | 9 | 1 | 1 | 0 | 0 | 2 | 5 | 0 | 6 | 5 | 5 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 8 | 0 | 0 | 2 | 6 | 7 | 3 | 0 | 1 | 6 | 1 |
|:------------------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**Pesos** | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
|**Ponderação** |20 | 6 | 0 |54 | 0 |28 |18 |15 | 0 | 0 |18 |81 | 8 | 7 | 0 | 0 | 8 |15 | 0 |54 |40 |35 | 0 | 5 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |35 |32 | 0 | 0 |18 |48 |49 |18 | 0 | 4 |18 | 2 |

**Somatório das ponderações**: _644_

Dividindo o somatório das ponderações por **11**, temos: 644/11 = 58, restando **6**

Como o dígito verificador (DV) = 11 - (resto da divisão), temos: **11 - 6 = 5**

Neste caso o DV da chave de acesso da NF-e é igual a "5".

#### <a name="consistenciachave"></a> Verificação da _consistência_ da Chave de Acesso

Por ter uma [lei de formação](#lfchave) peculiar, o _[ValidadorChaveAcessoNFe](#vchave)_ verifica a consistência de uma determinada chave de acesso, observando:

* se os dois primeiros dígitos correspondem ao código, segundo o IBGE, de uma Unidade da Federação Brasileira;
* Se a data de emissão (**mês** e **ano**) *ano* de emissão não é **posterior** à data (mês e ano) atual;
* Se o *mês* de emissão, que corresponde ao terceiro par de dígitos, corresponde ao valor de um dos meses do ano;
* Se o *CNPJ* do emitente corresponde a um número de CNPJ válido.

> Desta forma, para que uma chave de acesso de NF-e seja válida, esta deverá passar pelo cálculo do Dígito Verificador e pelo teste de consistência.

### <a name="gchave"></a> GeradorChaveAcessoNFe

Gera uma [Chave de Acesso de NF-e](#chave) válida.

A chave gerada pelo [GeradorChaveAcessoNFe](#gchave) obedece às [regras de consistência](#consistenciachave) anteriormente citadas.

#### Utilização

    >>> chave = GeradorChaveAcessoNFe.gerar()
    >>> chave
    <BRADocs4Py.bradocs4py.chaveacessonfe.ChaveAcessoNFe('25181230173834000160651227059459841838300521')>
    >>> print(chave)
    2518 1230 1738 3400 0160 6512 2705 9459 8418 3830 0521
    >>> chave.rawValue
    '25181230173834000160651227059459841838300521'
    >>> chave.isValid
    True

    OU

    >>> chave = gerarChaveAcessoNFe
    >>> chave
    <BRADocs4Py.bradocs4py.chaveacessonfe.ChaveAcessoNFe('11181205001709000125650428522143493956800409')>
    >>> print(chave)
    1118 1205 0017 0900 0125 6504 2852 2143 4939 5680 0409
    >>> chave.rawValue
    '11181205001709000125650428522143493956800409'
    >>> chave.isValid
    True

É possível passar para o gerador qualquer um dos seguintes parâmetros, ou combinação deles:

* UF - [Gera de uma chave de acesso para uma determinada Unidade da Federação](#gchaveUF) Brasileira
* anoEmissao - [Gera uma chave de acesso para um determinado ano de emissão](#gchaveAno)
* mesEmissao - [Gera uma chave de acesso para um determinado mês de emissão](#gchaveMes)
* cnpjEmitente - [Gera uma chave de acesso informando o CNPJ do emitente](#gchaveCNPJ)
* modelo - [Gera uma chame de acesso informando o modelo do documento fiscal](#gchaveModelo)
* serie - [Gera uma chave de acesso informando a série do Documento Fiscal](#gchaveSerie)
* numero - [Gera uma chave de acesso informando o núemro do Documento Fiscal](#gchaveNumero)
* formaEmissao - [Gera uma chave de acesso informando o tipo de emissão da NF-e](#gchaveEmissao)

##### <a name="gchaveUF"></a> Gerar uma chave de acesso para uma determinada Unidade da Federação (23 - Ceará):

    >>> chave = GeradorChaveAcessoNFe.gerar(UF=23)
    >>> chave.rawValue
    '23181200840039000117652898295631409915000755'

##### <a name="gchaveAno"></a> Gerar uma chave de acesso para um determinado ano:

    >>> chave = GeradorChaveAcessoNFe.gerar(anoEmissao=2015)
    >>> chave.rawValue
    '23151289106950000109651490922639616463100456'

##### <a name="gchaveMes"></a> Gerar uma chave de acesso para um determinado mês:

    >>> chave = GeradorChaveAcessoNFe.gerar(mesEmissao=8)
    >>> chave.rawValue
    '15180853477826000102655678711686215463600041'

##### <a name="gchaveMesAno"></a> Gerar uma chave de acesso para uma determinada data (mês e ano) de emissão:

    >>> chave = GeradorChaveAcessoNFe.gerar(anoEmissao=2015, mesEmissao=1)
    >>> chave.rawValue
    '29150139480855000100653317092547617382300904'

##### <a name="gchaveCNPJ"></a> Gerar uma chave de acesso informando o CNPJ do emitente:

    >>> chave = GeradorChaveAcessoNFe.gerar(cnpjEmitente='64802611000136')
    >>> chave.rawValue
    '13181264802611000136651456599176257515300837'

##### <a name="gchaveModelo"></a> Gerar uma chave de acesso de uma NF-e, utilizada nas operações de venda no varejo (modelo de documento fiscal = 55)

    >>> chave = GeradorChaveAcessoNFe.gerar(modelo=55)
    >>> chave.rawValue
    '27181282761929000106555079534095503558300935'

##### <a name="gchaveSerie"></a> Gerar uma chave de acesso para uma NF-e que não possui série:

    >>> chave = GeradorChaveAcessoNFe.gerar(serie=0)
    >>> chave.rawValue
    '13181202699369000160650006987155021599900654'

> Nota: A série também pode ser informada como uma cadeia de caracteres numéricos. No exemplo acima, poderia ter sido informado **'000'** para _serie_.

##### <a name="gchaveNumero"></a> Gerar uma chave de acesso informando o número do documento fiscal:

    >>> chave = GeradorChaveAcessoNFe.gerar(numero=1766829)
    >>> chave.rawValue
    '23181241761925000132652850017668297691400378'

##### <a name="gchaveEmissao"></a> Gerar uma chave de acesso para uma NF-e emitida com Contingência FS-IA, com impressão do DANFE em formulário de segurança (Tipo de emissã0 = 2)

    >>> chave = GeradorChaveAcessoNFe.gerar(formaEmissao=2)
    >>> chave.rawValue
    '51181278981604000153656457693627102018200143'

Isto posto, desejando-se criar uma chave de acesso emitida no Ceará (Código IBGE=23) em Maio de 2016, para o CNPJ 64802611/0001-36, teríamos:

    >>> chave = GeradorChaveAcessoNFe.gerar(formaEmissao=2, UF=23, anoEmissao=2016, mesEmissao=5, cnpjEmitente=64802611000136)
    >>> chave.rawValue
    '23160564802611000136554038699639442073100081'
    >>> chave.isValid
    True

> **Atenção**: a forma abreviada do gerador _(gerarChaveAcessoNFe)_ não permite a passagem de parâmetros.

### <a name="gtin"></a>GTIN

Representa um Número Global do Item Comercial - Global Trade Item Number (GTIN)

O GTIN é um identificador para itens comerciais desenvolvido e controlado pela [GS1][gs1], antiga EAN/UCC. Os GTINs,
anteriormente chamados de códigos EAN, são atribuídos para qualquer item (produto ou serviço) que pode ser
precificado, pedido ou faturado em qualquer ponto da cadeia de suprimentos. O GTIN é utilizado para recuperar
informação pré-definida e abrange desde as matérias primas até produtos acabados. GTIN é um termo “guarda-chuva”
para descrever toda a família de identificação das estruturas de dados GS1 para itens comerciais (produtos e serviços).
Os GTINs podem ter o tamanho de 8, 12, 13 ou 14 dígitos e podem ser construídos utilizando qualquer uma das quatro
estruturas de numeração dependendo da aplicação. O GTIN-8 é codificado no código de barras EAN-8. O GTIN-12 é mais
utilizado no código de barras UPC-A, o GTIN-13 é codificado no EAN-13 e o GTIN-14 no ITF-14.

#### Utilização

##### Criando uma instância de [GTIN](#gtin) a partir de um inteiro

    >>> gtin = GTIN(6291041500213)
    >>> gtin
    <BRADocs4Py.bradocs4py.gtin.GTIN(GTIN-13 '6291041500213')>
    >>> gtin.rawValue
    '6291041500213'
    >>> gtin.isValid
    True

##### Criando uma instância de [GTIN](#gtin) a partir de uma cadeia de caracteres numéricos

    >>> gtin = GTIN('35723189')
    >>> gtin
    <BRADocs4Py.bradocs4py.gtin.GTIN(GTIN-8 '35723189')>
    >>> gtin.rawValue
    '35723189'
    >>> gtin.isValid
    True

### <a name="vgtin"></a> ValidadorGTIN

Valida uma instância de GTIN, um inteiro ou uma cadeia de caracteres numéricos que representa um GTIN, a partir do [cálculo de seu dígito verificador][calculo-digito-gtin], o qual assegura a sua integridade.

> Nota: Muito embora o ValidadorGTIN valide uma instância de GTIN, a validação desta instância pode ser verificada através da sua propriedade _isValid_, conforme exemplos acima.

#### Utilização

    >>> gtin = GTIN('35723189')
    >>> ValidadorGTIN.validar(gtin)
    True
    >>> ValidadorGTIN.validar('3572318')
    False
    >>> ValidadorGTIN.validar('35723189')
    True
    >>> ValidadorGTIN.validar(6291041500213)
    True
    >>> ValidadorGTIN.validar('62910415OO213')
    False

**OU**

    >>> gtin = GTIN('35723189')
    >>> validar_gtin(gtin)
    True
    >>> validar_gtin('3572318')
    False
    >>> validar_gtin('35723189')
    True
    >>> validar_gtin(6291041500213)
    True
    >>> validar_gtin('62910415OO213')
    False

### <a name="ggtin"></a> GeradorGTIN

Gera uma instância de um [GTIN](#gtin) válido.

>IMPORTANTE: Este gerador de GTIN tem como intenção ajudar estudantes, programadores, analistas e testadores de sistemas computacionais a gerar GTINs válidas. Normalmente necessárias parar testar seus softwares em desenvolvimento. A má utilização dos dados aqui gerados é de total responsabilidade do usuário. Os números são gerados de forma aleatória, respeitando as regras de criação de um GTIN.

#### Utilização

    >>> gtin = GeradorGTIN.gerar()
    >>> gtin
    <BRADocs4Py.bradocs4py.gtin.GTIN(GTIN-8 '93490399')>

**ou**

    >>> gtin = gerar_gtin()
    >>> gtin
    <BRADocs4Py.bradocs4py.gtin.GTIN(GTIN-8 '33409382')>

É possível informar ao gerador o tipo de GTIN que se deseja gerar. Para isso, deve-se passar o _GeradorGTIN.TipoGTIN_ desejado.

##### Para gerar um GTIN-8

    >>> gtin = GeradorGTIN.gerar(GeradorGTIN.TipoGTIN.GTIN8)
    >>> gtin
    <BRADocs4Py.bradocs4py.gtin.GTIN(GTIN-8 '33409382')>

Também é possível gerar GTINs chamando diretamente _gerar_gtin_:

    >>> gtin = gerar_gtin(GeradorGTIN.TipoGTIN.GTIN13)
    >>> gtin
    <BRADocs4Py.bradocs4py.gtin.GTIN(GTIN-13 '4332497941617')>

Utilize:

* GeradorGTIN.TipoGTIN.GTIN8 para gerar GTIN-8
* GeradorGTIN.TipoGTIN.GTIN12 para gerar GTIN-12
* GeradorGTIN.TipoGTIN.GTIN13 para gerar GTIN-13, ou
* GeradorGTIN.TipoGTIN.GTIN14 para gerar GTIN-14

> Se não for passado nenhum tipo para o gerador, este gerará sempre um GTIN-8.

[gs1]: https://www.gs1br.org
[calculo-digito-gtin]: https://www.gs1.org/services/how-calculate-check-digit-manually
