# Decimal to Binary Converter

A short Python script that converts a whole number into binary using **repeated division by 2**.

## How it works
1. The user enters a number.
2. While the number is greater than or equal to 1:
   - If it equals `1`, print `1` and stop.
   - Otherwise print the remainder of dividing by 2 (`0` for even, `1` for odd).
   - Replace the number with `num // 2`.
3. Print `====Next number====` and ask for another number (the program loops forever; stop it with `Ctrl + C`).

## Example
Input: `6`
```
0
1
1
====Next number====
```
The bits are printed **least significant bit first**, one per line. Read them from bottom to top to get the binary value: `110`.

## Concepts practiced
- `while` loops (nested)
- Modulo (`%`) and floor division (`//`)
- The manual algorithm behind decimal-to-binary conversion

## How to run
```bash
python from_num_to_binary.py
```

## Limitations / ideas for improvement
- Bits appear in reverse order; collecting them in a string and reversing it would give the normal binary form on one line.
- Entering `0` or a negative number prints nothing.
- Non-integer input raises a `ValueError`.
- There is no built-in way to exit besides `Ctrl + C`.
