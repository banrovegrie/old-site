---
title: "OS1"
date: 2021-07-18T06:48:10+05:30
---

# Operating System

<p style="text-align:right;"> By
<a href="http://pages.cs.wisc.edu/~remzi/Classes/537/Spring2018/">Remzi</a>
</p>

# Virtualization

## Lecture 1

- Illusion of the running program:
    - own CPU
    - own Memory.

- Key aspects:
    - Efficiency
    - Security

- CPU Virtualization
    - Time Sharing
    - Space sharing
    - **Multi-programming:**  A computer running more than one program at a time.

- Abstraction: **Process** ~ a running program
- Components of a process:
    - Memory (private) {Address space}
    - Registers (their states actually) are a part of process.

### Mechanisms (& Policies): How?

- Core mechanism behind virtualization: **Limited Direct Execution**
    - Limited -> security.
    - DE -> efficiency.

### Limited Direct Execution:

- Problems: 
    1. What if an "A" wants to do something `restricted` (User and Kernel mode by [mode bit](https://stackoverflow.com/questions/13185300/where-is-the-mode-bit))?
    2. What if OS wants to `schedule` (stop "A", run "B")?
    3. What if "A" does something that is slow (`spooling and all`)?


1.  How to change modes? 
    - At boot time, *Kernel mode*.
    - We want to run user program, then we need a) transition from kernel to user mode, b) jumps to some location in user program.
    - If user program wants resources (`restricted`), jumps in kernel mode to a specific . We can't specify specific address to jump to, but the OS decides where we can jump to in the kernel. 
    - We use 2 instructions:
        - **Trap/ System Calls**: Jumps into kernel but restricted positions (remember the table). Elevate privileges.
        - **Return from Trap**: 
    Restore the "state" of the registers. (Self-explanatory)

2.  Co-operative Approach: Hope that "A" doesn't do bad stuff per se.
    Non-cooperative/ preemptive Approach: Based on H/W approach.
        - Starts *Timer interrupt*

**Note:** 

1. The kernel installs a **trap table** at boot time.

2. ***Trap Handler***:
   `The trap handler is the code that will run when the trap is triggered. In your example, the OS will have installed a handler (i.e. told the CPU a memory address of code to run when the trap happens), and the handler will execute the system call. It is NOT the program that jumps to kernel mode. The program is interrupted immediately after it triggers the trap. Execution resumes with the trap handler. This way, the three layers (program that runs in protected mode, operating system that runs in privileged mode and CPU/hardware that enforces that currently executing code cannot break out of protected mode) can hand off control between each-other.`
3. `To specify the exact system call, a system-call number is usually assigned to each system call. The user code is thus responsible for placing the desired system-call number in a register or at a specified location on the stack; the OS, when handling the system call inside the trap handler, examines this number, ensures it is valid, and, if it is, executes the corresponding code. This level of indirection serves as a form of protection; user code cannot specify an exact address to jump to, but rather must request a particular service via number.`

<br>

## Lecture 2

**CPU virtualization**
    - Mechanism
    - Policies (Scheduler)

- The `fetch, decode, execute` model is just based while considering while working with a single process.
    The Execute (**Interrupt handler**) basically checks the mode bit before execution. If it's not okay, hardware detects that error and raises an exception, which OS handles(**exception handler**).

- Handling *pending interrupts:* OS does this. (How tho? Ans: **Signalling**)

### CPU Virtualization mechanisms

- At Boot time: OS runs first (Kernel loads up)
    1. Installs *Handlers*: Tells h/w what code to run on what exception/ interrupt/ traps. {This is done by a privileged instruction. In x86: `lidt`}
    
2. Initialize *timer interrupt*: {privileged} Way to regain control of CPU by OS. OS handler can switch to different process, `context switch`.
  
       Use `lmbench` to measure time taken for sys-calls or context-switch.
  
    Now, Ready to run user programs. 
  
- OS must track the different user processes, done by **process list** (queues).
- Slow Operations (I/O): Tracked by the structure defined in Silberschatz.
  
    - States: READY, RUNNING, BLOCKED (I/O).

### OS: Policy

Each process "job".
*Assumptions:*

- All arrive at @ same time.
- Each job only uses CPU.
- Each job runs same amount of time `T_i`
- No I/O occurs.
- $T_i$​ is *same* for all processes (known ahead of time).
- **Metric:** *Turnaround time* i.e. $time_{end}\ -\ time_{arrived}$

#### **Policies**:

1.) FIFO {Checkout Gantt chart if you want.}

