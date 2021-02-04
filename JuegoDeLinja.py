#!/usr/bin/env python
#-*- coding: UTF-8 -*-

'''
* Integrante 1:
* **** Nombre: Javier Simón Naranjo Herrera
* **** Código: 201255229
* Integrante 2: 
* **** Nombre: Jhon Edinsón Blandón Quintero
* **** Código: 201255414
* Integrante 3: 
* **** Nombre: Álvaro Andrés Loaiza Duque
* **** Código: 201355982
* Archivo 
* **** Nombre: Linja.py
* **** fecha de creación: 03/Mayo/2016
* **** fecha de última modificación: 11/Junio/2016
******************************************************************************************
Control + C -> selecciona una ficha a mover
Control + V -> ubica la ficha seleccionada en la posicion donde se ha desplazado con las techas de desplazamiento
'''

import pygame, sys
import time
from pygame.locals import *

#.. Ancho y alto de la ventana
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

INFINITO_POSITIVO = 9e9999
INFINITO_NEGATIVO = -9e9999
#...
Color_negro = (0, 0, 0)
Color_rojo = (255, 0, 0)

listaTableroNegras = [[7,5],[7,4],[7,3],[7,2],[7,1],[7,0],[6,0],[5,0],[4,0],[3,0],[2,0],[1,0]]
listaTableroRojas = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5]]

listaNodos = []

movHumano = 1
movMaquina = 1

def agregarNodo(tipo, profundidad, estadoFichasNegras, estadoFichasRojas, indexPadre):
	if tipo == "MAX":
		utilidad = INFINITO_POSITIVO
	else:
		utilidad = INFINITO_NEGATIVO
	nodoCreado = [tipo, profundidad, utilidad, estadoFichasNegras, estadoFichasRojas, indexPadre]
	listaNodos.append(nodoCreado)
'''
def crearArbol(profundidad):
	for i in range(1, profundidad):

	# Agregamos el primer nodo
	agregarNodo("MAX", 0, listaTableroNegras, listaTableroRojas, None)

	# Agregamos los nodos de profundidad dos
	for ficha in listaTableroNegras:
'''
def esPosibleMoverFicha(tipoJugador, posActualX, posActualY, posFuturaX, posFuturaY):
	if tipoJugador == "humano":
		if posActualX == 7:
			return False
		else:
			if posFuturaX != 7:
				return (posFuturaX == (posActualX + movHumano)) and (fichasEnFranja(posFuturaX) < 6)
			else:	
				return posFuturaX <= (posActualX + movHumano)
	else:
		if posActualX == 0:
			return False
		else:
			if posFuturaX != 0:
				return (posFuturaX == (posActualX - movMaquina)) and (fichasEnFranja(posFuturaX) < 6)
			else:	
				return posFuturaX >= (posActualX - movMaquina)


class Maquina_IA(pygame.sprite.Sprite):
	def __init__(self):
		self.idFichaMover = 1  # identificador de la ficha a mover por parte de la maquina
		self.indiceX_FichaMover = 2 # indice de la posicion en x donde una ficha ha de ser ubicada por parte de la maquina
		self.indiceY_FichaMover = 3 # indice de la posicion en x donde una ficha ha de ser ubicada por parte de la maquina	 

	def select_id_ficha(self,unaFicha):
		self.idFichaMover =  unaFicha

