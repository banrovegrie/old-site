> "It is stupid to claim that birds are better than frogs because they see farther, or that frogs are better than birds because they see deeper. The world of mathematics is both broad and deep, and we need birds and frogs working together to explore it."
> — **Freeman Dyson**


![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled.png)

# Introduction
---
> "Why should I care about your stupid foundations if I already know Set Theory?"
 — **Kunwar**

Would you ever ask the same question if you were learning Python and knew a language like x86 beforehand? Probably no. If yes, then sorry I definitely can't convince you.

What I will try to introduce here is basically what is referred to as "Univalent Foundations". It is an approach to the foundations of mathematics in which mathematical structures are built out of objects called types.

Set Theory is a low-level programming language when compared to UF. Type Theories are way more expressive and convenient to write proofs (and most importantly programs) in. Moreover, set theory (ZFC) might feel smaller and less complicated but type theory is way more elegant and combines the rules of first order logic and axioms of ZFC into one system. Finally, UF provides a better conceptual foundation for all of mathematics than set theory does.

# Motivation
---
Here, we shall be introducing Martin-Löf's Type Theory, Category Theory and how they are related to the shitty programs that I write.

By why would be willing to learn any of these?

- To be able to reason about programs and algorithms
- To get better at understanding or contructing features of any programming language
- To formalize concepts from different areas of mathematics into a single framework (You don't believe me? Check out Lean mathlib)
- For building automated proof assistants and theorem provers, and maybe even get your computer to prove theorems

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%201.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%201.png)

# Search for Foundations
---
Our story starts with the promise of Cantor's platonic idea presented in "On a Property of the Collection of All Real Algebraic Numbers". Set Theory was born. Today, when we say set theory we refer to ZFC or Zermelo–Fraenkel set theory with the Axiom of Choice.

```markdown
# Axiom of Choice
For any set X of nonempty sets, there exists a choice function f defined on X.

# Equivalent Statements
- Every vector space has a basis
- Well Ordering Principle
- Every connected graph has a spanning tree
- ...
```

Since, the first half of the $20^{th}$ century someone who wanted to get to the bottom of things in mathematics had a simple road to follow: learn predicate logic, learn a particular theory called ZFC, then learn how to translate propositions about a few basic mathematical concepts into formulas of ZFC, and then learn to believe, through examples till you convince yourself, that the rest of mathematics can be reduced to these few basic concepts.

"This state of affairs was extremely beneficial for mathematics, and it is rightly credited for the great successes of abstract mathematics in the twentieth century."

The first problems with ZFC started to occur with the decline of the great Bourbaki mostly because the main organizational ideas of mathematics of the second half of the $20^{th}$ century were based upon category theory — which couldn't well be presented in terms of ZFC.

"So why don't we convert everything to category theory? Grothendieck emphasized it a lot, so it must be something legit?", you may ask. Well problem is unlike ZFC, category theory doesn't provide a complete foundational system. We gravely need a structured formal deduction system. This need was fulfilled by the development of a system based on a combination of ideas from the theory and practice of computer languages with ideas in constructive mathematics. Type Theory was born.

With the advent of type theory and category theory many sweeping changes took place, the most revolutionary of which was that the study of programming languages turned into a profound study formal systems and not just means to computation. However, what didn't change was the way people did mathematics.

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%202.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%202.png)

> Today mathematical research relies on a complex system of mutual trust based on reputations.
> The work of a mathematician is now 5% creative insight and 95% self-verification. Moreover, the more original the insight, the more one has to pay for it later in self-verification work.
> 

In $2013$, Vladimir Voevodsky explained how new ideas that make this goal attainable arise from the meeting of two streams of development — one in the theory and practice of programming languages, and the other in pure mathematics. Finally, Univalent Foundations in the form of  Homotopy Type Theory came into the mainstream with the promise of formalizing mathematics and one day making proof generation an automated task. 

> The dream was to formulate mathematical reasoning in a language precise enough for a computer to follow, as well as for a human to understand. This meant using a foundational system of mathematics not as a standard of consistency to establish a few fundamental theorems, but as a tool that can be employed in ­everyday mathematical work.
> 

# Point of Rigor: in math and programming

---

