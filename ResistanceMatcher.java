// Ryan Qin, Alexander Lu, Hannah Radom
// I pledge my honor that I have abided by the Stevens Honor System.
import java.io.*;
import java.util.*;

public class ResistanceMatcher {

    /**
     * Backtracks through the dp table to find the resistance values that are part of a solution.
     * @param values The array of approximated resistance values.
     * @param lookup The dp table.
     * @param row The row you start backtracking from.
     * @param col The column you start backtracking from.
     * @param origValues The original resistance values that haven't been approximated.
     * @param numResistors The maximum number of resistors we're allowed to use.
     * @param solutions The arraylist that keeps track of the possible solutions.
     */
    public static void backtrack(int[] values, boolean[][] lookup, int row, int col, ArrayList<Float> origValues, int numResistors, ArrayList<ArrayList<Float>> solutions) {
        ArrayList<Float> solution = new ArrayList<Float>();
        if (lookup[row][col]) {
            while (row > 0 && col > 0) {
                row--;
                if (!lookup[row][col]) {
                    float sol = origValues.get(row);
                    int curr = values[row];
                    solution.add(sol);
                    col -= curr;
                }
            }
        }
        if (solution.size() <= numResistors) {
            Collections.sort(solution);
            solutions.add(solution);
        }
    }

    /**
     * Uses dynamic programming to determine if it's possible to create the target sum +/- the tolerance 
     * out of the values in the 'values' array
     * @param values The array of approximated resistance values.
     * @param targetSum The target sum you want to make.
     * @param bound The tolerance level.
     * @param origValues The original resistance values that haven't been approximated.
     * @param numResistors The maximum number of resistors we're allowed to use.
     * @return An arraylist of arraylists of resistance values.
     */
    public static ArrayList<ArrayList<Float>> subsetSum(int[] values, int targetSum, int bound, ArrayList<Float> origValues, int numResistors) {
        int n = values.length;

        // Make the 2D lookup table.
        boolean[][] lookup = new boolean[n + 1][targetSum + bound + 1];

        // If the sum is 0, then the answer is True.
        for (int row = 0; row < n + 1; row++) {
            lookup[row][0] = true;
        }

        // Initialize an arraylist of arraylists to keep track of possible solutions
        // that fall within the target sum +/- the bound.
        ArrayList<ArrayList<Float>> solutions = new ArrayList<ArrayList<Float>>();

        // Fill in the lookup table using a bottom-up approach.
        for (int row = 1; row < n + 1; row++) {
            for (int col = 1; col < targetSum + bound + 1; col++) {
                int curr = values[row - 1];
                lookup[row][col] = lookup[row - 1][col];
                if (col >= curr) {
                    lookup[row][col] = lookup[row][col] || lookup[row - 1][col - curr];
                }
            }
        }

        // After building the table that goes up to target sum + bound,
        // Get a list of the possible solutions that fall between the 
        // target sum - bound to target sum + bound.
        for (int i = targetSum - bound; i < targetSum + bound + 1; i++) {
            if (lookup[n][i]) {
                backtrack(values, lookup, n, i, origValues, numResistors, solutions);
            }
        }
        return solutions;
    }

    /**
     * Given a list of resistance values, calculates the resistance
     * using the parallel formula.
     * @param arr The arraylist of resistance values.
     * @return The resistance using the resistors from the list in parallel.
     */
    public static float formula(ArrayList<Float> arr) {
        // Get the inverse of each resistance value
        ArrayList<Float> inverses = new ArrayList<Float>();
        for (int i = 0; i < arr.size(); i++) {
            inverses.add(1 / arr.get(i));
        }

        // Sum those inversed values up
        float sum = 0;
        for (float value: inverses) {
            sum += value;
        }

        // Get the inverse of the sum
        return 1 / sum;
    }

    /**
     * Gets the minimum value of an array.
     * @param arr An array of percent errors.
     * @return The smallest percent error.
     */
    public static float getMin(float[] arr) {
        float min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }

