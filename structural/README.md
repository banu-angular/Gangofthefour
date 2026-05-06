# 🧩 Structural Design Patterns

> A complete guide to **Structural Patterns** from the Gang of Four (GoF)

Structural design patterns focus on:

* ✅ Object composition
* ✅ Reducing tight coupling
* ✅ Improving flexibility
* ✅ Organizing relationships between classes

---

# 📚 What are Structural Patterns?

Structural patterns deal with:

> 👉 **How objects and classes are connected to form larger systems**

Instead of rewriting code, they help you:

* Combine objects efficiently
* Hide complexity
* Make systems scalable
* Improve maintainability

---

# 🧩 Types of Structural Patterns

| Pattern      | Purpose                               |
| ------------ | ------------------------------------- |
| 🔌 Adapter   | Convert incompatible interfaces       |
| 🌉 Bridge    | Separate abstraction & implementation |
| 🌳 Composite | Treat part & whole uniformly          |
| 🎭 Decorator | Add behavior dynamically              |
| 🧱 Facade    | Simplify complex systems              |
| 🛡️ Proxy    | Control access                        |
| 🔗 Flyweight | Optimize memory usage                 |

---

# 1️⃣ Adapter Pattern

## 📖 Definition

Converts one interface into another that the client expects.

## 📖 Hint

Makes incompatible interfaces work together.

## 💡 Idea

Wrap an existing class and translate its interface.

## 🧠 Think

🔌 Power adapter → fits different plugs.

---

## ❌ Bad Approach

```ts
const oldApi = new OldBankApi();
oldApi.transferFunds(10000, 'USD'); // Different interface ❌
```

---

## ✅ Good Approach

```ts
interface PaymentProcessor {
  makePayment(amount: number): string;
}

class OldBankApi {
  transferFunds(valueInCents: number, currency: string): string {
    return `Transferred ${valueInCents} ${currency}`;
  }
}

class PaymentAdapter implements PaymentProcessor {
  constructor(private oldApi: OldBankApi) {}

  makePayment(amount: number): string {
    return this.oldApi.transferFunds(amount * 100, 'USD');
  }
}
```

---

## 🎯 Use Cases

* Third-party integrations
* Legacy systems
* API transformations

---

## 🎯 Benefits

* Reuse existing code
* Avoid breaking changes
* Clean integration

---

# 2️⃣ Bridge Pattern

## 📖 Definition

Separates abstraction from implementation so both can vary independently.

## 📖 Hint

Avoids class explosion.

## 💡 Idea

Split class into abstraction + implementation layers.

## 🧠 Think

🌉 Bridge connects two sides independently.

---

## ❌ Problem

```ts
class WindowsButton {}
class MacButton {}
class LinuxButton {}
// Too many combinations ❌
```

---

## ✅ Good Example

```ts
interface Renderer {
  render(): string;
}

class HtmlRenderer implements Renderer {
  render() {
    return '<button>Click</button>';
  }
}

class Component {
  constructor(protected renderer: Renderer) {}

  display() {
    return this.renderer.render();
  }
}
```

---

## 🎯 Benefits

* Independent scalability
* Cleaner architecture
* Avoids duplication

---

# 3️⃣ Composite Pattern

## 📖 Definition

Allows treating individual objects and groups uniformly.

## 📖 Hint

Tree structure.

## 💡 Idea

Compose objects into tree-like structures.

## 🧠 Think

🌳 File system (files + folders)

---

## ✅ Example

```ts
interface Node {
  show(): void;
}

class File implements Node {
  constructor(private name: string) {}
  show() { console.log(this.name); }
}

class Folder implements Node {
  private children: Node[] = [];

  add(node: Node) {
    this.children.push(node);
  }

  show() {
    this.children.forEach(child => child.show());
  }
}
```

---

## 🎯 Benefits

* Uniform handling
* Recursive structures
* Clean hierarchy

---

# 4️⃣ Decorator Pattern

## 📖 Definition

Adds behavior dynamically without modifying the original object.

## 📖 Hint

Wrap and extend functionality.

## 💡 Idea

Layer features on top of objects.

