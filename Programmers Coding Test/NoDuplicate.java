import java.util.*;

public class NoDuplicate {
    public static void main(String[] args) {
        NoDupSolution s = new NoDupSolution();
        int[] arr = {4,4,4,3,3};
        int[] ss = s.solution(arr);
        for (int i : ss) {
            System.out.println(i);
        }
    }

}

class NoDupSolution {
    public int[] solution(int []arr) {
        ArrayList<Integer> raw = new ArrayList<>();
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        int past = arr[0];
        raw.add(past);
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == past) continue;
            else{
                raw.add(arr[i]);
                past = arr[i];
            }
        }
        int[] answer = new int[raw.size()];
        for (int i = 0; i < raw.size(); i++) {
            answer[i] = raw.get(i);
        }
        return answer;
    }
}