    /**
     * Keeps track of the indices of the solutions with the smallest
     * percent error, if there are multiple.
     * @param arr An array of percent errors.
     * @param val The smallest percent error.
     * @return An arraylist with the indices of the solutions with the
     * smallest percent error.
     */
    public static ArrayList<Integer> getIndices(float[] arr, float val) {
        ArrayList<Integer> indices = new ArrayList<Integer>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == val) {
                indices.add(i);
            }
        }
        return indices;
    }

    /**
     * Gets the solution that uses the least amount of resistors.
     * If there are multiple, then it just gets the first one that comes up.
     * @param indices The list of indices of the solutions with the smallest percent errors.
     * @param sols The list of solutions.
     * @return The first solution that uses the least amount of resistors.
     */
    public static ArrayList<Float> getMinLen(ArrayList<Integer> indices, ArrayList<ArrayList<Float>> sols) {
        ArrayList<Float> ans = sols.get(indices.get(0));
        int minLen = sols.get(indices.get(0)).size();
        for (int i = 1; i < indices.size(); i++) {
            if (sols.get(indices.get(i)).size() < minLen) {
                ans = sols.get(indices.get(i));
                minLen = ans.size();
            }
        }
        return ans;
    }

    public static void main(String[] args) throws Exception {
        float target = 0;
        float tolerance = -1;
        int numResistors = 0;
        String inputFile = "";
        BufferedReader reader = null;

        // Parsing and error handling
        if (args.length != 4) {
            System.out.println("Usage: java ResistanceMatcher <target> <tolerance %> <num resistors> <input file>");
            System.exit(1);
        }
        try {
            target = Float.parseFloat(args[0]);
        } catch (NumberFormatException nfe) {
            System.err.println("Error: Invalid target value '" + args[0] + "'.");
            System.exit(1);
        }
        if (target <= 0) {
            System.err.println("Error: Invalid target value '" + args[0] + "'.");
            System.exit(1);
        }
        try {
            tolerance = Float.parseFloat(args[1]);
        } catch (NumberFormatException nfe) {
            System.err.println("Error: Invalid tolerance value '" + args[1] + "'.");
            System.exit(1);
        }
        if (tolerance < 0) {
            System.err.println("Error: Invalid tolerance value '" + args[1] + "'.");
            System.exit(1);
        }
        try {
            numResistors = Integer.parseInt(args[2]);
        } catch (NumberFormatException nfe) {
            System.err.println("Error: Invalid number of resistors '" + args[2] + "'.");
            System.exit(1);
        }
        if (numResistors <= 0) {
            System.err.println("Error: Invalid number of resistors '" + args[2] + "'.");
            System.exit(1);
        }
        try {
            inputFile = args[3];
            reader = new BufferedReader(new FileReader(inputFile));
        } catch (FileNotFoundException fnfe) {
            System.out.println("Error: Input file '" + args[3] + "' not found.");
            System.exit(1);
        }
        ArrayList<Float> origValues = new ArrayList<Float>();
        String line;
        int lineNumber = 1;
        Float input;
        while ((line = reader.readLine()) != null) {
            try {
                // Add each resistor numResistor times to account for using a resistor more than once
                for (int i = 0; i < numResistors; i++) {
                    input = Float.parseFloat(line);
                    if (input <= 0) {
                        System.out.println("Error: Invalid value '" + line + "' on line " + lineNumber + ".");
                        System.exit(1);
                    }
                    origValues.add(input);
                }
                lineNumber++;
            } catch (NumberFormatException nfe) {
                System.out.println("Error: Invalid value '" + line + "' on line " + lineNumber + ".");
                System.exit(1);
            }
        }
        reader.close();
        // Part of the output
        System.out.println("Max resistors in parallel: " + numResistors);
        System.out.println("Tolerance: " + tolerance + " %");

        // Prepare all the necessary values that are going to be used
        // Approximate to 5 decimal places
        float targetInverse = 1 / target;
        int[] inverseValues = new int[origValues.size()];
        for (int i = 0; i < origValues.size(); i++) {
            inverseValues[i] = Math.round(1 / origValues.get(i) * 100000);
        }
        tolerance /= 100;
        float bound = (1 / target * 100000) * tolerance;

        // Get the list of possible solutions
        ArrayList<ArrayList<Float>> solutions = subsetSum(inverseValues, Math.round(targetInverse * 100000), Math.round(bound), origValues, numResistors);

        // If there are no solutions, then it isn't possible to reach within the target +/- tolerance
        // using an approximation to 5 decimal places.
        if (solutions.isEmpty()) {
            System.out.println("Target resistance of " + target + " ohms is not possible.");
        } else {
            // Get the list of percent errors for each possible solution in the filtered list
            float[] errors = new float[solutions.size()];
            for (int i = 0; i < solutions.size(); i++) {
                float pError = Math.abs(formula(solutions.get(i)) - target) / target * 100;
                errors[i] = pError;
            }
            // Find the smallest percent error
            float min = getMin(errors);
            // Get a list of indices of all the solutions that have the smallest percent error
            ArrayList<Integer> minIndices = getIndices(errors, min);
            // Get the first occurrence of the solution that uses the least number of resistors
            ArrayList<Float> ans = getMinLen(minIndices, solutions);

            // Rest of Output
            System.out.println("Target resistance of " + target + " ohms is possible with " + ans.toString() + " ohm resistors.");
            System.out.printf("Best fit: %.4f ohms\n", formula(ans));
            System.out.printf("Percent error: %.2f %%\n", min);
        }
        System.exit(0);
    }
}