def fichasEnFranja(numFranja):
    fichasEnFranja = 0
    posicionXFichaNegra0 = listaTableroNegras[0][0]
    posicionXFichaNegra1 = listaTableroNegras[1][0]
    posicionXFichaNegra2 = listaTableroNegras[2][0]
    posicionXFichaNegra3 = listaTableroNegras[3][0]
    posicionXFichaNegra4 = listaTableroNegras[4][0]
    posicionXFichaNegra5 = listaTableroNegras[5][0]
    posicionXFichaNegra6 = listaTableroNegras[6][0]
    posicionXFichaNegra7 = listaTableroNegras[7][0]
    posicionXFichaNegra8 = listaTableroNegras[8][0]
    posicionXFichaNegra9 = listaTableroNegras[9][0]
    posicionXFichaNegra10 = listaTableroNegras[10][0]
    posicionXFichaNegra11 = listaTableroNegras[11][0]

    posicionXFichaRoja0 = listaTableroRojas[0][0]
    posicionXFichaRoja1 = listaTableroRojas[1][0]
    posicionXFichaRoja2 = listaTableroRojas[2][0]
    posicionXFichaRoja3 = listaTableroRojas[3][0]
    posicionXFichaRoja4 = listaTableroRojas[4][0]
    posicionXFichaRoja5 = listaTableroRojas[5][0]
    posicionXFichaRoja6 = listaTableroRojas[6][0]
    posicionXFichaRoja7 = listaTableroRojas[7][0]
    posicionXFichaRoja8 = listaTableroRojas[8][0]
    posicionXFichaRoja9 = listaTableroRojas[9][0]
    posicionXFichaRoja10 = listaTableroRojas[10][0]
    posicionXFichaRoja11 = listaTableroRojas[11][0]

    if posicionXFichaNegra0 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra1 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra2 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra3 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra4 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra5 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra6 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra7 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra8 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra9 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra10 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaNegra11 == numFranja:
        fichasEnFranja += 1

    if posicionXFichaRoja0 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja1 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja2 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja3 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja4 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja5 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja6 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja7 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja8 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja9 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja10 == numFranja:
        fichasEnFranja += 1
    if posicionXFichaRoja11 == numFranja:
        fichasEnFranja += 1

    return fichasEnFranja

def calcularUtilidadNegra():
    fichasEnFranja7 = 0
    fichasEnFranja6 = 0
    fichasEnFranja5 = 0
    fichasEnFranja4 = 0
    posicionXFichaNegra0 = listaTableroNegras[0][0]
    posicionXFichaNegra1 = listaTableroNegras[1][0]
    posicionXFichaNegra2 = listaTableroNegras[2][0]
    posicionXFichaNegra3 = listaTableroNegras[3][0]
    posicionXFichaNegra4 = listaTableroNegras[4][0]
    posicionXFichaNegra5 = listaTableroNegras[5][0]
    posicionXFichaNegra6 = listaTableroNegras[6][0]
    posicionXFichaNegra7 = listaTableroNegras[7][0]
    posicionXFichaNegra8 = listaTableroNegras[8][0]
    posicionXFichaNegra9 = listaTableroNegras[9][0]
    posicionXFichaNegra10 = listaTableroNegras[10][0]
    posicionXFichaNegra11 = listaTableroNegras[11][0]

    if posicionXFichaNegra0 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra1 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra2 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra3 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra4 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra5 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra6 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra7 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra8 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra9 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra10 == 7:
        fichasEnFranja7 += 1
    if posicionXFichaNegra11 == 7:
        fichasEnFranja7 += 1

    if posicionXFichaNegra0 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra1 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra2 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra3 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra4 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra5 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra6 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra7 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra8 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra9 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra10 == 6:
        fichasEnFranja6 += 1
    if posicionXFichaNegra11 == 6:
        fichasEnFranja6 += 1

    if posicionXFichaNegra0 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra1 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra2 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra3 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra4 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra5 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra6 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra7 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra8 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra9 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra10 == 5:
        fichasEnFranja5 += 1
    if posicionXFichaNegra11 == 5:
        fichasEnFranja5 += 1

    if posicionXFichaNegra0 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra1 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra2 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra3 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra4 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra5 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra6 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra7 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra8 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra9 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra10 == 4:
        fichasEnFranja4 += 1
    if posicionXFichaNegra11 == 4:
        fichasEnFranja4 += 1

    utilidadNegra = (fichasEnFranja7*5)+(fichasEnFranja6*3)+(fichasEnFranja5*2)+(fichasEnFranja4)
    return utilidadNegra

