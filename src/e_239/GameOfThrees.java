package e_239;

/**
 * Created by osk on 2016-02-21.
 */
public class GameOfThrees {
    public static void main(String[] args) {
        int input = 31337357;
        solve(input);
    }

    private static void solve(int input) {
        while (input != 1) {
            if (input % 3 == 0) {
                System.out.print(input + "\t0\n");
                input /= 3;
            } else if ((input + 1) % 3 == 0) {
                System.out.print(input + "\t1\n");
                input++;
            } else if ((input - 1) % 3 == 0) {
                System.out.print(input + "\t-1\n");
                input--;
            }
        }
        System.out.print(input + "\n");
    }
}
