<template>
  <div class="container mt-5 animate__animated animate__fadeInUp">
    <h1 class="text-center text-primary mb-4 animate__animated animate__zoomInDown">
      <i class="bi bi-robot me-3"></i> Pannello di Controllo Macchina <i class="bi bi-gear-wide-connected ms-3"></i>
    </h1>
    <p class="text-center text-secondary lead mb-5">
      Monitoraggio avanzato e in tempo reale dello stato del sistema industriale.
    </p>

    <div class="card main-card">
      <div class="card-header text-white text-center">
        <h3><i class="bi bi-bar-chart-fill me-2"></i> Dati Macchina #{{ machine.id }}</h3>
      </div>
      <div class="card-body">
        <div class="row g-4 text-center">
          <div class="col-md-6 animate__animated animate__fadeInLeft">
            <div class="p-3 border rounded">
              <i class="bi bi-power icon me-2 text-primary"></i>
              <span class="fw-bold">Stato:</span>
              <span class="machine-status ms-2" :class="{'text-success': isRunning, 'text-danger': !isRunning}">
                {{ machine.status }}
              </span>
            </div>
          </div>

          <div class="col-md-6 animate__animated animate__fadeInRight">
            <div class="p-3 border rounded">
              <i class="bi bi-clock icon me-2 text-secondary"></i>
              <span class="fw-bold">Ultimo Aggiornamento:</span>
              <span class="ms-2">{{ machine.lastUpdated }}</span>
            </div>
          </div>
        </div>

        <hr class="my-4" />

        <ul class="list-group list-group-flush">
          <li class="list-group-item data-list-item animate__animated animate__fadeInUp">
            <i class="bi bi-thermometer-half icon me-2 text-info"></i>
            <strong>Temperatura:</strong> <span class="float-end">{{ machine.temperature }} °C</span>
          </li>
          <li class="list-group-item data-list-item animate__animated animate__fadeInUp animate__delay-1s">
            <i class="bi bi-speedometer2 icon me-2 text-warning"></i>
            <strong>Pressione:</strong> <span class="float-end">{{ machine.pressure }} Bar</span>
          </li>
          <li class="list-group-item data-list-item animate__animated animate__fadeInUp animate__delay-2s">
            <i class="bi bi-lightning-charge icon me-2 text-danger"></i>
            <strong>Consumo Energia:</strong> <span class="float-end">{{ machine.energyConsumption }} kWh</span>
          </li>
        </ul>

        <div class="text-center mt-4">
          <button
            @click="fetchData"
            class="btn btn-primary btn-lg btn-update animate__animated"
            :class="{'animate__pulse': pulseButton}"
          >
            <i class="bi bi-arrow-repeat me-2"></i> Aggiorna Dati
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      machine: {
        id: 1,
        status: 'In funzione',
        temperature: 25.0,
        pressure: 5.2,
        energyConsumption: 125,
        lastUpdated: new Date().toLocaleTimeString(),
      },
      pulseButton: false,
    };
  },
  computed: {
    isRunning() {
      return this.machine.status === 'In funzione';
    },
  },
  methods: {
    fetchData() {
      console.log('Simulazione chiamata API...');

      setTimeout(() => {
        this.machine.status = Math.random() > 0.8 ? 'Manutenzione' : 'In funzione';
        this.machine.temperature = (Math.random() * (35 - 20) + 20).toFixed(1);
        this.machine.pressure = (Math.random() * (7.0 - 4.0) + 4.0).toFixed(1);
        this.machine.energyConsumption = Math.floor(Math.random() * (200 - 100) + 100);
        this.machine.lastUpdated = new Date().toLocaleTimeString();

        this.pulseButton = true;
        setTimeout(() => (this.pulseButton = false), 1000);
      }, 500);
    },
  },
};
</script>

<style scoped>
body {
  background-color: #f0f2f5;
  color: #333;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.container {
  max-width: 960px;
}
.main-card {
  border-radius: 1.5rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
  animation-duration: 1s;
}
.card-header {
  background-color: #004d99 !important;
  border-top-left-radius: 1.5rem !important;
  border-top-right-radius: 1.5rem !important;
}
.machine-status {
  font-size: 1.5rem;
  font-weight: bold;
}
.btn-update {
  transition: transform 0.3s ease-in-out;
}
.btn-update:hover {
  transform: scale(1.05);
}
.data-list-item {
  border-bottom: 1px solid #eee;
  padding: 10px 0;
}
.data-list-item:last-child {
  border-bottom: none;
}
.icon {
  font-size: 1.2rem;
  width: 2rem;
}
</style>