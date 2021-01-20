<template>
  <div class="topBar-div--container">
    <div class="topBar-div--left">
      <div
        class="menuBtn-div--left can-show-flex"
        @click="showVerticalMenu = !showVerticalMenu"
      >
        <span
          :class="[
            'menuBtn-span--left',
            showVerticalMenu ? 'menuBtn-sapn-change' : '',
          ]"
          ref="verticalMenu"
        ></span>
      </div>
      <!-- <img class="logo-img--left" src="@/assets/logo.png" /> -->
      <transition name="fade">
        <a-menu
          theme="dark"
          mode="vertical"
          v-show="showVerticalMenu"
          class="menuContent-div--left"
        >
          <a-menu-item key="1">
            <user-outlined />
            <span>主页</span>
          </a-menu-item>
          <a-menu-item key="2">
            <video-camera-outlined />
            <span>工具</span>
          </a-menu-item>
          <a-menu-item key="3">
            <upload-outlined />
            <span>配置</span>
          </a-menu-item>
        </a-menu>
      </transition>
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
import {
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
  MenuUnfoldOutlined,
  MenuFoldOutlined,
} from '@ant-design/icons-vue';
import { Vue, Options } from 'vue-class-component';
@Options({
  components: {
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
    MenuUnfoldOutlined,
    MenuFoldOutlined,
  },
})
export default class TopBar extends Vue {
  private showVerticalMenu = false;
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
