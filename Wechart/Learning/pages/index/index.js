// pages/index/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    msg: 'hallo world',
    UserInfo: {} //用户基本信息
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log('onLoad()');
    // 数据绑定更新
    // console.log(this.data.msg);
    // setTimeout(() => {
    //   this.setData({
    //     msg: 'hallo'
    //   })
    //   console.log(this.data.msg)
    // }, 2000)
    wx.getUserInfo({
      success: (res) => {
        console.log(res);
        this.setData({
          UserInfo: res
        })
      },
      fail: (error) => {
        console.log(error);
      }
    })
  },
  handparent() {
    console.log('parent');
  },
  handchild() {
    console.log('child');
  },
  // 获取用户信息的回调
  handgetuserinfo(res) {
    console.log(res);
    if (res.detail.userInfo) { //允许授权
      //修改userInfo的内容
      this.setData({
        UserInfo: res.detail.userInfo
      })
    }
    console.log(this.data.UserInfo);
  },
  // 跳转到log页面的方法,需要使用api
  toLogs() {
    wx.navigateTo({
      url: '/pages/log/log',
    });
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    console.log('onReady()');
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    console.log('onShow()');

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    console.log('onHide()');
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    console.log('onUnload()');
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})