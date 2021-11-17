import java.util.Arrays;

public class ArrayMinMaxMid {
    public static void Solve(int[] ar){
        for (int i = 1; i < ar.length; i++) {
            for (int j = i; j >= 0 ; j--) {
                if (ar[i]>ar[j]){
                    int temp;
                    temp = ar[i];
                    ar[i] = ar[j];
                    ar[j] = temp;
                }
                else break;
            }
        }
        System.out.println("제일 큰 값은 "+ar[ar.length-1]+" 입니다.");
        System.out.println("제일 작은 값은 "+ar[0]+" 입니다.");
        System.out.println("중간값은 "+ar[ar.length/2]+" 입니다.");
    }

    public static void main(String[] args) {
        int[] ar = {1,2,3,4,5};
        Solve(ar);
    }
}

/*
리뷰 : for 문을 한번 만 써서 구하는 방법을 오랫동안 고민해보았지만 마땅히 떠오르는것이 없어 for, if, else 를 모두 쓰는 선택 정렬을 사용하여 배열을 정렬해주었다.
배열의 길이가 짝수인 경우도 생각해보았으나 애초에 짝수인 경우 중간값을 구하기 모호하다 판단되어 길이가 홀수인 배열을 입력받는것을 전제로 구현하였다.
복잡도 면에서 비효율적이라 판단되어 추후에 고민을 더 해봐야겠다고 느꼈다.
 */