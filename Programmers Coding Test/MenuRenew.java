import java.util.Arrays;

public class MenuRenew {
    static class Solut {
        public String[] solution(String[] orders, int[] course) {
            String[] answer = {};
            return answer;

            // 일단 메뉴들을 오름차순으로 정렬
            for (int i = 0; i < orders.length; i++) {
                String[] str =orders[i].split("");
                Arrays.sort(str); // 문자열 배열을 오름차순으로 정렬
                orders[i] = String.join("",str); // orders[i] 를 다시 문자열로 저장
            }

            for (int i = 0; i < course.length; i++) {

            }

        }
    }

    public static void main(String[] args) {
        Solut s = new Solut();
        String [] orders= {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int[] course = {2,3,4};
        s.solution(orders,course);
    }
}
