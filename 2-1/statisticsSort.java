import java.util.*;

public class statisticsSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 수의 개수
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt(); // 배열에 숫자 입력 받고 담아준다
        }
        double avg = Arrays.stream(numbers).sum()/(n*1.0);
        // 산술 평균
        System.out.printf("%.0f\n",avg); // 소수점 1의 자리에서 반올림
        // 중앙 값
        Arrays.sort(numbers);
        System.out.println(numbers[n/2]); // n은 항상 홀수이기에 중앙값은 n/2 가 됨
        // 최빈 값
        HashMap<Integer,Integer> countNum = new HashMap<>(); // 키: 수 , 벨류 : 빈도수
        for (int number : numbers) {
            if (countNum.get(number)==null){
                countNum.put(number, 1); // 만약 해당 수를 카운트 하는게 처음이라면
            }
            else {
                countNum.put(number,countNum.get(number)+1); // 해당 수가 존재한다면
            }
        }
        Integer maxVal = Collections.max(countNum.values()); // 빈도수중 max 값을 찾는다
        int maxFreq = Collections.frequency(countNum.values(),maxVal); // 빈도수 max값이 여러개 존재하는지 확인
        // maxFreq 가 1을 초과할 경우 최빈값중 두번째로 작은 값을 출력하게 한다
        Object[] sortedKey = countNum.keySet().toArray();
        Arrays.sort(sortedKey); // 키값을 기준으로 정렬해준다
        if (maxFreq > 1){
            boolean isSecond = false;
            for (Object target : sortedKey) {
                if(isSecond){
                    // 만약 최대빈도수 이면서 두번째로 작은 값이라면 isSecond는 True 가 된다
                    System.out.println(target);
                    break; // 그뒤는 고려할 필요가 없으므로 탈출
                }
                if(countNum.get(target)==maxVal){
                    isSecond = true;
                    continue;
                    // 만약 타겟값의 빈도수가 최대 빈도수와 같다면 isSecond를 True로 바꿔준다
                }
            }
        }else {
            for (Integer target : countNum.keySet()) {
                if(countNum.get(target)==maxVal){
                    System.out.println(target);
                    break; // 하나 밖에 존재하지 않는다면 최대빈도수를 가진 수만 출력하고 종료
                }
            }
        }
        // 범위
        // 이미 정렬되어진 수들이기 때문에 가장 뒤에있는 수 - 가장 앞에있는 수를 하면 범위를 알 수 있다
        int bound = numbers[numbers.length-1]-numbers[0];
        System.out.println(bound);
    }
}

/*
리뷰 : 자바에는 Counter 라이브러리가 있는지 모르겠지만 변수타입이 다양하다 보니 헤메는 시간이 많았던것같습니다. 같은 부류의 정렬이지만
하는 법이 다르기 때문에 학습에도 좋은 기회가 되었던것 같습니다.
 */