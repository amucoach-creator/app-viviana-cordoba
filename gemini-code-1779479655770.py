import streamlit as st
import datetime

# --- CONFIGURACIÓN DE LA PÁGINA Y ESTILOS PREMIUM (Verde, Azul Petróleo, Blanco) ---
st.set_page_config(page_title="Psicóloga Viviana Córdoba - Premium App", page_icon="🌱", layout="centered")

st.markdown("""
    <style>
        /* Paleta de Colores y Estilos Globales */
        :root {
            --verde-principal: #2D6A4F;
            --azul-petroleo: #1A3A4B;
            --blanco: #FFFFFF;
            --gris-claro: #F4F6F4;
        }
        
        .stApp {
            background-color: var(--blanco);
            color: var(--azul-petroleo);
        }
        
        /* Botones Premium */
        .stButton>button {
            background-color: #1A3A4B !important; /* Azul Petróleo */
            color: white !important;
            border-radius: 20px !important;
            border: none !important;
            padding: 10px 24px !important;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #2D6A4F !important; /* Verde */
            transform: translateY(-2px);
        }
        
        /* Tarjetas y Contenedores */
        .card-servicio {
            background-color: #F4F6F4;
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #2D6A4F;
            margin-bottom: 15px;
        }
        
        h1, h2, h3 {
            color: #1A3A4B !important;
        }
        
        .header-app {
            text-align: center;
            padding: 20px;
            background-color: #2D6A4F;
            color: white !important;
            border-radius: 0px 0px 25px 25px;
            margin-bottom: 25px;
        }
        .header-app h1 { color: white !important; }
    </style>
""", unsafe_index=True)

# --- NAVEGACIÓN INFERIOR (Tabs estilo App Móvil) ---
tab_inicio, tab_reserva, tab_chat, tab_recursos, tab_faq = st.tabs([
    "🏠 Inicio", "📅 Reservar", "🤖 Chat IA", "📚 Recursos", "❓ FAQ"
])

