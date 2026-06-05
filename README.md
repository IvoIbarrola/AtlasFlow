# Asistente Virtual para WhatsApp

Asistente inteligente integrado con WhatsApp diseñado para automatizar tareas cotidianas mediante lenguaje natural. El objetivo del proyecto es centralizar herramientas de productividad en una única interfaz conversacional, permitiendo a los usuarios gestionar recordatorios, redactar correos electrónicos, buscar archivos, investigar información y obtener resúmenes de contenido sin necesidad de interactuar con múltiples aplicaciones.

## Objetivos

* Simplificar tareas repetitivas y administrativas.
* Centralizar herramientas de productividad en WhatsApp.
* Aplicar conocimientos de programación, APIs, microservicios y automatización.
* Explorar la integración de modelos de inteligencia artificial en entornos reales.
* Construir un proyecto escalable y demostrable para fines académicos y profesionales.

## Funcionalidades previstas

### Gestión de recordatorios

* Crear recordatorios mediante lenguaje natural.
* Consultar recordatorios pendientes.
* Modificar o eliminar eventos existentes.
* Recepción automática de notificaciones.

### Asistencia en correos electrónicos

* Generación de correos formales.
* Corrección y mejora de textos.
* Envío de correos desde la plataforma.

### Búsqueda de archivos

* Localización de archivos mediante consultas en lenguaje natural.
* Exploración de directorios configurados.
* Presentación de resultados relevantes.

### Investigación y resúmenes

* Búsqueda de información en fuentes externas.
* Generación de resúmenes.
* Respuesta a consultas puntuales.

### Historial conversacional

* Registro de interacciones.
* Seguimiento de solicitudes realizadas.
* Posibilidad de futuras mejoras basadas en contexto.

## Arquitectura propuesta

```text
WhatsApp
    │
    ▼
Webhook/API
    │
    ▼
Servicio Principal (FastAPI)
    │
    ├── Gestión de Recordatorios
    ├── Generación de Correos
    ├── Búsqueda de Archivos
    ├── Investigación y Resúmenes
    └── Base de Datos
```

## Tecnologías

| Componente             | Tecnología                                 |
| ---------------------- | ------------------------------------------ |
| Backend                | Python                                     |
| Framework API          | FastAPI                                    |
| Contenedores           | Docker / Docker Compose                    |
| Base de Datos          | MySQL                                      |
| IA                     | OpenAI / Ollama                            |
| Programación de tareas | APScheduler                                |
| Integración WhatsApp   | API Cloud de Meta o alternativa compatible |
| Control de versiones   | Git                                        |

## Estado del proyecto

🚧 En etapa de planificación y diseño.

Actualmente se está definiendo la arquitectura general, el alcance inicial del MVP y la estrategia de integración con WhatsApp.

## Roadmap inicial

* [ ] Definición de arquitectura.
* [ ] Configuración del entorno Docker.
* [ ] Implementación de API principal.
* [ ] Integración con WhatsApp.
* [ ] Gestión de recordatorios.
* [ ] Generación de correos.
* [ ] Búsqueda de archivos.
* [ ] Investigación y resúmenes mediante IA.
* [ ] Persistencia y gestión de usuarios.

## Motivación

Este proyecto surge de la necesidad de reducir el tiempo dedicado a tareas simples que suelen requerir múltiples herramientas o aplicaciones. La propuesta busca ofrecer una experiencia más natural e intuitiva utilizando WhatsApp como interfaz principal, aprovechando una plataforma ampliamente conocida por los usuarios.

## Autor

**Ivo Ibarrola**

Proyecto desarrollado con fines de aprendizaje, experimentación y crecimiento profesional.
