import os
import time
from typing import Dict, Any
from state import AgentState

# Cargar variables de entorno (GEMINI_API_KEY)
try:
    from dotenv import load_dotenv
    from litellm import completion
    load_dotenv()
except ImportError:
    pass

def analyst(state: AgentState) -> Dict[str, Any]:
    """
    Nodo Analista (Dia 2 - Gemini Brain).
    Genera inferencia de riesgo financiero y operativo.
    Implementa medicion de latencia de red (Telemetria).
    """
    print(" -> [Analyst Node] Inicializando Cerebro Gemini (gemini-2.0-flash)...")
    
    system_prompt = """Eres un Senior Risk Analyst y Arquitecto de Telematica operando en Colombia en marzo de 2026.
Tu objetivo es analizar riesgos financieros y operativos basandote en el contexto proveido. DEBES enfocarte en:
1. El impacto del TRM (Tasa Representativa del Mercado) en el sector especifico.
2. La interconexion de sistemas de pago e interoperabilidad (liquidez y conexion en Sart, CENIT - Banco de la Republica).
3. Evaluar el riesgo operativo y la volatilidad de infraestructura (ej. latencia, cuellos de botella y caidas en redes de compensacion).

FORMATO DE SALIDA ESTRICTO:
Responde tu analisis descriptivo empleando formato Markdown puro legible en terminal (no uses caracteres raros que rompan la vista).
Al final de tu analisis, INCLUYE obligatoriamente un bloque de codigo JSON con este esquema exacto para que el Agente Critico lo parsee en la fase posterior:
```json
{
  "trm_risk_level": "Alto|Medio|Bajo",
  "operational_latency_risk": "Alto|Medio|Bajo",
  "key_contingency": "Resumen de contingencia operativa",
  "cenit_sart_status": "Observacion critica sobre interconexion"
}
```
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Contexto a analizar:\n{state['input']}"}
    ]
    
    start_time = time.time()
    try:
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=messages,
            temperature=0.2
        )
        latency = time.time() - start_time
        print(f"    [!] Telemetria: Respuesta de la API LLM recibida en {latency:.3f} segundos.")
        
        analysis_result = response.choices[0].message.content
        return {"analysis": analysis_result}
    except Exception as e:
        latency = time.time() - start_time
        print(f"    [X] Error de API / latencia critica tras {latency:.3f} s: {e}")
        return {"analysis": f"ERROR DE INFRAESTRUCTURA LLM: {str(e)}"}

def critic(state: AgentState) -> Dict[str, Any]:
    """
    Nodo Critico Auditor (Placeholder para Dia 3 - Claude).
    Aplica una auditoria logica a los datos de salida del analista,
    buscando sesgos cognitivos o falacias predictivas.
    """
    print(" -> [Critic Node] Ejecutando validacion logica del analisis...")
    return {"critique": "Auditoria de viabilidad y sesgos evaluada (Mock)"}

def reflector(state: AgentState) -> Dict[str, Any]:
    """
    Nodo de Re-evaluacion o Self-Correction (Placeholder para Dia 5).
    Cuantifica e inserta ruido blanco o calcula el error (Prediccion vs Realidad)
    para ajustar los umbrales de decision futuros.
    """
    print(" -> [Reflector Node] Calculando varianza de prediccion...")
    return {"error_score": 0.05}
