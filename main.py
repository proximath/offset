from collections import defaultdict

code = "24$32>25=99< 'THE XOR OF (1) IS ( )' 2=10$38<      10 END OF CODE | "
tape = defaultdict(lambda: '0')
for i, c in enumerate(code):
    tape[i] = c

ip = 0
offset = 0
register = '0'
step = 1
MAX_STEP = 100

while step < MAX_STEP:
    print(f"Step #{step} | IP = {ip} | Register = {register} | Offset = {offset}")
    for i in range(105):
        if i == ip:
            print('[', end="")
        print(tape.get(i, '0'), end="")
        if i == ip:
            print(']', end="")

    print()
    print()
    step += 1
    if tape.get(ip, '0') == "=":
        tape[ip + offset] = register
        offset = 0
        ip += 1
    elif tape.get(ip, '0') == "$":
        register = tape[ip + offset]
        offset = 0
        ip += 1
    elif tape.get(ip, '0') == ">":
        ip += offset 
        offset = 0
    elif tape.get(ip, '0') == "<":
        ip -= offset 
        offset = 0
        if ip < 0:
            break
    elif tape.get(ip, '0').isdigit():
        offset = offset * 10 + int(tape.get(ip, '0'))
        ip += 1
    else:
        ip += 1


print(f"Finished | IP = {ip} | Register = {register} | Offset = {offset}")
for i in range(105):
    if i == ip:
        print('[', end="")
    print(tape.get(i, '0'), end="")
    if i == ip:
        print(']', end="")
print()
