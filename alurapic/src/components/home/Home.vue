<template>
  <div>
    <h1 class="centralizado">{{ titulo }}</h1>

    <p v-show="mensagem" class="centralizado">{{ mensagem }}</p>

    <input type="search" class="filtro" placeholder="Filtre por parte do título" @input="filtro = $event.target.value" >

    {{ filtro }}

    <ul class="lista-fotos">
      <li class="lista-fotos-item" v-for="foto of fotosFiltradas" :key="foto._id">
        <meu-painel :titulo="foto.titulo">
            <imagem-responsiva v-meu-transform:scale.animar="1.2" :url="foto.url" :titulo="foto.titulo"/>
            <router-link :to="{ name: 'alteracao', params: { id: foto._id }}">
                <meu-botao tipo="button" rotulo="Alterar"/>
            </router-link>
            <meu-botao tipo="button" rotulo="Remover" @botaoAtivado="remove(foto)" :confirmacao="true" estilo="perigo"/>
        </meu-painel>
      </li>
    </ul>
  </div>
</template>

<script>

import Painel from '../shared/painel/Painel';
import ImagemResponsiva from '../shared/imagem-responsiva/ImagemResponsiva';
import Botao from '../shared/botao/Botao';

import Transform from '../../directives/Transform';

import FotoService from '../../domain/foto/FotoService';

export default {
  components: {
    'meu-painel': Painel,
    'imagem-responsiva': ImagemResponsiva,
    'meu-botao': Botao
  },

  directives: {
      'meu-transform': Transform
  },

  data() {
    return {
      titulo: "Alurapic",
      fotos: [],
      filtro: '',
      mensagem: ''
    };
  },

  computed: {
    fotosFiltradas() {
      if (this.filtro) {
        let exp = new RegExp(this.filtro.trim(), 'i');
        return this.fotos.filter(foto => exp.test(foto.titulo));
      } else {
        return this.fotos;
      }
    }
  },

  methods: {

      remove(foto) {
        this.service
            .apaga(foto._id)
            .then(
            () => {
                let indice = this.fotos.indexOf(foto);
                this.fotos.splice(indice, 1);
                this.mensagem = 'Foto removida com sucesso'
            }, 
            err => this.mensagem = err.message)
     }

  },

  created() {

      this.service = new FotoService(this.$resource);

      this.service
            .lista()
            .then(fotos => this.fotos = fotos, err => this.mensagem=err.message);
  }
};
</script>

<style>

  .centralizado {
    text-align: center;
  }

  .lista-fotos {
    list-style: none;
  }

  .lista-fotos .lista-fotos-item {
    display: inline-block;
  }

  .filtro {
    display: block;
    width: 100%;
  }
</style>