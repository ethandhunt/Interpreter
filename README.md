# Interpreter
BrainF*** like interpreter

Commands:
- \> Seperates commands
- \+ Increments pointer position
- \- Decrements pointer position
- ! Jumps to another point in the program string using RAA or an integer
- \* Adds a value to the RAA that can be refrenced later by it's name
- @ Set the pointer using integers or RAA values
- $ Sets the memory under the pointer using integers or RAA values
- \# Delays the program by integer or RAA value milliseconds
- ?arg1:arg2 Conditional jump, jumps to arg2 if the memory under the pointer is equivalent to arg1
- . Prints the memory currently under the pointer
- %OperatorValue:Address Performs the operator to Address from Value
- P Creates a refferable point equivalent to the instruction address

Basic Scripts:
- i1>.>?10:4>!0 Counts to ten
- $5>+>$2>*_add>%+M0:R_add>+>$R_add>. Adds two values, in this case 5 and 2: set by $5>+>$2> _add being a RAA value
- $10>+>$2>%*M0:M1>. Multiplies two values, in this case 10 and 2: set by $10>+>$2>
- +>.>$1>.>+>$M1>%+M0:M2>.>-->$M1>+>$M2>@2>!6 Prints the Fibbonacci sequence
