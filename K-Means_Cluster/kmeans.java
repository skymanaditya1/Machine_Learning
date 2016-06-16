import java.util.Scanner;
import java.util.Random;

public class kmeans{

	public static int number_clusters = 2;
	public static int dimension = 2;
	public static int number_points = 4;
	public static int[][] cluster;
	public static int[][] points;
	public static int iterations = 10;

	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		// System.out.println("Enter the number of clusters : " );
		// int number_clusters = in.nextInt();
		// int number_clusters = 2;
		// System.out.println("Enter the dimension of the data points : ");
		// int dimension = in.nextInt();
		// int dimension = 2;
		cluster = new int[number_clusters][dimension];

		// code for randomly initializing the cluster points
		initialize_cluster_centres();

		System.out.println("The initial cluster centres are : ");
		// Print the cluster centres
		for (int i=0; i<number_clusters; i++){
			for (int j=0; j<dimension; j++){
				System.out.print(cluster[i][j] + " ");
			}
			System.out.println();
		}

		// function to randomly initalize the clusters
		// System.out.println("Enter the number of data points : ");
		// int number_points = in.nextInt();
		// int number_points = 5;
		// Each of the data points will have dimension and a cluster number associated with it
		points = new int[number_points][dimension + 1];
		// Insert the data points
		System.out.println("Insert the data points : " );
		for (int i=0; i<number_points; i++){
			// Assign a random cluster number to each of the points
			// The cluster number can be assigned as -> points[i][dimension + 1]
			points[i][dimension] = 0; // Assigns a random cluster number of 0
			System.out.print("Insert dimensions of data point " + i + " : ");
			for (int j=0; j<dimension; j++){
				points[i][j] = in.nextInt();
			}
			System.out.println();
		}

		// Print out the points and their dimensions
		/**for (int i=0; i<number_points; i++){
			for (int j=0; j<dimension + 1; j++){
				System.out.print(points[i][j] + " ");
			}
			System.out.println();
		}*/

		// perform the kmeans function for the given number of iterations
		for (int i=0; i<iterations; i++){
			dokmeans();
		}

		// print out the cluster's dimensions and the points in those cluster with dimension
		for (int i=0; i<number_clusters; i++){

			System.out.println("Points in the " + i + " cluster are : ");
			for (int j=0; j<number_points; j++){
				if (points[j][dimension] == i){
					System.out.print("Point " + j + ". ");
					// Print out the dimensions of this point
					System.out.print("Dimensions are : " );
					for (int k=0; k<dimension; k++){
						System.out.print(points[j][k] + " ");
					}
				}		
			}
			System.out.println();
		}
	}

	// do this step iteratively for the given number of iterations
	public static void dokmeans(){
		// Step 1 - Calculate the data points and cluster distances
		// find out the cluster distance for all the data points from all the cluster centres
		for (int i=0; i<number_points; i++){
			// assume min as the disance betweek the ith data point and the 0th cluster
			double min = calculate_difference(i, 0);
			for (int j=1; j<number_clusters;j++){
				if (calculate_difference(i, j) < min){
					// Set the value of the min as the new min and assign new cluster number
					min = calculate_difference(i, j);
					points[i][dimension] = j;
				}
			}
		}

		// Step 2 - Calculate the cluster averages for all the points in a cluster and assign it to the cluster centre
		for (int i=0; i<number_clusters; i++){
			// check if the point is present in the cluster for all the points
			int[] dim_sum = new int[dimension];
			int cluster_points = 0; // represents the number of points in that cluster
			for (int j=0; j<number_points; j++){
				if (points[j][dimension] == i){
					// sum for all the dimensions
					for (int k=0; k<dimension; k++){
						dim_sum[k] += points[j][k];
					}
				}
			}
			// update the cluster averages, if the cluster_points != 0
			if (cluster_points != 0){
				// Update the dimensions of the ith cluster
				for (int j=0; j<dimension; j++){
					cluster[i][j] = dim_sum[j] / cluster_points;
				}
			}
		}
	}

	// Code for randomly initializing the cluster centres
	public static void initialize_cluster_centres(){
		Random random = new Random();
		// initialize randomly the cluster centres for all the clusters
		for (int i=0; i<number_clusters; i++){
			for (int j=0; j<dimension; j++){
				cluster[i][j] = random.nextInt(5) + 1;
			}
		}
	}

	// Function to calculate the difference of distance between the cluster centre and the sample point
	public static double calculate_difference(int point_number, int cluster_number){
		double distance = 0;
		for (int d=0; d<dimension; d++){
			distance += Math.pow(cluster[cluster_number][d] - points[point_number][d], 2); 
		}
		return Math.sqrt(distance);
	}
}
