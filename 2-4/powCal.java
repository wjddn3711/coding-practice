import java.util.ArrayList;
import java.util.Scanner;

public class powCal {
    // 제곱수: 1,4,9,16,25,36,49,64,81,100,121,144,169,225,256,289,324,361,400
    public static boolean isSqrt(int target){ // 만약 제곱수가 존재하면 true
        double sqrtNum = Math.sqrt(target);
        if(sqrtNum!=(int)sqrtNum){
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        // 어떤 수가 제곱수인지 판단하려면 제곱근이 정수인지를 검사해야한다
        Scanner sc = new Scanner(System.in);
        ArrayList<String> answer = new ArrayList<>();
        for (int i = 0; i < 7; i++) {
            String inp = sc.next();
            if (inp.contains("(")){ // 만약 ( 를 포함한다면 n(k)를 변환하는거
                String lSqrt = ""; // 타겟을 처음 공백으로 초기화
                String sqrtCnt = ""; // 제곱수를 공백으로 초기화
                int num = 0; // 제곱될 수
                int start=0; // 제곱수가 시작되는 시점
                // 문자열 조작으로 타겟과 제곱수를 구한다
                for (int j = 0; j < inp.length(); j++) {
                    if(inp.charAt(j)=='(') {
                        start=j+1; // j 부터 끝-1 까지는 제곱수이다
                        break; // (를 만날때 까지 계속
                    }
                    lSqrt += inp.charAt(j);
                }
                for (int j = start; j < inp.length()-1; j++) {
                    sqrtCnt+=inp.charAt(j); // 마지막 (는 항상 마지막이기 때문에 start부터 length-1까지가 제곱수
                }

                num = Integer.parseInt(lSqrt);
                for (int j = 0; j < Integer.parseInt(sqrtCnt); j++) {
                    num = (int) Math.pow(num,2);
                }
                answer.add(String.format("%d",num)); // 정답에 제곱되어진 수를 넣는다
            }
            else{ // 만약 n(k) 로 변환해야한다면
                int target = Integer.parseInt(inp);
                int cnt = 0;
                if (isSqrt(target) && target>1) { // 1이하는 제곱수가 될 수 없기에 아래로
                    while (true) { // 더이상 제곱수가 없을때 까지 반복
                        target = (int) Math.sqrt(target);
                        cnt++; // 루트한 횟수를 cnt 에 저장한다
                        if (isSqrt(target) == false) {
                            break;
                        } // 탈출 조건은 최소 제곱근일때이다
                    }
                }
                answer.add(String.format("%d(%d)",target,cnt)); // 정답에 올바른 형태로 저장한다
            }
            for (String s : answer) {
                System.out.println(s); // 리스트에 저장된 변환된 수를 반환한다
            }
        }
    }
}

/*
리뷰: breakpoint 가 따로 요구사항에 나와있지 않아 예시대로 7번만 입력 받아 출력하는 형태로 코딩을 하였습니다. 문자열 조작을 통하여 제곱되어질 수와 제곱횟수를 찾아내는 것을
간소화 할 수 있을 것같은데 Java에 아직 능숙하지 않아 원시적인 방법으로 하나하나 조회하여 따로 구했습니다. 제곱수로 변환 같은 경우 isSqrt를 통하여 제곱이 되는지를 판별하였습니다
이 또한 원시적으로 소수점 아래가 존재하는지를 통하여 true 또는 false 로 나누어 만약 true 라면 최소 제곱수가 나오도록 반복하여 루트된 횟수를 cnt에 저장하였습니다.
마지막으로 format 함수를 통하여 answer에 답을 넣었는데 변수를 너무 많이 쓴 점과 로직 자체가 올바른지는 아직도 명확하지 않습니다. 1 의 제곱수가 있다고 할시 무한 반복되기에 1보다
큰경우일때만 제곱수를 구하도록 하였습니다.
 */