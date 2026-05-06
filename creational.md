# 🏗️ Creational Design Patterns

> A complete guide to **Creational Patterns** from the Gang of Four (GoF)

Creational design patterns focus on:

- ✅ Object creation mechanisms  
- ✅ Reducing tight coupling  
- ✅ Improving flexibility & reuse  
- ✅ Making code scalable and testable  

---

# 📚 What are Creational Patterns?

Creational patterns deal with **how objects are created**.

Instead of using direct instantiation (`new`), they provide:

- Controlled object creation
- Better abstraction
- Flexible architecture

---

# 🧩 Types of Creational Patterns

| Pattern | Purpose |
|---|---|
| 🧍 Singleton | Only one instance |
| 🏭 Factory Method | Create objects without exposing logic |
| 🏢 Abstract Factory | Create families of related objects |
| 🍔 Builder | Build complex objects step by step |
| 📄 Prototype | Clone existing objects |

---

# 1️⃣ Singleton Pattern

## 📖 Definition

Ensures a class has **only one instance** and provides a global access point.

## 📖 Hint
Ensures a class has **only one instance**.

## 💡 Idea
Control object creation so only one instance exists.

## 🧠 Think
🧍 One CEO for a company — not multiple CEOs.

---

## ✅ Example

```ts
class Logger {
  private static instance: Logger;

  private constructor() {}

  static getInstance(): Logger {
    if (!Logger.instance) {
      Logger.instance = new Logger();
    }
    return Logger.instance;
  }

  log(message: string) {
    console.log(message);
  }
}

const logger1 = Logger.getInstance();
const logger2 = Logger.getInstance();

console.log(logger1 === logger2); // true
```


---

## 🎯 Use Cases

- Logging
- Configuration
- Database connection

---

## 🎯 Benefits

- Controlled instance creation  
- Global access  
- Memory efficiency  

---

# 2️⃣ Factory Method Pattern

## 📖 Definition

Defines an interface for creating objects but lets subclasses decide which class to instantiate.

## 📖 Hint
Creates objects without exposing creation logic.

## 💡 Idea
Delegate object creation to a factory instead of using `new`.

## 🧠 Think
🏭 Factory machine → you request product, it creates it.

---

## 💡 When to Use

- Dynamic object creation  
- Plugin systems  
- UI components  

---

## ✅ Example

```ts
interface Animal {
  speak(): void;
}

class Dog implements Animal {
  speak() {
    console.log('Bark');
  }
}

class Cat implements Animal {
  speak() {
    console.log('Meow');
  }
}

class AnimalFactory {
  static create(type: string): Animal {
    if (type === 'dog') return new Dog();
    return new Cat();
  }
}

const animal = AnimalFactory.create('dog');
animal.speak();
```

---

## 🎯 Benefits

- Loose coupling  
- Centralized object creation  
- Easy extension  

---

# 3️⃣ Abstract Factory Pattern

## 📖 Definition

Provides an interface for creating **families of related objects** without specifying their concrete classes.

## 📖 Hint
Creates families of related objects.

## 💡 Idea
Group related objects and create them together.

## 🧠 Think
📱 Android vs iPhone ecosystem  
Each has its own buttons, UI, and style.
---

## 💡 When to Use

- UI frameworks  
- Cross-platform applications  
- Theming systems  

---

## ✅ Example

```ts
interface Button {
  render(): void;
}

class WindowsButton implements Button {
  render() {
    console.log('Windows Button');
  }
}

class MacButton implements Button {
  render() {
    console.log('Mac Button');
  }
}

interface UIFactory {
  createButton(): Button;
}

class WindowsFactory implements UIFactory {
  createButton(): Button {
    return new WindowsButton();
  }
}

class MacFactory implements UIFactory {
  createButton(): Button {
    return new MacButton();
  }
}

// Usage
const factory: UIFactory = new WindowsFactory();
const button = factory.createButton();
button.render();
```

---

## 🎯 Benefits

- Ensures consistency between related objects  
- Scalable architecture  
- Easy to switch product families  

---

# 4️⃣ Builder Pattern

## 📖 Definition

Separates the construction of a complex object from its representation.

## 📖 Hint
Builds complex objects step by step.

## 💡 Idea
Separate object construction from representation.

## 🧠 Think
🍔 Build your burger step-by-step  
(add cheese, sauce, veggies)


---

## 💡 When to Use

- Complex object creation  
- Optional parameters  
- Step-by-step configuration  

---

## ✅ Example

```ts
class User {
  constructor(
    public name: string,
    public age: number,
    public email?: string
  ) {}
}

class UserBuilder {
  private name = '';
  private age = 0;
  private email?: string;

  setName(name: string): UserBuilder {
    this.name = name;
    return this;
  }

  setAge(age: number): UserBuilder {
    this.age = age;
    return this;
  }

  setEmail(email: string): UserBuilder {
    this.email = email;
    return this;
  }

  build(): User {
    return new User(this.name, this.age, this.email);
  }
}

const user = new UserBuilder()
  .setName('Banu')
  .setAge(25)
  .setEmail('banu@example.com')
  .build();
```

---

## 🎯 Benefits

- Readable object creation  
- Handles optional fields cleanly  
- Reduces constructor complexity  

---

# 5️⃣ Prototype Pattern

## 📖 Definition

Creates new objects by **cloning existing ones** instead of creating from scratch.

## 📖 Hint
Creates new objects by cloning existing ones.

## 💡 Idea
Reuse existing object instead of creating from scratch.

## 🧠 Think
📄 Copy-paste a document instead of rewriting.


---

## 💡 When to Use

- Expensive object creation  
- Copying objects  
- Performance optimization  

---

## ✅ Example

```ts
class User {
  constructor(public name: string, public age: number) {}

  clone(): User {
    return new User(this.name, this.age);
  }
}

const user1 = new User('Banu', 25);
const user2 = user1.clone();

console.log(user1 !== user2); // true
```

---

## 🎯 Benefits

- Faster object creation  
- Avoids repeated initialization  
- Useful for deep copies  

---

# 🧠 Quick Comparison

| Pattern | Best Use Case |
|---|---|
| Singleton | One shared instance |
| Factory | Dynamic object creation |
| Abstract Factory | Related object families |
| Builder | Complex objects |
| Prototype | Cloning objects |

---

# 🚀 Real-World Usage (Angular / Enterprise)

| Pattern | Example |
|---|---|
| Singleton | Angular Services (`providedIn: 'root'`) |
| Factory | Dependency Injection |
| Builder | FormBuilder |
| Prototype | Object spread `{...obj}` |
| Abstract Factory | UI themes / component libraries |

---

# 📌 Why Use Creational Patterns?

Without patterns:

- ❌ Tight coupling  
- ❌ Hard to maintain  
- ❌ Difficult to test  

With patterns:

- ✅ Flexible architecture  
- ✅ Reusable code  
- ✅ Clean design  
- ✅ Scalable systems  

---

# ⭐ Final Thoughts

Creational patterns = **Control how objects are created**

Master this →  
👉 Better architecture  
👉 Cleaner code  
👉 Strong system design  
👉 Scalable systems  


---

# 👨‍💻 Happy Coding

Master SOLID + Design Patterns = 🚀 Next-Level Developer
