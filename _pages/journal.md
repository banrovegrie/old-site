---
layout: archive
permalink: /journal/
title: "Journal"
author_profile: true
redirect_from:
  - /wordpress/blog-posts/
---

<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-AMS_CHTML"></script>

---

> It is sad that we get so used to the world that we fail to recognize how bewildering and even unreasonable, at times, everything is.

## [A Treatise on Thinking and Problem Solving]()

Now, to give a preface, let me state this as clearly as possible. I am neither a mathematician nor a computer scientist and nor can I consider myself a philosopher. I am just a young guy with a laptop and a lot of time. However, I indeed love each of those fields, and given that thinking is not a monopoly of the old and experienced — I decided to explore as much as I can into two questions that have been grappling my mind for quite some time.

The two questions are:

1. Do mathematicians, physicists and computer scientists approach a given problem differently? Is mathematical thinking different from algorithmic thinking? I love the word algorithmic rather than computational because the latter presents an erroneous scope of considering computational thinking an equivalent of thinking/working as a computer.
2. Are some really generalizable heuristics that can be used or applied to any formal problem?

Both of the questions are very dear to my heart, and I will try my best to put forward several ideas I have come across and as they have been filtered and modified by my own point of view.

### Mathematical Thinking and Algorithmic Thinking

Mathematical Thinking and Algorithmic Thinking have a lot in common. It shall be easier to first define what we consider Mathematical Thinking to be and what it means to be a mathematician.

### Mathematical Thinking

Mathematical Thinking involves the skills of modeling a given problem formally and rigorously arguing about the formal statement.

- Here, the <ins>point of rigor</ins> is not to destroy all intuition; instead, it should be used to eliminate bad intuition while clarifying and elevating good intuition.
- Even though rigor is merely the instrument of demonstration, just as intuition and curiosity are the instruments of invention, there is no denying that it alone can provide us with certainty.

Moreover, in mathematics, there are two cultures involved. They differ based on the following two ideologies.

1. The point of understanding mathematics is to become better able to solve problems.
2. The point of solving problems is to understand mathematics better.

I subscribe more towards the second culture, probably because I have a greater passion for theory building. After all, you really can't deny that there is something truly romantic about extracting underlying structures and generalizing them to create a much bigger, expressive, and beautiful framework.

### Differences

There are two major differences between Mathematical and Algorithmic Thinking. These involve two basic notions inherent to Computer Science and are totally absent (to a large extent in mathematics).

- notion of complexity and economy of operation (complexity theories)
- dynamic notion of the state of any process (data structures)

These notions are inherently associated with the idea of implementability, which can be used to put forward the following picture — is computer science implementable mathematics? And if it were so, then computer science is rooted in physics as much as we believe it is rooted in mathematics. After all, it is the nature of our universe and existence which determines what is implementable and what is not.

<img src="../images/mathcs.png" width="50%"/>

<ins>Footnote</ins>: The more I read about this, the more I can't help thinking about whether Computer Science isn't just a whole new way of understanding Physics.

### On Heuristics

- <ins>Proofs are Programs</ins>: Often, we find that the approaches we make (both mathematical and psychological) while trying to prove some statement or construct an algorithm are similar.

    This became even clearer when I started reading more about the correspondence between proofs, programs, and algebraic structures. Such a trinity allows me to say with certainty that proofs and algorithms are complementary and analogous to a great extent. Furthermore, thinking about proofs and programs in this manner often gives me a clearer perspective while approaching any given problem.

- <ins>Wishful Thinking, Modularity and First Principles</ins>: This is basically a modular approach to the idea of constructing an algorithm or proving a theorem. You start off by wishing for simplifications in your problem. You achieve simplifications by breaking it down or transforming it into a simpler problem and try your hand at that.

    Moreover, on a similar note, you might keep stringing lemmas (or functions or data structures) together with speculation that has been cleaned and sharpened with rigor to construct a proof (or algorithm).

