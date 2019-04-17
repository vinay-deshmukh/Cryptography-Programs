import java.io.*;
import java.net.Socket;
import java.util.Scanner;
// sunny_dsouza
public class Client {
    final static int port = 9999;
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("127.0.0.1",port);
        DataOutputStream output = new DataOutputStream(socket.getOutputStream());
        DataInputStream input = new DataInputStream(socket.getInputStream());
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a private key :");
        int private1 = Integer.parseInt(sc.nextLine());
        System.out.println("Private key :"+private1);
        System.out.println("Enter public key 1 ");
        String p=sc.nextLine();
        System.out.println("Enter public key 2 ");
        String g=sc.nextLine();
        output.writeUTF(p);
        output.writeUTF(g);
        System.out.println("key sent");

        int P=0,G=0;
        try {
            P = Integer.parseInt(p);
            G = Integer.parseInt(g);
        }
        catch (NumberFormatException e){
            System.out.println(e);
        }

        double x_key = Math.pow(G,private1)%P;
        System.out.println("Generated key :"+x_key);
        output.writeUTF(String.valueOf(x_key));
        System.out.println("Sent for exchange");
        output.flush();
        String KEY_B = input.readUTF();
        System.out.println("Key recieved from B : "+KEY_B);
        double sym_key = Math.pow(Double.parseDouble(KEY_B),private1)%P;
        System.out.println("Generated key after exchange :"+sym_key);

        socket.close();
    }

}