- Say A, B, C each take 100 nanoseconds for execution. Then $T_A = 100$, $T_B = 200$ and $T_C = 300$. 

To improve this, we relax some impositions.   
- `All jobs have same runtime`. We come to a conclusion to schedule *Shortest Job First **SJF***.
    Generalisation for the same: **Shortest Time Completion First (STCP)** 
    New: ***Preempt*** the job (in cases, stopping existing jobs and starting another one)
    
- **New Metric: Response Time**
    1. Time until the process generates a "response".
    2. $Time_{first\ runs} - Time_{arrives}$
    We can change the policy to **Round Robin Scheduling**.
    *Trade off*: If there are short time slices, we get better response times but high context switch overheads, and vice versa for the opposite.

<br>

## Lecture 3

Problems with :

- **SJF**: Assumes knowledge of run-time.

- **Round-Robin**: Considering a preemptive system with time slicing. Is `responsive` but `context switch overheads`.

### Classic UNIX Scheduler

### Multi-level Feedback Queue MLFQ

**Problem:** Don't know much about processes! To overcome the same, we might try to learn the shorter jobs or which ones have longer running time!

**HOW?** *Measure*: Using history to predict.

**Many Queues:** Job is one one queue at any given time (which might change over time). Here, each queue has a priority.

**Rules.** 

a) If the Priority(A) > Priority(B) => A runs.

b) If Priority(A) = Priority(B) => Round Robin b/w them.

c) **Start:** at Highest Priority.  If the process uses the time slice @ given priority, at the end of time-slice, move down one level.

Basically, after the process consumes it's time slice, it descents in priority queues. Now, say some new shorter processes come along and get into the highest priority queue, they'll context switch and get processed. (**RR** in same priority does its work) All well and good? Actually no. What if we get a sequence of jobs hogging up the cycles?

**Starvation:**  How to ensure long-running jobs make other jobs progress?

**General Idea:** Long-running jobs need to move up.

**Rule d)** Every T seconds, move all jobs to highest priority. 

This new rule helps to `relearn` about the processes in every time period. The nature of job *might change* b/w interactive and batch, but we get improved performance.

**New Worry: I/O**

Say B runs for time less than time-slice and issues I/O.

*Naive rule for I/O jobs:* If jobs run for less than time slice, *stay* at *same level*. Problem with this becomes **Black hat/ Gaming the scheduler**. {Same processes again starving other processes.}

**Better accounting:** If the job uses up its *time slice*, move down.\

#### Parameters for MLFQ

1. $N$ : Number of queues.
2. $Q$ : Quantum length/ time-slice length (maybe **per queue**).
3. $T$: Reset period.

- How to configure? *Use defaults* :stuck_out_tongue:.  {But search for this !!! ~~Use ML to find the sweet stop for your configuration? Who's stopping you!!~~ We can  use `optimization techniques` to do so.}

  

### Virtual Memory

**Process**/ Running programs are abstraction of our computer.  Abstraction is basically implemented during the `context-switch`.

Each process along with other resources, has a `virtual address space`, Goals for such memory include *large memory* for ease, *private(protected) memory* and *efficient memory*.  Note that we don't want inter-process memory intrusion {personal lingo}. 

### Mechanisms:

- **Hardware support**
- **OS support**

**Memory Accesses:** a) Instruction fetch; and b) explicit loads, stores.

