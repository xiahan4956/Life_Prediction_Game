import { createApp } from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';

const app = createApp(App);

axios.defaults.withCredentials = true;
app.config.globalProperties.$http = axios;  // 将 Axios 绑定到 Vue 实例,绑定到了原型的属性

app.use(router);  // 使用 Vue Router
app.mount('#app');  // 挂载到 DOM
this.$http.get('http://qq4956.pythonanywhere.com/api/predict', { withCredentials: true });
