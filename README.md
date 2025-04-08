
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
