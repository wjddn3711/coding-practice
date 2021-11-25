import java.io.File;

public class CopyFolder {
    // 직박구리 폴더 경로를 데스크탑으로 잡고 시작한다
    public static void main(String[] args) {
        String path = "/Users/jungwoo/Desktop/직박구리/사본"; // 기본 경로를 데스크탑에 직박구리안으로 설정한다 (사본) 부터 만든다
        int fold_cnt = 0;
        try {
            File folder = new File(path); // 경로를 통해 새로운 폴더를 만든다
            while(!folder.mkdir()){ // 만약 해당 경로 중복되는 파일명이 없을때까지
                path = "/Users/jungwoo/Desktop/직박구리/사본_";
                fold_cnt++;
                path += fold_cnt; // 새로운 이름으로 경로 재설정
                folder = new File(path); // 폴더 재설정
            }
            System.out.println("파일 생성완료");
        } catch (Exception e) {
            System.out.println("해당 경로가 존재하지 않습니다");
        }

    }
}

/*
파일 디렉토리를 한번도 건드려본적이 없어서 새롭게 File 에 대한 공부를 하게 되었습니다. File.mkdir()은 디렉토리 하나를 만드는 것인데
리턴 타입은 boolean 으로 만약 해당 경로에 파일이 있다면 파일이 만들어 지지 않으며 false를 리턴한다. 이것을 이용하여 초기에 while
조건문을 통하여 파일을 생성하고 만약 생성되지 않았다면 다음 순서의 파일로 다시 다음으로 만들 수 있을때가지 계속한다. 이후에 폴더가 삭제되더라도
cnt 가 0 부터 시작하기 때문에 앞자리 부터 디렉토리를 생성한다. 새로운 클래스 File에 대해 심도있게 공부할 수 있어 좋았다
 */