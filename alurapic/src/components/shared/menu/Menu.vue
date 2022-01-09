<template>
  <nav>
    <ul>
      <li v-for="rota of rotasFiltradas">
        <router-link :to="rota.path ? rota.path : '/'">{{ rota.titulo }}</router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {

    props: { 
        rotas: {
            type: Array,
            required: true
        } 
    },

    computed: {
        rotasFiltradas() {
            return this.rotas.filter(rota => rota.titulo);
        }
    }

};
</script>

<style scoped>
</style>