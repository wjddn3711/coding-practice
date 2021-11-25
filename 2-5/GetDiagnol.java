public class GetDiagnol {
    static double getDiagnol(int x, int y){
        // 피타고라스의 정리에 의해 밑변제곱+높이제곱의 루트는 대각선의 길이다
        double result;
        result = Math.sqrt(Math.pow(x,2)+Math.pow(y,2));
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getDiagnol(5,4));
    }
}

/*
리뷰: 간단한 피타고라스 정리를 이용한 대각선의 길이를 구하는 법이였다. 직각삼각형일때만 해당한다
 */