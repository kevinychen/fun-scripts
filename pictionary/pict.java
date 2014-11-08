import java.util.*;
import java.awt.*;
import javax.swing.*;
import java.util.List;
import java.io.*;

public class pict
{
    public static void main(String[] orange) throws Exception
    {
        Scanner input = new Scanner(new File("pictionary_words.txt"));
        List<String> words = new ArrayList<String>();
        while (input.hasNext())
            words.add(input.next());
        System.out.println(words.size());

        while (true) {
            String word = words.get((int)(Math.random() * words.size()));
            JOptionPane.showMessageDialog(null, "Your word is " + word);
            long start = System.currentTimeMillis();
            JOptionPane.showMessageDialog(null, "starting");
            long end = System.currentTimeMillis();
            int score = (int)(-0.36 * (end - start) / 1000 + 11.8);
            System.out.println(score);
            JOptionPane.showMessageDialog(null, "Your score is " + score);
        }
    }
}