Remember that physical memory is byte-addressable.  On the contrary, disk memory is mostly divided into sectors (512 in '18, Now?) and we'll have to operate {read, modify, write} on all of it :frown: .

We need some way to `interpose` efficiently. So we mostly use:

- **Address Translation:** Give a temporary address illusion to the virtual address space.  On every memory reference, translate virtual memory address to physical memory address.

  1. *Mechanism #1* : **Dynamic Relocation** (or *Base/ Bounds*)

     Assume that a process $p_1$ as a `small` virtual address space and so does $p_2$. We'll allocate these to disjoint address spaces in physical memory. **Implementation:** ***Memory Management Unit MMU*** in CPU. 

     In MMU, we have 2 registers (per CPU): 

     - **Base**: Address in physical memory where the address space of currently running process starts. `Physical Address = Base + Virtual Address`.
     - We **CHECK** if it's within bounds.
     - **Bounds**.

     **Base/ Bounds** is fast & simple and virtualization (minimal), but it's hard to allocate address space (contiguous) and hard to expand & share memory.

     **Note:** Every address in user program is `virtual address`.

  2. **Modern OS** supports sharing of memory.

  **CPU Abstraction:** `while (true){fetch, decode, *execute* [limits imposed] [MMU bounds it.]}`

  If the virtual address space for a process is `fragmented`, we can't actually handle it properly (at least  with this structure.)

- **OS Roles:**

  - **Context Switch:** In context of the virtual address space associated with a process, OS saves/ restores base and bounds. Instructions to do so must be privileged. 

    If we need to allocate contiguous memory to the processes (a minimalist way), it becomes a question of `defragmentation`!

    1. Stop the process(es).
    2. Way to decide where to put each.
    3. Non-destructive copy
    4. Change Base to new values.
    5. Make $p_1, p_2, \ldots$  runnable. 

    Note that for **defragmentation** is not flexible and expensive.

  **NOTE**: One problem that the meltdown bug has the reason they had problem was that the Linux Kernel has all the physical memory mapped into the Kernel virtual space and kernel virtual space  actually mapped into every user process is generally not accessible. 

**OS:** When we use malloc -> sys call, we are asking for more memory (basically from the heap). We'll have to use defragmentation if there's not enough available physical memory. So what OS does is just change bounds and registers for the optimal memory usage.

`Every access is virtual.` 

- **<u>Lack of Flexibility</u>:** In our current virtual address space scenario, we have heap and stack growing towards each other. If we do this with dynamic relocation it doesn't work well <u>because</u> there's a lot of empty space b/w them, which is kinda `waste`. The `0` virtual address is basically left for the NULL pointer. 

Now, we are going to generalize `Base & Bounds` into a concept **SEGMENTATION** which basically consists of <u>multiple base/ bounds per process, one pair per logical region of address space (the code, heap and stack basically as different parts can be anywhere in the physical address space, and the region b/w heap and stack actually can be anywhere since it's not mapped to physical memory.).</u> (:warning: TO-DO Image) {TO-DO: Stack smashing!}

- Now waste (internal fragmentation), but we'll need defragmentation. 

- OS roles: a) Save/ restore base/bounds pair for each logical region.

  ​				b) Still have to apply defragmentation and malloc.

## Lecture 4

**<u>Virtual Memory</u>**:

- Mechanisms discussed

  - Dynamic Relocation

  - Segmentation (Generalisation of base/ bounds) {Sparse Address space}

    - Aside this, there were 2 levels of memory management
      - inside the virtual address space
        - Stack is managed by language run time.
        - Heap by C : malloc

    - **Problems:**

      1. Support sparseness: but limited. Same problem as Dynamic relocation but at lower level. Arbitrary sparseness not used :( .

      2. <u>**External fragmentation**</u>:  

         ​	1. For a process requiring memory, we either have to reject the request or compact the memory (expensive).

### Paging

<u>Potential Problems</u>:

- Slow
- Memory hog

**Paging:** Divide up a) Virtual Add. Spaces and b) Physical memory into <u>fixed-size units</u> called <u>pages</u>. 