# ==========================================
# 1. PESTAÑA: INICIO (Home & Conversión)
# ==========================================
with tab_inicio:
    st.markdown("""
        <div class="header-app">
            <h1>Psicóloga Viviana Córdoba</h1>
            <p>Tu espacio seguro para sanar, crecer y evolucionar</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🌟 Nuestros Servicios Especializados")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card-servicio"><h4>🛋️ Psicoterapia Individual</h4><p>Encuentra tu equilibrio emocional y herramientas para el día a día.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-servicio"><h4>🧸 Niños y Adolescentes</h4><p>Acompañamiento empático en las etapas más cruciales del desarrollo.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card-servicio"><h4>💞 Terapia de Pareja</h4><p>Reconecta, sana heridas y mejora la comunicación asertiva.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-servicio"><h4>🧠 Adultos</h4><p>Especialidad en ansiedad, depresión, duelo y crecimiento personal.</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📅 Próximos Eventos y Masterclasses")
    
    col_ev1, col_ev2 = st.columns(2)
    with col_ev1:
        st.image("https://images.unsplash.com/photo-1515187029135-18ee286d815b?auto=format&fit=crop&q=80&w=500", caption="Masterclass: Gestión de Ansiedad")
        st.write("**Fecha:** 15 de Junio | **Modalidad:** Online en Vivo")
        if st.button("Inscribirme a Masterclass", key="btn_ev1"):
            st.success("¡Cupo reservado! Recibirás el acceso a tu correo.")
            
    with col_ev2:
        st.image("https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?auto=format&fit=crop&q=80&w=500", caption="Curso: Crianza Respetuosa y Consciente")
        st.write("**Fecha:** 5 de Julio | **Duración:** 4 Semanas")
        if st.button("Ver Detalles del Curso", key="btn_ev2"):
            st.info("Redirigiendo al temario premium...")

# ==========================================
# 2. PESTAÑA: RESERVA EN LÍNEA (Conversión Directa)
# ==========================================
with tab_reserva:
    st.markdown("## 📅 Reserva tu Sesión de Psicoterapia")
    st.write("Selecciona el tipo de terapia, la fecha y la hora que mejor se adapten a ti. El proceso toma menos de 2 minutos.")
    
    tipo_terapia = st.selectbox(
        "¿Qué tipo de apoyo necesitas hoy?",
        ["Terapia Individual (Adultos)", "Terapia de Pareja", "Psicoterapia para Adolescentes", "Psicoterapia Infantil"]
    )
    
    col_fecha, col_hora = st.columns(2)
    with col_fecha:
        fecha = st.date_input("Selecciona el día:", min_value=datetime.date.today())
    with col_hora:
        hora = st.selectbox("Selecciona la hora disponible:", ["08:00 AM", "10:00 AM", "02:00 PM", "04:00 PM", "06:00 PM"])
        
    st.markdown("### Detalle del Pago (Pasarela Premium)")
    st.write("**Inversión:** $70 USD por sesión de 50 minutos.")
    
    nombre = st.text_input("Nombre Completo")
    correo = st.text_input("Correo Electrónico")
    
    if st.button("Proceder al Pago Seguro y Confirmar Reserva"):
        if nombre and correo:
            st.success(f"¡Felicidades {nombre}! Tu sesión de **{tipo_terapia}** ha sido reservada para el **{fecha} a las {hora}**. Te hemos enviado los datos de acceso y el link de pago a *{correo}*.")
        else:
            st.error("Por favor, completa tu nombre y correo para agendar.")

# ==========================================
# 3. PESTAÑA: CHAT IA (Soporte y Contención)
# ==========================================
with tab_chat:
    st.markdown("## 🤖 Asistente de Bienestar IA")
    st.caption("Un espacio de desahogo y orientación automatizado 24/7 basado en el enfoque de la Psicóloga Viviana Córdoba. *Nota: No reemplaza a la terapia.*")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hola, soy tu acompañante virtual de bienestar. ¿Cómo te sientes hoy? Estoy aquí para escucharte y darte algunas herramientas iniciales."}
        ]
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
        
    if user_input := st.chat_input("Escribe cómo te sientes (ej. Me siento muy ansioso hoy)..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        
        # Lógica de respuesta simulada con enfoque clínico empático
        input_lower = user_input.lower()
        if "ansiedad" in input_lower or "ansioso" in input_lower or "asustado" in input_lower:
            respuesta_ia = "Lamento que te sientas así. La ansiedad es una señal de que tu cuerpo intenta protegerte, pero estás a salvo aquí. Vamos a hacer una pausa: Inhala profundamente en 4 tiempos, retén el aire por 4 tiempos y exhala despacio en 4 tiempos. ¿Te gustaría que agendemos una cita con la Dra. Viviana para trabajar esto a fondo?"
        elif "triste" in input_lower or "deprimido" in input_lower or "llorar" in input_lower:
            respuesta_ia = "Siento mucho que estés pasando por este momento gris. Permítete sentir la tristeza, no tiene nada de malo. Recuerda que no tienes que cargar con esto a solas. La Dra. Viviana Córdoba tiene espacios disponibles esta semana en la pestaña 'Reservar' si deseas un espacio seguro para hablar."
        else:
            respuesta_ia = "Gracias por compartir esto conmigo. Validar tus emociones es el primer paso para sanar. Te sugiero revisar nuestra sección de Recursos para encontrar guías gratuitas, o agendar una sesión personalizada con la Dra. Viviana para profundizar."
            
        st.session_state.messages.append({"role": "assistant", "content": respuesta_ia})
        st.chat_message("assistant").write(respuesta_ia)

# ==========================================
# 4. PESTAÑA: RECURSOS (Ebooks, Videos y Guías)
# ==========================================
with tab_recursos:
    st.markdown("## 📚 Biblioteca de Bienestar")
    st.write("Recursos exclusivos creados por la Psicóloga Viviana Córdoba para tu crecimiento autoasistido.")
    
    tipo_recurso = st.radio("Filtrar por tipo:", ["Todos", "Ebooks y Guías", "Videos"], horizontal=True)
    
    if tipo_recurso in ["Todos", "Ebooks y Guías"]:
        st.markdown("### 📄 Ebooks y Guías Descargables")
        col_eb1, col_eb2 = st.columns(2)
        with col_eb1:
            st.markdown("""
                <div style='background-color:#F4F6F4; padding:15px; border-radius:10px;'>
                    <h5>📘 Guía de Autoestima para Adultos</h5>
                    <p>10 ejercicios prácticos diarios.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Descargar PDF (Gratis)", key="pdf1"):
                st.toast("Descargando: Guia_Autoestima_VivianaCordoba.pdf")
        with col_eb2:
            st.markdown("""
                <div style='background-color:#F4F6F4; padding:15px; border-radius:10px;'>
                    <h5>📙 Manual de Gestión Emocional en Niños</h5>
                    <p>Para padres y cuidadores.</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Descargar PDF (Gratis)", key="pdf2"):
                st.toast("Descargando: Manual_Crianza_VivianaCordoba.pdf")

    if tipo_recurso in ["Todos", "Videos"]:
        st.markdown("### 🎥 Cápsulas de Video")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Reemplazar con el link real de YouTube/Vimeo de Viviana
        st.caption("Video destacado: Cómo poner límites sanos en la pareja sin sentir culpa.")

# ==========================================
# 5. PESTAÑA: FAQ (Preguntas Frecuentes)
# ==========================================
with tab_faq:
    st.markdown("## ❓ Preguntas Frecuentes")
    
    with st.expander("¿Cómo son las sesiones con la Psicóloga Viviana Córdoba?"):
        st.write("Las sesiones duran 50 minutos y se realizan de manera online a través de videollamada cifrada de alta seguridad. El enfoque es empático, basado en evidencia y personalizado según tu motivo de consulta.")
        
    with st.expander("¿Tienen terapia para niños y adolescentes?"):
        st.write("Sí. Contamos con dinámicas lúdicas para niños y un enfoque de confianza y cero juzgamiento para los adolescentes, involucrando activamente a los padres en sesiones de guía parental periódicas.")
        
    with st.expander("¿Cuál es la política de cancelación?"):
        st.write("Puedes reprogramar o cancelar tu cita con un mínimo de 24 horas de anticipación directamente desde la app o escribiendo a nuestro soporte sin costo adicional.")

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: grey;'>© 2026 Psicóloga Viviana Córdoba. Creado con fines de alta conversión y salud mental premium.</p>", unsafe_allow_html=True)