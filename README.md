
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







