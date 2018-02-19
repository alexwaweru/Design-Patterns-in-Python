# Design Patterns in Python #
Design patterns represent the best practices used by experienced 
object-oriented software developers. Design patterns are solutions
to general problems that software developers faced during software
development.

You can think of a pattern as an especially clever and 
insightful way of solving a particular class of problems. That is,
 it looks like a lot of people have worked out all the angles of a 
 problem and have come up with the most general, flexible solution 
 for it. The problem could be one you have seen and solved before, 
 but your solution probably didn’t have the kind of completeness 
 you’ll see embodied in a pattern.

Often, the most difficult part of developing an elegant and 
cheap-to-maintain design is in discovering what I call 
“the vector of change.” (Here, “vector” refers to the 
maximum gradient and not a container class.) This means 
finding the most important thing that changes in your system, 
or put another way, discovering where your greatest cost is. 
Once you discover the vector of change, you have the focal 
point around which to structure your design. So the goal of design
 patterns is to isolate changes in your code.
 
**I have researched and tried to implement the following design patterns:** 

## 1. Singleton Pattern (Creational)
##### Description
Singleton pattern provides a mechanism to limit the number of the 
instances of the class to one. Thus the same object is always shared 
by different parts of the code. Singleton can be seen as a more elegant 
solution to global variable because actual data is hidden behind 
Singleton class interface.

The singleton pattern solves the following problems:
1. How can it be ennsured that a class has only one instance?
2. How can the sole instance of a class be accessed easily?
2. How can a class control its instantiation? 
3. How can the number of instances of a class be restricted?

##### Implementation
Make sure the class can never be instantiated from outside. But since
python does not have a private constructor we have to find another way 
to prevent instantiations. 

##### Implementating the lazy instantiation
Lazy Initialization postpones the instantiation 
of a object until its first use. In other words the instance of a class 
is created when its required to be used for the first time.  

When we say s=Singleton(), it calls the __init__ method but no new 
object gets created. However, actual object creation happens when 
we call Singleton.getInstance(). This is how lazy instantiation is 
achieved.

## 2. Template method Pattern (Structural)
##### Description
The template method pattern is a behavioral design pattern that defines 
the program skeleton of an algorithm in an operation, deferring some 
steps to subclasses.

##### Implementation
Implement a Game abstract class defining operations with a 
template method set to be final so that it cannot be overridden. Rugby 
and Football are concrete classes that extend Game and override its methods.
TemplatePatternDemo, our demo class, will use Game to demonstrate use of 
template pattern.

## 3. Proxy Pattern (structural)
##### Description
Proxy pattern provides a surrogate class that you use in your code. The real 
class that does the work is hidden behind this surrogate class. Proxy is used
for fronting an implementation. This is important when the access to an object
should be controlled or additional functionality should be provided when 
accessing an object.

##### Implementation
Used the __getattr__( ) to delegate from the proxy class to the implementation.

## 4. State Pattern (Behavioural)
The State pattern adds more implementations to Proxy, along with a way to switch
 from one implementation to another during the lifetime of the surrogate. Unlike
 proxy, state has more than one implementation and allows you to change 
 implementation dynamically. This pattern is used in computer programming to 
 encapsulate varying behavior for the same object based on its internal state.
 
##### Implementation
1. Define separate (state) objects that encapsulate state-specific behavior for 
    each state. That is, define an interface (State) for performing state-specific
     behavior, and define classes that implement the interface for each state.
2. A class delegates state-specific behavior to its current state object instead
     of implementing state-specific behavior directly.
     
## 5. Decorator pattern (Structural)
##### Description
The use of layered objects to dynamically and transparently add responsibilities 
to individual objects without affecting the behaviour of other objects from the 
same class.

Problems the decorator design solves:
1. Responsibilities should be added to an object dynamically at runtime.
2. A flexible alternative to subclassing for extending functionality should be 
provided.

What solution does the decorator pattern describe:
1. Implement the interface of the extended(decorated) object (component) 
transparently by forwarding all requests to it and
2. perform additional functionality before/after forwarding a request.

##### Implementation
Consider going down to the local coffee shop for a coffee. There are 
typically many different drinks on offer – espressos, lattes, teas, iced coffees, 
hot chocolate to name a few, as well as a number of extras (which cost extra too)
such as whipped cream or an extra shot of espresso. You can also make certain 
changes to your drink at no extra cost, such as asking for decaf coffee instead 
of regular coffee.

Quite clearly if we are going to model all these drinks and combinations, there 
will be sizeable class diagrams. So for clarity we will only consider a subset of
the coffees: Espresso, Espresso Con Panna, Café Late, Cappuccino and Café Mocha. 
We’ll include 2 extras - whipped cream (“whipped”) and an extra shot of espresso; 
and three changes - decaf, steamed milk (“wet”) and foamed milk (“dry”).

## 6. Iterator Pattern (Behavioral)
##### Description
Used to get a way to access the elements of a collection object in sequential 
manner without any need to know its underlying representation. The iterator 
pattern decouples algorithms from containers; in some cases, algorithms are 
necessarily container-specific and thus cannot be decoupled.

##### Implementation
Python prescribes a syntax for iterators as part of the language itself, so that 
language keywords such as for work with what Python calls sequences. A sequence 
has an \_\_iter__() method that returns an iterator object. The "iterator protocol" 
requires \_\_next__() return the next element or raise a StopIteration exception upon 
reaching the end of the sequence. Iterators also provide an \_\_iter__() method 
returning themselves so that they can also be iterated over e.g., using a for 
loop.

##### Implementing type-safe iterator
To design a container that only accept a particular type of object, you would 
design an iterator that imposes the constraint that the type of objects it iterates
over be of a certain type. Use the decorator pattern to create a class that simply
wraps the enumeration/iterator that is produced, generating a new object that has 
the iteration behaviour that we want but the same interface as the original 
enumeration/iterator.

## 7. Factory method Pattern (Creational)
##### Description
It is a creational pattern that uses factory methods to deal with the problem of 
creating objects without having to specify the exact class of the object that 
will be created.
The Factory Method design pattern solves problems like:
1. How can an object be created so that subclasses can redefine which class to instantiate?
2. How can a class defer instantiation to subclasses?

The Factory Method design pattern describes how to solve such problems:
1. Define a separate operation (factory method) for creating an object.
2. Create an object by calling a factory method.

##### Implementation

