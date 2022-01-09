import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';
import { routes } from './routes';
import './directives/Transform';
import VeeValidate from 'vee-validate'; // quando o caminho é informado sem usar o '.', o arquivo é procurado dentro da pasta node_modules
import msg from './pt_BR'; // quando o caminho é informado usando ./ ou .//, o arquivo é procurado dentro da pasta src do projeto
import 'bootstrap/dist/css/bootstrap.css';

Vue.use(VueResource);
Vue.http.options.root = 'http://localhost:3000';
Vue.use(VueRouter);

const router = new VueRouter({
    routes: routes,
    mode: "history"
})

Vue.use(VeeValidate, {
  locale: 'pt_BR',
  dictionary: {
    pt_BR: {
      messages: msg
    }
  }
});

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
})