## 🧠 Think

🎭 Add toppings to coffee.

---

## ❌ Problem

```ts
class CoffeeWithMilkAndSugar {} // Explosion ❌
```

---

## ✅ Good Example

```ts
interface Coffee {
  cost(): number;
}

class BasicCoffee implements Coffee {
  cost() { return 5; }
}

class MilkDecorator implements Coffee {
  constructor(private coffee: Coffee) {}

  cost() {
    return this.coffee.cost() + 2;
  }
}
```

---

## 🎯 Benefits

* Flexible extensions
* No class explosion
* Open/Closed Principle

---

# 5️⃣ Facade Pattern

## 📖 Definition

Provides a simplified interface to a complex system.

## 📖 Hint

Hide complexity.

## 💡 Idea

Expose one simple entry point.

## 🧠 Think

🧱 One switch controls many systems.

---

## ✅ Example

```ts
class UserService {
  getUser() { return 'User'; }
}

class OrderService {
  getOrders() { return 'Orders'; }
}

class DashboardFacade {
  constructor(
    private user: UserService,
    private orders: OrderService
  ) {}

  load() {
    return {
      user: this.user.getUser(),
      orders: this.orders.getOrders()
    };
  }
}
```

---

## 🎯 Benefits

* Simplifies usage
* Reduces dependencies
* Cleaner APIs

---

# 6️⃣ Proxy Pattern

## 📖 Definition

Controls access to an object.

## 📖 Hint

Acts as a gatekeeper.

## 💡 Idea

Add control logic before accessing object.

## 🧠 Think

🛡️ Security guard.

---

## ✅ Example

```ts
class ApiService {
  fetch() { return 'Server Data'; }
}

class ApiProxy {
  private cache: string | null = null;

  constructor(private api: ApiService) {}

  fetch() {
    if (!this.cache) {
      this.cache = this.api.fetch();
    }
    return this.cache;
  }
}
```

---

## 🎯 Benefits

* Access control
* Caching
* Lazy loading

---

# 7️⃣ Flyweight Pattern

## 📖 Definition

Reduces memory usage by sharing common data.

## 📖 Hint

Reuse instead of duplicate.

## 💡 Idea

Store shared objects instead of creating new ones.

## 🧠 Think

🔗 Reuse same letter in a text editor.

---

## ✅ Example

```ts
class Icon {
  constructor(public name: string) {}
}

class IconFactory {
  private cache: Record<string, Icon> = {};

  get(name: string): Icon {
    if (!this.cache[name]) {
      this.cache[name] = new Icon(name);
    }
    return this.cache[name];
  }
}
```

---

## 🎯 Benefits

* Memory optimization
* Performance improvement
* Efficient reuse

---

# 🧠 Quick Comparison

| Pattern   | Best Use Case          |
| --------- | ---------------------- |
| Adapter   | Interface mismatch     |
| Bridge    | Abstraction separation |
| Composite | Tree structures        |
| Decorator | Dynamic features       |
| Facade    | Simplification         |
| Proxy     | Access control         |
| Flyweight | Memory optimization    |

---

# 🚀 Real-World Usage (Angular / Enterprise)

| Pattern   | Example                     |
| --------- | --------------------------- |
| Adapter   | API response transformation |
| Bridge    | Component abstraction       |
| Composite | Nested components           |
| Decorator | HTTP Interceptors           |
| Facade    | Service layer               |
| Proxy     | Route Guards / caching      |
| Flyweight | Shared services/config      |

---

# 📌 Why Use Structural Patterns?

Without patterns:

* ❌ Tight coupling
* ❌ Complex dependencies
* ❌ Hard to scale

With patterns:

* ✅ Flexible systems
* ✅ Clean architecture
* ✅ Maintainable code
* ✅ Scalable design

---

# ⭐ Final Thoughts

Structural patterns = **How objects are connected**

Master this →
👉 Cleaner architecture
👉 Better system design
👉 Scalable applications
👉 Professional-level code

---

# 👨‍💻 Happy Coding

Master SOLID + Design Patterns = 🚀 Next-Level Developer
