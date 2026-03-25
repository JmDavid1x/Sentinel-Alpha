from langgraph.graph import StateGraph, START, END
from state import AgentState
from nodes import analyst, critic, reflector, optimizer

def build_graph() -> StateGraph:
    """
    Construye la topologia del Grafo de Estados del ecosistema Sentinel-Alpha (Days 3-7).
    Diseno de Pipeline Multi-Agente: START -> Analyst -> Critic -> Reflector -> Optimizer -> END
    """
    workflow = StateGraph(AgentState)
    
    # Registro de Agentes (Instancias Nodos)
    workflow.add_node("analyst", analyst)
    workflow.add_node("critic", critic)
    workflow.add_node("reflector", reflector)
    workflow.add_node("optimizer", optimizer)
    
    # Definicion del Enrutamiento Lineal Reflexivo (Routing/Edges)
    workflow.add_edge(START, "analyst")
    workflow.add_edge("analyst", "critic")
    workflow.add_edge("critic", "reflector")
    workflow.add_edge("reflector", "optimizer")
    workflow.add_edge("optimizer", END)
    
    # Resolucion y Compilacion Semiotica
    app = workflow.compile()
    return app

if __name__ == "__main__":
    print("=== Iniciando Ecosistema Autonomo Sentinel-Alpha v1.0 ===")
    
    # Levantar el kernel de comunicacion LangGraph
    app = build_graph()
    
    # Payload o Datagrama Inicial (Gen-1)
    initial_state = {
        "input": "Analisis de riesgo macroeconomico en las transacciones digitales por fluctuacion de TRM y estres de latencia en la pasarela CENIT/Sart bajo carga alta del Banco de la Republica (Marzo 2026).",
        "analysis": "",
        "critique": "",
        "error_score": 0.0,
        "memory_context": []
    }
    
    print("\n[>>] Vectorizando Inferencia de Red Descentralizada...")
    
    # Ejecutar la transaccion sincronamente
    result = app.invoke(initial_state)
    
    print("\n=== Estado Final del Datagrama (Payload) ===")
    print(f"-> SCORE DE ERROR RESULTANTE vs Realidad: {result.get('error_score')}")
    print(f"-> OBSERVACIONES EN MEMORIA RAM: {result.get('memory_context')}")
    print("\nMision Sentinel-Alpha Finalizada con Exito.")
