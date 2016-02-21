package e_245;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

/**
 * Created by osk on 2016-02-21.
 */
public class DateValidator {
    public static void main(String[] args) {
        String[] input = { "2/13/2015", "1-31-10", "5 10 2015", "2012 3 17", "2001-01-01", "2008/01/07" };

        for (String s : input) {
            System.out.println(s + "\n" + reformatDate(s) + "\n");
        }
    }

    private static String reformatDate(String s) {
        Scanner scan = new Scanner(s);
        scan.useDelimiter("[^0-9]");

        int month = scan.nextInt();
        int day = scan.nextInt();
        int year = scan.nextInt();

        if (month > 12) {
            int temp = month;
            month = day;
            day = year;
            year = temp;
        }

        if (year < 100) {
            year += 2000;
        }

        LocalDate date = LocalDate.of(year, month, day);
        DateTimeFormatter formatter = DateTimeFormatter.ISO_LOCAL_DATE;

        scan.close();
        return date.format(formatter);
    }
}
