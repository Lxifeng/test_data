import random
answer = []
something = []
for i in range(1,50):
    something.append(random.randint(1,50))
print(answer)
for new in something:
    if answer:
        is_insert = False
        for index, num in enumerate(answer):
            if new < num:
                is_insert = True
                answer = answer[:index] + [new] +answer[index:]
        if not is_insert:
            answer = answer + [new]
    else:
        answer = [new]
print(answer)