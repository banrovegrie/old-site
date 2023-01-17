# The Fuck is Haskell?
---
A *pure*, *lazy*, *functional* programming language. Basically, it is something that happens when like-minded cool people come together.

## Meaning of the above bullshit words?

### Functional

- All hail functions. Children of the idea behind lambda calculus. Use functions just like any other sort of values.
- Evaluate not execute.

### Pure

- Immutability is the key.
- Fuck all side-effects.
- Deterministic as fuck.
- Benefits: equational reasoning, parallelism, happiness

### Lazy

- Infinity? ez.
- Compositional programming — you feel like Mozart.
- Disadvantage: Wot is time? Wot is space?

## Haskell, the new cool guy in campus

### Types

- Statically typed: run time errors $\rightarrow$ compile-time errors
- Expressive: the code is the documentation
- Expressive: brings clarity into coding

### Abstraction

- Eat, Code, Sleep, ~~Repeat~~: Haskell has polymorphism, higher-order functions and type classes — so fuck repetition.
- Think about the big picture and don't cry about some stupid exception.

### What can I do with it?

- Program Correctness (QuickCheck)
- Fail safe programming (Cardano)
- High-load concurrent programming (web back-end)

# Haskell: A Functional Programming Langauge
---
What does it mean for Haskell to be a functional programming language? Well, it means that Haskell follows the principle of functional programming — a programming paradigm where functions are the basic building blocks of computation.

**Def:** *A function is a mapping that takes one or more arguments and produces a single result.*

## Properties of Haskell

- Consice programs
- Powerful type system
- List comprehension
- Recursive functions
- Higher-order functions
- Effectful functions
- Generic functions
- Lazy evaluation
- Equational reasoning

# First Steps
---
Haskell comes with a large number of built-in functions, which are defined in a library file called the standard prelude.

- `head <list>`
- `tail <list>`
- `take <num> <list>`
- `drop <num> <list>`
- `sum <list>`
- `reverse <list>`
- `product <list>`

## GHCi Command

![Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled.png](Programming%20and%20Systems/images/Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled.png)

## Function Format

Just as in lambda calculus haskell follows a fixed pattern for functions. Here are some examples to elaborate:

- $f(x)$ as `f x`
- $f(x, y)$ as `f x y`
- $f(g(x))$ as `f (g x)`
- $f(x, g(y))$ as `f x (g y)`
- $f(x)g(y)$ as `f x * g y`
- Function application has the highest priority than all other operators.
- `x `f` y` is a syntactic sugar for `f x y`

## Examples

```haskell
-- Program 1
main = print (a ++ b ++ c)
a = [((2**3) * 4)]
b = [(2*3) + (4*5)]
c = [2 + (3 * (4**5))]

-- Program 2
main = print (n)
n = (a `div` (length xs))
    where
        a = 10
        xs = [1 .. 5]

-- Program 3
main = print (a [1 .. 5])
a xs = sum (drop (length xs - 1) (take (length xs) xs))
main = putStrLn "hello, world"
```

# Types and class
---
### **Types**

- They are a collection of related values.
- `f :: A -> B` and `e :: A` then, `f e :: B`
- **Bool** – logical values
- **Char** – single characters
- **String** – strings of characters
- **Int** – fixed-precision integers
- **Integer** – arbitrary-precision integers
- **Float** – single-precision floating-point numbers
- **Double** – double-precision floating-point numbers
- `[[’a’,’b’],[’c’,’d’,’e’]] :: [[Char]]`
- **List** types — `["One","Two","Three"] :: [String]`
- **Tuple** types — `("Yes",True,’a’) :: (String,Bool,Char)`
- **Function** types — `not :: Bool -> Bool` and `add :: (Int,Int) -> Int`
- **Polymorphic** types — `length :: [a] -> Int` and `zip :: [a] -> [b] -> [(a, b)]`

### Classes