def calcularUtilidadRoja():
    fichasEnFranja0 = 0
    fichasEnFranja1 = 0
    fichasEnFranja2 = 0
    fichasEnFranja3 = 0
    posicionXFichaRoja0 = listaTableroRojas[0][0]
    posicionXFichaRoja1 = listaTableroRojas[1][0]
    posicionXFichaRoja2 = listaTableroRojas[2][0]
    posicionXFichaRoja3 = listaTableroRojas[3][0]
    posicionXFichaRoja4 = listaTableroRojas[4][0]
    posicionXFichaRoja5 = listaTableroRojas[5][0]
    posicionXFichaRoja6 = listaTableroRojas[6][0]
    posicionXFichaRoja7 = listaTableroRojas[7][0]
    posicionXFichaRoja8 = listaTableroRojas[8][0]
    posicionXFichaRoja9 = listaTableroRojas[9][0]
    posicionXFichaRoja10 = listaTableroRojas[10][0]
    posicionXFichaRoja11 = listaTableroRojas[11][0]

    if posicionXFichaRoja0 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja1 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja2 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja3 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja4 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja5 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja6 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja7 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja8 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja9 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja10 == 0:
        fichasEnFranja0 += 1
    if posicionXFichaRoja11 == 0:
        fichasEnFranja0 += 1

    if posicionXFichaRoja0 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja1 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja2 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja3 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja4 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja5 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja6 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja7 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja8 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja9 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja10 == 1:
        fichasEnFranja1 += 1
    if posicionXFichaRoja11 == 1:
        fichasEnFranja1 += 1

    if posicionXFichaRoja0 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja1 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja2 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja3 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja4 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja5 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja6 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja7 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja8 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja9 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja10 == 2:
        fichasEnFranja2 += 1
    if posicionXFichaRoja11 == 2:
        fichasEnFranja2 += 1

    if posicionXFichaRoja0 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja1 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja2 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja3 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja4 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja5 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja6 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja7 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja8 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja9 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja10 == 3:
        fichasEnFranja3 += 1
    if posicionXFichaRoja11 == 3:
        fichasEnFranja3 += 1

    utilidadRoja = (fichasEnFranja0*5)+(fichasEnFranja1*3)+(fichasEnFranja2*2)+(fichasEnFranja3)
    return utilidadRoja

def utilidadNeta():
    utilidadNeta = calcularUtilidadNegra()-calcularUtilidadRoja()
    return utilidadNeta

