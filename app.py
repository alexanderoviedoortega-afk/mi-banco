import streamlit as st

st.set_page_config(page_title="BANCO", page_icon="🏦")

# Saldo inicial
if "saldo" not in st.session_state:
    st.session_state.saldo = 100000

if "mensaje" not in st.session_state:
    st.session_state.mensaje = ""

if "tipo_mensaje" not in st.session_state:
    st.session_state.tipo_mensaje = "info"


def consultar():
    st.session_state.mensaje = f"Tienes ${st.session_state.saldo:,} pesos en tu cuenta"
    st.session_state.tipo_mensaje = "info"


def depositar():
    cantidad = st.session_state.cantidad

    if cantidad > 0:
        st.session_state.saldo += cantidad
        st.session_state.mensaje = (
            f"Depósito realizado. Ahora tienes "
            f"${st.session_state.saldo:,} pesos en tu cuenta"
        )
        st.session_state.tipo_mensaje = "success"
    else:
        st.session_state.mensaje = "Ingrese una cantidad mayor que cero"
        st.session_state.tipo_mensaje = "error"


def retirar():
    cantidad = st.session_state.cantidad

    if cantidad <= 0:
        st.session_state.mensaje = "Ingrese una cantidad mayor que cero"
        st.session_state.tipo_mensaje = "error"

    elif cantidad <= st.session_state.saldo:
        st.session_state.saldo -= cantidad
        st.session_state.mensaje = (
            f"Retiro realizado. Ahora tienes "
            f"${st.session_state.saldo:,} pesos en tu cuenta"
        )
        st.session_state.tipo_mensaje = "success"

    else:
        st.session_state.mensaje = "No tienes suficiente dinero"
        st.session_state.tipo_mensaje = "error"


st.title("🏦 BANCO")
st.subheader("¿QUÉ QUIERES HACER?")

st.number_input("Ingrese la cantidad de pesos", min_value=0, step=1000, key="cantidad")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Consultar saldo", on_click=consultar, use_container_width=True)

with col2:
    st.button("Depositar", on_click=depositar, use_container_width=True)

with col3:
    st.button("Retirar", on_click=retirar, use_container_width=True)

if st.session_state.mensaje:
    tipo = st.session_state.tipo_mensaje

    if tipo == "success":
        st.success(st.session_state.mensaje)
    elif tipo == "error":
        st.error(st.session_state.mensaje)
    else:
        st.info(st.session_state.mensaje)

st.caption("Simulador educativo. No utiliza dinero real.")
