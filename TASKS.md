# The Ultimate LLD Learning Plan: An Iterative Guide

This plan is structured to build your skills incrementally. Each task introduces a core concept and immediately applies it to a small, practical project.

---

### **Part 1: The Foundation - SOLID Principles** 🏛️

These principles are the bedrock of good design. We'll tackle them in logical groups.

#### **Task 1: Single Responsibility & Open/Closed Principles**
* **Concept:** Learn why a class should have one job and how to add features without changing existing code.
* **Project:** A Discount Calculator.
* **Goal:** Build a simple class to apply discounts. Start with a hardcoded "percentage" discount. Then, refactor your code so that adding a new discount type (e.g., `BuyOneGetOneFree`) means adding a *new class*, not changing old ones.
* **Acceptance Criteria:**
    * ✅ A `Discount` interface or abstract class is created.
    * ✅ Each discount type (`PercentageDiscount`, `FixedDiscount`) is its own class implementing the interface.
    * ✅ The main calculator class can use any new discount type without modification.
* **Resources:**
    * **Article:** The Open-Closed Principle by Uncle Bob - [http://www.butunclebob.com/ArticleS.UncleBob.TheOpenClosedPrinciple](http://www.butunclebob.com/ArticleS.UncleBob.TheOpenClosedPrinciple)
    * **Video:** SOLID Principles Explained - [https://www.youtube.com/watch?v=rtmFCcjEgEw](https://www.youtube.com/watch?v=rtmFCcjEgEw)

#### **Task 2: Liskov Substitution & Interface Segregation Principles**
* **Concept:** Understand how to create reliable abstractions and avoid "fat" interfaces.
* **Project:** A Worker Management System.
* **Goal:** Create a `Worker` system. A `HumanWorker` can `work()` and `takeBreak()`. A `RobotWorker` can `work()` but can't `takeBreak()`. A `Manager` doesn't `work()` but can `manage()`. Refactor the system using smaller, specific interfaces (e.g., `IWorkable`, `IManageable`) to avoid forcing classes to implement methods they don't need.
* **Acceptance Criteria:**
    * ✅ No class is forced to implement a method it doesn't need.
    * ✅ The system is broken down into smaller role-based interfaces.
    * ✅ Your code demonstrates that a function expecting an `IWorkable` can seamlessly accept any class that implements it.
* **Resources:**
    * **Article:** Interface Segregation Principle - [https://www.baeldung.com/solid-principles#4-interface-segregation](https://www.baeldung.com/solid-principles#4-interface-segregation)

---

### **Part 2: Foundational Patterns in Action** 🚀

#### **Task 3: The Factory Method Pattern**
* **Concept:** Delegating object creation to subclasses.
* **Project:** A Cross-Platform UI Creator.
* **Goal:** Create a base `Dialog` class with a `createButton()` factory method. Create `WindowsDialog` and `MacDialog` subclasses that override this method to return a `WindowsButton` and `MacButton`, respectively.
* **Acceptance Criteria:**
    * ✅ The main application code has no idea which specific type of button it's getting.
    * ✅ To support a new OS, you only need to add new creator and product classes.
* **Resources:**
    * **Article:** Factory Method by Refactoring Guru - [https://refactoring.guru/design-patterns/factory-method](https://refactoring.guru/design-patterns/factory-method)

#### **Task 4: The Strategy Pattern**
* **Concept:** Switching out algorithms or behaviors at runtime.
* **Project:** A Map Navigator.
* **Goal:** Build a `Navigator` context class that can switch between `DrivingStrategy`, `WalkingStrategy`, etc., without a bunch of `if/else` statements.
* **Acceptance Criteria:**
    * ✅ The main `Navigator` class is completely decoupled from the specific routing algorithms.
    * ✅ You can add a new `PublicTransportStrategy` without modifying the `Navigator`.
* **Resources:**
    * **Video:** Strategy Pattern by Christopher Okhravi - [https://www.youtube.com/watch?v=v9ejT8FO-7I](https://www.youtube.com/watch?v=v9ejT8FO-7I)

#### **Task 5: The Observer Pattern**
* **Concept:** Creating a subscription mechanism to notify multiple objects of any events.
* **Project:** A YouTube Channel Notifier.
* **Goal:** When the `YouTubeChannel` (subject) uploads a new video, all subscribed `Subscriber` objects (observers) should be notified automatically.
* **Acceptance Criteria:**
    * ✅ The `YouTubeChannel` has methods to `subscribe()` and `unsubscribe()` observers.
    * ✅ The `YouTubeChannel` does not know about the concrete `Subscriber` classes, only an `Observer` interface.
* **Resources:**
    * **Article:** Observer Pattern by Refactoring Guru - [https://refactoring.guru/design-patterns/observer](https://refactoring.guru/design-patterns/observer)

---

### **Part 3: Milestone Project #1** 🏆

#### **Task 6: Design a Parking Lot**
* **Goal:** Design a parking lot system that can handle different vehicle types, parking spots, and pricing.
* **How to use your knowledge:**
    * **Factory Method:** To create different types of `ParkingSpot` objects.
    * **Strategy:** For different pricing models (`HourlyPricing`, `DailyPricing`).
    * **Singleton:** The `ParkingLot` itself could be a Singleton.
* **Acceptance Criteria:**
    * ✅ You must produce a simple Class Diagram for your design.
    * ✅ The implementation correctly uses at least two of the patterns mentioned.
    * ✅ Your design document (`README.md`) clearly explains your choices.

---

### **Part 4: Patterns for Structure & Flexibility** 🧩

#### **Task 7: The Decorator Pattern**
* **Concept:** Adding new functionalities to an object dynamically.
* **Project:** A Coffee Shop Order System.
* **Goal:** Start with a base `Beverage` (like an Espresso). Create decorator classes for condiments (`Milk`, `Mocha`) so you can "wrap" a beverage with them. The final price should be calculated correctly.
* **Acceptance Criteria:**
    * ✅ You can create a complex order like `new Mocha(new Milk(new Espresso()))`.
    * ✅ The cost calculation correctly sums the base beverage and all decorators.
* **Resources:**
    * **Video:** Decorator Pattern Explained - [https://www.youtube.com/watch?v=GCraGHx6gso](https://www.youtube.com/watch?v=GCraGHx6gso)

#### **Task 8: The Adapter Pattern**
* **Concept:** Making two incompatible interfaces work together.
* **Project:** A Data Analytics Tool.
* **Goal:** Your application uses a `JsonAnalytics` interface. You acquire a new library that only works with `XML`. Create an `XmlAdapter` that implements your interface but internally translates calls to work with the new library.
* **Acceptance Criteria:**
    * ✅ Your main application code doesn't change and continues to use the `JsonAnalytics` interface.
    * ✅ The adapter successfully makes the incompatible library usable in your system.
* **Resources:**
    * **Article:** Adapter Pattern by Refactoring Guru - [https://refactoring.guru/design-patterns/adapter](https://refactoring.guru/design-patterns/adapter)

#### **Task 9: The State Pattern**
* **Concept:** Letting an object change its behavior when its internal state changes.
* **Project:** A Vending Machine.
* **Goal:** Implement a vending machine where each state (`NoCoinState`, `HasCoinState`, `SoldOutState`) is its own class. The machine's main class will delegate actions to its current state object.
* **Acceptance Criteria:**
    * ✅ The main `VendingMachine` class has no large `if/else` or `switch` statements for checking states.
    * ✅ Adding a new state is self-contained and easy.
* **Resources:**
    * **Video:** State Design Pattern Explained - [https://www.youtube.com/watch?v=N12L5D78MAA](https://www.youtube.com/watch?v=N12L5D78MAA)

---

### **Part 5: Capstone Project** 🏅

#### **Task 10: Design a Movie Ticket Booking System**
* **Goal:** Design the core logic for a system like BookMyShow. It must handle cities, cinemas, shows, and seat booking.
* **Key Challenge:** Concurrency. How do you prevent two users from booking the exact same seat at the same time?
* **Potential Patterns to Use:**
    * **Observer:** To notify users if a seat they wanted becomes available.
    * **Facade:** To simplify the booking process into a single method.
    * **Factory/Builder:** For creating complex `Show` or `Booking` objects.
    * **Concurrency Patterns:** Use locking mechanisms (like Mutex or Semaphore).
* **Acceptance Criteria:**
    * ✅ A clear class diagram and explanation of object relationships.
    * ✅ The design explicitly describes how it handles the concurrent booking problem.
    * ✅ The code implements the core booking flow, demonstrating the use of at least two design patterns.