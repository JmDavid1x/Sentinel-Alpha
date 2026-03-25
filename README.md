# Sentinel-Alpha: Autonomous Risk Arbiter

## Contexto del Proyecto

Desarrollado como proyecto de alta ingenieria para estudiantes de Ingenieria telematica y de Sistemas. 
Sentinel-Alpha es un sistema Multi-Agentes de IA diseñado para analizar riesgos financieros en Colombia. 
El nucleo del proyecto utiliza un bucle de auto-correccion (Self-Correction Loop) apoyado por Machine Learning, permitiendo a los distintos agentes (Gemini y Claude) interactuar, cuestionarse y aprender de manera iterativa de los errores de calculo y estimacion pasados.

## Estructura de Desarrollo (Plan de 7 Dias)

Este repositorio mantiene una evolucion estructurada a traves de 7 dias, con integraciones progresivas para el pipeline AI:

### Dia 1: Foundation
Se establecieron las capas fundamentales para la interaccion de componentes. Se estructuro el manejo del estado global (State Management) y el esqueleto de directorios basado en LangGraph.
- Se definieron los requisitos del proyecto en `requirements.txt`.
- Se declaro la clase principal `AgentState` en `state.py` para normalizar el payload transmitido.
- Se configuraron los placeholders para los nodos principales en `nodes.py` (analista, critico y reflector).
- Se enlazo e implemento la maquina de estados base en `main.py`, trazando una ruta elemental `START -> analyst -> END`.

### Dia 2: Gemini Brain (Proximamente)
Integracion de 'gemini-2.0-flash' en el nodo de analisis. Actuara como el motor de extraccion heuristica, formulando el primer analisis de riesgo a partir de las metricas del contexto en crudo.

### Dia 3: Claude Auditor (Proximamente)
Integracion de 'claude-3-5-sonnet' en el nodo critic. Actuara como la capa de resiliencia logica y auditoria para desafiar cualquier sesgo cognitivo, falacia de costo hundido o asunciones infundadas originadas por el nodo Gemini, estableciendo de manera conjunta el nivel real de riesgo.

### Dia 4: Vector Memory (Proximamente)
Inclusion de ChromaDB para persistencia neuronal vectorial a largo plazo. Todos los analisis, errores probados y retroalimentaciones pasaran a almacenarse aqui como tensores contextuales recuperables mediante similitud para enriquecer las proximas inferencias del sistema.

### Dia 5: Self-Correction Loop (Proximamente)
Activacion del nodo de reflexion. Mediante tecnicas analiticas, el nodo cuantificara el error (Prediccion teorica vs Realidad empobrecedora / mercado). Esta validacion de contraste genera el `error_score` del datagrama.

### Dia 6: ML Prompt Optimizer (Proximamente)
Inclusion de logica dinamica de optimizacion. A traves del indice de error registrado en dias pasados, el orquestador re-escribira de forma autonoma el System Prompt de base de los agentes intervinientes ("Prompt Engineering on-the-fly"), afinando el comportamiento sin intervencion humana.

### Dia 7: Final Polish (Proximamente)
Refinamiento, visualizaciones de control, presentacion de grafos generados por LangGraph y consideraciones excepcionales para la mitigacion de fallos por latencia de API (toque 'antigravity').

## Instalacion y Ejecucion del Entorno

A partir de la raiz del proyecto, siga estos pasos:

1. Instalar modulos (LangGraph y dependencias locales):
   pip install -r requirements.txt
   
2. Inicializar la secuencia de grafos actual:
   python main.py
