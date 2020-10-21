import Vue from 'vue'
import App from './App.vue'
// importing vuetify
import vuetify from './plugins/vuetify';
// import antdv
import './plugins/antdv';

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
