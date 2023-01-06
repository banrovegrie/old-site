---
title: "OS2"
date: 2021-07-18T06:48:10+05:30
---

# Concurrency

### Single-threaded process

- OS during a process could switch to another process (Context-switch).
  - Save registers(old)
  - Restore registers(new)
  - Load page table.

We want many `activities` going on w/in the process at the same time.

Enter **Multi-threaded process**.

## Threads

- These share the same `address space` (no need to switch page tables b/w context switches b/w threads) and can access the same data.

Note: With processes, we had PCB, now we'll need one or more **Thread Control Blocks (TCBs)** to store the state of each thread of a process.

- Each thread has it's own stack (thread local storage).

### Why Threads? 

- **Parallelism**
  - CPU execution parallelism.
  - I/O parallelism.

### Issues:

- Uncontrolled scheduling, resulting in formation of **synchronisation primitives**.
- Race conditions.

## Thread API

### Locks

```markdown
When pthread_mutex_lock() is called, the thread will acquire the lock and enter the critical section. If another thread does indeed hold the lock, the thread trying to grab the lock will not return from the call until it has acquired the lock 
```

**NOTE:** 

1. Always initialise the lock properly.

2. Destroy the lock (good practices)

3. There exists variants like:

   ```c
   int pthread_mutex_trylock(pthread_mutex_t *mutex); // returns FAILURE if lock is already held
   nit pthread_mutex_timedlock(pthread_mutex_t *mutex,
                              	struct timespec *abs_timeout); // wait for atleast abs_timeout before returning (FAILURE when it can't grab the lock)
   ```


### Condition Variables

Useful when some kind of signalling must take place b/w threads, if one tread is waiting for the other to complete execution before it can continue.

```c
// a)
int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
// b)
int pthread_cond_signal(pthread_cond_t *cond);
```

a) Puts the calling thread to sleep (waiting queue) and waits for a signal.

b) Signals the process to change state from waiting to runnable.

#### USE **[HELGRIND](http://cs.swan.ac.uk/~csoliver/ok-sat-library/internet_html/doc/doc/Valgrind/3.8.1/html/hg-manual.html)** to debug race related issues 

- TODO:- Make a short explanation on how to use the tool for the same and explain every situation as in the link.
- Explore [Communicating sequential processes.]([https://en.wikipedia.org/wiki/Communicating_sequential_processes#:~:text=In%20computer%20science%2C%20communicating%20sequential,on%20message%20passing%20via%20channels.](https://en.wikipedia.org/wiki/Communicating_sequential_processes#:~:text=In computer science%2C communicating sequential,on message passing via channels.))

## Locks

- Hidden info that might be stored in locks:- 

  - Thread pid holding the lock.
  - Queue for ordering lock acquisition.


## Event Based Concurrency

- Different from thread based concurrency in the basic aspect, that can be summarised by the following code:

  ```c
  while (true)
  {
      events = getEvents();
      for (e in events)
          processEvent();			// for some quanta of computational time 
  }
  ```
