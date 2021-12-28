/*******************************************************************************
 * Name        : PathSumTwoWays.java
 * Author      : Brian S. Borowski
 * Version     : 1.0
 * Date        : April 6, 2015
 * Description : Solution to Project Euler #81
 ******************************************************************************/
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PathSumTwoWays {
    private int[][] values, F;
    private int minSum;

    public PathSumTwoWays(String filename) throws FileNotFoundException,
            IOException,
            NumberFormatException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        List<String> valueList = new ArrayList<String>();
        String line;
        while ((line = reader.readLine()) != null) {
            valueList.add(line);
        }
        reader.close();
        values = new int[valueList.size()][];
        for (int row = 0; row < values.length; row++) {
            line = valueList.get(row);
            String[] parts = line.split(",");
            values[row] = new int[parts.length];
            for (int col = 0; col < parts.length; col++) {
                try {
                    values[row][col] = Integer.parseInt(parts[col]);
                } catch (NumberFormatException nfe) {
                    throw new NumberFormatException("Bad value " + parts[col]
                            + " on line " + (row + 1) + ".");
                }
            }
        }
        // Uncomment if you wish to see the values table used in this program.
        // displayTable(values);
    }

    /**
     * Dynamic programming solution that uses a two-dimensional array as the
     * cost table.
     * @return the minimum sum from the top left cell to the bottom right
     * cell in the two-dimensional values member variable.
     */
    public int getMinSum() {
        int m = values[0].length, n = values.length;
        F = new int[n][m];

        F[0][0] = values[0][0];
        for (int col = 1; col < m; col++) {
            F[0][col] = F[0][col - 1] + values[0][col];
        }
        for (int row = 1; row < n; row++) {
            F[row][0] = F[row - 1][0] + values[row][0];
            for (int col = 1; col < m; col++) {
                F[row][col] = Math.min(F[row - 1][col], F[row][col - 1])
                        + values[row][col];
            }
        }
        displayTable(F);
        minSum = F[n - 1][m - 1];
        // Uncomment if you wish to see the cost table used in this program.
        // displayTable(F);
        return minSum;
    }
    
    /**
     * Displays a two-dimensional array of integers on the screen, nicely
     * formatted to the width of the widest cell.
     * @param table a two-dimensional array of integers
     */
    public void displayTable(int[][] table) {
        int m = table[0].length,
            n = table.length,
            maxCellWidth = numDigits(Math.max(Math.max(m, n), getMax(table))),
            maxRowWidth = numDigits(m);
        for (int i = 0, len = numDigits(n); i < len; i++) {
            System.out.print(" ");
        }
        for (int col = 0; col < m; col++) {
            System.out.print(" ");
            int cellLength = numDigits(col);
            for (int i = maxCellWidth - cellLength; i > 0; i--) {
                System.out.print(" ");
            }
            System.out.print(col);
        }
        System.out.println();
        for (int row = 0; row < n; row++) {
            int cellLength = numDigits(row);
            for (int i = maxRowWidth - cellLength; i > 0; i--) {
                System.out.print(" ");
            }
            System.out.print(row);
            for (int col = 0; col < m; col++) {
                cellLength = numDigits(table[row][col]);
                for (int i = maxCellWidth - cellLength; i > 0; i--) {
                    System.out.print(" ");
                }
                System.out.print(" " + table[row][col]);
            }
            System.out.println();
        }
    }
    
    /**
     * Backtracks over the cost table to determine the integers that comprise
	 * the minimum sum, starting in the top left and ending in the bottom right
	 * cell.
     * @return an array of integers that comprise the minimum sum.
     */
    public int[] getSolution() {
        ArrayList<Integer> solutionList = new ArrayList<Integer>();
        int row = F.length - 1, col = F[0].length - 1;
        while (row > 0 && col > 0) {
            solutionList.add(values[row][col]);
            if (F[row - 1][col] < F[row][col - 1]) {
                row--;
            } else {
                col--;
            }
        }
        while (row > 0) {
            solutionList.add(values[row][0]);
            row--;
        }
        while (col > 0) {
            solutionList.add(values[0][col]);
            col--;
        }
        solutionList.add(values[0][0]);
        int[] solution = new int[solutionList.size()];
        for (int i = solutionList.size() - 1, j = 0; i >= 0; i--, j++) {
            solution[j] = solutionList.get(i);
        }
        // Sanity check to verify the sum of the numbers found during back-
        // tracking is equal to the minimum sum found in the cost table.
        assert getSum(solution) == minSum;
        return solution;
    }

    public static int numDigits(int num) {
        int count = 1;
        while (num >= 10) {
            num /= 10;
            ++count;
        }
        return count;
    }

    public static int getSum(int[] array) {
        int sum = 0;
        for (int value : array) {
            sum += value;
        }
        return sum;
    }

	private int getMax(int[][] table) {
        int m = table[0].length, n = table.length, max = Integer.MIN_VALUE;
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < m; col++) {
                if (table[row][col] > max) {
                    max = table[row][col];
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        String filename = "matrix.txt";
        PathSumTwoWays pathSum = null;
        try {
            pathSum = new PathSumTwoWays(filename);
        } catch (FileNotFoundException fnfe) {
            System.err.println("Error: File '" + filename + "' not found.");
            System.exit(1);
        } catch (IOException ioe) {
            System.err.println("Error: Cannot read '" + filename + "'.");
            System.exit(1);
        } catch (NumberFormatException nfe) {
            System.err.println("Error: " + nfe.getMessage());
            System.exit(1);
        }
        System.out.println("Min sum: " + pathSum.getMinSum());
        System.out.println(
			"Values:  " + Arrays.toString(pathSum.getSolution()));
        System.exit(0);
    }
}
