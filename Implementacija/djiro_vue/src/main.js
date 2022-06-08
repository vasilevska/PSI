import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: "login" });
    } else if (to.matched.some((record) => record.meta.restrictedToUser)) {
      if (store.state.id == to.params.id) {
        next();
      }
      else {
        next({ name: "home" });
      }
    }
  } else {
    next();
  }
});

createApp(App).use(store).use(router, axios).mount("#app");