def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("UNIVALLE TULUA - 3743 - Inteligencia Artificial - EL JUEGO DE LINJA")
    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("imagenes/tablerolinja.jpg").convert()

    laMaquina = Maquina_IA()
    
    matriztablero_x = (95, 155, 220, 285, 350, 415, 480, 540)
    matriztablero_y = (110, 150, 190, 230, 270, 310)

    recuadroSelectx = int(matriztablero_x[0]) - 10 # valor inicial en x donde aparecera el recuadro selector
    recuadroSelecty = int(matriztablero_y[0]) - 10 # valor inicial en y donde aparecera el recuadro selector
    recSel_indicex  = 0
    recSel_indicey  = 0

    retardoFlechas = 0.1
    retardoTeclas = 0.2
  
    id_retornado = -1
    turno = 0 # 0 = juega humano 1 = juega maquina
    #........
    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))

     # se muestran lo cambios en pantalla
    pygame.display.flip()

    reloj = pygame.time.Clock()

    # el bucle principal del juego
    while True:

    	
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pulsada = pygame.key.get_pressed()
        #botonI,botonC,botonD = pygame.mouse.get_pressed()
        
        #..................
        if turno == 0: # Turno para que el humano juegue
            if pulsada[K_c]:
                time.sleep(retardoTeclas)
                posActualX=recSel_indicex
                posActualY = recSel_indicey
                if (posActualX == listaTableroRojas[0][0]) and (posActualY == listaTableroRojas[0][1]):
                    id_retornado = 0
                if (posActualX == listaTableroRojas[1][0]) and (posActualY == listaTableroRojas[1][1]):
                    id_retornado = 1
                if (posActualX == listaTableroRojas[2][0]) and (posActualY == listaTableroRojas[2][1]):
                    id_retornado = 2
                if (posActualX == listaTableroRojas[3][0]) and (posActualY == listaTableroRojas[3][1]):
                    id_retornado = 3
                if (posActualX == listaTableroRojas[4][0]) and (posActualY == listaTableroRojas[4][1]):
                    id_retornado = 4
                if (posActualX == listaTableroRojas[5][0]) and (posActualY == listaTableroRojas[5][1]):
                    id_retornado = 5
                if (posActualX == listaTableroRojas[6][0]) and (posActualY == listaTableroRojas[6][1]):
                    id_retornado = 6
                if (posActualX == listaTableroRojas[7][0]) and (posActualY == listaTableroRojas[7][1]):
                    id_retornado = 7
                if (posActualX == listaTableroRojas[8][0]) and (posActualY == listaTableroRojas[8][1]):
                    id_retornado = 8
                if (posActualX == listaTableroRojas[9][0]) and (posActualY == listaTableroRojas[9][1]):
                    id_retornado = 9
                if (posActualX == listaTableroRojas[10][0]) and (posActualY == listaTableroRojas[10][1]):
                    id_retornado = 10   
                if (posActualX == listaTableroRojas[11][0]) and (posActualY == listaTableroRojas[11][1]):
                    id_retornado = 11
        if turno == 0: # Turno para que el humano juegue	
            if pulsada[K_v]:
                time.sleep(retardoTeclas)
                posFuturaX = recSel_indicex
                posFuturaY = recSel_indicey
                if esPosibleMoverFicha("humano", posActualX, posActualY, posFuturaX, posFuturaY):
                    if id_retornado == 0:
                        listaTableroRojas[0][0] = posFuturaX
                        listaTableroRojas[0][1] = posFuturaY
                    if id_retornado == 1:
                        listaTableroRojas[1][0] = posFuturaX
                        listaTableroRojas[1][1] = posFuturaY
                    if id_retornado == 2:
                        listaTableroRojas[2][0] = posFuturaX
                        listaTableroRojas[2][1] = posFuturaY
                    if id_retornado == 3:
                        listaTableroRojas[3][0] = posFuturaX
                        listaTableroRojas[3][1] = posFuturaY
                    if id_retornado == 4:
                        listaTableroRojas[4][0] = posFuturaX
                        listaTableroRojas[4][1] = posFuturaY
                    if id_retornado == 5:
                        listaTableroRojas[5][0] = posFuturaX
                        listaTableroRojas[5][1] = posFuturaY
                    if id_retornado == 6:
                        listaTableroRojas[6][0] = posFuturaX
                        listaTableroRojas[6][1] = posFuturaY
                    if id_retornado == 7:
                        listaTableroRojas[7][0] = posFuturaX
                        listaTableroRojas[7][1] = posFuturaY
                    if id_retornado == 8:
                        listaTableroRojas[8][0] = posFuturaX
                        listaTableroRojas[8][1] = posFuturaY
                    if id_retornado == 9:
                        listaTableroRojas[9][0] = posFuturaX
                        listaTableroRojas[9][1] = posFuturaY
                    if id_retornado == 10:
                        listaTableroRojas[10][0] = posFuturaX
                        listaTableroRojas[10][1] = posFuturaY
                    if id_retornado == 11:
                        listaTableroRojas[11][0] = posFuturaX
                        listaTableroRojas[11][1] = posFuturaY
                    turno = 1  # hace el cambio para darle el turno a la Maquina

        if turno==1:
            id_retornado = laMaquina.idFichaMover
            if id_retornado == 0:
                listaTableroNegras[0][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[0][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 1:
                listaTableroNegras[1][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[1][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 2:
                listaTableroNegras[2][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[2][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 3:
                listaTableroNegras[3][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[3][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 4:
                listaTableroNegras[4][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[4][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 5:
                listaTableroNegras[5][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[5][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 6:
                listaTableroNegras[6][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[6][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 7:
                listaTableroNegras[7][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[7][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 8:
                listaTableroNegras[8][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[8][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 9:
                listaTableroNegras[9][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[9][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 10:
                listaTableroNegras[10][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[10][1] = laMaquina.indiceY_FichaMover
            if id_retornado == 11:
                listaTableroNegras[11][0] = laMaquina.indiceX_FichaMover
                listaTableroNegras[11][1] = laMaquina.indiceY_FichaMover
            turno = 0  # hace el cambio para darle el turno al humano
        #.................            	
        if pulsada[K_LEFT]:
           recSel_indicex -= 1
           if recSel_indicex < 0:
           	  recSel_indicex = 0
           time.sleep(retardoFlechas)
           recuadroSelectx = matriztablero_x[recSel_indicex] - 10
        if pulsada[K_RIGHT]:
           recSel_indicex += 1 
           if recSel_indicex > 7:
           	  recSel_indicex = 7
           time.sleep(retardoFlechas)
           recuadroSelectx  = matriztablero_x[recSel_indicex] - 10
        if pulsada[K_UP]:
           recSel_indicey -= 1
           if recSel_indicey < 0:
           	  recSel_indicey = 0 
           time.sleep(retardoFlechas)
           recuadroSelecty  = matriztablero_y[recSel_indicey] - 10     
        if pulsada[K_DOWN]:
           recSel_indicey += 1
           if recSel_indicey > 5:
           	  recSel_indicey = 5 
           time.sleep(retardoFlechas)
           recuadroSelecty  = matriztablero_y[recSel_indicey]  - 10   
        # Re dibujar los elementos en pantalla
        reloj.tick(30) # tiempo de refresco 
        screen.blit(fondo, (0, 0)) # pone en fondo en la pantalla

        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[0][0]]), int(matriztablero_y[listaTableroNegras[0][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[1][0]]), int(matriztablero_y[listaTableroNegras[1][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[2][0]]), int(matriztablero_y[listaTableroNegras[2][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[3][0]]), int(matriztablero_y[listaTableroNegras[3][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[4][0]]), int(matriztablero_y[listaTableroNegras[4][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[5][0]]), int(matriztablero_y[listaTableroNegras[5][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[6][0]]), int(matriztablero_y[listaTableroNegras[6][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[7][0]]), int(matriztablero_y[listaTableroNegras[7][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[8][0]]), int(matriztablero_y[listaTableroNegras[8][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[9][0]]), int(matriztablero_y[listaTableroNegras[9][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[10][0]]), int(matriztablero_y[listaTableroNegras[10][1]])), 15)
        pygame.draw.circle(screen, Color_negro, (int(matriztablero_x[listaTableroNegras[11][0]]), int(matriztablero_y[listaTableroNegras[11][1]])), 15)

        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[0][0]]), int(matriztablero_y[listaTableroRojas[0][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[1][0]]), int(matriztablero_y[listaTableroRojas[1][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[2][0]]), int(matriztablero_y[listaTableroRojas[2][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[3][0]]), int(matriztablero_y[listaTableroRojas[3][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[4][0]]), int(matriztablero_y[listaTableroRojas[4][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[5][0]]), int(matriztablero_y[listaTableroRojas[5][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[6][0]]), int(matriztablero_y[listaTableroRojas[6][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[7][0]]), int(matriztablero_y[listaTableroRojas[7][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[8][0]]), int(matriztablero_y[listaTableroRojas[8][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[9][0]]), int(matriztablero_y[listaTableroRojas[9][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[10][0]]), int(matriztablero_y[listaTableroRojas[10][1]])), 15)
        pygame.draw.circle(screen, Color_rojo, (int(matriztablero_x[listaTableroRojas[11][0]]), int(matriztablero_y[listaTableroRojas[11][1]])), 15)
        
        pygame.draw.rect(screen, (0, 0, 255), [recuadroSelectx,recuadroSelecty, 15, 15], 3)
        if turno == 0:
        	text = "Humano tu turno."
        else:
        	text = "Maquina tu turno."
        fuente = pygame.font.Font(None, 24)
        mensaje = fuente.render(text, 1, (0, 0, 0))
        screen.blit(mensaje, (15, 10))
        pygame.display.flip()
        
if __name__ == "__main__":
    main()