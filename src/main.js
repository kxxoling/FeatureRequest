import Vue from 'vue';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import VueI18N from 'vue-i18n';

import App from 'src/App';
import urls from 'src/urls';
import locales from 'src/locales';

Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(VueI18N, {
  lang: 'en',
  locales,
});

const router = new VueRouter();
router.map(urls);
router.start(App, 'body');
