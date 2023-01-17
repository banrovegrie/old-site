# JavaScript
---
Originally created to be a browser only language, JS is currently the most used, highly optimised browser language with uses in other environments as well.

> There are many languages that get “transpiled” to JavaScript and provide certain features. It is recommended to take a look at them, at least briefly, after mastering JavaScript.> 

[The Modern JavaScript Tutorial](https://javascript.info)

Use this to learn JavaScript, it is really well written.

# Introduction
---
- **What can the in-browser JS do?**
    - Add new HTML (modify content and styling)
    - React to actions
    - Send requests over the network to download and upload files
    - Get and Set cookies
    - Client-side local data storage
- **Good doc for reference**
    
    [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)

# Fundamentals
---
![Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled.png](Programming%20and%20Systems/images/Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled.png)

To make the code run in the modern way, use `"use strict";`, at the beginnning.

Modern JavaScript supports “classes” and “modules” – advanced language structures (we’ll surely get to them), that enable use strict automatically. So we don’t need to add the "use strict" directive, if we use them.

## Basics

```jsx
/* -- let --*/
let user = 'John', age = 25, message = 'Hello';

/* -- const --*/
const COLOR_RED = "#F00";
const COLOR_GREEN = "#0F0";
const COLOR_BLUE = "#00F";
const COLOR_ORANGE = "#FF7F00";

// ...when we need to pick a color
let color = COLOR_ORANGE;
alert(color); // #FF7F00
```

```jsx
alert(Infinity); // Infinity

// null
let age = null;
age = 100;

// change the value to undefined
age = undefined;
alert(age); // "undefined"

// the "n" at the end means it's a BigInt
const bigInt = 1234567890123456789012345678901234567890n;
```

Double and single quotes are “simple” quotes. There’s practically no difference between them in JavaScript. Backticks are “extended functionality” quotes. They allow us to embed variables and expressions into a string by wrapping them in `${…}`, for example:

```jsx
let name = "John";

// embed
alert(`Hello, ${name}!`); 
// Hello, John!
alert(`the result is ${1 + 2}`); 
// the result is 3
```

![Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%201.png](Programming%20and%20Systems/images/Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%201.png)

## Interactions

- `alert(message);`
- `prompt(message, default);`
- `confirm(boolean_question);`
 
![Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%202.png](Programming%20and%20Systems/images/Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%202.png)

## Type Conversions

- String: `String()`
- Numeric: `Number()`
- Boolean: `Boolean()`

![Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%203.png](Programming%20and%20Systems/images/Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%203.png)

## Things similar to `C++`

- Logical Operators
- Conditionals (`if` statements)
- Loops: `while`, `for`, and `do while`
- Jump statements: `break` and `continue`
- Switch-case staements

## Nullish coalescing operator `??`

The operation `a ?? b` results in `a` if a is defined and `b` is a is not defined.

![Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%204.png](Programming%20and%20Systems/images/Notes%20on%20JavaScript%20ee2f8b018bb743ed8ab2fd9d3ac29c10/Untitled%204.png)

- The operator `??` has a very low precedence, only a bit higher than $?$ and $=$ so consider adding parentheses when using it in an expression.
- It’s forbidden to use it with `||` or `&&` without explicit parentheses.

## Label based breaking

```jsx
outer: for (let i = 0; i < 3; i++) {

  for (let j = 0; j < 3; j++) {

    let input = prompt(`Value at coords (${i},${j})`, '');

    // if an empty string or canceled, 
		// then break out of both loops
    if (!input) break outer; // (*)

    // do something with the value...
  }
}
alert('Done!');
```

We can also move the label to a different line:

```jsx
outer:
for (let i = 0; i < 3; i++) { ... }
```

However, this doesn't allow you the freedom to jump anywhere from anywhere unlike `goto` command in C.

# Functions
---
A function declaration looks like this:

```jsx
function name(parameters, delimited, by, comma) {
  /* code */
	return 100; // optional ofcourse
}
```

- Values passed to a function as parameters are copied to its local variables.
- A function may access outer variables. But it works only from inside out. The code outside of the function doesn’t see its local variables.
- A function can `return` a value. If it doesn’t, then its result is `undefined`.

```jsx
// Function Declaration
function sum(a, b) {
  return a + b;
}
```

```jsx
// Function Expression
let sum = function(a, b) {
  return a + b;
};
```

## Callback functions

```jsx
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}

function showOk() {
  alert( "You agreed." );
}

function showCancel() {
  alert( "You canceled the execution." );
}

// usage: functions showOk, showCancel are passed 
// as arguments to ask
ask("Do you agree?", showOk, showCancel);
```

- If the function is declared as a separate statement in the main code flow, that’s called a “Function Declaration”.
- If the function is created as a part of an expression, it’s called a “Function Expression”.
- Function Declarations are processed before the code block is executed. They are visible everywhere in the block.
- Function Expressions are created when the execution flow reaches them.
- Functions are values. They can be assigned, copied or declared in any place of the code.

## Arrow functions

The jorney from functions to arrow functions:

```jsx
1. var anon = function add(a, b) { return a + b };
2. var anon = (a, b) => a + b;
3. var anon = (a, b) => { return a + b };
4. var anon = a => a; // if we have only one parameter
5. var () => {} // noop

// this looks pretty nice when you change something like:
[1,2,3,4].filter(function (value) {return value % 2 === 0});
// to:
[1,2,3,4].filter(value => value % 2 === 0);
```

## JavaScript Specials

```jsx
let userName = prompt("Your name?", 2);
alert( "Visitor: " + userName );
```

```jsx
// expression at the right side
1. let sum = (a, b) => a + b;

// or multi-line syntax with { ... }, need return here:
2. let sum = (a, b) => {
		  // ...
		  return a + b;
		}

// without arguments
3. let sayHi = () => alert("Hello");

// with a single argument
4. let double = n => n * 2;
```

- Parameters can have default values: `function sum(a = 1, b = 2) {...}`.
- Functions always return something. If there’s no `return` statement, then the result is `undefined`.

# Objects
---
Objects are associative arrays with several special features.

They store properties (key-value pairs), where:

- Property keys must be strings or symbols (usually strings).
- Values can be of any type.

To access a property, we can use:

- The dot notation: `obj.property`.
- Square brackets notation `obj["property"]`. Square brackets allow to take the key from a variable, like `obj[varWithKey]`.

Additional operators:

- To delete a property: `delete obj.prop`.
- To check if a property with the given key exists: `"key" in obj`.
- To iterate over an object: `for (let key in obj)` loop.

What we’ve studied in this chapter is called a “plain object”, or just `Object`.

There are many other kinds of objects in JavaScript:

- `Array` to store ordered data collections,
- `Date` to store the information about the date and time,
- `Error` to store the information about an error.
- …and so on.

## Copying an Object

Well, objects are copied as reference.

`Object.assign ()` servers to produce a clone of one or several objects combined.

## Object methods

```jsx
**// Method 1**
let user = {
  name: "John",
  age: 30
};

user.sayHi = function() {
  alert("Hello!");
};

**// Method 2**
let user = {
  name: "John",
  age: 30
};

function sayHi() {
  alert("Hello!");
};

user.sayHi = sayHi;

**// Method 3**
user = {
  sayHi: function() {
    alert("Hello");
  }
};

**// Method 4**
user = {
  sayHi() {
    alert("Hello");
  }
};
```

## Keyword: `this`

- Methods can reference the object as `this`.
- Arrow functions don't have `this` and when `this` is accessed in an arrow function, it is taken from outside.
- When a function is declared, it may use `this`, but that `this` has no value until the function is called.

## Constructor and `new`

```jsx
function User(name) 
{
	  this.name = name;

	  this.sayHi = function() {
	    alert( "My name is: " + this.name );
		};
}

let john = new User("John");
```

## Optional Chaining using `?.`

The optional chaining `?.` syntax has three forms:

1. `obj?.prop` – returns `obj.prop` if `obj` exists, otherwise `undefined`.
2. `obj?.[prop]` – returns `obj[prop]` if `obj` exists, otherwise `undefined`.
3. `obj.method?.()` – calls `obj.method()` if `obj.method` exists, otherwise returns `undefined`.

## Conversions

`obj.toString()` can be used to convert an object to a string.