from typing import TypedDict, List, Any

class AgentState(TypedDict):
    """
    Representa el estado del Grafo (StateGraph) en LangGraph.
    
    Desde la perspectiva de la Ingenieria Telematica, este TypedDict
    actua como el formato del datagrama o payload que transita a traves
    de la topologia de red de nuestro sistema experto de multiples agentes.
    Mantiene el contexto global entre todas las transiciones (routers y endpoints).
    """
    input: str
    analysis: str
    critique: str
    error_score: float
    memory_context: List[Any]
