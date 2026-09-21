// URL de Render 
const API_URL = "https://backend-equipo4-5pb1.onrender.com";

// Función para verificar que el backend responda
async function checkBackendStatus() {
    const statusLabel = document.getElementById("api-status");
    const logBox = document.getElementById("response-log");

    try {
        const response = await fetch(`${API_URL}/`);
        const data = await response.json();
        statusLabel.innerText = "ONLINE ✅";
        statusLabel.style.color = "green";
        logBox.innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        statusLabel.innerText = "OFFLINE / ERROR ❌";
        statusLabel.style.color = "red";
        logBox.innerText = "Error de conexión con el backend.";
    }
}

// Función para llamar al endpoint que fuerza el error capturado por Sentry
async function triggerError() {
    const logBox = document.getElementById("response-log");
    logBox.innerText = "Enviando petición a /sentry-debug...";

    try {
        const response = await fetch(`${API_URL}/sentry-debug`);
        if (!response.ok) {
            logBox.innerText = `HTTP ${response.status} Internal Server Error.\n¡Error capturado y enviado a Sentry!`;
        }
    } catch (error) {
        logBox.innerText = "Petición ejecutada. Revisa el Dashboard de Sentry.";
    }
}

// Ejecutar verificación al cargar la página
checkBackendStatus();