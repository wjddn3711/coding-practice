import java.util.Arrays;
import java.util.Comparator;

public class StringSort {
    static class Sorts {
        public String[] solution(String[] strings, int n) {
            Arrays.sort(strings,new Comparator<String>() {
                @Override
                public int compare(String o1, String o2) {
                    char c1 = o1.charAt(n);
                    char c2 = o2.charAt(n);
                    if(c1==c2) return o1.compareTo(o2); // 만약 두문자가 같다면 문자열을 사전순으로
                   return o1.charAt(n)-o2.charAt(n); // 문자의 사전순으로
                }
            });
            return strings;
        }
    }
    public static void main(String[] args) {
        Sorts s = new Sorts();
        String[] strings = {"sun", "bed", "car"};
        String answer[] = s.solution(strings,1);

    }
}
