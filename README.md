
# Principios SOLID con Python - Sistema de Notificaciones

Este proyecto implementa un ejemplo práctico de los 5 principios SOLID utilizando Python. Simula el envío de notificaciones por Email y SMS.

## 🔧 Tecnologías
- Python 3
- GitHub Actions (automatización)

## ✅ Principios aplicados

| Principio | Aplicación |
|----------|------------|
| SRP      | `Mensaje` solo representa un mensaje |
| OCP      | Nuevas clases como WhatsApp se pueden añadir sin modificar `ServicioEnvio` |
| LSP      | `EnvioEmail` y `EnvioSMS` pueden reemplazarse entre sí |
| ISP      | `Enviador` es una interfaz específica para enviar |
| DIP      | `ServicioEnvio` depende de la interfaz `Enviador`, no de clases concretas |

## 🚀 Cómo ejecutar
```bash
python solid_example.py
```
# What is a Principle?

A principle is a broad behavioral guideline applicable to many situations. In general, a principle doesn't tell you exactly what to do, but rather gives you clues as to the correct course of action across a wide range of situations. The details are up to you.

## Don't Repeat Yourself (DRY)

- **You should avoid repeating code as much as possible.**
- We must keep in mind that we must find ways to reuse code we've already created to avoid getting tangled up.

### Why is it important?

- ➢ **Makes the code more maintainable:** Avoiding repeating code helps us make changing functionality more practical.
- ➢ **Reduces code size:** It makes it more readable and understandable because there's less code to understand.
- ➢ **Saves time:** By having the code available for reuse, we can use it and shorten coding time.

## KISS = Keep It Simple [,] Stupid

This principle establishes that code, design, documentation, and everything related to it should be simple.

It establishes that:

- ➢ Software should have as few components as possible
- ➢ No unused functionality
- ➢ Documentation should contain strict and necessary information
- ➢ Code should be as obvious and simple as possible
- ➢ Design should be simple

### Why is it important?

- ➢ **More maintainable projects.** The code is easier to maintain and update.
- ➢ **Less documentation.** There are fewer weird things to document by making the code simpler.
- ➢ **Faster debugging.** By reducing complexity, errors can be found more quickly.
- ➢ **Greater economic returns.** The three effects above allow the initial financial investment in the code created to yield greater returns.

> *"Simplicity is the ultimate sophistication."*

The following principles are based on these two principles.

SOLID is an acronym that brings together five key principles for efficient, replicable, maintainable, and scalable software development.

	S - Single Responsibility Principle (SRP)  
“Every class should have a single responsibility: It should have a single purpose in the system, and there should be only one reason to change it.”

Each class should have a single responsibility, a single task that should be applied to classes, components, and microservices. 

	O - Open/Closed Principle (OCP)  
“…code should be open for extension but closed to modification. When we have a good design, we just don’t have to change code much to add new features.”  
A software entity (class) should be open to extension (its functionality can be expanded with external entities) but closed to modification.  
If one of the extensions doesn't work, you can remove it without damaging the original code.


	L - Liskov Substitution Principle (LSP)  
“Objects of subclasses should be substitutable for objects of their superclasses throughout our code.”  
The Liskov Substitution Principle speaks of interfaces: if a software entity uses a class, it should be able to use classes derived from that class.
 
	I - Interface Segregation Principle (ISP)  
“A client-specific interface for a particular set of clients.”  
Instead of one large, common interface, multiple scenario-specific interfaces should be planned to improve decoupling and change management:  
Clients (software entities) that use a software entity (originally a class) should not be forced to depend on methods they don't use. To address this, large interfaces should be segregated, i.e., broken up, into smaller ones.
 

	D - Dependency Inversion Principle (DIP)  

“It is better to depend on interfaces or abstract classes than it is to depend on concrete classes.”  
The Dependency Inversion Principle states that high-level modules, that is, those closest to human ideas of what the software should do, should not depend on low-level modules (those closest to the implementation details for the computer). Both should depend on the abstractions of the problem (interfaces). Furthermore, the implementation details should depend on the abstractions as well.
