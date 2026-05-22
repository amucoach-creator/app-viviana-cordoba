export default function VivianaCordobaMentalHealthApp() {
  const services = [
    {
      title: 'Psicoterapia Individual',
      desc: 'Espacios terapéuticos profundos para comprender tu historia emocional y transformar patrones repetitivos.',
      icon: '🧠'
    },
    {
      title: 'Terapia de Pareja',
      desc: 'Reconstruyan la comunicación, la intimidad y el vínculo emocional desde una mirada profesional.',
      icon: '💞'
    },
    {
      title: 'Niños y Adolescentes',
      desc: 'Acompañamiento emocional especializado para infancia y adolescencia con enfoque humano y clínico.',
      icon: '🌱'
    },
    {
      title: 'Adultos',
      desc: 'Procesos terapéuticos para ansiedad, vacío emocional, crisis vitales y relaciones.',
      icon: '✨'
    }
  ]

  const resources = [
    {
      title: 'Ebook: Comprender el Autismo desde el Amor',
      type: 'Ebook'
    },
    {
      title: 'Guía emocional para migrantes colombianos',
      type: 'Guía'
    },
    {
      title: 'Masterclass: Relaciones que Sanan',
      type: 'Video'
    }
  ]

  const faqs = [
    {
      q: '¿Cómo funcionan las sesiones online?',
      a: 'Las sesiones se realizan por videollamada privada y segura desde cualquier país.'
    },
    {
      q: '¿Cuánto dura cada sesión?',
      a: 'Cada sesión tiene una duración aproximada de 50 minutos.'
    },
    {
      q: '¿Puedo reservar desde Estados Unidos o Europa?',
      a: 'Sí. La plataforma está diseñada para pacientes en Colombia y el exterior.'
    },
    {
      q: '¿Hay terapia para adolescentes?',
      a: 'Sí. Se ofrece acompañamiento especializado para adolescentes y sus familias.'
    }
  ]

  return (
    <div className="min-h-screen bg-white text-slate-800">
      {/* Hero */}
      <section className="relative overflow-hidden bg-gradient-to-br from-emerald-900 via-teal-800 to-slate-900 text-white">
        <div className="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_top_right,white,transparent_40%)]" />

        <div className="max-w-7xl mx-auto px-6 py-24 grid lg:grid-cols-2 gap-16 items-center relative z-10">
          <div>
            <div className="inline-flex items-center gap-2 bg-white/10 border border-white/20 rounded-full px-4 py-2 text-sm mb-6 backdrop-blur-sm">
              <span>●</span>
              Psicoterapia Premium Online
            </div>

            <h1 className="text-5xl lg:text-7xl font-bold leading-tight tracking-tight">
              Psicoterapia humana para volver a encontrarte contigo.
            </h1>

            <p className="mt-6 text-lg text-emerald-50 leading-relaxed max-w-xl">
              Agenda sesiones online con la Psicóloga Viviana Córdoba. Un espacio seguro para sanar relaciones, ansiedad, vacío emocional y procesos familiares desde una mirada clínica y profundamente humana.
            </p>

            <div className="mt-10 flex flex-wrap gap-4">
              <button className="bg-white text-emerald-900 px-6 py-4 rounded-2xl font-semibold shadow-2xl hover:scale-105 transition">
                Reservar Sesión
              </button>

              <button className="border border-white/30 bg-white/10 backdrop-blur-sm px-6 py-4 rounded-2xl font-semibold hover:bg-white/20 transition">
                Ver Servicios
              </button>
            </div>

            <div className="mt-10 flex items-center gap-8 text-sm text-emerald-100">
              <div>
                <p className="text-3xl font-bold">16+</p>
                <p>Años de experiencia</p>
              </div>

              <div>
                <p className="text-3xl font-bold">Online</p>
                <p>Atención mundial</p>
              </div>

              <div>
                <p className="text-3xl font-bold">Premium</p>
                <p>Atención personalizada</p>
              </div>
            </div>
          </div>

          <div className="relative">
            <div className="bg-white/10 border border-white/20 backdrop-blur-xl rounded-[32px] p-6 shadow-2xl">
              <div className="bg-white rounded-[28px] overflow-hidden shadow-xl">
                <div className="bg-emerald-900 px-6 py-4 text-white flex justify-between items-center">
                  <div>
                    <p className="font-semibold">Reserva tu sesión</p>
                    <p className="text-sm text-emerald-100">Agenda online en minutos</p>
                  </div>

                  <div className="w-12 h-12 rounded-full bg-emerald-600 flex items-center justify-center text-xl">
                    📅
                  </div>
                </div>

                <div className="p-6 space-y-4">
                  <input
                    placeholder="Nombre completo"
                    className="w-full border border-slate-200 rounded-xl px-4 py-4 outline-none focus:ring-2 focus:ring-emerald-500"
                  />

                  <input
                    placeholder="Correo electrónico"
                    className="w-full border border-slate-200 rounded-xl px-4 py-4 outline-none focus:ring-2 focus:ring-emerald-500"
                  />

                  <select className="w-full border border-slate-200 rounded-xl px-4 py-4 outline-none focus:ring-2 focus:ring-emerald-500">
                    <option>Selecciona un servicio</option>
                    <option>Psicoterapia Individual</option>
                    <option>Terapia de Pareja</option>
                    <option>Niños y Adolescentes</option>
                    <option>Adultos</option>
                  </select>

                  <input
                    type="date"
                    className="w-full border border-slate-200 rounded-xl px-4 py-4 outline-none focus:ring-2 focus:ring-emerald-500"
                  />

                  <button className="w-full bg-emerald-700 hover:bg-emerald-800 text-white py-4 rounded-xl font-semibold transition-all duration-300 shadow-lg">
                    Confirmar Reserva
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Services */}
      <section className="py-24 bg-slate-50">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center max-w-3xl mx-auto">
            <p className="text-emerald-700 font-semibold uppercase tracking-[0.2em]">
              Servicios
            </p>

            <h2 className="mt-4 text-4xl lg:text-5xl font-bold text-slate-900">
              Un acompañamiento terapéutico para cada etapa de la vida
            </h2>
          </div>

          <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-6 mt-16">
            {services.map((service, index) => (
              <div
                key={index}
                className="bg-white rounded-3xl p-8 shadow-lg hover:-translate-y-2 transition-all duration-300 border border-slate-100"
              >
                <div className="w-16 h-16 rounded-2xl bg-emerald-100 flex items-center justify-center text-3xl mb-6">
                  {service.icon}
                </div>

                <h3 className="text-2xl font-bold text-slate-900">
                  {service.title}
                </h3>

                <p className="mt-4 text-slate-600 leading-relaxed">
                  {service.desc}
                </p>

                <button className="mt-8 text-emerald-700 font-semibold hover:underline">
                  Agendar sesión →
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* AI Chat */}
      <section className="py-24 bg-gradient-to-br from-slate-900 via-teal-900 to-emerald-950 text-white">
        <div className="max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-16 items-center">
          <div>
            <p className="uppercase tracking-[0.25em] text-emerald-300 font-semibold">
              Asistente IA
            </p>

            <h2 className="mt-4 text-5xl font-bold leading-tight">
              Habla con un asistente emocional inteligente antes de agendar.
            </h2>

            <p className="mt-6 text-lg text-slate-300 leading-relaxed max-w-xl">
              Un chat IA diseñado para orientar a pacientes, responder dudas frecuentes y ayudar a encontrar el servicio terapéutico ideal.
            </p>

            <div className="mt-8 flex flex-wrap gap-3">
              <span className="bg-white/10 border border-white/10 px-4 py-2 rounded-full text-sm">
                Orientación emocional
              </span>

              <span className="bg-white/10 border border-white/10 px-4 py-2 rounded-full text-sm">
                Recomendación de servicios
              </span>

              <span className="bg-white/10 border border-white/10 px-4 py-2 rounded-full text-sm">
                Atención 24/7
              </span>
            </div>
          </div>

          <div className="bg-white rounded-[32px] p-6 text-slate-900 shadow-2xl">
            <div className="flex items-center gap-3 border-b pb-4">
              <div className="w-12 h-12 rounded-full bg-emerald-700 text-white flex items-center justify-center font-bold">
                IA
              </div>

              <div>
                <p className="font-semibold">Asistente Viviana IA</p>
                <p className="text-sm text-slate-500">En línea</p>
              </div>
            </div>

            <div className="space-y-4 mt-6">
              <div className="bg-slate-100 rounded-2xl p-4 max-w-sm">
                Hola 👋 ¿Qué tipo de apoyo emocional estás buscando hoy?
              </div>

              <div className="bg-emerald-700 text-white rounded-2xl p-4 max-w-sm ml-auto">
                He estado sintiendo ansiedad y mucho agotamiento emocional.
              </div>

              <div className="bg-slate-100 rounded-2xl p-4 max-w-md">
                Entiendo. La psicoterapia individual puede ayudarte a comprender lo que estás viviendo y recuperar estabilidad emocional.
              </div>
            </div>

            <div className="mt-6 flex gap-3">
              <input
                placeholder="Escribe tu mensaje..."
                className="flex-1 border rounded-xl px-4 py-3"
              />

              <button className="bg-emerald-700 text-white px-6 rounded-xl font-semibold">
                Enviar
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Resources */}
      <section className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col lg:flex-row justify-between gap-8 items-end">
            <div>
              <p className="uppercase tracking-[0.25em] text-emerald-700 font-semibold">
                Recursos Premium
              </p>

              <h2 className="mt-4 text-5xl font-bold text-slate-900 max-w-2xl">
                Ebooks, guías y videos para continuar tu proceso emocional.
              </h2>
            </div>

            <button className="bg-slate-900 text-white px-6 py-4 rounded-2xl font-semibold">
              Explorar Biblioteca
            </button>
          </div>

          <div className="grid md:grid-cols-3 gap-8 mt-16">
            {resources.map((item, index) => (
              <div
                key={index}
                className="rounded-[32px] overflow-hidden border border-slate-100 shadow-lg hover:-translate-y-2 transition"
              >
                <div className="h-56 bg-gradient-to-br from-emerald-700 to-teal-900 flex items-center justify-center text-7xl text-white">
                  📘
                </div>

                <div className="p-8">
                  <span className="text-sm bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full font-medium">
                    {item.type}
                  </span>

                  <h3 className="mt-5 text-2xl font-bold text-slate-900 leading-snug">
                    {item.title}
                  </h3>

                  <button className="mt-8 text-emerald-700 font-semibold hover:underline">
                    Ver recurso →
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Events */}
      <section className="py-24 bg-slate-50">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center max-w-3xl mx-auto">
            <p className="uppercase tracking-[0.25em] text-emerald-700 font-semibold">
              Eventos y Formación
            </p>

            <h2 className="mt-4 text-5xl font-bold text-slate-900">
              Cursos, talleres y masterclass con Viviana Córdoba
            </h2>
          </div>

          <div className="grid lg:grid-cols-2 gap-8 mt-16">
            <div className="bg-gradient-to-br from-emerald-800 to-teal-900 rounded-[36px] p-10 text-white shadow-2xl">
              <div className="inline-flex bg-white/10 border border-white/20 px-4 py-2 rounded-full text-sm mb-6">
                Próxima Masterclass
              </div>

              <h3 className="text-4xl font-bold leading-tight">
                Relaciones que Sanan
              </h3>

              <p className="mt-6 text-emerald-50 text-lg leading-relaxed">
                Aprende a identificar patrones emocionales, heridas afectivas y formas de construir vínculos más conscientes.
              </p>

              <div className="mt-8 flex items-center gap-6 text-sm">
                <div>
                  <p className="font-semibold">📅 Fecha</p>
                  <p>28 Mayo 2026</p>
                </div>

                <div>
                  <p className="font-semibold">🌎 Modalidad</p>
                  <p>Online en vivo</p>
                </div>
              </div>

              <button className="mt-10 bg-white text-emerald-900 px-6 py-4 rounded-2xl font-bold">
                Reservar Cupo
              </button>
            </div>

            <div className="bg-white rounded-[36px] p-10 border border-slate-100 shadow-lg">
              <h3 className="text-3xl font-bold text-slate-900">
                Próximos Eventos
              </h3>

              <div className="mt-8 space-y-5">
                {[
                  'Taller de autoestima y ansiedad',
                  'Curso emocional para padres',
                  'Masterclass sobre vínculos afectivos',
                  'Taller de inteligencia emocional'
                ].map((event, index) => (
                  <div
                    key={index}
                    className="flex items-center justify-between border rounded-2xl p-5 hover:border-emerald-500 transition"
                  >
                    <div>
                      <p className="font-semibold text-slate-900">{event}</p>
                      <p className="text-sm text-slate-500 mt-1">Online • Cupos limitados</p>
                    </div>

                    <button className="text-emerald-700 font-semibold">
                      Ver
                    </button>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-24 bg-white">
        <div className="max-w-5xl mx-auto px-6">
          <div className="text-center">
            <p className="uppercase tracking-[0.25em] text-emerald-700 font-semibold">
              Preguntas Frecuentes
            </p>

            <h2 className="mt-4 text-5xl font-bold text-slate-900">
              Resolvemos tus dudas
            </h2>
          </div>

          <div className="mt-16 space-y-5">
            {faqs.map((faq, index) => (
              <details
                key={index}
                className="border border-slate-200 rounded-2xl p-6 group"
              >
                <summary className="cursor-pointer list-none flex justify-between items-center text-xl font-semibold text-slate-900">
                  {faq.q}
                  <span className="group-open:rotate-45 transition">+</span>
                </summary>

                <p className="mt-5 text-slate-600 leading-relaxed">
                  {faq.a}
                </p>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* Footer CTA */}
      <section className="py-24 bg-gradient-to-r from-emerald-900 to-teal-900 text-white">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <h2 className="text-5xl font-bold leading-tight">
            Tu bienestar emocional merece atención profesional.
          </h2>

          <p className="mt-6 text-lg text-emerald-50 max-w-2xl mx-auto leading-relaxed">
            Agenda tu primera sesión online y comienza un proceso terapéutico profundo, humano y transformador.
          </p>

          <div className="mt-10 flex flex-wrap justify-center gap-4">
            <button className="bg-white text-emerald-900 px-8 py-4 rounded-2xl font-bold shadow-xl hover:scale-105 transition">
              Reservar Ahora
            </button>

            <button className="border border-white/20 bg-white/10 px-8 py-4 rounded-2xl font-semibold backdrop-blur-sm">
              Hablar con IA
            </button>
          </div>
        </div>
      </section>
    </div>
  )
}
