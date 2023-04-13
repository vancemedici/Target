import javax.swing.JOptionPane;

public class Fibonacci {
    public static void main(String[] args) {
        // Ler o número informado pelo usuário
        String input = JOptionPane.showInputDialog("Digite um número:");
        int number = Integer.parseInt(input);

        // Encontrar a sequência de Fibonacci até o número informado
        int a = 0, b = 1, c = 0;
        while (c < number) {
            c = a + b;
            a = b;
            b = c;
        }

        // Verificar se o número informado pertence à sequência
        if (c == number) {
            JOptionPane.showMessageDialog(null, "O número " + number + " pertence à sequência de Fibonacci!");
        } else {
            JOptionPane.showMessageDialog(null, "O número " + number + " NÃO pertence à sequência de Fibonacci.");
        }
    }
}
