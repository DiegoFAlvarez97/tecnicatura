/*
Proyecto caja:
Ejercicio 1: Crear un proyecto segun las espesificaciones
mostradas a continuacion.
La formula es: volumen= ancho * alto *profundidiad
*/
package caja;


public class PruebaCaja {
    public static void main(String[] args) {
        // Variables locales
        
        int medidaAncho = 3; // Valores ingresados en codigo duro
        int medidaAlto = 5;
        int medidaProf = 6;
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //Le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //Llamamos al metodo
        //Primer resultado
        System.out.println("Resultado volumen de caja 1 = "+ resultado);
        
        Caja caja2 = new Caja(2, 4, 6); //Llamamos al constructor 2 con nuevos argumentos
        //LLamamos con el nuevo objeto al metodo para un nuevo calculo
        System.out.println("Resultado volumen de caja 2 = "+ caja2.calcularVolumen());
    }
}
