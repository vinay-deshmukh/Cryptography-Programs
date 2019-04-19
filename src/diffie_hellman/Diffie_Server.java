import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Arrays;
import java.util.Scanner;
// sunny_dsouza
public class Server {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        ServerSocket serverSocket = new ServerSocket(Client.port);
        Socket socket = serverSocket.accept();
        DataInputStream inputStream = new DataInputStream(socket.getInputStream());
        DataOutputStream outputStream = new DataOutputStream(socket.getOutputStream());
        System.out.println("Enter a private key :");
        int private2 = Integer.parseInt(sc.nextLine());
        System.out.println("Private key :"+private2);
        String p  = inputStream.readUTF();
        String g  = inputStream.readUTF();
        System.out.println("Public Key :"+ p +" "+g);

        int P=0;
        int G=0;
        try {
            P = Integer.parseInt(p);
            G = Integer.parseInt(g);
        }
        catch (NumberFormatException e){
            System.out.println(e);
        }

        double y_key = Math.pow(G,private2)%P;
        outputStream.writeUTF(String.valueOf(y_key));
        System.out.println("Generated key :"+y_key);
        System.out.println("Sent to exchange");
        outputStream.flush();
        String KEY_A =inputStream.readUTF();
        System.out.println("Key recieved from A :"+KEY_A);
        double sym_key = Math.pow(Double.parseDouble(KEY_A),private2)%P;
        System.out.println("Generated key after exchange :"+sym_key);
        serverSocket.close();
    }
}
