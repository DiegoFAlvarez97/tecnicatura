/*
Ejercicio 5: Realizar un juego para adivinar un numero, 
para ello generar un numero aleatorio entre 0-100, y
luego ir pidiendo numeros indicando "ES MAYOR" o "ES MENOR"
segun sea mayor o menor con respecto a N 
El proceso termina cuando el usuario acierta y mostramoss el numero 
de intentos hechos.
 */
package Ciclos05;

import javax.swing.JOptionPane;


public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100);//Esto genera un numero aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numemro MAYOR: ");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numemro MENOR: ");
            }
            else{
                JOptionPane.showMessageDialog(null,"FELICIDADES HAS ADIVINADO EL NUMERO!!!! ");
            }
            conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Adivinaste el numero en: "+ conteo +" intentos");
    }
}
