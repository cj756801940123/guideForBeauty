<template>
  <div style="margin: 0; padding: 0">
    <el-menu
      :default-active="activeIndex"
      class="el-menu"
      mode="horizontal"
      background-color="#545c64"
      active-text-color="#fff"
      active-backgroud-color="#545c64"
      text-color="#fff">
      <el-menu-item class="el-menu-item" index="/" @click="getIndex()">美妆商品导购系统</el-menu-item>
      <el-menu-item class="el-menu-item" index="focus" @click="getFocus(username)">我的降价通知商品</el-menu-item>
      <el-button class="menu-btn" type="text" id="register" @click="dialogRegisterVisible=true" v-if="isLogin">{{ btnRegister }}
      </el-button>
      <el-button class="menu-btn" type="text" id="login" @click="dialogLoginVisible=true" v-if="isLogin">{{ btnLogin }}
      </el-button>

      <el-button class="menu-btn" type="text" id="logout" @click="dialogLogoutVisible=true" v-if="isLogout">{{ btnLogout }}
      </el-button>
      <el-button class="menu-btn" type="text" id="name">{{ btnName }}
      </el-button>
    </el-menu>

    <!--登录 对话框-->
    <el-dialog
      title="登录"
      :visible.sync="dialogLoginVisible"
      width="500px"
      :before-close="handleLoginCansel">
      <el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="90px">
        <el-form-item label="账号" prop="username">
          <el-input type="text" v-model="loginForm.username" placeholder="手机号码..."></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" placeholder="密码..."></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleLoginCansel">取 消</el-button>
        <el-button type="primary" @click="handleLoginSubmit">确 定</el-button>
      </span>
    </el-dialog>

    <!--注册 对话框-->
    <el-dialog
      title="注册"
      :visible.sync="dialogRegisterVisible"
      width="500px"
      :before-close="handleRegisterCansel">
      <el-form :model="loginForm" :rules="rules" ref="loginForm" label-width="90px">
        <el-form-item label="账号" prop="username">
          <el-input v-model="loginForm.username" placeholder="手机号码..."></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="name">
          <el-input v-model="loginForm.name" placeholder="昵称..."></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" placeholder="密码..."></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="loginForm.email" placeholder="邮箱..."></el-input>
        </el-form-item>

      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleRegisterCansel">取 消</el-button>
        <el-button type="primary" @click="handleRegisterSubmit">确 定</el-button>
      </span>
    </el-dialog>

    <!--退出 对话框-->
    <el-dialog
      title="退出"
      :visible.sync="dialogLogoutVisible"
      width="500px"
      :before-close="handleLogoutCansel">
      <p>您是否确定退出登录？</p>

      <span slot="footer" class="dialog-footer">
        <el-button @click="handleLogoutCansel">取 消</el-button>
        <el-button type="primary" @click="handleLogoutSubmit">确 定</el-button>
      </span>
    </el-dialog>
  </div>


</template>

