from langgraph.graph import StateGraph, START, END
from state import AgentState
from nodes import analyst, critic, reflector

def build_graph() -> StateGraph:
    """
    Construye la topologia del Grafo de Estados del sistema multi-agente.
    En terminos de Sistemas de Informacion, define el control de flujo
    de ejecucion y las rutas posibles en la maquina de estados de LangGraph.
    
    Dia 1: Conexion fundamental (START -> analyst -> END).
    """
    # Inicializacion del layout en memoria utilizando la estructura del agente
    workflow = StateGraph(AgentState)
    
    # Registro de nodos (endpoints dentro del flujo)
    workflow.add_node("analyst", analyst)
    workflow.add_node("critic", critic)
    workflow.add_node("reflector", reflector)
    
    # Definicion del enrutamiento (Edges)
    workflow.add_edge(START, "analyst")
    workflow.add_edge("analyst", END)
    
    # Compilacion y resolucion de grafos aciclicos / ciclos para su ejecucion
    app = workflow.compile()
    
    return app

if __name__ == "__main__":
    print("=== Iniciando Sentinel-Alpha: Autonomous Risk Arbiter ===")
    
    # Compilar el entorno
    app = build_graph()
    
    # Establecer la semilla de estado (Payload de inicializacion)
    initial_state = {
        "input": "Analisis de riesgo cambiario por fluctuacion del dolar en el sector exportador de cafe (Colombia).",
        "analysis": "",
        "critique": "",
        "error_score": 0.0,
        "memory_context": []
    }
    
    print("\nEjecutando recorrido del flujo (Dia 1 Config)...")
    # Invocar el arbol de decisiones
    result = app.invoke(initial_state)
    
    print("\n=== Estado Final en la Topologia ===")
    for key, value in result.items():
        print(f"{key.upper()}: {value}")