"The point of rigour is not to destroy all intuition; instead, it should be used to destroy bad intuition while clarifying and elevating good intuition. It is only with a combination of both rigorous formalism and good intuition that one can tackle complex mathematical problems; one needs the former to correctly deal with the fine details, and the latter to correctly deal with the big picture. Without one or the other, you will spend a lot of time blundering around in the dark. So once you are fully comfortable with rigorous mathematical thinking, you should revisit your intuitions on the subject and use your new thinking skills to test and refine these intuitions rather than discard them."

# The Holy Trinity

---

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%203.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%203.png)

### Fuzzy Example

Write a program to check if a word has more than three letters.

```haskell
len :: [Char] -> Int
len [] = 0
len (x:xs) = 1 + len xs

f :: [Char] -> Bool
f x = len x > 3
```

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%204.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%204.png)

This holy trinity to be kept in mind and believed in. But don't worry, unlike the Bible, I will provide reproducible evidence for believing.

# Category Theory

---

> What is a category anyway?
> 

A category $C$ consists of some data that satisfy certain properties:

### Data

💠 A class of objects, $x,y,z,…$

💠 Morphisms between pairs of objects; $x \xrightarrow{f}y$ means "$f$ is a morphism from $x$ to $y$," and the set of all such morphisms is denoted $\hom_C(x,y)$

💠 A composition rule: whenever the codomain of one morphism matches the domain of another, there is a morphism that is their composition, i.e. given $x \xrightarrow{f}y$ and $y \xrightarrow{g}z$ there is a morphism $x \xrightarrow{g \circ f}z$

### Structure

💠 Each object $x$ has an identity morphism $x \xrightarrow{id_x}x$ which satisfies $id_y \circ f = f = f \circ id_x$ for any $x \xrightarrow{f} y$.

💠 The composition rule must be associative ****i.e., $**(h \circ g) \circ f = h \circ (g \circ f)$** whenever we have $x\overset{f}{\longrightarrow}y\overset{g}{\longrightarrow}z\overset{h}{\longrightarrow}w.$

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%205.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%205.png)

### Examples

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%206.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%206.png)

## Bit more on Categories

> A mathematical object is determined by its relationships to other objects.

Category theory strips away details of a system, structure or program and leaves us only with pure mathematical structures and their relationships.

With relationship comes two other entities: 

- Functors: represent relationships between categories
- Natural Transformations: represent relationships between functors

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%207.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%207.png)

What blows my mind is how effective and complicated thinking categorically can be. Don't believe me? Let me show you some astonishing connections between seemingly unrelated things in category terms.

- Axiom of choice is the statement that construction called a limit (or product) exists in the category of sets.

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%208.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%208.png)

- Viewing $\mathbb{Z}$ and $\mathbb{R}$ as posets and hence categories allows you to visualize them as the following.

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%209.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%209.png)

- A functor called $\pi_1$ associates a group to every topological space.
    
    ![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2010.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2010.png)
    
    We can use this functor to prove the Fundamental Theorem of Algebra, Brouwer's Fixed Point Theorem, Perron-Frobenius Theorem.
    

So why did I provide a short overview of Category Theory over here anyway? Well, because Category Theory shall serve as a book-keeping method that will help us relate "formal proofs" and "programs" with general "mathematical structures".

# Computational Introduction to Type Theory
---
Premises: 

- Any suffiently expressive programming langauge can be the basis of all mathematics.
- We understand the notion of computation better than foundational mathematics.
- We have a programming language with deterministic operational semantics.

Plan: Develop Type Theory starting with computation

## Deterministic Operational Sematics

---

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2011.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2011.png)

A little more on semantics.

### Example

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2012.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2012.png)

## Types are Specifications of Behavior

There exists two principle forms of judgement (expressions of knowledge).

$$
A\ \text{type}\\
M \in A
$$

### Example

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2013.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2013.png)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2014.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2014.png)

Takeaway: Types are programs.

## Can Types depend on Types?

$$
seq(n) \text{ type, when } n \in \text{Nat}\\
n : \text{Nat}\ \exists\ seq(n)\ \text{type}
$$

The above relation is referred to as Hypothetical General Judgement.

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2015.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2015.png)

## Functionality

Families (of types, of elements) must respect equality of indices.

For example, $\text{seq}(1+2)$ is same as $\text{seq}(3)$ and similarly, $\text{seq}(\text{if}(17, 18)(M))$ is same as $\text{if}(\text{seq}(17), \text{seq}(18))(M)$.

