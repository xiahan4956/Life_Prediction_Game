import { createRouter, createWebHistory } from 'vue-router';
import StartPage from './components/StartPage.vue';
import ChooseStyle from './components/ChooseStyle.vue';
import SelectAttribute from './components/SelectAttribute.vue';
import SelectFeatures from './components/SelectFeatures.vue';
import PredictLife from './components/PredictLife.vue';

const routes = [
  {
    path: '/',
    name: 'StartPage',
    component: StartPage,  
  },
  {
    path: '/choose_style',
    name: 'ChooseStyle',
    component: ChooseStyle,  
  },
  {
    path: '/select_attribute/:feature',
    name: 'SelectAttribute',
    component: SelectAttribute,
  },
  {
    path: '/select_features',
    name: 'SelectFeatures',
    component: SelectFeatures,
  },
  {
    path: '/predict_life',
    name: 'PredictLife',
    component: PredictLife,
  },


];


const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
