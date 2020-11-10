<template>
<top-bar></top-bar>
</template>

<script lang="ts">
import {
  Options,
  Vue
} from 'vue-class-component';
import TopBar from '@/components/top-bar/top-bar.vue';
@Options({
  components: {
    'top-bar': TopBar,
  },
})
export default class Home extends Vue {}
</script>