$$
a : \text{Bool}\ \exists\ \text{seq}(\text{if}(17, 18)(a)) \ \dot=\ \text{if}(\text{seq}(17), \text{seq}(18))(a)

$$

Note: Things you write down in formalism can be never fully express what is TRUE (Godel's Incompleteness).

## Revision of Judgements

So, now after thinking about functionality we have a revision of judgements.

$$
A \text{ type}\\ A\  \dot{=}\ A' \text{type}\\
M \in A \\ M\  \dot{=}\ M' \in A
$$

Intention:

$$
\frac{M \doteq M' \in A,\ A \doteq A'}{M \doteq M' \in A'}
$$

## Meaning of Semantics

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2016.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2016.png)

### Meaning of the Boolean

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2017.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2017.png)

## Some Theorems

Theorem: If $M \in \text{Bool}$ and $A \text{ type}$ and $M_1 \in A$ and $M_2 \in A$ then, $\text{if}(M_1, M_2)(M) \in A$.

Why is is true? Because, $M$ is evaluated first.

Theorem: If $M' \in A$ and $M \to M'$ then $M \in A$.

# Martin-Löf's Dependent Type Theory
---
## Origin

The origin of Martin-Löf's Type Theory is Brouwer's Program which talks about the following things:

- Mathematics is a human activity (language for communication of mathematical concepts)
- Fundamental human faculty is the concept of an algorithm for performing a construction
- Proofs are mathematical objects (not just formal proofs which are a limiting concept)

A cool note to the third point is that just as in MLTT we formalize the notion of "proof of equations" as "programs" in HoTT it is extended to "proofs of equations" as "paths in a space".

Note: Problem with mathematicians is that they often fuck up the idea of abstraction as we understand in computer science and end up coding theorems in such a language which would be analogous to writing a persistent linked lists in assembly language. 

So things to keep eye on:

1. Abstraction
2. Structure
3. Proof Relevance
4. Identity and Equality

I shall present Dependent Type Theory as a formalization of Intuitionistic Type Theory (beware that I haven't covered even a tiny part of this huge rabit-hole). Dependent Type Theory shall serve as the sufficiently expressive language of our Univalent Foundations that shall allow us to implement mathematics.

Now, remembering the Computational Type Theoretic introduction that I presented let us review lambda calculus to warm up for the syntax of Dependent Types.

## Lambda Calculus

Lambda Calculus is a model of Turing-complete programming which has three main components:

- Variables
- Function application $\lambda x$
- Function creation $\lambda x.x+1$

It also has two rules:

- $\alpha$-conversion: $\lambda x.fx \implies \lambda y.fy$
- $\beta$-conversion: $(\lambda x.e_1)e_2 \implies e_1[e_2/x]$

## Constructs

So what is MLTT made of?

- Types (built up recursively)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2018.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2018.png)

- Terms-in-context (built up recursively)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2019.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2019.png)

- Contexts (finite ordered list of typing judgements)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2020.png](Programming%20and%20Systems/images/Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2020.png)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2021.png](Untitled%2021.png)

- Inference Rules
    
    ![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2022.png](Untitled%2022.png)
    
- Derivation

## Syntax

1. Type Formation Rules, which say on which basis a new type can be introduced
2. Term Introduction Rules, which say how that new type can be inhabited by terms
3. Term Elimination Rules, which say how from a term of the new type one gets terms of other types
4. Computation Rules, which constrain the result of combining term introduction with term elimination

## Booleans

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2023.png](Untitled%2023.png)

## Binary Products

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2024.png](Untitled%2024.png)

## Arrow Types

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2025.png](Untitled%2025.png)

## Correspondences

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2026.png](Untitled%2026.png)

# Curry-Howard: a Narrow Intuition
---
## Intuitionistic Propositional Logic

### Judgements

$$
A \text{ prop}\\
A \text{ true}
$$

The above are referred to as basic judgements. We also have another judgement in the form of entailment (a form of higher order judgement).

$$
A_1 \text{ true}, A_2 \text{ true}, ..., A_n \text{ true} \vdash A \text{ true}
$$

### Entailment Properties

1. Reflexivity
    $$
    A \text{ true} \vdash A\text{ true}
    $$
2. Transitivity
    
    $$
    \frac{A \text{ true}\ \ \ \ \ \ A \text{ true} \vdash B \text{ true}}{B \text{ true}}
    $$
    
