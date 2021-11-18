import java.util.Arrays;
import java.util.Collections;

public class StringOpsSort {
    class Solution {
        public String solution(String s) {
            String answer = "";
            String[] strings = s.split(""); //각 문자를 기준으로 나누어 배열로
            Arrays.sort(strings,Collections.reverseOrder()); // 배열을 내림차순으로
            return String.join("",strings); // 배열을 다시 문자열로 변환
        }
    }
}
