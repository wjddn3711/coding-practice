
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["marina", "josipa", "nikola", "filipa"]
def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(list(zip(participant, completion)))
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

print(solution(participant,completion))

