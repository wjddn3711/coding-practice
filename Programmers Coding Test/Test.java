import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        System.out.println("문자 세개를 입력해주세요");
//        int num1, num2, num3;
//        num1 = sc.nextInt();
//        num2 = sc.nextInt();
//        num3 = sc.nextInt();
//        if (num1%2==0) System.out.println(num1);
//        if (num2%2==0) System.out.println(num2);
//        if (num3%2==0) System.out.println(num3);

//        for (int i = 0; i < 3; i++) {
//           int num = sc.nextInt();
//           if(num%2==0) System.out.println(num);
//        }

        System.out.println("국어점수, 수학점수, 영어점수를 입력해주세요");
        System.out.print("국어점수\t: ");
        int kor = sc.nextInt();
        System.out.print("수학점수\t: ");
        int math = sc.nextInt();
        System.out.print("영어점수\t: ");
        int eng = sc.nextInt();
        System.out.println("총점\t\t: "+(kor+math+eng)+"점");

    }
}
