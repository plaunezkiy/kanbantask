// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import GSignInButton from 'vue-google-signin-button'
import App from './app';

Vue.config.productionTip = false

Vue.use(GSignInButton)

/* eslint-disable no-new */
var vm = new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
});
