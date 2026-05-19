# 🔄 Behavioral Design Patterns (GoF)

> Patterns that define **how objects communicate and interact**

---

# 📌 Overview

Behavioral Design Patterns focus on:

- Communication between objects  
- Responsibility distribution  
- Dynamic behavior changes  

They help build:

- ✅ Decoupled systems  
- ✅ Flexible workflows  
- ✅ Clean communication  
- ✅ Scalable logic  

---

# 🧩 GoF Behavioral Patterns (11)

| Pattern | Purpose |
|---|---|
| 👀 Observer | Notify subscribers |
| 🎯 Strategy | Switch algorithms |
| 📦 Command | Encapsulate requests |
| 🔁 State | Change behavior dynamically |
| 🧑‍⚖️ Mediator | Central communication |
| 🔗 Chain of Responsibility | Pass request along chain |
| 🧾 Template Method | Define algorithm structure |
| 🧍 Iterator | Traverse collections |
| 🗂 Memento | Save & restore state |
| 🗣 Interpreter | Interpret language |
| 🧑‍💼 Visitor | Add operations without modifying |

---

# 1️⃣ Observer Pattern

## 📖 Definition  
One-to-many dependency → notify all observers.

## 💡 Idea  
When one object changes, others automatically update.

## 🧠 Think  
📺 YouTube → subscribers get notified on upload.

---

```ts
class Subject {
  private observers: Function[] = [];

  subscribe(fn: Function) {
    this.observers.push(fn);
  }

  notify(data: string) {
    this.observers.forEach(fn => fn(data));
  }
}
```

---

# 2️⃣ Strategy Pattern

## 📖 Definition  
Encapsulates interchangeable algorithms.

## 💡 Idea  
Switch behavior at runtime.

## 🧠 Think  
💳 Payment methods (UPI / Card / Cash)

---

```ts
interface PaymentStrategy {
  pay(amount: number): void;
}

class CardPayment implements PaymentStrategy {
  pay(amount: number) {
    console.log('Card:', amount);
  }
}

class UpiPayment implements PaymentStrategy {
  pay(amount: number) {
    console.log('UPI:', amount);
  }
}
```

---

# 3️⃣ Command Pattern

## 📖 Definition  
Encapsulates a request as an object.

## 💡 Idea  
Turn actions into objects.

## 🧠 Think  
📺 Remote control (button = command)

---

```ts
class Light {
  on() {
    console.log('Light ON');
  }
}

class LightCommand {
  constructor(private light: Light) {}

  execute() {
    this.light.on();
  }
}
```

---

# 4️⃣ State Pattern

## 📖 Definition  
Change object behavior based on state.

## 💡 Idea  
Object behaves differently depending on its state.

## 🧠 Think  
🚦 Traffic light (Red / Green / Yellow)

---

```ts
interface State {
  handle(): void;
}

class Green implements State {
  handle() {
    console.log('Go');
  }
}

class Red implements State {
  handle() {
    console.log('Stop');
  }
}
```

---

# 5️⃣ Mediator Pattern

## 📖 Definition  
Centralizes communication between objects.

## 💡 Idea  
Objects don’t talk directly → use mediator.

## 🧠 Think  
🧑‍⚖️ Judge in court → controls communication

---

```ts
class Mediator {
  send(msg: string) {
    console.log('Message:', msg);
  }
}
```

---

# 6️⃣ Chain of Responsibility

## 📖 Definition  
Pass request through a chain of handlers.

## 💡 Idea  
Each handler decides to handle or pass.

## 🧠 Think  
🧾 Customer support levels (L1 → L2 → L3)

---

```ts
class Handler {
  next?: Handler;

  setNext(handler: Handler) {
    this.next = handler;
  }

  handle(req: string) {
    if (this.next) this.next.handle(req);
  }
}
```

---

# 7️⃣ Template Method

## 📖 Definition  
Defines algorithm structure, subclasses override steps.

## 💡 Idea  
Base class controls flow.

## 🧠 Think  
🍳 Recipe → steps fixed, ingredients vary

---

```ts
abstract class Game {
  start() {
    this.init();
    this.play();
    this.end();
  }

  abstract init(): void;
  abstract play(): void;
  abstract end(): void;
}
```

---

# 8️⃣ Iterator Pattern

## 📖 Definition  
Sequential access without exposing structure.

## 💡 Idea  
Traverse collections safely.

## 🧠 Think  
📚 Reading a book page by page

---

```ts
class Iterator {
  private index = 0;

  constructor(private items: number[]) {}

  next() {
    return this.items[this.index++];
  }
}
```

---

# 9️⃣ Memento Pattern

## 📖 Definition  
Save and restore object state.

## 💡 Idea  
Capture state without exposing internals.

## 🧠 Think  
💾 Undo / Redo

---

```ts
class Memento {
  constructor(public state: string) {}
}

class Editor {
  private content = '';

  save() {
    return new Memento(this.content);
  }

  restore(m: Memento) {
    this.content = m.state;
  }
}
```

---

# 🔟 Interpreter Pattern

## 📖 Definition  
Interprets language grammar.

## 💡 Idea  
Parse and evaluate expressions.

## 🧠 Think  
🧮 Calculator evaluating expressions

---

```ts
class Expression {
  interpret() {
    return 1;
  }
}
```

---

# 1️⃣1️⃣ Visitor Pattern

## 📖 Definition  
Add operations without modifying objects.

## 💡 Idea  
Separate algorithm from object structure.

## 🧠 Think  
👨‍🔧 Technician inspecting different machines

---

```ts
interface Visitor {
  visit(): void;
}

class ConcreteVisitor implements Visitor {
  visit() {
    console.log('Visited');
  }
}
```

---

# 🧠 Quick Memory Trick

| Pattern | Image |
|---|---|
| Observer | 📺 Subscribe |
| Strategy | 💳 Choose method |
| Command | 🎮 Button |
| State | 🚦 Mode |
| Mediator | 🧑‍⚖️ Middleman |
| Chain | 🔗 Pipeline |
| Template | 🍳 Recipe |
| Iterator | 📚 Traverse |
| Memento | 💾 Save |
| Interpreter | 🧮 Evaluate |
| Visitor | 👨‍🔧 Inspect |

---

# 🚀 Real-World Usage

| Pattern | Example |
|---|---|
| Observer | RxJS, Events |
| Strategy | Payment systems |
| Command | Undo/Redo |
| State | UI states |
| Mediator | Chat apps |
| Chain | Middleware |
| Template | Framework lifecycle |
| Iterator | Arrays |
| Memento | Undo systems |
| Interpreter | Query engines |
| Visitor | Compilers |

---

# ⭐ Final Thought

Behavioral patterns =  
👉 How objects **talk, react, and behave**

Master this →  
💡 Better system design  
💡 Cleaner logic  
💡 Scalable applications  

---

# 👨‍💻 Happy Coding

Design smart. Build powerful systems 🚀
