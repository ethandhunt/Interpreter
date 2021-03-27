# Interpreter
BrainF*** like interpreter

Commands:
- ```>``` Seperates commands
- ```+``` Increments pointer position
- ```-``` Decrements pointer position
- ```!``` Jumps to another point in the program string using RAA or an integer
- ```*``` Adds a value to the RAA that can be refrenced later by it's name
- ```@``` Set the pointer using integers or RAA values
- ```$``` Sets the memory under the pointer using integers or RAA values
- ```#``` Delays the program by integer or RAA value milliseconds
- ```?op:arg1:arg2``` Conditional jump, runs ```arg2``` as an instruction if the memory under the pointer and ```arg1``` evalute true under the op, operations are: ```=``` - Equivalent, ```Gt``` - >(Greater than), ```Lt``` - /<(Less than), ```Dv``` - Divisible
- ```.arg1``` Prints the memory currently under the pointer unless arg1 is a value
- ```%Operator:Value:Address``` Performs the operator to Address from Value
- ```P``` Creates a refferable point equivalent to the instruction address

Basic Scripts:
- ```i1>.>?10:4>!0``` Counts to ten
- ```$5>+>$2>*_add>%+:M0:R_add>+>$R_add>.``` Adds two values, in this case 5 and 2: set by ```$5>+>$2>``` _add being a RAA value
- ```$10>+>$2>%*:M0:M1>.``` Multiplies two values, in this case 10 and 2: set by ```$10>+>$2>```
- ```+>.>$1>.>+>$M1>%+:M0:M2>.>-->$M1>+>$M2>@2>!6``` Prints the Fibbonacci sequence
- ```+>#100>.>$1>#100>.>+>P_calc>$M1>%+:M0:M2>#100>.>-->$M1>+>$M2>@2>!P_calc``` Prints the Fibbonacci sequence with a delay and uses pointers
- ```P_start>+>.pointer>#100>!P_start``` Counts up to infinity incremented every 0.1 second (Accuracy not confirmed)

Expression Evaluation:
- ```...>*_name>...``` Refferable by R_name ```...>@R_name>...```
- ```...>@5>$_someValue>@_someOtherMemoryAddress>%+Mpointer:M5>...``` Reffering to a memory address (Snippet not tested)
- ```...>P_instructionNumber>...``` Stores instruction number in pointer dictionary when run (Not an actual pointer) ```...>@P_instructionNumber>...```
- ```...>.pointer>...``` Prints pointer value
- ```...>.atest>...``` Prints integer value of the string "test" (1952805748)
- ```...>.5%+|2>...``` Prints 5 + 10 using inline arithmetic, expressed as ```Value%Operator|Value```