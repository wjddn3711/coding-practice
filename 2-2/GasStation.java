import java.util.Arrays;
import java.util.Scanner;

public class GasStation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 도시의 개수
        int[] roadLen = new int[n-1];
        int[] gasVal = new int[n];
        int totalLen = 0;
        int cost = 0;
        int driven = 0;
        // 도로의 길이와 리터당 가격을 저장
        for (int i = 0; i < n-1; i++) {
            roadLen[i] = sc.nextInt();
            totalLen += roadLen[i]; // 전체  거리를 계산
        }
        for (int i = 0; i < n; i++) {
            gasVal[i] = sc.nextInt();
        }
        int minGas = Arrays.stream(gasVal).min().getAsInt(); // 기름값이 가장 낮은 곳을 저장한다
        for (int i = 0; i < gasVal.length; i++) {
            if (gasVal[i] == minGas) {
                // 만약 현재 위치가 경로상 가상 싼 주유소라면
                cost += totalLen*gasVal[i]; // 남은거리*리터당가격
                break;
            }
            else {
                // 아니라면 현재 주유소 보다 싼 주유소가 나올때 까지 채운다
                for (int j = i+1; j < gasVal.length; j++) {
                    if (gasVal[i]>gasVal[j]) {
                        // 다음 주유소 보다 비싸다면 j 번째 전까지 충전한다
                        driven += roadLen[j-1]; // j번째 주유소 까지 이동하고
                        totalLen -= driven; // 총 거리에서 주행거리를 빼준다
                        cost += driven*gasVal[i]; // 현재 주유소*주행거리를 비용에 더해준다
                        driven=0; // 주행거리를 다시 0으로 초기화
                        break;
                    }
                    else {
                        // 주행거리를 즐려준다
                        driven += roadLen[j-1];
                    }
                }
                if(totalLen==0){
                    // 거리를 모두 이동했다면 반복을 멈춘다
                    break;
                }
            }
        }
        System.out.println(cost);
    }
}
// 리뷰: 경로상의 각 주유소를 확인하여 현재 주유소를 기준으로 이후 더 값싼 주유소가 등장 할때까지
// 이동한뒤 움직인 거리가 총 거리에 다다를때 까지 반복을 하며 금액을 증가시켜주었습니다. for문을
// 두번 사용하여 복잡도가 O(n^2)이 되었는데 이를 개선할 방법이 있을지 더 최적화된 방법을 좀더
// 연구해봐야 될것같습니다.