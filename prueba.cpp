#include <iostream>
// Este es un comentario
/* Comentario de varias lineas
    Segunda línea del comentario */
#include <string>
#include <cctype>
#include <math.h>
using namespace std;

int sumar(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    float y = 3.14;
    cout << "Hola, mundo!" << endl;
    // Este es un comentario
    /* Comentario de varias lineas
        Segunda línea del comentario */
    if (x > 0 && y < 10.0) {
        cout << "x es positivo" << endl;
    }
    return 0;
}