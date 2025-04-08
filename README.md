
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

#The following principles are based on these two principles.


#  SOLID Principles

- SOLID is an acronym that brings together five key principles for efficient, replicable, maintainable, and scalable software development.
## S - Single Responsibility Principle (SRP)
> * “Every class should have a single responsibility: It should have a single purpose in the system, and there should be only one reason to change it.”

-Each class should have a single responsibility, a single task that should be applied to classes, components, and microservices. 

![image](https://github.com/user-attachments/assets/eab0fd19-d438-4d5a-a28c-16debb380d92)

## O - Open/Closed Principle (OCP)
> * “…code should be open for extension but closed to modification. When we have a good design, we just don’t have to change code much to add new features.”
-A software entity (class) should be open to extension (its functionality can be expanded with external entities) but closed to modification.
-If one of the extensions doesn't work, you can remove it without damaging the original code.

![image](https://github.com/user-attachments/assets/de8c4549-15b6-4d93-9a3c-f9501de37943)

## L - Liskov Substitution Principle (LSP)
> * “Objects of subclasses should be substitutable for objects of their superclasses throughout our code.”
-The Liskov Substitution Principle speaks of interfaces: if a software entity uses a class, it should be able to use classes derived from that class.

![image](https://github.com/user-attachments/assets/0f4a53d0-ac27-44eb-97a6-983b2127a853)

## I - Interface Segregation Principle (ISP)
> * “A client-specific interface for a particular set of clients.”
-Instead of one large, common interface, multiple scenario-specific interfaces should be planned to improve decoupling and change management:
-Clients (software entities) that use a software entity (originally a class) should not be forced to depend on methods they don't use. To address this, large interfaces should be segregated, i.e., broken up, into smaller ones.

![image](https://github.com/user-attachments/assets/55ae7526-b3d4-4f20-933d-c13caece7774)

## D - Dependency Inversion Principle (DIP)
> * “It is better to depend on interfaces or abstract classes than it is to depend on concrete classes.”
-The Dependency Inversion Principle states that high-level modules, that is, those closest to human ideas of what the software should do, should not depend on low-level modules (those closest to the implementation details for the computer).
-Both should depend on the abstractions of the problem (interfaces). Furthermore, the implementation details should depend on the abstractions as well.

![image](https://github.com/user-attachments/assets/04238a3f-bbd5-4d84-9a95-73ecff6c33fb)

![image](https://github.com/user-attachments/assets/3d8004f2-1ba3-4157-bf4a-181dfd0f3235)

## Considerations When Applying the Principles
> * The SOLID Principles can be applied to all phases of object-oriented programming (OOP), as well as to functional programming (FP) and multi-paradigm programming.
However, they should always be applied with proper planning and methodologies. And above all, without excessive rigidity. Excessive rigidity and rigor can make these principles the ultimate goal and hinder the development process.

## Conclusion
> * Design principles are not simply academic rules; they are practical tools that allow you to build quality software in the real world. Applying them reduces long-term development time, improves collaboration between teams, and ensures that your code scales safely.


## Code : 
![image](https://github.com/user-attachments/assets/eb158239-f1c7-4da3-9d43-bc7c5db2d1a5)

## Application Principle
-SRP The Message class is only responsible for representing a message.
-OCP We can add new delivery types without modifying DeliveryService.
-LSP EmailSend and SMSSend can be used without breaking the system logic.
-ISP The Sender interface defines only what is necessary: send(message).
-DIP DeliveryService depends on an abstraction (Sender), not on concrete classes.






