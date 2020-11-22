<template>
  <a-layout class="container-layout--home">
    <a-layout-sider
      v-model:collapsed="collapsed"
      :trigger="null"
      class="can-hidden"
    >
      <a-menu theme="dark" mode="inline" v-model:selectedKeys="selectedKeys">
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
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0"> </a-layout-header>
      <a-layout-content
        :style="{
          margin: '24px 16px',
          padding: '24px',
          background: '#fff',
          minHeight: '280px',
        }"
      >
        <div style="height:2000px;"></div>
      </a-layout-content>
      <a-layout-footer style="text-align: center">
        Red Squirrel ©2020 Created by GKJ
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script lang="ts">
import {
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
  MenuUnfoldOutlined,
  MenuFoldOutlined,
} from '@ant-design/icons-vue';
import { Options, Vue } from 'vue-class-component';

@Options({
  components: {
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
    MenuUnfoldOutlined,
    MenuFoldOutlined,
  },
})
export default class Home extends Vue {
  private selectedKeys = ['1'];
  private collapsed = true;
}
</script>

<style lang="less" src="./home-main.less"></style>
