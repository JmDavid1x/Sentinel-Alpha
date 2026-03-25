# Sentinel-Alpha: Autonomous Risk Arbiter (Versión 1.0)

## Sobre Mí y el Proyecto 🏆

¡Hola! Soy David, Senior Architect y estudiante de Ingeniería Telemática y de Sistemas. He desarrollado **Sentinel-Alpha** como mi proyecto de grado y portafolio tecnológico avanzado. Su propósito es demostrar mis habilidades en el liderazgo y construcción de ecosistemas autónomos descentralizados (Multi-Agent Systems), gestión de micro-estados distribuidos e IA generativa orientada a la contingencia real.

En este repositorio resolví el problema clásico de la **"alucinación predictiva"** y **"latencia transaccional"** de los modelos de inteligencia artificial aplicados sobre la fluctuación hiperdinámica propia de nuestro sector en Colombia. Para marzo de 2026, medir el impacto de la Tasa Representativa del Mercado (TRM) y el riesgo operativo en interoperabilidades físicas interbancarias (CENIT y Sart del Banco de la República), exige un modelo autónomo estricto de auto-corrección.

## Arquitectura Modular del Ecosistema (7 Días de Ingeniería)

Sinteticé toda una topología de red distribuida (Agent Pipeline) empleando el kernel avanzado de **LangGraph** para mantener consistencia de datagramas e historial entre agentes. El esqueleto final del orquestador maneja los siguientes subsistemas lógicos:

1. **[Día 2] Gemini Brain (El Científico / Heurística de Extracción):** Utilicé integración segura con API REST vía _LiteLLM_ para enlazar `gemini-2.0-flash`. Diseñé este nodo para recolectar e inferir vulnerabilidades interbancarias, y lo obligué programáticamente a estructurar sus descubrimientos en JSON crudo y calculable. Le implementé además lógica _Timer_ (Telemetría de Red Local) para vigilar caídas del Gateway.
2. **[Día 3] Claude Auditor (El Perro Guardián):** Implementé la inferencia algorítmica lógica de `claude-3-5-sonnet`. Actúa de contención para sesgos cognitivos o falacias de costo hundido propuestos por el propio Gemini. Es el firewall contra alucinaciones.
3. **[Día 4-5] Vector Memory y Self-Correction Loop:** Usé **ChromaDB** para levantar una base de datos vectorial local (como un buffer en RAM de persistencia larga). El sistema simula transacciones enfrentándolas contra el mercado "real". Con ello genera una métrica matemática de `Error Score` entre el riesgo real y el evaluado, castigando drásticamente el error de formato JSON o incoherencia.
4. **[Día 6] Inteligente Machine Learning (Optimizador de Prompting Recursivo):** Lógica avanzada. Si el Error Score alcanza métricas de colapso de fiabilidad superior al 0.4 de pérdida, este script asume que los agentes están infiriendo basura, y escribe dinámicamente **reglas en la Memoria del Prompt Futuro**, obligando a Gemini a enfocar mejor su output para la siguiente iteración de inferencia.

## Metodología y Telemetría Aplicada (Telemática Core) ⚙️

Como experto telemático abordé la capa de Transporte y Aplicación implementado control de latencia asíncrona por request, manejos de excepciones globales, entornos virtuales segregados (Variables de entorno .env protegidas) y Git tracking para asegurar consistencia del repositorio.

### ¿Cómo Desplegar mi Proyecto Localmente?

Es sumamente eficiente su levantamiento. Requiere las librerías mencionadas en `requirements.txt`:

1. Instala en tu máquina los vectores del entorno:
```bash
pip install -r requirements.txt
```

2. Duplica mi archivo plantilla `.env.example`, re-nómbralo como `.env` e integra allí tus claves de acceso de la API (Gemini Studio API y Anthropic API Key).

3. Ejecuta la prueba de estrés macroeconómica de LangGraph:
```bash
python main.py
```

---
*Este proyecto refleja mi capacidad para resolver contingencias complejas desde un enfoque puro de ingeniería e innovación de software. Gracias por visitar este apartado de mi portafolio.*
