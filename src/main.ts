import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import VueGtag from 'vue-gtag'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faMusic } from '@fortawesome/free-solid-svg-icons'
import { faBandcamp, faSoundcloud, faSpotify } from '@fortawesome/free-brands-svg-icons'

import App from './App.vue'
import router from './router'

library.add(faMusic, faBandcamp, faSoundcloud, faSpotify)

const app = createApp(App)

app.use(VueGtag, {
  config: {
    id: 'G-C60SDCE5GF'
  }
})
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(createHead())
app.use(createPinia())
app.use(router)

app.mount('#app')
