## Introduction

Error correction coding is the means whereby errors which may be introduced into digital data as a result of transmission through a communication channel can be corrected based upon received data.

TLDR of necessity: noise is fricking everywhere and we need to deal with it to have robust communication or computation systems.

## Information

At the heart of coding theory, lies the idea of information. So what is it? It can be considered as the amount of uncertainty resolved.

Information conveyed by a discrete random variable $x$ is $I(X) = -\log P(X = x)$.

Related to the concept of information is the idea of entropy, which tells us more about average information in a system.

Thus, entropy $= H(X) = E[-\log(P(X))]$.

Entropy: amount of information we need to actually pinpoint the state the system is in.

## Communication System

Here, we lay down the basic structure of any communication system.

### Data Compression

- **Source**: file (random numbers with a certain probability distribution)
- **Source encoder**: source $\xrightarrow{}$ number of mathematical bits (shannons)

The amount a particular source of data can be compressed without any loss of information (lossless compression) is governed theoretically by the source coding theorem of information theory,

If the data needs to be compressed below the entropy rate of the source, then some kind of distortion must occur. The theoretical limits of lossy data compression are established by the rate distortion theorem of information theory.

$$
\text{Distortion per bit} = H^{-1}(1 - r)\\
r = \text{rate with }p/ \text{bit distortion} = \frac{\text{bits provided}}{\text{bits required}}
$$

- **Encrypter**: scrambles info to prevent evesdroppers.

### Error Correction

- **Channel coder**: adds structured redundant information to the stream of input symbols in a way that allows errors which are introduced into the channel to be corrected

According to the source-channel separation theorem, treating the problems of data compression and error correction separately, rather than seeking a jointly optimal source/channel coding solution, is asymptotically optimal.

$$
\text{Rate of a channel coder} = k/n
$$

where a channel coder operates by accepting a block of k input symbols and producing at its output a block of n symbols, with n > k.

- **Modulator**: converts symbol sequences from the channel encoders into signals appropriate for transmission over the channel.
- **Channel**: medium over which information is conveyed (described by noise models)

Channels have different information-carrying capabilities. 

Associated with each channel is a quantity known as the capacity, C, which indicates how much information it can carry reliably.

According to Shannon’s channel coding theorem, provided that the rate R of transmission is less than the capacity C, there exists a code such that the probability of error can be made arbitrarily small.

- **Demodulator**: converts received signal into a sequence of symbols
- **Channel decoder**: demodulation, equalization, and decoding may be combined
- **Decrypter**: removes encryption
- **Source decoder**: provides uncompressed representation of the data
- **Sink**: ultimate destination of the data

## Binary Phase Shift Keying

$$
\hat{b}_i = 2b_i - 1\\
a_i = \sqrt{E_b}\hat{b}_i
$$

Now to transmit each bit, energy expended is 

$$
\int^\infty_{-\infty} (a_i \phi(t))^2 dt = E_b
$$

The overall signal is represented by the following.

$$
s(t) = \sum_i a_i \phi_i(t - iT)
$$

## General Digital Modulation

8-PSK signal constellation can be obtained from the following.

$$
s_k(t) = a_{1k}\phi_1(t) + a_{2k}\phi_2(t)
$$

Signal energy, in that case, is as follows.

$$
E_k = \int^{\infty}_{-\infty}(s_k(t))^2 dt = a^2_{1k} + a^2_{2k}
$$

Average signal energy is given by

$$
E_s = \frac{1}{M}\sum_{k = 0}^{M - 1} E_k
$$

with the required average energy per bit stated as follows.

$$
E_b = \frac{\text{energy per signal}}{\text{number of bits or signals}} = \frac{E_s}{m}
$$

Transmitted signal is $s(t) = \sum a_{1i}\phi_1(t - iT) + a_{2i}\phi_2(t - iT)$.