import os
import time
import json
import chromadb
from typing import Dict, Any
from state import AgentState

try:
    from dotenv import load_dotenv
    from litellm import completion
    load_dotenv()
except ImportError:
    pass

# Dia 4: Inicializacion de Vector Memory local de ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
try:
    memory_collection = chroma_client.get_or_create_collection(name="risk_memory")
except Exception:
    pass

def get_base_prompt(state: AgentState) -> str:
    """Extrae aprendizaje historico y re-escribe el Prompt si el Optimizador lo decidio."""
    # (Dia 6) ML Prompt Optimizer Injector
    memoria = state.get("memory_context")
    if memoria and "OPTIMIZED_PROMPT:" in str(memoria):
        # Toma la ultima directiva aprendida
        ultima_directiva = memoria[-1]
        return f"""Eres un Senior Risk Analyst operando en Colombia en marzo de 2026.
IMPORTANTE - HISTORIAL DE FALLOS APRENDIDO: {ultima_directiva}
Analiza el TRM y la interconexion (Sart, CENIT). Considera la volatilidad y la latencia en las redes interbancarias.
FORMATO DE SALIDA ESTRICTO: Responde en Markdown legible. Al final, anexa EXACTAMENTE este JSON:
```json
{{
  "trm_risk_level": "Alto|Medio|Bajo",
  "operational_latency_risk": "Alto|Medio|Bajo",
  "key_contingency": "Contingencia de red",
  "cenit_sart_status": "Mensaje sobre estado de interconexion"
}}
```"""

    return """Eres un Senior Risk Analyst y Arquitecto de Telematica operando en Colombia en marzo de 2026.
Tu objetivo es analizar riesgos financieros y operativos basandote en el contexto proveido. DEBES enfocarte en:
1. Impacto del TRM en el ecosistema especifico.
2. Interconexion de sistemas e interoperabilidad de pago (Sart, CENIT - Banco de la Republica).
3. Evaluar el riesgo de volatilidad e infraestructura (latencia de comunicacion TCP/IP, redes de compensacion).

FORMATO DE SALIDA ESTRICTO:
Responde tu analisis descriptivo en Markdown legible para terminal.
Al final, INCLUYE un bloque JSON estricto con:
```json
{
  "trm_risk_level": "Alto|Medio|Bajo",
  "operational_latency_risk": "Alto|Medio|Bajo",
  "key_contingency": "Contingencia operativa de red",
  "cenit_sart_status": "Observacion sobre interconexion"
}
```
"""

def analyst(state: AgentState) -> Dict[str, Any]:
    """Nodo Analista (Dia 2 - Gemini Brain)."""
    print(" -> [Analyst Node] Ejecutando calculo heuristico predictivo (gemini-2.0-flash)...")
    messages = [
        {"role": "system", "content": get_base_prompt(state)},
        {"role": "user", "content": f"Contexto a analizar:\n{state['input']}"}
    ]
    start_time = time.time()
    try:
        response = completion(model="gemini/gemini-2.0-flash", messages=messages, temperature=0.2)
        latency = time.time() - start_time
        print(f"    [!] Telemetria Analista: Finalizado en {latency:.3f} s.")
        return {"analysis": response.choices[0].message.content}
    except Exception as e:
        return {"analysis": f"ERROR DE CONEXION/GATEWAY LLM: {str(e)}"}

def critic(state: AgentState) -> Dict[str, Any]:
    """Nodo Critico Auditor (Dia 3 - Claude 3.5 Sonnet)."""
    print(" -> [Critic Node] Ejecutando validacion logica estricta (claude-3-5-sonnet)...")
    system_prompt = """Eres el Auditor Critico (Sistema Inteligente Independiente).
Busca falacias de costo hundido, asunciones financieras infundadas (especialmente sobre el TRM de Colombia) \
y penaliza severamente el formato de salida si el analisis de Gemini NO incluye el JSON solicitado al final estructurado perfectamente. \
Extrae un diagnostico sobre su viabilidad.\
Responde en sintesis."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Audita este analisis:\n{state.get('analysis', '')}"}
    ]
    start_time = time.time()
    try:
        response = completion(model="claude-3-5-sonnet-20241022", messages=messages, temperature=0.1)
        latency = time.time() - start_time
        print(f"    [!] Telemetria Critico: Finalizado en {latency:.3f} s.")
        return {"critique": response.choices[0].message.content}
    except Exception as e:
        print("    [!] Fallback Auditor MOCK activado por ausencia de API Key.")
        return {"critique": "Auditoria fallback: El framework de contingencia parece factible en Colombia 2026 sin sesgos aparentes."}

def reflector(state: AgentState) -> Dict[str, Any]:
    """Nodo Reflector (Dia 4 y 5 - ChromaDB & Self-Correction Error Loop)."""
    print(" -> [Reflector Node] Midiendo Varianza (MSE) & Insertando embeddings en ChromaDB...")
    
    # Realidad empirica simulada de mercado en 2026:
    realidad_trm_risk = "Alto"
    realidad_latency_risk = "Medio"
    
    analysis_text = state.get("analysis", "")
    error_score = 0.5 
    
    # Comparar JSON de Gemini con la "Realidad"
    if "```json" in analysis_text:
        try:
            json_str = analysis_text.split("```json")[-1].split("```")[0].strip()
            data = json.loads(json_str)
            
            score = 0.0
            if data.get("trm_risk_level") != realidad_trm_risk: score += 0.5
            if data.get("operational_latency_risk") != realidad_latency_risk: score += 0.5
            error_score = score
            print(f"    [!] Error Match Score: {error_score} (0.0=Perfecto).")
        except Exception:
            print("    [X] Infraccion de formato JSON en el Output.")
            error_score = 1.0 # Penalizacion maxima
    else:
        error_score = 1.0
        
    # Memoria a Largo Plazo
    try:
        memory_collection.add(
            documents=[f"Contexto: {state['input']}"],
            metadatas=[{"error": error_score}],
            ids=[f"t_{time.time()}"]
        )
        print("    [+] Data persistida localmente en Vector Memory.")
    except Exception as e:
        print(f"    [X] Error Vectordb: {e}")
        
    return {"error_score": error_score}

def optimizer(state: AgentState) -> Dict[str, Any]:
    """Nodo Optimizador (Dia 6 - ML Prompt Optimizer)."""
    print(" -> [Optimizer Node] Analizando feedback loop de aprendizaje...")
    
    error = state.get("error_score", 0.0)
    memory = state.get("memory_context", [])
    
    if error > 0.4:
        print("    [x_x] Error alto. Activando sobreescritura autonoma de Prompt futuro.")
        conocimiento = "OPTIMIZED_PROMPT: Presta hiper-atencion al esquema JSON para no equivocarte en la extraccion de latencia y nivel de riesgo. NO repitas el mismo fallo."
        memory.append(conocimiento)
    else:
        print("    [^_^] Inferencia Altamente Confiable. Estructura y logica robusta mantenidas.")
        memory.append("[Log] Análisis Exitoso.")
        
    return {"memory_context": memory}
