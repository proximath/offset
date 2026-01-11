# Offset
> Offset is a joke language with the philosophy of creating an esoteric programming language that achieves Turing Completeness via rewriting addresses.

### Overview
* You have an unbounded array of cells. 
* Each cell contains a symbol that is a valid ascii character. 
* Each cell has its corresponding address, starting from 0. 
* You have a pointer (`ip`), initially pointing to address 0. 
* There's a `register`, which can hold one symbol. 
* There's an `offset`, which accumulate digits and is the operand of `$`, `=`, `<`, and `>`.

### Notable Properties
* Your code, memory, input, and output share the same space.
* Branching is done via rewriting offsets. 
* Looping is made possible using the `<` symbol.

### Key Symbols
The language recognizes several key symbols:
* `$`:
    Store the value at address `ip + offset` into register, then move pointer right by 1, then reset `offset` to 0.
* `=`:
    Write the value in register to the cell at address `ip + offset`, then move pointer right by 1, then reset `offset` to 0.
* `<`:
    Move pointer left by `offset` amount, then reset `offset` to 0.
* `>`:
    Move pointer right by `offset` amount, then reset `offset` to 0.
* Digits (0-9):
    Concatenate the current digit to `offset`. In effect, similar to `offset = 10 * offset + digit`. Then move pointer right by 1.

Other symbols are treated as comments. The interpreter will skip them but they still occupy an address.

### Example
Negating a single bit.
```
29$37>30=99< 'THE NEGATION OF (1) IS ( )' 2=10$43<      10 END OF CODE | 
```

### Problem
I was trying to prove whether this language is Turing Complete or not. What stumbles me is the fact that it doesn't seem possible to implement an *unbounded incrementer*.
Here's what I'm trying to do: I want a program that when given an input number N produces N+1. The input is encoded in *unary*. Given that the input can be arbitrarily large, the program doesn't know where the input will end, so I have to place a special symbol to mark the end. Also, to give my program room to work with unbounded memory, I need to interleave the input with zeros. Example input, N = 5: `100010001000100010002`. The goal would be to replace that 2 with a 1. I couldn't do this because I wasn't able to create the "scanning" logic. The program needs to iterate and check if the symbol is 2. It requires either iteratively incrementing an offset at the start, or writing a code that duplicate itself. Both options seem to require some kind of incrementing logic, which is the problem we're trying to solve. So unless there's a clever trick, this language is not Turing Complete.
