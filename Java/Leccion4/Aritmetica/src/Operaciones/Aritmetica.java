/*

 */
package Operaciones;


public class Aritmetica {
    // Atributos de la clase 
    int a;
    int b;
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b;
        //return resultado;
        return this.a + this.b;
    }
    
    public int sumarConArgumentos(int a, int b){
        this.a = a; //El argumento a se le asigna al atributo this.a
        this.b = b;
        //return a + b;
        return sumarConRetorno();
    }
}