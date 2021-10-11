from queue import PriorityQueue

print('문자 개수? ', end='')
n = int(input())  # 문자개수
# ================================ 파일 열어서 기존에 있던거 저장하기 ================================
try:
    f = open('huff.txt', 'rt', encoding='utf-8')  # Open file with 'UTF-8' 인코딩
    line = f.readline()
    l = int(line.strip('\n'))  # 가장 첫째줄에는 문자의 개수가 있다
    charL = {}
    for i in range(l):
        line = f.readline().strip('\n').split()
        charL[line[0]] = int(line[1])  # 딕셔너리 형태로 만들어 저장한다
        if not line: break
    f.close()
except FileNotFoundError:
    print('디스크에 해당 파일이 없습니다')
# ================================ 파일 열어서 새로운 문자 추가하기 ================================
for i in range(n):
    print('문자? ', end='')
    char = input()
    print('빈도수? ', end='')
    freq = int(input())
    if char[i] in charL.keys():  # 문자가 이미 딕셔너리에 있는 상태라면
        charL[char] = charL[char] + freq  # 기존에 있던 빈도수에서 증가 시켜준다
    else:
        charL[char] = freq  # 새로운 문자라면 딕셔너리에 추가해준다
l = len(charL)  # 새롭게 라인수를 초기화 한다
f = open('huff.txt', 'w', encoding='utf-8')
f.write('{}\n'.format(l)) # 가장 앞줄에 문자의 개수 초기화
for i in range(l):
    f.write('{} {}\n'.format(list(charL.keys())[i],list(charL.values())[i]))
print('파일 덮어쓰기 완료!')
f.close()

# 파이썬에서 객체지향 프로그래밍을 위해 클래스를 생성한다
class HuffNode:  # 4개의 멤버 변수를 갖는다
    def __init__(self, char, freq):  # 문자와 빈도수를 파라미로 받는다
        self.char = char
        self.freq = freq
        self.left = None  # left, right 를 null로 초기화 한다
        self.right = None

    def __eq__(self, other):  # 우선 순위가 같다면
        return self.freq == other.freq

    def __ne__(self, other): # 우선 순위가 다르다면
        return self.freq != other.freq

    def preorder(self):  # root - left - right 순으로 채운다
        print(self.char, end=' ')
        if self.left is not None:
            self.left.preorder()  # 만약 왼쪽이 비지 않았다면 다시 재귀호출하여 왼쪽부터 채운다
        if self.right is not None:
            self.right.preorder()  # 똑같이 오른쪽이 비지 않았다면 재귀호출하여 오른쪽채운다

    def enbit(self, bit, target): # 문자가 같을때 까지 루트에서 left - right 순으로 순회
        if self.char == target:
            print(self.char + ': ' + bit)
            return
        if self.left is not None:
            bit += '1'
            self.left.enbit(bit, target)
        bit = bit[:-1]  # 만약 좌측에 자식노드가 없다면 마지막 비트 값은 삭제하고 오른쪽 순회
        if self.right is not None:
            bit += '0'
            self.right.enbit(bit, target)

def huffMan(PQ):
    depth = 1
    while PQ.qsize() >= 2:  # 0~n-1까지 호출한다 (n개의 요소를 2개씩 짝지어 반환하기 때문에 n-1번 반복한다)
        p = PQ.get()[1]  #
        q = PQ.get()[1]  # 빈도수가 가장 작은 값 두개를 갖고 root를 만든다
        r = HuffNode('H-' + str(depth), p.freq + q.freq)  # root 빈도 = p빈도 + q빈도
        r.left = p
        r.right = q
        PQ.put((r.freq, r))
        depth += 1
    return PQ.get()[1]  # 마지막 노드를 반환한다

PQ = PriorityQueue()  # 우선순위 큐를 생성한다

for i in range(len(charL)):
    node = HuffNode(list(charL.keys())[i], list(charL.values())[i])  # 허프 노드의 생성자로 문자와 빈도수를 준다
    PQ.put((node.freq, node))  # 빈도수를 기준으로 우선순위 큐를 생성한다

root = huffMan(PQ)
print('\n허프만 트리 생성 (Preorder): ')
root.preorder()
print('\n\n각 문자당 비트')
for c in sorted(list(charL.keys()), key=lambda x:charL[x], reverse=True):
    root.enbit('', c) # 빈도수가 가장 큰수 부터 차례로 출력한다

fourB = 1
while fourB <= l:
    fourB *= 2

print('\n4-비트 코드 시: {} bits'.format(fourB))  # 4비트 사용시 n 보다 큰 2^n 만큼 필요하다
print('허프만 코드 시: {} bits'.format(l))  # 허프만 사용시 문자의 개수 만큼만 있으면 된다