<script>
  import ElButton from "../../../../node_modules/element-ui/packages/button/src/button";
  import bus from '../../../assets/eventBus'
  export default {
    components: {ElButton},
    props: ["actives"],
    data () {
      return {
        mockUserNo: '', // 假的用户账号，用于模拟 传给Contents组件来对接“增-降价通知”
        username: '',
        usernameTmp:'',  // 辅助
        name: '',
        dialogLoginVisible: false,
        dialogRegisterVisible: false,
        dialogLogoutVisible: false,
        btnRegister: '注册',
        btnLogin: '登录',
        btnName: '',
        btnLogout: '退出',
        activeIndex: '',
        isLogin : false,
        isLogout : true,
        loginForm: {
          username: '',
          password: '',
          name: '',
          email: '',
        },
        registerForm: {},
        rules: {
          username: [
            {required: true, message: '请输入账号（手机号码）', trigger: 'blur'},
            {pattern: /^0?(13[0-9]|[15[7-9]|153|156|18[7-9])[0-9]{8}$/, message: '请正确地输入账号（手机号码）', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '请输入密码', trigger: 'blur'},
            {min: 6, max: 30, message: '长度在 6 到 30 个字符', trigger: 'blur'},
            {pattern: /^(\w){6,20}$/, message: '只能输入6-20个字母、数字、下划线', trigger: 'blur'}
          ],
          name: [
            {required: true, message: '请输入昵称', trigger: 'blur'},
          ],
          email: [
            {required: true, message: '请输入邮箱', trigger: 'blur'},
            {
              pattern: /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/,
              message: '请输入正确的邮箱地址',
              trigger: 'blur'
            }
          ]
        },
      }
    },
    mounted: function () {
      this.$nextTick(function () {
        this.fullscreenLoading= false;
        this.activeIndex = this.actives;
        this.btnName= '游客',
        // 设置 验证session

        this.isLogin = true;
        this.isLogout = false;

        this.checkLogin();
//        this.isLogin = true;
//        this.isLogout = false;


      })
    },
    methods: {
      handleLoginCansel(done) {  //登录
        this.dialogLoginVisible = false;
        this.$refs['loginForm'].resetFields();  // 清空
      },
      handleRegisterCansel(done) {  // 注册
        //
        this.dialogRegisterVisible = false;
        this.$refs['loginForm'].resetFields();  // 清空
      },
      handleLogoutCansel(done) {  // 退出
        //
        this.dialogLogoutVisible = false;
      },

      //dialogLogoutVisible
      handleLoginSubmit(){  //登录
        let _this = this;
        // 处理
        this.$refs['loginForm'].validate((valid) => {
          if (valid) {
            // console.log('submit!!');
            // console.log(this.loginForm.username);
            // console.log(this.loginForm.password);

            let url = 'http://127.0.0.1:8000/beauty/user/login'
            let params = new URLSearchParams();
            params.append('username', this.loginForm.username);       //你要传给后台的参数值 key/value
            params.append('password', this.loginForm.password);
            this.usernameTmp = this.loginForm.username;

            this.$http({
              method: 'post',
              url: url,
              data: params
            }).then(function (response) {
                if (response.data.error_code == 0) {
                  _this.isLogout = true;
                  _this.isLogin = false;
                  _this.btnName = response.data.username;
                  _this.name = _this.btnName;
                  _this.username = _this.usernameTmp;
                  _this.sendValueToContents();  // 给TopBar传值
                } else  {
                  _this.isLogout = false;
                  _this.isLogin = true;
                }

                _this.$message.success(response.data.msg);
              })
              .catch(function (error) {
                _this.$message.error(response.data.msg);
              });
            this.dialogLoginVisible = false;
            this.$refs['loginForm'].resetFields();  // 清空
          } else {
            _this.$message.error('登录不成功！');
            return false;
          }
        });
      },
      handleRegisterSubmit(){  // 注册
        let _this = this;
        // 处理
        this.$refs['loginForm'].validate((valid) => {
          if (valid) {
            // console.log('submit!!');

            let url = 'http://127.0.0.1:8000/beauty/user/register'
            let params = new URLSearchParams();
            params.append('username', this.loginForm.username);       //你要传给后台的参数值 key/value
            params.append('password', this.loginForm.password);
            params.append('name', this.loginForm.name);
            params.append('email', this.loginForm.email);

            this.usernameTmp = this.loginForm.username;

            this.$http({
              method: 'post',
              url: url,
              data: params
            })
              .then(function (response) {
                if (response.data.error_code == 0) {
                  _this.isLogout = true;
                  _this.isLogin = false;
                  _this.btnName = response.data.username;
                  _this.name = _this.btnName;
                  _this.username = _this.usernameTmp;
                  _this.sendValueToContents();  // 给TopBar传值
                } else  {
                  _this.isLogout = false;
                  _this.isLogin = true;
                }
              })
              .catch(function (error) {
                _this.$message.error(response.data.msg);
              });
            this.dialogRegisterVisible = false;
            this.$refs['loginForm'].resetFields();  // 清空
          } else {
            _this.$message.error('注册不成功！');
            return false;
          }
        });
      },
      handleLogoutSubmit(){  // 退出
        let _this = this;
        this.$http.get('http://127.0.0.1:8000/beauty/user/logout')
          .then((response) => {
            let res = response.data;
            // console.log('logout  submit!!');

            if (res.error_code === 0) {
              // console.log(res);
              _this.btnName = res.username;
              _this.sendValueToContents();  // 给TopBar传值
              _this.isLogin = true;
              _this.isLogout = false;

              _this.dialogLogoutVisible = false;
              _this.fullscreenLoading = false;

              // 跳回首页
              _this.getIndex();
              // 重新刷新——更新Cookie变化
              location.reload()
            } else {
              // console.log(res['msg']);
              _this.fullscreenLoading = false;
            }
          })
      },

      // 维护登录状态
      checkLogin() {
        let _this = this;
        this.$http.get('http://127.0.0.1:8000/beauty/user/home')
          .then((response) => {
            let res = response.data;

            if (res.error_code === 0) {
              // console.log(res);
              _this.btnName = res.name;
              _this.name = res.name;
              // console.log('checkLogin  函数')
              // console.log('现在username  = '+_this.username)
              _this.username = res.username;
              _this.sendValueToContents();  // 给TopBar传值
              // console.log('改变后username  = '+_this.username)
              _this.isLogin = false;
              _this.isLogout = true;
            } else {
              // console.log(res['msg']);
            }
          })
      },
      getFocus(username) {
        // console.log(this.username)
        // console.log(this.name)
        if (this.username === '' || this.name === '游客' || this.name === '') {
          this.$message.error('您还未注册或登录！请先进行注册登录操作！')
        } else {
          // console.log('转跳到 通知列表')
          // console.log('现在username  = '+this.username)
          this.$router.push({name: 'focus', params: {username: username}});
        }
      },
      getIndex() {
        this.fullscreenLoading= false;
        this.$router.push({name: 'index'});
      },
      sendValueToContents() {
        let _this = this;
        console.log('bus 帮助TopBar 给 Contents传送username================================发送')
        console.log('当前username = '+this.username);
        bus.$emit("getUsername", _this.username);
      }
    },

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .el-menu {
    .el-menu-item {
      height: 30px;
      line-height: 30px;
    }
    .menu-btn {
      height: 30px;
      line-height: 0;
      margin: 0 20px 0 5px;
    }

    #login, #register, #name, #logout {
      float: right;
    }
  }

  .el-dialog-div {
    margin-top: 10px;
    margin-bottom: 10px;
  }
</style>
