<script>
// Importa il tuo componente
import MachinePanel from './components/MachinePanel.vue';

export default {
  name: 'App',
  components: {
    MachinePanel // Registra il componente
  }
}
</script>
<template>
  <div id="app">
    <MachinePanel />
  </div>
</template>