- They are collections of types that support certain overloaded operations called methods.
- Eq — `(==) :: Eq a => a -> a -> Bool`
- Ord — `<, >, min, max` with `(<) :: Ord a => a -> a -> Bool`
- Show — `show :: a -> String`
- Read — `read :: String -> a`
- Num — e.g., `(+), (-), negate, abs, signum` with `(+) :: Num a => a -> a -> a`
- Integral — `div :: Int a => a -> a -> a` and `mod :: Int a => a -> a -> a`, also Int and Integer types are instances of this class.
- Fractional — Float and Double are instances of this class. We also have methods such as `/` and `recip`.

# Functions
---
Let us now introduce some really cool implementation techniques in haskell with respect to defining functions.

- Conditionals

```haskell
-- Let's see an example
even :: a -> Bool
even n = (n `mod` 2 == 0)

-- Conditional using "if else"
signum n = if n > 0 then 1 
					else if n < 0 then -1 
					else 0

-- Conditional using "such that"
signum n | n > 0 = 1
				 | n < 0 = -1
				 | otherwise  = 0
```

- Pattern Matching

```haskell
-- Define functions using '_'
len [] = 0
len (_:xs) = 1 + len xs

initials :: String -> String -> String  
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."  
		where (f:_) = firstname  (l:_) = lastname

-- Defining using '_' fundamentally
test :: Int -> Int
test 0 = 1
test 1 = 2
test _ = 0
```

- Lambda Functions

```haskell
\x -> x + 1
```

```haskell
-- For example,
add :: Int -> Int -> Int
add x y = x + y
-- and
odds n = map f [0 .. n - 1]
			where
					f x = x * 2 + 1

-- can be written as 
add :: Int -> (Int -> Int)
add = \x -> (\y -> x + y)
-- and
odds n = map (\x -> x * 2 + 1) [0 .. n - 1]
```

### Currying Functions

Let $x = f(a, b, c)$ then, we shall have the following.

$$
f :: (\text{Type}(a),\ \text{Type}(b),\ \text{Type}(c)) \to \text{Type}(x)
$$

Upon currying, this gets translated to the below expression.

$$
f :: \text{Type}(a) \to (\text{Type}(b) \to (\text{Type}(c) \to (\text{Type}(x))))\\
\text{or, } f :: \text{Type}(a) \to \text{Type}(b) \to \text{Type}(c) \to \text{Type}(x)
$$

This is because, $x = f(a, b, c)$ becomes $h = g(a), i = h(b), x = i(c)$ or if called in sequence $x = g(a)(b)(c)$.

```haskell
fst :: (a, b) -> a
zip :: [a] -> [b] -> [(a, b)]
id :: a -> a
take :: Int -> [a] -> [a]
head :: [a] -> a
```

### Operator Sections

```haskell
-- Operator Sections
w = 1 + 2
-- is same as
x = (+) 1 2
-- is same as
y = (1+) 2
-- or
z = (+2) 1
```

This is very useful to construct certain functions.

![Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled%201.png|center|500](Programming%20and%20Systems/images/Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled%201.png)

# List Comprehension
---
The idea is based on set construction from other sets.

```haskell
xy = [(x, y) | x <- [1..3], y <- [x..3]]

-- The above is an example of dependent generators.
-- Definitions of x and y serve as generators.
-- Check out the usability of .. operator.

concat :: [[a]] -> [a]
concat xss = [x | xs <- xss, x <- xs]

-- Guards are possible for example as bellow.
evens = [x | x <- [1..10], even x]
```

# Recursion
---
## How to think recursively?

- Name the function
- Define its type
- Enumerate the cases
- Define the base cases
- List the "ingredients"
- Reason about the parameters
- Define the transition (non-trivial cases)
- Think about the result

### Recursion

```haskell
-- Example of a recursion
zip :: [a] -> [b] -> [(a, b)]
zip [] _ = []
zip _ [] = []
zip (x:xs) (y:ys) = (x, y) : zip xs ys

-- Append Definition
(++) :: [a] -> [a] -> [a]
[] ++ ys = ys
(x:xs) ++ ys = x : (xs ++ ys)
```

### Memoization

