---
title: "Bitcoin Script"
date: 2021-07-18T06:48:10+05:30
tags: ["Bitcoin", "dev"]
categories: ["Summer of Bitcoin"]
---

# Bitcoin Script 

<!-- <p style="text-align:right;"> By <em> Aman Rojjha </em> -->

## Philosophy

- *Stack-based*.
- Non-Turing completeness: Mitigates malicious scripts on the network.

> Generically, the expression that must be satisfied in Bitcoin in order to spend a coin is known as an "encumbrance". 

### Condition for validity

- No failure in executing scripts.
- Top element of stack is true.

## The Execution Stack

- Holds *byte vectors* in little-endian format. 
- Max size: 520 bytes.
- Opcodes taking integers and returning bool: Max size 4 bytes.
- Addition/ Subtraction overflows and results in 5 byte integer in stack. (How is it handled?)


    ### Flow control 

    - `OP_IF/OP_NOTIF`: If the top stack value is not False, the statements are executed. The top stack value is removed. 
    - `OP_VERIFY`: Marks transaction as invalid if top stack value is not true. The top stack value is removed. 
    - `OP_RETURN`: Since 0.12, standard relay rules allow a single output with OP_RETURN, that contains any sequence of push statements (or OP_RESERVED) after the OP_RETURN provided the total scriptPubKey length is at most 83 bytes. [🔗](https://bitcoin.org/en/release/v0.12.0?__cf_chl_jschl_tk__=add0ddcad785b83e0f504212e5ffc59c4096cbec-1626569012-0-Ad8Z-ZkdzSDDFfvzy9vWdEOdpHX9FjUJNpafVrKqvzuxyUdmV-0VFq8HYTGWZ6MNXHnEH7OB3N-NDqizGLINlTB1embMx9NpicH_xBA1Pxzfe1iQsbICOPGTapRnVgkyb2IjpKsyY3S8xN1WZ-T-OdAH8SRtos7bvLGm4z29tYs5GExZwDlh__Mjk6F_p59pYXdZnw3o6Qc_H_V4QfZ_-e1B_md0oOIELujVxNq5210orWxbOLOQ-RtnpC_A2_3qec1dHVVcmiBJxNIc1_l13MWZVsSRo9pnnaYRLJ3UNltFFTBMvZCgehSEv8WSi_TGftFJ7BWNBc-KFhaChGQpF33tDG895Q0780Dn34oE5Dcdfhft41cdZ3ZjlQZcLuy2Gm64AeI-IIhCal6UfLQJUkbLGGYLoErazH9YyEYsKUnc#relay-any-sequence-of-pushdatas-in-opreturn-outputs-now-allowed)

    ### Stack

    > **What is [Alt Stack](https://bitcoin.stackexchange.com/questions/32133/what-is-the-alt-stack)?**

    Supports generic stack operations with interesting ones like `OP_ROLL` and `OP_PICK` and some (really) redundant ones.
    *Possible Reason**: Efficiency while executing script.

    <!-- READ [🔗](http://www.csc.lsu.edu/~fchen/publications/papers/icdcs20-bitcoin.pdf) -->

    ### Arithmetic

    - Signed 32-bit integers, might overflow. Failure if `> 4 bytes`.
    Our script has all the basic arithmetic operations available.

- `OP_CHECKLOCKTIMEVERIFY` and `OP_CHECKSEQUENCEVERIFY` -> powerful tools for enabling smart contracts.

## Example scripts

1. TODO 

## Bibliography

1. [Alt Script Wiki](https://wiki.bitcoinsv.io/index.php/Script)
