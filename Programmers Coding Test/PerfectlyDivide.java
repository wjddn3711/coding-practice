import java.util.ArrayList;
import java.util.Arrays;

public class PerfectlyDivide {
    public static void main(String[] args) {
        int[] arr = {3,2,6};
        int divisor = 10;
        DivisionSolution s= new DivisionSolution();
        int[] x = s.solution(arr,divisor);
        for (int i : x) {
            System.out.println(i);
        }
    }
}

class DivisionSolution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> divided = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % divisor ==0){
                divided.add(arr[i]);
            }
        }
        if (divided.size()==0){
            return new int[]{-1};
        }
        int[] answer = new int[divided.size()];
        for (int i = 0; i < divided.size(); i++) {
            answer[i] = divided.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}