# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from webservices_flags import (NFSE_AMBIENTE_HOMOLOGACAO,
                               NFSE_AMBIENTE_PRODUCAO,
                               SIAFI_SOROCABA_SP)


WS_NFSE_ENVIO_LOTE = 0
WS_NFSE_CONSULTA_LOTE = 1
WS_NFSE_CANCELAMENTO = 2
WS_NFSE_CONSULTA_NOTA = 3
WS_NFSE_CONSULTA_NFSERPS = 4
WS_NFSE_CONSULTA_SEQUENCIA_RPS = 5


METODO_WS = {
    WS_NFSE_ENVIO_LOTE: {
        'metodo'    : 'enviar',
    },
    WS_NFSE_CONSULTA_LOTE: {
        'metodo'    : 'consultarLote',
    },
    WS_NFSE_CANCELAMENTO: {
        'metodo'    : 'cancelar',
    },
    WS_NFSE_CONSULTA_NOTA: {
        'metodo'    : 'consultarNota',
    },
    WS_NFSE_CONSULTA_NFSERPS: {
        'metodo'    : 'consultarNFSeRps',
    },
    WS_NFSE_CONSULTA_SEQUENCIA_RPS: {
        'metodo'    : 'consultarSequencialRps',
    }
}


CIDADE_SOROCABA_SP = {
    NFSE_AMBIENTE_HOMOLOGACAO: {
        'servidor': 'treinamento.dsfweb.com.br',
        'url'     : 'WsNFe2/LoteRps.jws'
    },
    NFSE_AMBIENTE_PRODUCAO: {
        'servidor': 'www.issdigitalsod.com.br',
        'url'     : 'WsNFe2/LoteRps.jws'
    }
}


CIDADE_WS = {
    SIAFI_SOROCABA_SP: CIDADE_SOROCABA_SP,
}
