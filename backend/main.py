import os
import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Lectura de variables de entorno desde PaaS (Render)
SENTRY_DSN = os.getenv("SENTRY_DSN")

# 2. Inicialización de Sentry SDK si la variable DSN está presente
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
        environment=os.getenv("ENVIRONMENT", "production")
    )

app = FastAPI(
    title="API Punto Tecno - Equipo 9",
    version="1.0.0"
)

# 3. Configuración de CORS para permitir peticiones desde el Frontend en Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción permite conectar con Netlify
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz
@app.get("/")
def read_root():
    return {
        "status": "online",
        "equipo": "Equipo N° 9",
        "message": "Backend FastAPI desplegado exitosamente con Sentry"
    }

# Endpoint obligatorio para probar Sentry en la exposición en vivo
@app.get("/sentry-debug")
def trigger_error():
    # Forzamos un error no controlado de división por cero
    division_by_zero = 1 / 0
    return division_by_zero