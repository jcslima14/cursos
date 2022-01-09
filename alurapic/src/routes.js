// import Cadastro from './components/cadastro/Cadastro.vue';
const Cadastro = () => System.import('./components/cadastro/Cadastro.vue').then(m => m.default);
import Home from './components/home/Home.vue';

export const routes = [
    { path: '', name: 'home', component: Home, titulo: 'Home' },
    { path: '/cadastro', name: 'cadastro', component: Cadastro, titulo: 'Cadastro' },
    { path: '/cadastro/:id', name: 'alteracao', component: Cadastro },
    { path: '*', component: Home }
];