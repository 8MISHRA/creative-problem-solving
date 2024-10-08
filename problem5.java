// Given a matrix as input (2D array). Print out all the items in that array:

// E.g, Input: [ [1 2 3], [4,5,6], [7,8,9]]

// Output:
// 1 2 3
// 4 5 6
// 7 8 9

public class problem5 {

    public static void main(String[] args) {
        int[][] arr = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        print_matrix(arr);
    }
    static void print_matrix(int[][] arr){
        for (int row = 0; row < arr.length; row++){
            for (int col = 0; col < arr[row].length; col++){
                System.out.print(arr[row][col] + " ");
            }
            System.out.println();
        }
    }
}
