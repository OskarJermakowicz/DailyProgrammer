package e_149;

/**
 * Created by osk on 2016-02-21.
 */
public class Disemvoweler {
    private static final String[] VOWELS = { "a", "o", "u", "e", "i", "u" };

    public static void main(String[] args) {
        String text = "did you hear about the excellent farmer who was outstanding in his field";
        disemvowel(text);
    }

    private static void disemvowel(String text) {
        String result = "";
        String vowel = "";

        for (int i = 0; i < text.length(); i++) {
            if (contains(VOWELS, String.valueOf(text.charAt(i)))) {
                vowel += String.valueOf(text.charAt(i));
            } else if (text.charAt(i) != ' ') {
                result += String.valueOf(text.charAt(i));
            }
        }
        System.out.println(result);
        System.out.println(vowel);
    }

    private static boolean contains(String[] array, String element) {
        for (String s : array) {
            if (s.equals(element)) {
                return true;
            }
        }
        return false;
    }

}
