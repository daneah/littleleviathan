import Vue from 'vue'
import VueAnalytics from 'vue-analytics'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faMusic } from '@fortawesome/free-solid-svg-icons'
import {
  faBandcamp,
  faSoundcloud,
  faSpotify,
} from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import App from '@/App'
import router from '@/router'
import store from '@/store'
import '@/registerServiceWorker'

// FontAwesome
library.add(faBandcamp, faMusic, faSoundcloud, faSpotify)
Vue.component('FontAwesome', FontAwesomeIcon)

// Google Analytics
Vue.use(VueAnalytics, {
  id: 'UA-47967013-1',
  router,
  debug: {
    enabled: process.env.NODE_ENV !== 'production',
    sendHitTask: process.env.NODE_ENV === 'production',
  },
})

// Main setup
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
