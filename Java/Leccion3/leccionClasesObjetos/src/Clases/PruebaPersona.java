
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona();//LLamamos al contructor
        persona1.nombre = "Diego"; //El valor hexagecimal normalmente comienza con 0x
        persona1.apellido = "Alvarez";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = "+ persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Mariano";
        persona2.apellido = "Martinez";
        persona2.obtenerInformacion();
    }
}
