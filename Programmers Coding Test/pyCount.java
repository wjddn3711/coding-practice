import java.util.Locale;

public class pyCount {
    class Py {
        boolean solution(String s) {
            boolean answer = false;
            int pCnt=0, yCnt=0;
            s = s.toLowerCase(); // 우선 대소문자를 가리지 않기 때문에 소문자로 모두 바꿔준다
            for (int i = 0; i < s.length(); i++) {
                if(s.charAt(i)=='p') pCnt++;
                else if(s.charAt(i)=='y') yCnt++;
            }
            if(pCnt==yCnt) answer=true;
            // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
            return answer;
        }
    }
}
