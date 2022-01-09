<template>
    <button class="botao" :class="estiloDoBotao" :type="tipo" @click="disparaAcao()">{{ rotulo }}</button>
</template>

<script>
export default {

    props: {
        tipo: {
            required: true,
            type: String
        },

        rotulo: {
            required: true,
            type: String
        },

        confirmacao: Boolean,
        estilo: String
    },

    methods: {
        disparaAcao() {
            if (this.confirmacao) {
                if (!confirm('Confirma exclusão?')) {
                    return;
                }
            }
            this.$emit('botaoAtivado');
        }
    },

    computed: {
        estiloDoBotao() {

            if (this.estilo == 'perigo') return 'botao-perigo';
            return 'botao-padrao';

        }
    }

}
</script>

<style lang="sass" scoped>

    @import './Botao.scss';

</style>