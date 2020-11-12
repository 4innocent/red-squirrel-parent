<template>
  <div class="topBar-div--container">
    <div class="topBar-div--left">
      <div class="slideBtn-div--left can-show">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          role="img"
          viewBox="0 0 448 512"
        >
          <path
            fill="currentColor"
            d="M436 124H12c-6.627 0-12-5.373-12-12V80c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12zm0 160H12c-6.627 0-12-5.373-12-12v-32c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12zm0 160H12c-6.627 0-12-5.373-12-12v-32c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12z"
          ></path>
        </svg>
      </div>
      <img class="logo-img--left" src="@/assets/logo.png" />
    </div>
    <div class="topBar-div--right">
      <div class="can-hidden">
        <a-auto-complete v-model:value="value" :options="options">
          <a-input>
            <template #suffix>
              <search-outlined class="certain-category-icon" />
            </template>
          </a-input>
        </a-auto-complete>
      </div>
      <div class="can-show">
        <search-outlined class="certain-category-icon" />
      </div>
      <a-button type="primary" class="login-btn--topBar">登录</a-button>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Options } from 'vue-class-component';
export default class TopBar extends Vue {
  private value = '';
  private options = [
    {
      value: '1',
    },
    {
      value: '2',
    },
    {
      value: '3',
    },
  ];
}
</script>

<style lang="less" src="./top-bar.less"></style>