- <ins>Speculations, Questions and Partial Progress</ins>: While solving a problem it is vital to keep changing your perspective. You need to look at it and attack it differently (using different tools with different tricks). For example, try contradictions, then maybe induction, then maybe something else and so on.

    Likewise, never hesitate to keep asking questions, no matter how dumb they might seem. Don't take anything you don't really understand for granted! Where's the fun in that?

    Also, you need to realize how crucial partial progress is. Failures are often crucial advances. In fact, people should write about their failures and speculations while writing a paper. Because well, if we don't at all have any insight into what made someone come up with an argument or construction, then what is the fricking point at all?

- <ins>Grothendieck and Abstraction</ins>: "While looking at a problem through different lenses ideally you would want to find the natural world for the problem, express it cohomologically and often the cohomology of that world may solve your problem, like a ripe avocado bursts in your hand."

    Grothendieck was a guy who literally rebuilt algebraic geometry from scratch. His unique skill was to burrow into an area so deeply that its inner patterns on the most abstract level revealed themselves, and solutions to old problems fell out in straightforward ways quite naturally to fit into a larger conceptual framework.

    > From Grothendieck, I have also learned not to take glory in the difficulty of a proof: difficulty means we have not understood. The idea is to be able to paint a landscape in which the proof is obvious.

    Moreover, in computer science, abstraction is fundamentally how we approach the most exciting problems. Or do you want to write optimizations in binary (a horrible example but you do get it)?

- <ins>Formalism and Writing</ins>: Formalism is arguably the most important and constant step towards solving any problem. This is something I learned while studying functional programming. Often, the act of describing a problem and stating it formally reveals what you need to solve it.

    And in case you are dealing with an algorithm or a computer system, formalism through programming is literally both the crux and beauty of it.

    Similarly, on a broader note, writing too is hugely essential. In fact, ideally, it is the primary mechanism for doing research and not just for reporting it.

### Conclusion

Heuristics, as mentioned above, serve as more of a psychological strategy than a tangible cut out path for solving problems. Almost all major problems that lurk in the horizon of human understanding are mainly solved by "knowledge (of your own field and of other fields), experience, patience and hard work".

Furthermore, we don't really understand how a human being thinks. We do have some understanding that our linguistic capabilities serve as the operating system of our minds supporting abstraction other cognitive abilities. However, that being said, there is so much more that we don't understand. But, don't let this lack of understanding reflect any kind of unimportance of the subject -- for if we don't even understand how we think, how could we possibly make machines that can truly think like and for us?

### References

