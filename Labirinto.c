#include <stdlib.h>
#include <stdio.h>

void imprimirMapa(char mapa[10][10]);
void mover(char mapa[10][10], char loc, int* x, int* y);
int parede(char mapa[10][10], int* x, int* y);

int main()
{
    int vida = 1;
    char loc;
    char mapa[10][10] = {
        "#@#######",
        "#  ######",
        "##    ###",
        "#####  ##",
        "##### ###",
        "##### ###",
        "##### ###",
        "###   ###",
        "### #####",
        "#########"
    };
    int x = 0, y = 1;

    while (vida == 1) {
        imprimirMapa(mapa);
        printf("Digite a direção que deseja andar (w/a/s/d): ");
        scanf(" %c", &loc);
        mover(mapa, loc, &x, &y);
        vida = parede(mapa, &x, &y);
    }

    return 0;
}

void imprimirMapa(char mapa[10][10]) {
    for (int i = 0; i < 10; i++) {
        printf("%s\n", mapa[i]);
    }
}

void mover(char mapa[10][10], char loc, int* x, int* y) {
    int nx = *x, ny = *y;
    char jogador = '@';
    char vazio = ' ';

    // Calcula a nova posição baseada na entrada do usuário
    if (loc == 'w' && nx > 0) nx--;
    if (loc == 's' && nx < 9) nx++;
    if (loc == 'a' && ny > 0) ny--;
    if (loc == 'd' && ny < 9) ny++;

    // Verifica se a nova posição é um espaço vazio
    if (mapa[nx][ny] == ' ') {
        // Move o jogador
        mapa[*x][*y] = vazio;
        mapa[nx][ny] = jogador;
        *x = nx;
        *y = ny;
    } else if (mapa[nx][ny] == '#') {
        // Atualiza as coordenadas mesmo se o jogador colidir com uma parede
        *x = nx;
        *y = ny;
    }
}

int parede(char mapa[10][10], int* x, int* y) {
    if (mapa[*x][*y] == '#') {
        printf("\nGame Over\n");
        return 0;
    } else {
        return 1;
    }
}
