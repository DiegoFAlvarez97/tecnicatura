
package CicloWhile1;



public class EjercicioWhile01 {
    public static void main(String[] args) {
        int conteo = 0; // Inferencia de tipos
        while(conteo <= 7){
            System.out.println("Conteo = " + conteo);
            conteo ++; //Vamos aumemtando en uno la variable    
        }
        
        
        int contador = 0;
        do{
            System.out.println("contador = "+ contador);
            contador++;
        }while(contador <= 7);
        
        //Uso de las palabras break y continue junto a las etiquetas (labels)
        
        for (int contando = 0 ;contando < 7 ;contando++){
            if(contando % 2 != 0){
                System.out.println("contando = "+ contando);
                break;
            }
        }
        inicio:
        for (int contando = 0 ;contando < 7 ;contando++){
            if(contando % 2 != 0){
                continue inicio; //Vamos a la siguiente iteracion
            }
            System.out.println("contando = "+ contando);
        }
        
        // Etiquetas Lebels
        
        for (int contando = 0 ;contando < 7 ;contando++){
            if(contando % 2 == 0){
            System.out.println("contando = "+ contando);
            
            }
        }
        
        
    }
    
}
