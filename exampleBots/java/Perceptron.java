import java.util.ArrayList;
import java.util.Random;
import java.util.List;

public class Perceptron {
    private ArrayList<Double> weights;
    private static final Random rand = new Random();

    // Constructor to initialize weights with random values between -1 and 1.
    public Perceptron(int numInputs) {
        weights = new ArrayList<>();
        for (int i = 0; i <= numInputs; i++) {
            weights.add(rand.nextDouble() * 2 - 1); // Random value between -1 and 1
        }
    }

    // Set the weights of the perceptron manually.
    public void setWeights(ArrayList<Double> newWeights) {
        weights.clear();
        weights.addAll(newWeights);
    }

    // Method to predict the output for given inputs.
    public int predict(ArrayList<Integer> inputs) {
        inputs.add(-1); // Constant -1 input for the threshold weight (bias).
        
        // Calculate the dot product between the weights and the inputs.
        double weightedSum = 0;
        for (int i = 0; i < weights.size(); i++) {
            weightedSum += weights.get(i) * inputs.get(i);
        }
        return activation(weightedSum);
    }

    // Activation function to determine output.
    private int activation(double x) {
        return x > 0 ? 1 : 0; // If the weighted sum is positive, output 1, otherwise, output 0.
    }

    // Train the perceptron using the given inputs and desired outcomes.
    public void train(ArrayList<ArrayList<Integer>> trainingInputs, ArrayList<Integer> outcomes, double learningRate, int rounds) {
        for (int round = 0; round < rounds; round++) {
            for (int i = 0; i < trainingInputs.size(); i++) {
                ArrayList<Integer> inputs = new ArrayList<>(trainingInputs.get(i));
                int expectedOutcome = outcomes.get(i);
                int prediction = predict(inputs);
                int error = expectedOutcome - prediction; // Compute the error: difference between expected outcome and prediction.
                inputs.add(-1); // Add bias input for the weight update.

                // Adjust each weight in the direction to reduce the error using the perceptron rule.
                for (int j = 0; j < weights.size(); j++) {
                    weights.set(j, weights.get(j) + learningRate * error * inputs.get(j));
                }
            }
        }
    }

    // Get the current weights.
    public ArrayList<Double> getWeights() {
        return new ArrayList<>(weights);
    }

    public static void main(String[] args) {
        // Generate all 32 possible inputs for a 5-input binary perceptron.
        ArrayList<ArrayList<Integer>> trainingInputs = new ArrayList<>();
        for (int i = 0; i < 32; i++) {
            ArrayList<Integer> bits = new ArrayList<>();
            String bitString = String.format("%05d", Integer.parseInt(Integer.toBinaryString(i)));
            for (char c : bitString.toCharArray()) {
                bits.add(Character.getNumericValue(c));
            }
            trainingInputs.add(bits);
        }

        // Generate desired outputs based on the specified input patterns.
        ArrayList<Integer> desiredOutputs = new ArrayList<>();
        for (ArrayList<Integer> inp : trainingInputs) {
            if (inp.equals(new ArrayList<Integer>(List.of(0, 1, 1, 1, 1))) ||
                    inp.equals(new ArrayList<Integer>(List.of(1, 0, 1, 1, 1))) ||
                    inp.equals(new ArrayList<Integer>(List.of(1, 1, 0, 1, 1))) ||
                    inp.equals(new ArrayList<Integer>(List.of(1, 1, 1, 0, 1))) ||
                    inp.equals(new ArrayList<Integer>(List.of(1, 1, 1, 1, 0))) ||
                    inp.equals(new ArrayList<Integer>(List.of(1, 1, 1, 1, 1)))) {
                desiredOutputs.add(1);
            } else {
                desiredOutputs.add(0);
            }
        }

        ArrayList<Double> manualWeights = new ArrayList<>(List.of(0.1, 0.3, 0.4, 0.3, 0.3, 1.0));

        // Test the perceptron with manually set weights.
        Perceptron perceptron = new Perceptron(5);
        perceptron.setWeights(manualWeights);
        System.out.println("Testing with manually set weights...");
        for (int i = 0; i < trainingInputs.size(); i++) {
            ArrayList<Integer> inputs = new ArrayList<>(trainingInputs.get(i));
            int desiredOutput = desiredOutputs.get(i);
            System.out.println("Input: " + inputs + " -> Predicted Output: " + perceptron.predict(inputs) + ", Desired Output: " + desiredOutput);
        }

        // Train the perceptron and then test with the trained weights.
        Perceptron trainedPerceptron = new Perceptron(5);
        trainedPerceptron.train(trainingInputs, desiredOutputs, 0.1, 1000);
        System.out.println("\nTesting with trained weights...");
        for (int i = 0; i < trainingInputs.size(); i++) {
            ArrayList<Integer> inputs = new ArrayList<>(trainingInputs.get(i));
            int desiredOutput = desiredOutputs.get(i);
            System.out.println("Input: " + inputs + " -> Predicted Output: " + trainedPerceptron.predict(inputs) + ", Desired Output: " + desiredOutput);
        }

        // Print the final weights after training.
        System.out.println("\nFinal weights: " + trainedPerceptron.getWeights());
    }
}