3. Weakening: The principle of weakening says that we can add assumptions to a proof without invalidating that proof.
    
    $$
    \frac{\Gamma \vdash A \text{ true}}{\Gamma, B \text{ true} \vdash A \text{ true}}
    $$
    
4. Contraction: The principle of contraction says that we are unconcerned about the number of copies of an assumption $A \text{ true}$, one copy is as good as two.
    
    $$
    \frac{A \text{ true}\ \ \ \  A \text{ true} \vdash C \text{ true}}{A \text{ true} \vdash C \text{ true}}
    $$
    
5. Permutation: The principle of permutation, or exchange, says that the order of assumptions does not matter; we can apply any permutation $\pi$ to the assumptions and still have a valid proof.
    
    $$
    \frac{\Gamma \vdash C \text{ true}}{\pi(\Gamma) \vdash C \text{ true}}
    $$
    

Here, you can see that I have not been using $\Gamma$ always and in that case I am not assuming context and reasoning locally. So, you might consider that to be implicit.

Note: Entailment is called structured (lattice) if all 5 of the above hold true. If only the first two hold (it kinda must), we call such an entailment substructured. Denying permutation (along with weakening and contraction) leads to ordered or noncommutative logic. It is a powerful way to express ordered structures, like lists or even formal grammars.

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2027.png](Untitled%2027.png)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2028.png](Untitled%2028.png)

The above shows the negative fragment of IPL. It begins with the following.

$$
\frac{}{\top \text{ prop}}\\
\frac{}{\top \text{ true}}
$$

In the negative segment we do not have an elimination rule.

We can also have a positive fragment with disjunctions. The starters in that case would be the following.

$$
\frac{}{\bot \text{ prop}} \ \ \ \ \ \ \ \ \ 
\frac{\bot \text{ true}}{A \text{true}}
$$

In the positive fragment we do not have an introduction rule.

## Order Theoretic Formulation of IPL

We define $A \leq B$ to hold exactly when $A \text{ true} \vdash B \text{ true}$.

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2029.png](Untitled%2029.png)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2030.png](Untitled%2030.png)

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2031.png](Untitled%2031.png)

### Exponentials as Implication

$$
\frac{}{A \wedge (A \supset B) \leq B}
$$

$$
\frac{A \wedge C \leq B}{C \leq A \supset B}
$$

We can use the idea of exponentials, $B^A$,  for the above.

We can also use neagtion in terms of exponentials since we have the following.

$$
\neg A  := A \supset \bot \equiv A^{\bot}
$$

### Complement

$$
A \vee \bar A \simeq \top\\
\top \leq A \vee \bar A
$$

Note: Boolean algebra is Heyting Algebra with complements. So every Boolean algebra is a Heyting algebra, with the following statement as true.

$$
B^A := \bar A \vee B
$$

### Recap

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2032.png](Untitled%2032.png)

## Provability of IPL

![Foundations%20and%20Motivations%2071ccf5c878fd4ed49490282bf566ca0e/Untitled%2033.png](Untitled%2033.png)

### Decidability and stability

Theorem: $A \text{ prop}$ is decidable if and only if $A \vee \neg A \text{ true}$.

Idea: Disjunction property which says that if $A \vee B$ true, then $A$ true or $B$ true.

Corollary: We must have a proof or a refutation to call something decidable.

This (in Heyting Algebra) is unlike Boolean Algebra where everything is decidable.

Now, how the fuck do I know if decidable propositions even exist?

- $\top$  and $\bot$ are decidable.
- We would expect $m=_\mathbb{N} n$ to be a decidable proposition, where $=_\mathbb{N}$ denotes equality on the natural numbers.
- We would not expect $x =_\mathbb{R} y$ to be a decidable proposition because real numbers are not finite objects. (No recursive decisive procedure exists and by the recursion theorem no computational decisive procedure exists).

If you have doubts regarding the last two points go back to Turing's decidability problem (Halting Problem).

Theorem: $A$ prop is stable if and only if $((\neg \neg A) \supset A)$ true.

Again, in classical logic, every proposition is stable. Okay if this doesn't make sense think about the following statement in your mind.

$$
\text{I don't dislike binging South Park.}
$$

Proof: Suppose $\neg \neg(A \vee \neg A)$ true, that is, **LEM is not refuted**.