cat << 'EOF' > solid_example.py
from abc import ABC, abstractmethod

# Principio SRP: Una clase, una responsabilidad.
class Mensaje:
    def __init__(self, destinatario, contenido):
        self.destinatario = destinatario
        self.contenido = contenido

# Principio ISP: Una interfaz específica.
class Enviador(ABC):
    @abstractmethod
    def enviar(self, mensaje: Mensaje):
        pass

# Principio OCP y LSP: Nuevas implementaciones sin modificar código existente.
class EnvioEmail(Enviador):
    def enviar(self, mensaje: Mensaje):
        print(f"Enviando Email a {mensaje.destinatario}: {mensaje.contenido}")

class EnvioSMS(Enviador):
    def enviar(self, mensaje: Mensaje):
        print(f"Enviando SMS a {mensaje.destinatario}: {mensaje.contenido}")

# Principio DIP: Servicio depende de la abstracción.
class ServicioEnvio:
    def __init__(self, enviador: Enviador):
        self.enviador = enviador

    def procesar_envio(self, mensaje: Mensaje):
        self.enviador.enviar(mensaje)

if __name__ == "__main__":
    email = EnvioEmail()
    sms = EnvioSMS()

    servicio_email = ServicioEnvio(email)
    servicio_sms = ServicioEnvio(sms)

    mensaje1 = Mensaje("juan@example.com", "Hola, Juan!")
    mensaje2 = Mensaje("+123456789", "¡Hola por SMS!")

    servicio_email.procesar_envio(mensaje1)
    servicio_sms.procesar_envio(mensaje2)
EOF
