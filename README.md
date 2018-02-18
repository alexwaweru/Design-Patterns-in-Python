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

## 1. Singleton Pattern
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

## 2. Template method Pattern
#### Description
The template method pattern is a behavioral design pattern that defines 
the program skeleton of an algorithm in an operation, deferring some 
steps to subclasses.

#### Implementation
Implement a Game abstract class defining operations with a 
template method set to be final so that it cannot be overridden. Rugby 
and Football are concrete classes that extend Game and override its methods.
TemplatePatternDemo, our demo class, will use Game to demonstrate use of 
template pattern.

## 3. Proxy
#### Description
Proxy pattern provides a surrogate class that you use in your code. The real 
class that does the work is hidden behind this surrogate class. Proxy is used
for fronting an implementation. This is important when the access to an object
should be controlled or additional functionality should be provided when 
accessing an object.

#### Implementation
Used the __getattr__( ) to delegate from the proxy class to the implementation.



