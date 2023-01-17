# Introduction
---
The following shows all the major steps associated with the compilation of any given langauge.

- IRs allow for massive abstractions such as, they allow you to pipeline your code to any already present IR and you then no need to worry about further implementations! Code Gen, for example IR $\to$ Machine Code, will not be required to be handled by you, since it shall already exist.
- Bytecode always requires a VM to work upon.
- Optimizing compilers is a deep deep trench. Many people are found lost in there.
- As a theorist, you may hate OOPs but guess what, unlike Haskell, they are useful! Yay! (I love Haskell, don't kill me).

![Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled.png](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled.png)

# Compilers v/s Interpreters
---
- Compilers convert your source code to another language without executing. Now this new language may or may not low-level language like Machine Code.
- Interpreters, on the other hand, take in source code and executes it immediately.

![Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%201.png](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%201.png)

# LLVM and why do I care?
---
- "A compiler infrastructure is useful whenever you need to do stuff with programs."
- We are interested in reasoning about programs.
- Understand compilation and related techniques.
- Requirement of architecture simulation.
- Automated Verification (✓) and Theorem Proving (‽).

# Understanding LLVM IR
---
![Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%202.png](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%202.png)

- Modules contain Functions, which contain BasicBlocks, which contain Instructions.
- Everything but Module descends from Value.
- A basic block is a straight-line code sequence with no branches in except to the entry and no branches out except at the exit — which makes it easy to analyze.

![Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%203.png](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%203.png)

As seen above the passes are where we optimize a current IR at hand.

We mostly do not have to care about Front End (parsing and analysis) and Back End (code generation). For most cases, we shall be mostly concerned about the Middle End with optimizations and writing passes.

# Toolchain
---
| Compiled Programs | Interpreted Programs |
| --- | --- |
| Process of converting source code, written in a language such as C, to a binary file ready to be executed is called compiling | Interpreted programs execute the code line by line. As a result even though they are convenient regarding not being required to produce executable after every change, it is slower. |
|  | Many interpreted languages actually run in a virtual machine that is abstracted from the underlying hardware. |

![Untitled](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%204.png)

## Virtual Machines

A compiled program is completely dependent on the hardware of the machine it is compiled for.

A virtual machine is an abstraction of hardware into software. Interpreted or hybrid langauges (like Java) utilize the concept of virtual machines to operate as “write once, run anywhere”.

## Creating an executable

1. Compiling
2. Assembling
3. Linking

## Compiling

- Pre-processing: `#define` and other shit is replaced.
- Syntax: often described using Backus-Naur Form, we do parsing and lexing

### **Assembly generation**

- Alignment of variables in memory is an important consideration for the compiler.
- Cache line alignment

### Optimisation

- Occurs after the compiler has an internal representation of the code.
- general optimising (yeet a part of unused code)
- unrolling loops (increases size of code but also decreases time by helping the processor efficiently work through instructions)
- inlining function (again space-time tradeoff, time decreases)
- branch prediction (using simple logic)

Some compilers can actually compile the program, have the user run it and take note of which way the branches go under real conditions. It can then re-compile it based on what it has seen.

## Assembler

The mechanical process of converting the assembly code into a binary form. It combines these opcodes with the registers specified in the assembly to produce a binary output file.

## Linker

Combining all object files into one executable file and then going through each object file to resolve any symbols.

Usually takes 2 passes:

1. read all symbol definitions
2. take note of unresolved symbols

We call `a` in `int a` and `function` in `function()` **symbols** since they are a symbolic representation of an area of memory.

Primary job in compilation process becomes the removal of symbols.

**Symbol visibility**: `extern` says to the compiler that it should not allocate any space in memory for this variable. The purpose of the linker is to figure out “where it has seen this symbol before in which file”. 

Thus te compiler can modify the symbol value to be the memory value of the variable in the first file.

`static` on the other hand places restrictions on the visibility of the symbol it modifies. If you declare a variable with static that says to the compiler "don't leave any symbols for this in the object code".

All of this is static linking.

In case of dynamic linking, part of the OS loads and links the shared libraries needed by an executable when it is executed. UNIX like systems use ELF (Executable and Linkable Format) for executable images and dynamic libraries.

# LLVM: More Introduction
---
## **A Simple Compilation Strategy**

Programs are sequences of statements, so repeatedly call `compile_statement(statement)`:

- Unconditional: `expr;`
- Compound: `{ statement1; statement2; ... }`
- Conditional: `if (expr) statement1; else statement2;`
- Iteration: `while (expr) statement;`

We also need `compile_expr(expr)` to generate code 

- Constants
- Variables: `a, b[expr]`
- Statement: `a = expr`
- Operations: `expr1 + expr2 = expr`
- Procedure calls

Compiling expressions: recursive descent

Optimisation: keep values in registers (move store and load instructions out of the loop)

## Anatomy of a Modern Computer

1. Analysis (front-end): $\text{source code} \to \text{IR}$
2. Optimisation passes (middle-end): $\text{IR} \to \text{IR}$
3. Synthesis (backend): $\text{IR} \to \text{code for ISA}$

After translating IR to ASM, we can also have options to optimise ASM further.

### Front-end

- Lexical analysis (scanning): source $\to$ list of tokens
- Syntactic analysis (parsing): tokens $\to$ syntax tree
- Semantic analysis (mainly type checking): syntactically correct AST

![Untitled](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%205.png)

### Back-end and optimisations

IR is an internal compiler language which is language and machine independent and is easy to optimise.

- Common IR: convert AST to a Control Flow Graph
- Basic block: sequence of assignments with an optional branch at the end.

![Untitled](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%206.png)

### IR Optimisation

Perform a set of passes over the CFG.

- each pass does a specific simple task over the CFG
- by repeating multiple simple passes on the CFG over and over we achieve very complex optimisations

Example opimisations:

- **dead code elimination**: eliminate assignment to variables which are never used and basic blocks that are never reached
- **constant propagation**: identify variables that are contant and substitute the constant elsewhere
- **constant folding**: compute and substitute constant expressions
- loop unrolling
- loop invariant code motion
- common subexpression elimination

### Code Generation

- Translate IR to assembly
- **Register allocation**: map variables to registers: if variables are greater than registers, map some to memory and load or store when required
- Translate assignments to instructions
- Emit each basic block labels
- ISA and CPU-specific optimisation

## Questions

1. Details on Register Allocation.
    - NP complete problem
    - Graph coloring to achieve allocation and assignment (Chaitin et al. reduction)
    - Decides which values will recide in register and which register will hold what
    - **Problems**:
        - Aliasing: for example, assigning a 32 bits value to the eax will affect the al register
        - Pre-coloring: some variables are forced into fixed registers
        - NP completeness
    - **Nomenclature**:
        - move insertion: increasing number of move instruction between registers (make varibale live in multiple registers in its lifetime)
        - spilling (storing variable in memory rather than registers)
        - assignment (assigning register to a variable)
        - coalescing (limiting the number of moves between registers)
    - **Graph coloring register allocation**
        
        ![Untitled](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%207.png)
        
        - Finding the optimal or minimal graph coloring is also NP complete.
        - Unless live-range splitting is used, evicted variables are spilled.
        - A variable that is not spilled is kept in the same register throughout its whole lifetime.
    - Linear Scan
2. How does the compiler generates code for function calls (like prolog, epilog etc)?
    - In very short terms, they are pulled out of the expression and a temporary variable is created to hold the result of their computation.
3. How is runtime stack maintained (like local variables, arguments etc go on to the stack, how activation record is created for each function call)?
    - Has a stack of activation records
    - runtime stack is kept in the data segment of memory
    - **store return address of the caller function**
    - methods also have parameters and local varibles and all these are stored in the stack frame (activation record) of a method (pushed and poped out when called and terminates respectively)
    - methods are executed when they are called (we shall have a call tree)
    - it shows which method is being executed and which methods called it (gg for debugging)

## LLVM

![Untitled](Programming%20and%20Systems/images/Compiler%20Review%20020673ce66f64d8ea2ea8a0fdeee1575/Untitled%208.png)

LLVM uses CFG internally after AST is converted to CFG.

In compiler design, static single assignment form (often abbreviated as SSA form or simply SSA) is a property of an intermediate representation (IR), which requires that each variable be assigned exactly once, and every variable be defined before it is used.

- [**Constant propagation**](https://en.wikipedia.org/wiki/Constant_propagation) – conversion of computations from runtime to compile time, e.g. treat the instruction `a=3*4+5;` as if it were `a=17;`
- [**Value range propagation**](https://en.wikipedia.org/w/index.php?title=Value_range_propagation&action=edit&redlink=1) – precompute the potential ranges a calculation could be, allowing for the creation of branch predictions in advance
- [**Sparse conditional constant propagation**](https://en.wikipedia.org/wiki/Sparse_conditional_constant_propagation) – range-check some values, allowing tests to predict the most likely branch
- [**Dead code elimination**](https://en.wikipedia.org/wiki/Dead_code_elimination) – remove code that will have no effect on the results
- [**Global value numbering**](https://en.wikipedia.org/wiki/Global_value_numbering) – replace duplicate calculations producing the same result
- [**Partial redundancy elimination**](https://en.wikipedia.org/wiki/Partial_redundancy_elimination) – removing duplicate calculations previously performed in some branches of the program
- [**Strength reduction**](https://en.wikipedia.org/wiki/Strength_reduction) – replacing expensive operations by less expensive but equivalent ones, e.g. replace integer multiply or divide by powers of 2 with the
potentially less expensive shift left (for multiply) or shift right (for divide).
- [**Register allocation**](https://en.wikipedia.org/wiki/Register_allocation) – optimize how the limited number of machine registers may be used for calculations