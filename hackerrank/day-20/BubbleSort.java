import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;


public class BubbleSort {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int elementCount = Integer.parseInt(bufferedReader.readLine().trim());
        List<Integer> array = Stream.of(bufferedReader.readLine()
                                    .replaceAll("\\s+$", "")
                                    .split(" "))
                                    .map(Integer::parseInt)
                                    .collect(toList());
        bufferedReader.close();

        int numberOfSwaps = 0;
        for (int i = 0; i < elementCount; i++) {
            // Swap adjacent elements if they are in decreasing order
            for (int j = 0; j < elementCount - 1; j++)
                if (array.get(j) > array.get(j + 1)) {
                    int temp = array.get(j);
                    array.set(j, array.get(j + 1));
                    array.set(j + 1, temp);
                    numberOfSwaps++;
                }

            // If no elements were swapped during a traversal, array is sorted
            if (numberOfSwaps == 0)
                break;
        }

        System.out.println("Array is sorted in " + numberOfSwaps + " swaps.");
        System.out.println("First Element: " + array.get(0));
        System.out.println("Last Element: " + array.get(array.size() - 1));
    }
}