The following memoize function takes a function of type `Int -> a` and returns a memoized version of the same function. The trick is to turn a function into a value because, in Haskell, functions are not memoized but values are.

```haskell
import Data.Function (fix)

memoize :: (Int -> a) -> (Int -> a)
memoize f = (map f [0 ..] !!)

fib :: (Int -> Integer) -> Int -> Integer
fib f 0 = 0
fib f 1 = 1
fib f n = f (n - 1) + f (n - 2)

fibMemo :: Int -> Integer
fibMemo = fix (memoize . fib)
```

## Higher Order Function

A function is called a higher order if it takes a function as an argument or returns a function as a result.

```haskell
twice :: (a -> a) -> a -> a
twice f x = f (f x)
```

- Common programming idioms can be encoded as functions within the language itself.
- Domain specific languages can be defined as collections of higher order functions.
- Algebraic properties of higher-order functions can be used to reason about numbers.

```haskell
-- Example
map :: (a -> b) -> [a] -> [b]
map f xs = [f x | x <- xs]

-- Alternate
map :: (a -> b) -> [a] -> [b]
map f [] = []
map f (x:xs) = f x : map f xs
```

```haskell
-- Example
filter :: (a -> Bool) -> [a] -> [a]
filter f xs = [x | x <- xs, f x]

-- Alternatively
filter f [] = []
filter f (x:xs) | f x = x : filter f xs
								| otherwise = filter f xs
```

### Foldr

A number of functions on lists can be defined using the following simple pattern of recursion.

```haskell
f [] = v
f (x:xs) = x ⊕ f xs
```

Here $f$ maps the empty list to some value $v$ and any non-empty list  to some function $⊕$ applied to its head and $f$ of its tail.

![Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled%202.png|center|500](Programming%20and%20Systems/images/Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled%202.png)

The higher-order library function foldr (fold-right) encapsulates this simple pattern of recursion with the function  $⊕$ and the value $v$ as arguments.

![Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled%203.png|center|400](Programming%20and%20Systems/images/Haskell%20in%20Harsh%20Words%200ae733c038f9426d8f9700f3d416fb9a/Untitled%203.png)

```haskell
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f v [] = v
foldr f v (x:xs) = f x (foldr f v xs)
```

```haskell
-- Generic Examples
sum = foldr (+) 0
product = foldr (*) 1
or = foldr (||) False
and = foldr (&&) True

-- Other examples
length = foldr (\ _ n -> 1 + n) 0
reverse = foldr (\ x xs -> xs ++ [x]) []
(++ ys) = foldr (:) ys
```

### Composition

```haskell
(.) :: (b -> c) -> (a -> b) -> (a -> c)
f . g = \x -> f (g x)

odd :: Int -> Bool
odd = not . even
```

### Other nice library functions

```haskell
all :: (a -> Bool) -> [a] -> Bool
all f xs = and [f x | x <- xs]

any :: (a -> Bool) -> [a] -> Bool
any f xs = or [f x | x <- xs]

takeWhile :: (a -> Bool) -> [a] -> [a]
takeWhile f [] = []
takeWhile f (x:xs) | f x = x : takeWhile f xs
									 | otherwise  = []

dropWhile :: (a -> Bool) -> [a] -> [a]
dropWhile f [] = []
dropWhile f (x:xs) | f x = dropWhile f xs
									 | otherwise  = x:xs
```

Moreover, curried functions are higher-order functions that returns a function.

### Where and Let Clauses

```haskell
-- Let
f = let x = 1; y = 2 in (x + y)

-- Where
f = x + y where x = 1; y = 1
```

# Type and Class Declaration

---

```haskell
type Pos = (Int, Int)
type Trans = Pos -> Pos

type Tree = (Int, [Tree])
```

A completely new type can be defined by specifying its values in context-free formulation.

```haskell
data Bool = False | True
```

```haskell
data Answer = Yes | No | Unknown

answers :: [Answer]
answers = [Yes, No, Unknown]

flip :: Answer -> Answer
flip Yes = No
flip No = Yes
flip Unknown = Unknown
```

