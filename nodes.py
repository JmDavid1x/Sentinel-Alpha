from typing import Dict, Any
from state import AgentState

def analyst(state: AgentState) -> Dict[str, Any]:
    """
    Nodo Analista (Placeholder para Dia 2 - Gemini).
    Toma la entrada inicial y genera una inferencia sobre el riesgo financiero.
    Retorna un diccionario que actualiza el estado global.
    """
    print(" -> [Analyst Node] Procesando parametros de entrada...")
    return {"analysis": "Analisis de contingencia y riesgo inicial (Mock)"}

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
