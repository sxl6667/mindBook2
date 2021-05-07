<template>
  <div class="container clearfix">
    <header>
      <Click class="fl click"></Click>
    </header>
    <aside class="fl">
      <!-- <div style="margin: 0 auto;">
        <el-upload
          class="avatar-uploader"
          action="https://jsonplaceholder.typicode.com/posts/"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload">
          <img v-if="imageUrl" :src="imageUrl" class="avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </div> -->
      <div class="SideBar">
        <el-menu
          :default-active="$route.path"
          :collapse="isCollapse"
          router
          overflow-y:
          scroll
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose">
          <el-menu-item index="/blog/StudyPlan">
            <i class="fa fa-map-o" aria-hidden="true"></i>
            <span slot="title">学习计划</span>
          </el-menu-item>
          <el-menu-item index="/blog/Idea">
            <i class="fa fa-lightbulb-o" aria-hidden="true"></i>
            <span slot="title">想法</span>
          </el-menu-item>
          <el-menu-item index="/blog/Navigation">
            <i class="fa fa-paper-plane-o" aria-hidden="true"></i>
            <span slot="title">导航</span>
          </el-menu-item>
          <el-menu-item index="/blog/Case">
            <i class="fa fa-newspaper-o" aria-hidden="true"></i>
            <span slot="title">案例</span>
          </el-menu-item>
          <el-menu-item index="/blog/Photo">
            <i class="fa fa-picture-o" aria-hidden="true"></i>
            <span slot="title">相册</span>
          </el-menu-item>
          <el-menu-item index="/blog/StudyMaterials">
            <i class="fa fa-university" aria-hidden="true"></i >
            <span slot="title">学习资源</span>
          </el-menu-item>
          <el-menu-item index="/blog/Api">
            <i class="fa fa-share-alt-square" aria-hidden="true"></i>
            <span slot="title">API</span>
          </el-menu-item>
        </el-menu>
      </div>
    </aside>
    <main class="fr"><router-view></router-view></main>
    <footer class="fr"></footer>
  </div>
</template>
<script>
import '../lib/font-awesome/css/font-awesome.min.css'
import Click from "../components/Click";
import '../common/font.css'
export default {
  name: "Mystudyplan",
  components: {
    Click,
  },
  data() {
    return {
      imageUrl: '',
      windowWidth: document.documentElement.clientWidth, //实时屏幕宽度
      isCollapse:'',
    };
  },
  created(){
    if(this.windowWidth<=850){
      this.isCollapse = true
    }
    if(this.windowWidth >850){
      this.isCollapse = false
    }
  },
  mounted(){
    let that = this;
    window.onresize = () => {
    return (() => {
    window.fullHeight = document.documentElement.clientHeight;
    window.fullWidth = document.documentElement.clientWidth;
    that.windowWidth = window.fullWidth; // 宽
    })()
    };
  },
  methods:{
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
        return isJPG && isLt2M;
      }
  },
  watch:{
    windowWidth(newName, oldName){
      console.log(this.windowWidth)
      if(this.windowWidth<=850){
        this.isCollapse = true
      }
      if(this.windowWidth >850){
        this.isCollapse = false
      }
    }
  }
};
</script>
<style lang="less" scoped>
.container {
  // min-height: 100%;
//   height: 1000px;
  background: rgb(216, 17, 133);
  position: relative;
  header {
    height: 180px;
    width: 100%;
    background: rgb(119, 78, 78);
    position: fixed;
    .click{
      position: absolute;
      left: 18%;
      top: 50%;
      transform: translateX(52%);
    }
  }
  aside{
    position: fixed;
    height: 100%;
    width: 15%;
    z-index: 10;
    background: white;
  }
  aside .SideBar{
    position: fixed;
    top: 180px;
    height: 100%;
    width: 15%;
    background: white;
    font-family: "stx";
    z-index: 10;
    letter-spacing:10px; //字体间隔
  }
  .el-menu{
    display: block;
  }
  // .avatar-uploader{
  //   border: 1px dashed pink;
  //   border-radius: 50px;
  //   width: 100px;
  //   height: 100px;
  // }
  // .avatar-uploader .el-upload {
  //   cursor: pointer;
  //   border: 1px dashed pink;
  //   border-radius: 50px;
  //   position: relative;
  //   overflow: hidden;
  // }
  // .avatar-uploader .el-upload:hover {
  //   border-color: #409EFF;
  // }
  // .avatar-uploader-icon {
  //   font-size: 28px;
  //   color: #8c939d;
  //   width: 100px;
  //   height: 100px;
  //   line-height: 100px;
  //   text-align: center;
  // }
  // .avatar {
  //   width: 100px;
  //   height: 100px;
  //   border-radius: 50px;
  //   display: block;
  // }
  // .fa{
  //   border: 0;
  //   position: relative;
  // }
  .el-menu-vertical-demo{
    height: 760px;
    width: 100%;
    min-width: 64px;
  }
  main {
    margin-top: 180px;
    width: 85%;
    min-width: 326px;
    background: rgb(171, 171, 230);
    height: 620px;
  }
  footer {
    height: 100px;
    width: 85%;
    background: rgb(56, 56, 92);
  }
}
</style>