```haskell
Circle :: Float -> Shape
Rect :: Float -> Float -> Shape

data Shape = Circle Float | Rect Float Float

square :: Float -> Shape
square n = Rect n n

area :: Shape -> Float
area (Circle r) = pi * r^2
area (Rect x y) = x * y
```

### Maybe, Nothing, Just

```haskell
data Maybe a = Nothing | Just a

safediv :: Int -> Int -> Maybe Int
safediv _ 0 = Nothing
safediv m n = Just (m `div` n)

safehead :: [a] -> Maybe a
safehead [] = Nothing
safehead xs = Just (head xs)
```

This is basically a cool syntactic encapsulation to prevent crashing. This is used to often deal with exceptions and create failsafe programs.

### Recursive Types

```haskell
data Nat = Zero | Succ Nat

-- we have Zero :: Nat
-- and Succ :: Nat -> Nat
```

```haskell
data Expr = Val Int
          | Add Expr Expr
          | Mul Expr Expr

eval :: Expr -> Int
eval (Val n) = n
eval (Add x y) = eval x + eval y
eval (Mul x y) = eval x * eval y
```

# Interactive Programming
---
This is a problem because Haskell is designed to have no side effects and thus only to create batch programs.

Interactive programs, on the other hand, necessarily require side effects.

### Solution

- We will use types to describe impure actions involving side effects (`IO a`).
- `IO Char` is the type of actions that return a character.
- `IO ()` is the type of purely side effecting actions that return no result value.

The standard library provides a number of actions including the following three primitives.

```haskell
-- reads character from the keyboard 
-- and echoes it o the screen
-- returning the character as the result value
getChar :: IO Char

-- takes a character as a input and writes it to the screen 
-- and returns no result value
putChar :: Char -> IO ()

-- simply return value without performing any interaction
-- this is basically a pure to impure conversion
return :: a -> IO a
```

### Sequencing

```haskell
act :: IO (Char, Char)
act = do x <- getChar
				getChar
				y <- getChar
				return (x, y)
```

### Derived Primitives

```haskell
getLine :: IO String
getLine = do x <- getChar
						 if x == '\n' then return []
						 else
								do xs <- getLine
									return (x:xs)
```

```haskell
putStr :: String -> IO ()
putStr [] = return ()
putStr (x:xs) = do putChar x
										putStr xs
```

```haskell
-- Just mentioned here so that 
-- one can try out problems with input

import Control.Arrow ((>>>))

main :: IO ()
main = interact $
        lines >>> head >>> read >>> solve >>> (++ "\n")

solve :: Int -> String

-- Type 2
import Control.Arrow ((>>>))

main :: IO ()
main =
  interact $
    words >>> map read >>> solve >>> show >>> (++ "\n")

solve :: [Integer] -> Integer
```

### Simple I/O Operations

These are in-built.

```haskell
putChar :: Char -> IO()
putStr :: String -> IO ()
putStrLn :: String -> IO ()
print :: Show a => a -> IO ()

getChar :: IO Char
getLine :: IO String
getContents :: IO String
interact :: (String -> String) -> IO ()

show :: Show a => a -> String
read :: Read a => String -> a
```

```haskell
main = do
		     putStrLn "enter value for x: "
			   input1 <- getLine
	       putStrLn "enter value for y: " 
	       input2 <- getLine 
	       let x = (read input1 :: Int)
	       let y = (read input2 :: Int)
	       print (x + y)
```

# Lazy Evaluation
---
$$
\text{lazy evaluation} = \text{outermost evaluation}\ +\ \text{shared arguments}
$$

Why is it important?

- No unnecessary evaluation
- Ensures termination when possible
- Supports programming with infinite structures
- Allows programs to be modular (separates control from data)

# Notes on Functional Programming
---
Haskell is very expressive language. It makes you think abstractly and forces to model and define the problem mathematically.

- Focus on what to compute (definitions) rather than how
- Power of abstraction and modularity
- Equational reasoning
- How powerful types are

The main drawback is that it is hard to reason about efficiency.