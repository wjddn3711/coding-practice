import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class VectorSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 좌표의 개수
        int[][] vector = new int[n][2];
        for (int i = 0; i < n; i++) {
            vector[i][0] = sc.nextInt();
            vector[i][1] = sc.nextInt();
        }
        Arrays.sort(vector, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0]==o2[0]){
                    // 만약 x좌표가 같다면
                    return o1[1] - o2[1]; // y좌표를 내림차순으로
                }else{ // 아니라면 x좌표를 오름차순으로
                    return o1[0] - o2[0];
                }
            }
        });
                for (int[] xyVector : vector) {
            for (int xy : xyVector) {
                System.out.print(xy+" ");
            }
            System.out.println();
        }
    }
}
// 리뷰: 이번에는 두 인자값을 비교하여 같을시 다시 정렬 조건을 설정하는 문제가 핵심이었습니다.
// 객체간의 비교를 할때에는 theComparing으로 첫번째 비교이후의 비교값을 설정하였다면 이번에는
// Comparator를 직접설정하여 만약 값이 같을때는 y좌표를 기준으로 정렬이 되도록 해보았습니다.
// lambda 식을 통해 하는 방법을 찾았으나 식 하나로 완성하는 법을 발견하지 못하여 compare 메서드를
// 오버라이드하여 직접 정렬 조건을 만들었습니다. 앞으로도 자바 실력의 부족함을 느꼈습니다.
