import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

// 이름과 나이를 갖는 유저 객체를 생성하기
class User{
    private String name; // 이름
    private int age; // 나이
    private int idNum; // 가입 순서

    // 생성자
    public User(int age, String name, int idNum) {
        this.name = name;
        this.age = age;
        this.idNum = idNum;
    }
    // private 이기 떄문에 출력 메소드 따로 지정해준다
    public void UserPrint() {
        System.out.println(age+""+name);
    }

    public int getIdNum() {
        return idNum;
    }

    public int getAge() {
        return age;
    }
}

public class OrderByAge {
    public static void main(String[] args) {
        String name;
        int age;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 회원의 수
        User [] users = new User[n];
        for (int i = 0; i < n; i++) {
            age = sc.nextInt();
            name  = sc.nextLine();
            users[i] = new User(age,name,i); // id 는 회원 가입 순서대로 객체를 생성한다
        }
        List<User> usersSort = Arrays.asList(users);
        System.out.println(usersSort);
        // 리스트 타입으로 객체를 리스트로 변한한뒤 Comparator을 이용하여 나이순대로 정렬후 다음 가입 순서 대로 정렬한다
        usersSort.sort(Comparator.comparing(User::getAge).thenComparing(User::getIdNum));
        for (User user : users) {
            user.UserPrint();
        }
    }
}
/*
리뷰 : 평소 문제풀이식 코딩은 파이썬으로만 접하고 있었는데 이번을 기회로 자바를 연습하고 싶어 자바를 통하여 구현을 해보았습니다
평소와는 다른 방식으로 객체를 생성하고 각 유저들을 객체로 저장하며 캡슐화 한다는것의 이점을 살리는것에 목적을 두고 문제에 접근하였습니다
자바 공부도 앞으로 게을리 하지않고 열심히 하여 서브 언어가 아닌 메인 언어급으로 성장시켜야할 필요성을 느꼈습니다.
 */