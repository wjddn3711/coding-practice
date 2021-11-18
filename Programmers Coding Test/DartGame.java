public class DartGame {
    public static void main(String[] args) {
        DartSolution s = new DartSolution();
        System.out.println(s.solution("1D#2S*3S"));
        // 1의 1승 + 2의 2승 *2
    }
}

class DartSolution {
    public int solution(String dartResult) {
        int answer = 0;
        String pows = "SDT";
        int currNum = 0;
        String num = "";
        int pastNum = 0;
        for (int i = 0; i < dartResult.length(); i++) {
            char target = dartResult.charAt(i); // i 번째에 있는 char를 비교한다
            if (Character.isDigit(target)){
                num += target;
                continue;
            }
            else if (target == 'S' || target=='D' || target=='T') {
                pastNum = currNum; // 지난 넘버를 더해준다
                currNum = Integer.parseInt(num);
                num = ""; // num 초기화
                int x = pows.indexOf(target)+1; // S,M,T의 인덱스를 받아온다
                currNum = (int)Math.pow(currNum,x); // currNum 의 x 승을 답에 저장해준다
            }
            else if (target=='*'){
                answer += pastNum+currNum;
                pastNum *=2;
                currNum *=2;
                continue;
                // 스타상을 받을 경우 기존 answer에 *2를 해준다
            }
            else if (target=='#'){
                answer += -2*currNum;
                currNum*=-1;
                continue;
                // 아차상을 받을 경우 기존 answer에 *-1
            }
            answer += currNum;
        }
        return answer;
    }
}

