import streamlit as st
import datetime

# Configuración básica de la página
st.set_page_config(page_title="Psicóloga Viviana Córdoba", page_icon="🌱", layout="centered")

# Estilos visuales de la marca (Verde y Azul Petróleo)
st.markdown("""
    <style>
        .stApp { background-color: #FFFFFF; color: #1A3A4B; }
        .stButton>button { background-color: #1A3A4B !important; color: white !important; border-radius: 20px !important; font-weight: bold; }
        .stButton>button:hover { background-color: #2D6A4F !important; }
        .card-servicio { background-color: #F4F6F4; padding: 20px; border-radius: 15px; border-left: 5px solid #2D6A4F; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Menú de navegación móvil
tab_inicio, tab_reserva, tab_chat, tab_recursos = st.tabs(["🏠 Inicio", "📅 Reservar", "🤖 Chat IA", "📚 Recursos"])

with tab_inicio:
    st.markdown("<h1 style='color: #2D6A4F; text-align:center;'>Psicóloga Viviana Córdoba</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Servicios psicoterapéuticos premium</p>", unsafe_allow_html=True)
    st.markdown("### 🌟 Áreas de Especialidad")
    st.markdown('<div class="card-servicio"><h4>🛋️ Individual y Parejas</h4><p>Espacios de sanación para adultos y relaciones.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card-servicio"><h4>🧸 Niños y Adolescentes</h4><p>Acompañamiento empático en etapas de desarrollo.</p></div>', unsafe_allow_html=True)

with tab_reserva:
    st.markdown("## 📅 Reserva tu Sesión")
    tipo = st.selectbox("Selecciona el servicio:", ["Individual", "Pareja", "Infantil", "Adolescentes"])
    fecha = st.date_input("Fecha:", min_value=datetime.date.today())
    hora = st.selectbox("Hora:", ["09:00 AM", "11:00 AM", "03:00 PM", "05:00 PM"])
    nombre = st.text_input("Tu Nombre")
    correo = st.text_input("Tu Correo")
    if st.button("Confirmar y Agendar"):
        if nombre and correo:
            st.success(f"¡Gracias {nombre}! Sesión de apoyo agendada para el {fecha} a las {hora}. Revisa tu correo.")
        else:
            st.warning("Por favor completa tus datos.")

with tab_chat:
    st.markdown("## 🤖 Asistente de Bienestar IA")
    st.caption("Espacio automatizado de orientación y desahogo 24/7. No reemplaza la terapia formal.")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hola, soy el asistente virtual de la Dra. Viviana. ¿Cómo te sientes hoy?"}]
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    if user_input := st.chat_input("Escribe aquí..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        respuesta = "Gracias por compartirlo. Validar lo que sientes es el primer paso. Te sugiero agendar una sesión en la pestaña 'Reservar' para que la Dra. Viviana Córdoba te brinde herramientas personalizadas."
        st.session_state.messages.append({"role": "assistant", "content": respuesta})
        st.chat_message("assistant").write(respuesta)

with tab_recursos:
    st.markdown("## 📚 Recursos y Guías")
    st.markdown("🔹 **Guía de Autoestima** (PDF) - Descargable en tu sesión.")
    st.markdown("🔹 **Manual de Crianza Respetuosa** - Disponible para pacientes.")
