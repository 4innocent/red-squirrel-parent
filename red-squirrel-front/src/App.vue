<template>
  <top-bar></top-bar>
  <home class="container-home-app"></home>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import Home from './views/home/home-main.vue';
import TopBar from './components/top-bar/top-bar.vue';
@Options({
  components: {
    Home,
    TopBar,
  },
})
export default class App extends Vue {}
</script>

<style lang="less">
#app {
  position: relative;
  height: calc(100% - 3.6rem);
  display: flow-root;
  @media (max-width: 719px) {
    .can-hidden {
      display: none;
    }
    .can-show {
      display: block;
    }
    .can-show-flex {
      display: flex;
    }
  }
}
</style>
