
package caja; //Package


public class Caja {// Clase publica
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores (Acciones)
    public Caja(){ //Constructor 1 = Vacio
        
    }
    //Constructor con Parametros
    public Caja(int ancho, int alto, int profundo) { //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){ //Metodo para calcular
        return ancho * alto * profundo;
    }
}
