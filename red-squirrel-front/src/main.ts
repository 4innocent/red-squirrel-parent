import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import { Button, AutoComplete, Input } from 'ant-design-vue';
import { SearchOutlined } from '@ant-design/icons-vue';

const app = createApp(App);
app
  .use(Button)
  .use(AutoComplete)
  .use(Input);
app.component('SearchOutlined', SearchOutlined);
app.use(store).use(router);
app.mount('#app');
