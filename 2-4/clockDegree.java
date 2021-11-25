import java.util.Scanner;

public class clockDegree {
    public static void main(String[] args) {
        // 시계를 구현하고 분침, 시침간의 각도를 구하여 입력되는 A 와 각도가 같을시 리스트에 저장하도록 한다
        // 초당 분침, 시침이 이동하는 것을 통해 초당 시침과 분침의 각도는 0.0083333 과 0.1 도 이다
        // 하루는 총 86400초이기 때문에 이동안 분침, 시침이 증가되면서 이루는 각도의 차가 입력받은 값일때 answer에 담도록한다
        Scanner sc = new Scanner(System.in);
        int angle = sc.nextInt();
        double hourD = 0;
        double minD = 0;

        for (int hour = 0; hour < 24; ++hour) {
            for (int min = 0; min < 60; ++min) {
                for (int sec = 1; sec < 60; ++sec) {
                    hourD += 1/120*sec; // 매초 시침과 분침의 증가치
                    minD += 0.1*sec;
                    if(hourD>=360) hourD = 0; // 만약 360도 이상이라면 0으로 초기화
                    if(minD>=360) minD = 0; // 분침또한
                    if((double) angle==Math.abs(hourD-minD)||(double) angle==360-Math.abs(hourD-minD)){
                        // 만약 각도가 시침각과 분침각의 차라면 , 단 차는 180을 넘어가면 360-차 이기 때문에 두가지 경우를 생각한다
                        System.out.println(String.format("%02d:%02d:%02d",hour,min,sec)); // 출력형식에 맞게 두자리로 출력하되 앞자리가 없다면 0으로 채워준다
                    }
                }
            }
        }
    }
}
/*
리뷰: 본래 구상했던 것은 반복문 한번으로 시, 분, 초 를 증가시켜 구하는 것이였는데 60분마다, 60초마다 if 로 조건식을 덕지덕지 붙이니 오히려 가독성이 떨어지는 것 같아 직관적으로 3중 for문으로
시침각과 분침각이 이루는 각도를 구하였습니다. 간단한 수학적 지식으로 1초당 움직이는 시침의 각도와 분침의 각도를 이용하여 360도를 초과할시 0으로 초기화 되도록 하였습니다. 분침각과 시침각이 이루는 각도중
기준이 되는 각을 알기 어려웠기에 절대값을 적용하여 이 각도의차가 목표 각도와 동일할시 시분초가 출력되도록 하였습니다. 그리고 문제의 요구상 0초 일때는 증가하는 것이 없어야 하므로 1초부터 시작하도록 하였습니다.
조건 하나라도 잘못 설정할시 답이 출력되지 않아 제약조건에 대한 중요성을 다시 한번 알게 되어 좋았던것같습니다.
 */