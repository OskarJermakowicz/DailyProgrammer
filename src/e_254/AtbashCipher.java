package e_254;

/**
 * Created by osk on 2016-02-21.
 */
public class AtbashCipher {
    private static final String[] PLAIN = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
    private static final String[] CIPHER = {"z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"};

    public static void main(String[] args) {
        String[] input = {"foobar", "wizard", "/r/dailyprogrammer", "gsrh rh zm vcznkov lu gsv zgyzhs xrksvi"};

        for (String s : input) {
            System.out.println(s + "\n" + atbashCipher(s) + "\n");
        }
    }

    private static String atbashCipher(String s) {
        String result = "";

        for (int i = 0; i < s.length(); i++) {
            int j = contains(PLAIN, String.valueOf(s.charAt(i)));
            if (j != -1) {
                result += CIPHER[j];
            } else {
                result += String.valueOf(s.charAt(i));
            }
        }
        return result;
    }

    private static int contains(String[] array, String element) {
        int index = 0;
        for (String s : array) {
            if (s.equals(element)) {
                return index;
            }
            index++;
        }
        return -1;
    }
}