![](https://i.imgur.com/SISGnJc.png)

**Issues:**

1. This is a lot of information.
   - Generally stored in memory, so not so super-fast :(.

- **VPN** - Virtual Page Number (In a page, some of the first bytes of all the bytes stored there are same, which is then used to uniquely identify the page.)
  **PFN** - Physical Frame number (Page/chunk in the physical memory.)

  - **Translation** here occurs just by changing the VPN -> PFN. 

  - **Offset** - The specific index inside a Page.	    

  - ![](https://i.imgur.com/m4Jwg8c.png)

  - **Translation Information:** 

    - Store this in memory somewhere.

    - Call <u>**D.S.**</u> that stores this info into a **Page Table**.

      - *Array*/ Linear Page Table: One per process. (thinking for simplicity)

    - **Contents of Page Table:**

      - Considering our linear model, one entry per VPN. So, just index by VPN. 
      - We take our VPN, and index it ( **Page Table Entry PTE** ). {simple indexing and storing the transformation.} 
      - For pages not used, we should throw some exception {fault}. Hence we also have a *valid* bit in each PTE.

    - How does translation occur?

      ​	We don't generally want OS to do this. Why? Great that I asked. Sped.

      ​	We do want hardware efficiency. 

      What does the h/w need to know?

      - Location/ physical address of page table in physical memory.
        - Per CPU register: **Page table base register PTBR**. In a multi-CPU scenario, we have a PTBR on each CPU core which helps with the translation.
      - Page size.
      - Structure of page table entry

    - Say in memory @ address 4, PT is saved. Hence, we set PTBR: 4.

    - This PTBR changes on context switch.

  - Given a **VA** we need to translate, we need to figure out the physical address of the desired page table entry. So ,

    1.  `VA: PTBR + (VPN * sizeof(PTE)) `
    2. Load PTE.
    3. Do translation
    4. Load data.

  - **PTBR** details:

    - restricted (not all can update)
    - Process table: save/ store PTBR in context switching

  - **Problems:**

    1. Slow
    2. Big

- Note that this whole mechanism is way slower than what was in Segmentation or Dynamic Relocation.

- Cache: **Translation Look-aside Buffer TLB**/ **Address Translation Cache**

- Translation (re-visited)

  1. **VA**: VPN + Offset
  2. **CPU:** extract VPN and lookup in TLB.
     - *HIT*: great and fast. **PFN: form PA** + do memory reference
     - *MISS:* fetch **PTE** from memory (slow) and update TLB with contents.

- **TLB** contents: 
  
  - A list of tuple of  *VPN -> PFN*, with each valid bit (and pid) also present.
  - During context-switch: *flush* TLB-contents.
- <u>Different</u> way to structure memory management support in h/w:
  
  - So far: **h/w** managed **TLB**. (complexity of h/w is high)
  - Now: **OS** managed **TLB**.
    - Idea:
      - If **TLB** hits, still all **h/w**;
      - If **TLB miss**,
        -  Raise *TLB miss exception*,
        - Consult Page table + find translation
        - Update *TLB* (priviledged process).
        - Return from trap.
    - Freedom in OS:
      - H/W doesn't need to know the details of the page table. 
      - **NO PTBR NEEDED**.
      - H/W simpler.

## Lecture 5

- Page Tables: Linear
  - Problems: 
    1. Paging: too slow even with hardware support. Solution: TLB.
    2. Page Tables are too big
    3. What if the amt. of memory accessed by program > amt. of physical memory? (Paging yeeee!)

***Problem 2.*** 32-bits VA space, and page size: 1 KB, then *size* of page table = `1 << 22 ~ 4M`. Also, we need top know about PTE. (Refer to the notes.) Also, there's one page table for each process. Approximately with 100 processes, it hogs up `1600 M` space :astonished:. Now, note that in address space, we have to map the high invalid spaces right? That's way too much inefficient.

**Solutions** for this: 1. Multi-level Page Table; 2. Hybrid (Segmentation + Paging); 3. Inverted: one per system. 

1. Multi-level Page table: **Page Directory entry PDE**: It has PTE in chunks, and each has a bit signifying whether the chunk has a valid bit or not. 

   Q. Why is now OS management easier vs linear?

   Sol. *Tradeoff* - MLPT is slower but smaller. 

   ​		But if we have a large page table (page directory doesn't fit in a page), we do `multi-level` page table. Most processes don't utilise all of their page table, So better.

***Problem 3.*** 

*Memory Hierarchy.* We try to optimise according to where the data required is stored. 

- Swap space (on disk) {in blocks (sector addressable 4KB)} and we have the physical memory.<br />Now we have the Virtual Address space and we make the page table. Now, say a page is valid but is swapped into disk. How do we track that? Keep a present bit too! <br />
  - **Page miss/ fault**: If we don't have the data in memory (tracked by the page table) but swapped out in the disk. (check notes for further mechanism.)<br />
  - **OS: page fault handler**
    - Find free physical frame. If NOT, page out existing page [**Page replacement policy**]
    - Bring in desired page and update the present bit.
  - Now note that if the page is swapped out, we need to store the address where the page will be stored right? We can do that by storing that address instead of PFN (no use then).

### Policy

- **Page replacement:** {These below use history to predict Future.}
  - <u>Least Recently Used LRU</u> (better but harder to implement)
  - <u>Least Frequently Used LFU</u> (better but harder to implement)
  - <u>Most Recently used MRU</u>
  - Random (easy to implement)
  - FIFO (easy to implement)

- **Optimal Policy**:

  - Kick out the page that will be furthest used in <u>future.</u>

- How to implement "approximate" (cuz it requires knowledge of access time of each page) LRU?

  Replacement (in LRU) will take too long if done accurately. We just need an approximate guess.

  **H/W**: When page accessed, it sets bits (*reference bit*)

  **What OS does for replacement?** 

  It scans through the pages. If `ref == 0`, replace.

**RESEARCH:** Belady's Anomaly. 

## Notes

1. Non-blocking vs async: [🔗](https://stackoverflow.com/questions/2625493/asynchronous-vs-non-blocking). 