1. [The Two Cultures of Mathematics](https://www.dpmms.cam.ac.uk/~wtg10/2cultures.pdf) by Gowers
2. [On Proof and Progress in Mathematics](https://arxiv.org/pdf/math/9404236.pdf) by Thurston
3. Poincaré on [Intuition in Mathematics](https://mathshistory.st-andrews.ac.uk/Extras/Poincare_Intuition/)
4. [Algorithmic Thinking and Mathematical Thinking](https://sci-hub.do/https://doi.org/10.1080/00029890.1985.11971572) by Knuth
5. [There’s more to mathematics than rigor and proofs](https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/) by Tao
6. [Ask yourself dumb questions](https://terrytao.wordpress.com/career-advice/ask-yourself-dumb-questions-and-answer-them/) by Tao
7. [Solving mathematical problems](https://terrytao.wordpress.com/career-advice/solving-mathematical-problems/) by Tao
8. [How to write a great research paper](https://www.youtube.com/watch?v=WP-FkUaOcOM)

## [What is Communication?]()

Today, there a more than $7$ billion people living on this planet. We have surpassed all other species of animals by an incredibly long margin. We have achieved feats that were inconceivable once. We have touched the moon, discovered particles that are infinitesimally small and galaxies that are larger than we can even conceive, we have conquered the high mountains, trekked impassable deserts, scoured the skies and tamed even the raging seas. But one feat that separates us completely from all that came before us - the ability to believe in an imagined reality, to believe in a collective myth and values and this is what has ultimately given shape to modern human society.

The telling of myths and stories allow Homo sapiens to collaborate in large numbers in extremely flexible ways. This separates us from all other animals. And, all this is possible because of the human ability to communicate with extreme efficiency and precision. This ability to communicate efficiently and effectively is what creates scientific and artistic breakthroughs, leads to the establishment of companies, corporations, markets and even nations. It is indeed how we human beings have literally conquered the world. 

The word communication is derived from the latin word communicare which means to share. "Communication is the act of conveying meanings from one entity or group to another." Language serves the most organised and efficient mode of communication. But it is not the only mode. Visual arts in the form of sculpture, paintings and photography, performance arts in the form of acting and dancing often convey deep emotions that get deeply engraved in our minds, something that even the finest constructed sentences fail to do. Such forms of communication certainly do not rely on words or grammatical structures. 

Much of modern linguistic theory is based on the assumption that the primary and
fundamental function of language is communication. But that certainly doesn't make language the sole authority or mode over communication.

## [Rosch and Whorf's Hypothesis: an  excerpt]()

Rosch's early studies were on color. She learned of the Berlin-Kay color research midway through her own research and found that their results meshed with her own work on Dani, a New Guinea language that has only two basic color categories: mili (dark-cool, including black, green, and blue) and mola (light-warm, including white, red, yellow).

Berlin and Kay had shown that focal colors had a special status within color categoraies-that of the best example of the category. Rosch found that Dani speakers, when asked for the best exampies of their two color categories, chose focal colors, for example, white, red, or yellow for mola with different speakers making different choices.

In a remarkable set of experiments, Rosch set out to show that primary color categories were psychologically real for speakers of Dani, even though they were not named. She set out to challenge one of Whorf's hypotheses, namely, that language determines one's conceptual system. If Whorf were right on this matter, the Dani's two words for colors would determine two and only two conceptual categories of colors. 

Rosch reasoned that if it was language alone that determined color categorization, then the Dani should have equal difficulty learning new words for colors, no matter whether the color ranges had a primary color at the center or a nonprimary color. 

She then went about studying how Dani speakers would learn new, made-up color terms. One group was taught arbitrary names for eight focal colors, and another group, arbitrary names for eight nonfocal colors (Rosch $1973$). The names for focal colors were learned more easily. Dani speakers were also found (like English speakers) to be able to remember focal colors better than nonfocal colors (Heider $1972$).

In an experiment in which speakers judged color similarity, the Dani were shown to represent colors in memory the same way English speakers do (Heider and Olivier $1972$).

## [Knowledge]()

Let's say that Knowledge is "Justified True Belief". But what does it mean to justify something? This definition results in an infinite regression. This can be solved using ideas of Foundationalism (use of axioms).

## [Logic]()

Truth is a property of a statement which determines whether the given statement is in agreement with reality (to the best of our knowledge). In a given argument, we always talk about the truth value of all premises associated.

On the other hand, validity is a property of an argument which implies whether or not it is impossible for the given premises to be true and the conclusion, at the same time, to be false. In other words, an argument is valid if and only if truth of its premises guarantees truth of its conclusion. However, it is not required for a valid argument to have premises that are actually true.

Meanwhile, soundness is a property of both an argument along with the given premises (property of a formal system). An argument is said to be sound if and only if it is valid and all given premises are true. Thus, soundness effectively combines both validity and truth. This is best reflected by the fact that, a sound argument is necessarily valid, but a valid argument may not be sound.

A deductive argument is an argument that is intended by the arguer to provide a guarantee of the truth of the conclusion provided that the argument’s premises are true. All deductive arguments are either valid or invalid, and either sound or unsound; there is no middle ground, such as being somewhat valid.

Example: "All women are mortal. My mother is a woman. Therefore, my mother is mortal."

Explanation: The above statement has two premises. Firstly that, all women are mortal and secondly, that my mother is a woman. The argument is deductive because provided the premises are true, the conclusion is guaranteed, rather than being guaranteed with a probability less than one.

An inductive argument is an argument that is intended by the arguer to be strong enough that, if the premises were to be true, then it would be unlikely that the conclusion is false. So, an inductive argument’s success or strength is a matter of degree, unlike with deductive arguments. It is basically a probabilistic answer.

Example: "Every raven in a random sample of $3200$ ravens is black. This strongly supports the following conclusion: All ravens are black."

Explanation: Since, the sample test size is considerably large, we can safely conclude that it is highly likely that all ravens are black. Here, in the above argument, the premise is constituted of the first statement - "every raven in a random sample of $3200$ ravens is black".
