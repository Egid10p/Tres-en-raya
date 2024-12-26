# Tres en raya

## Descripcion

Tenemos que hacer el clasico _"Tres en raya"_ o _"Gato"_ con un array.

No se necesario que el usuario pueda introducir sus movimientos desde el terminal, por ahora lo unico que necesitamos es que el programa reciba un array y mediante el determine si gano el jugador 1 "X" o el jugador 2 "O".

## Ideas
Se me ocurre que el programa primero compruebe si el tablero ingresado es posible con las siguientes reglas:
1. Las _"X"_ siempre seran el jugador 1, por lo tanto las _"X"_ siempre empiezan.
2. Dado a que las _"X"_ siempre empiezan no podra haber mas _"O"_ que _"X"_.
3. No puede haber menos de un _"O"_ con respecto a las _"X"_.
4. No puede haber mas de 1 ganador y no puede haber mas de 1 punto por queda jugador.

## Pseudo codigo
