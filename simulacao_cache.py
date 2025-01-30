import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

# Inicialização de dados
cache_size = 5
bd_size = 20

# Banco de dados simulado
bd = {i: fruta for i, fruta in enumerate([
    "Maçã", "Banana", "Cereja", "Tâmara", "Elderberry", "Figo", "Uva", "Melão", "Kiwi", "Limão", 
    "Manga", "Nectarina", "Laranja", "Mamão", "Marmelo", "Framboesa", "Morango", "Tangerina", "Fruta Ugli", "Melancia"
], start=1)}

# Inicializar estado
if "cache" not in st.session_state:
    st.session_state.cache = []
    st.session_state.frequencies = {}
    st.session_state.hits = 0
    st.session_state.misses = 0
    st.session_state.algorithm = "LRU"
    st.session_state.reset_data_key = False

# Função para simular busca de dados
def fetch_from_cache(item_key):
    cache = st.session_state.cache
    frequencies = st.session_state.frequencies

    if item_key in cache:
        st.session_state.hits += 1
        if st.session_state.algorithm == "LRU":
            cache.remove(item_key)
            cache.append(item_key)
        elif st.session_state.algorithm == "LFU":
            frequencies[item_key] += 1
        return bd[item_key]
    else:
        st.session_state.misses += 1
        if len(cache) >= cache_size:
            if st.session_state.algorithm == "LRU":
                cache.pop(0)
            elif st.session_state.algorithm == "LFU":
                least_used = min(frequencies, key=frequencies.get)
                cache.remove(least_used)
                frequencies.pop(least_used)
            elif st.session_state.algorithm == "FIFO":
                cache.pop(0)

        cache.append(item_key)
        if st.session_state.algorithm == "LFU":
            frequencies[item_key] = 1
        return bd[item_key]

# Interface Streamlit
st.set_page_config(page_title="Simulação de Cache", layout="wide")
st.title("Simulação de Algoritmos de Cache")

# Layout principal
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("⚙️ Configurações")
    st.session_state.algorithm = st.radio(
        "Escolha o algoritmo de substituição", ["LRU", "LFU", "FIFO"], horizontal=True, index=["LRU", "LFU", "FIFO"].index(st.session_state.algorithm)
    )
    st.markdown("### 📂 Banco de Dados")
    bd_display = [f"{k}: {v}" for k, v in bd.items()]
    st.dataframe({"Posição": list(bd.keys()), "Valor": list(bd.values())}, use_container_width=True)

with col2:
    st.subheader("📥 Cache Atual")
    if st.session_state.cache:
        cache_display = {i: bd[i] for i in st.session_state.cache}
        st.dataframe({"Posição": list(cache_display.keys()), "Valor": list(cache_display.values())}, use_container_width=True)
    else:
        st.write("Cache está vazia.")

# Estatísticas
st.markdown("---")
st.subheader("📊 Estatísticas")
col3, col4 = st.columns(2)
with col3:
    st.metric(label="Cache HITs", value=st.session_state.hits, delta_color="inverse")
with col4:
    st.metric(label="Cache MISSes", value=st.session_state.misses, delta_color="normal")
style_metric_cards()

# Simular busca
st.markdown("---")
st.subheader("🔎 Simular Busca")

# Controle de redefinição para o número da chave
if "reset_data_key" in st.session_state and st.session_state.reset_data_key:
    st.session_state.data_key = 1
    st.session_state.reset_data_key = False  # Desativa o estado de reset

# Entrada para a chave de busca
data_key = st.number_input(
    "Digite a chave do dado para buscar (1-20):",
    min_value=1,
    max_value=20,
    step=1,
    key="data_key"
)

if st.button("Buscar Dado", use_container_width=True):
    result = fetch_from_cache(data_key)
    st.success(f"✅ Dado encontrado: {result}")

# Resetar sistema
if st.button("🔄 Resetar Estatísticas e Cache", use_container_width=True):
    st.session_state.cache = []
    st.session_state.frequencies = {}
    st.session_state.hits = 0
    st.session_state.misses = 0
    st.session_state.reset_data_key = True
    st.query_params  # Força a atualização sem erro

# Rodapé com instruções
st.markdown("---")
st.caption("🛠️ Desenvolvido para simular políticas de cache (LRU, LFU, FIFO). Experimente diferentes configurações e observe as estatísticas!")
