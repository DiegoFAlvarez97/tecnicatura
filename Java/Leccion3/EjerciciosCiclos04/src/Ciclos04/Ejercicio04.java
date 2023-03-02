/*
Ejercicio 4: Pedisr numeros hasta que se teclee uno negativo,
y mostrar cuantos numeros se han introducido.
Lo hacemos primero con las clases Scanner
Luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int conteo = 0;
        
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO" );
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
            
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + conteo +" numeros que no son negativos");
    }
}
