# Sentinel-Alpha: Autonomous Risk Arbiter (MVP)

Un sistema multi-agente autocritico impulsado por inteligencia artificial generativa, diseñado para analizar contextos de riesgo financiero y operativo. Todo el pipeline de procesamiento se basa en **LangGraph** para el control de estados distribuidos y en **ChromaDB** para la persistencia a largo plazo de la memoria (Vector DB).

## Arquitectura del MVP

Esta iteración consolidada (100% Free Tier) utiliza la Native SDK de Google (`google-generativeai`) y el modelo `gemini-1.5-flash`. Cubre multiples roles operacionales de manera simultánea mediante simulación de personalidades cognitivas independientes:
1.  **Analyst Node:** Actúa como *Senior Risk Analyst*, generando una abstracción inicial del riesgo a partir del input textual del usuario.
2.  **Critic Node:** Adopta un perfil de *Auditor Interno*, inspeccionando el analisis previo de su homólogo para destrozar sesgos cognitivos, redundancias heurísticas o supuestos infundados.
3.  **Memory Store Node:** Almacena ambas variables (Proposición + Antítesis) localmente en un embedding de ChromaDB, generando memoria a largo plazo para futuras consultas interbancarias.

## Ejecución Gratuita (Free Tier Setup) 🚀

El entorno opera dentro de los límites del plan gratuito de Google. Siga estos pasos para ejecutar la terminal telemática en su máquina:

### 1. Obtención de Credenciales
1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Haz clic en **"Create API Key"**.
3. Copia la clave secreta generada (El proceso no requiere tarjetas de crédito y es 100% gratis).

### 2. Configuración Local
1. Instale las dependencias base de Python en la raíz del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
2. Renombre el archivo de la bóveda local `.env.example` para que se llame `.env`. Abra el archivo y pegue su llave respetando esta nomenclatura estricta:
   ```env
   GEMINI_API_KEY="AIzaSy_TU_CLAVE_COPIADA_AQUI"
   ```
3. Ejecute el ecosistema Multi-Agente:
   ```bash
   python main.py
   ```

El programa arrancará una interfaz interactiva por terminal (CLI) que le pedirá describir un sustrato de riesgo.

## Licencia
Distribuido bajo la [Licencia MIT](https://opensource.org/licenses/MIT). Podrá utilizar, modificar, y emplear este orquestador multi-agente bajo su propia discrecionalidad en entornos comerciales e institucionales de manera Open Source.
