import Vue from 'vue'
import App from './App.vue'

import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-datepicker";
import "bootstrap-datepicker/dist/css/bootstrap-datepicker.min.css";
import "font-awesome/css/font-awesome.min.css";


Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
