import os
import chromadb
import google.generativeai as genai
from typing import TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

# ==========================================================
# 1. SETUP: Variables de Entorno y Configuracion API
# ==========================================================
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY no encontrada en .env")

genai.configure(api_key=GOOGLE_API_KEY)
# Utilizamos gemini-2.0-flash que es el estandar mas reciente
model = genai.GenerativeModel('gemini-2.0-flash')

# Inicializacion persistente de Base Vectorial Local
chroma_client = chromadb.PersistentClient(path="./chroma_db_mvp")
memory_collection = chroma_client.get_or_create_collection(name="sentinel_memory")

# ==========================================================
# 2. STATE: Definicion del Datagrama (Payload)
# ==========================================================
class AgentState(TypedDict):
    input: str
    analysis: str
    critique: str
    refined_analysis: str
    memory_id: str

# ==========================================================
# 3. NODOS: Logica de Agentes (Gemini-Centric)
# ==========================================================
def analyst_node(state: AgentState) -> dict:
    print(" -> [Analyst Node] Solicitando evaluacion de riesgo inicial a Gemini...")
    system_prompt = "Eres un Senior Risk Analyst operando en Colombia. Evalua riesgos operativos y financieros del escenario planteado."
    
    try:
        response = model.generate_content(
            f"INSTRUCCION: {system_prompt}\n\nESCENARIO A EVALUAR:\n{state['input']}"
        )
        return {"analysis": response.text}
    except Exception as e:
        return {"analysis": f"[ERROR DEL MODELO/SDK]: {str(e)}"}

def critic_node(state: AgentState) -> dict:
    print(" -> [Critic Node] Activando auditoria interna (Gemini self-critique)...")
    system_prompt = "Eres un Auditor Interno riguroso. Critica el siguiente analisis de riesgo buscando sesgos cognitivos o falencias logicas."
    
    try:
        response = model.generate_content(
            f"INSTRUCCION: {system_prompt}\n\nANALISIS A AUDITAR:\n{state.get('analysis', '')}"
        )
        return {"critique": response.text}
    except Exception as e:
        return {"critique": f"[ERROR DEL MODELO/SDK]: {str(e)}"}

def mem_store_node(state: AgentState) -> dict:
    print(" -> [Mem Store Node] Persistiendo experiencia en DB Vectorial (ChromaDB)...")
    
    doc_id = f"mem_{os.urandom(4).hex()}"
    final_knowledge = f"Escenario: {state['input']}\nAnalisis: {state.get('analysis', '')}\nCritica: {state.get('critique', '')}"
    
    memory_collection.add(
        documents=[final_knowledge],
        ids=[doc_id]
    )
    return {"memory_id": doc_id, "refined_analysis": final_knowledge}

# ==========================================================
# 4. GRAFO: Topologia de Flujo LangGraph
# ==========================================================
def build_graph() -> StateGraph:
    workflow = StateGraph(AgentState)
    
    workflow.add_node("analyst_node", analyst_node)
    workflow.add_node("critic_node", critic_node)
    workflow.add_node("mem_store_node", mem_store_node)
    
    workflow.add_edge(START, "analyst_node")
    workflow.add_edge("analyst_node", "critic_node")
    workflow.add_edge("critic_node", "mem_store_node")
    workflow.add_edge("mem_store_node", END)
    
    return workflow.compile()

# ==========================================================
# 5. EJECUCION: Interfaz Interactiva de Consola
# ==========================================================
if __name__ == "__main__":
    print("="*60)
    print(" Sentinel-Alpha MVP: Autonomous Risk Arbiter (100% Free Tier)")
    print("="*60)
    
    app = build_graph()
    
    # Input Dinamico
    user_input = input("\n[>] Ingrese el contexto de riesgo a analizar en Colombia: \n>>> ")
    
    initial_state = {
        "input": user_input,
        "analysis": "",
        "critique": "",
        "refined_analysis": "",
        "memory_id": ""
    }
    
    print("\nEjecutando Pipeline Autoritativo...\n")
    final_state = app.invoke(initial_state)
    
    print("\n" + "="*60)
    print(" RESULTADOS DEL CICLO MULTI-AGENTE")
    print("="*60)
    print(f"\n[ANALISIS INICIAL]:\n{final_state.get('analysis')}")
    print(f"\n[CRITICA DEL AUDITOR]:\n{final_state.get('critique')}")
    print(f"\n[MEMORIA GUARDADA ID]: {final_state.get('memory_id')}")
