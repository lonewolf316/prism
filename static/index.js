var SERVER_ADDRESS = location.origin;

var defaultProps = {
  hex: '#ffffff',
  rgba: {a:1, r:255, g:255, b:255}
}

var vm = new Vue({
  el: '#app',
  components: {
    'material-picker': VueColor.Material,
    'compact-picker': VueColor.Compact,
    'swatches-picker': VueColor.Swatches,
    'slider-picker': VueColor.Slider,
    'sketch-picker': VueColor.Sketch,
    'chrome-picker': VueColor.Chrome,
    'photoshop-picker': VueColor.Photoshop
  },
  data: {
    colors: defaultProps,
    white: "0",
    autoUpdate: false,
  },
  watch: {
    colors: function(val, oldVal) {
      if (this.autoUpdate) this.sendColor()
    },
    white: function(val, oldVal) {
      if (this.autoUpdate) this.sendColor()
    }
  },
  methods: {
    sendColor: function() {
      var r = this.colors.rgba.r;
      var g = this.colors.rgba.g;
      var b = this.colors.rgba.b;
      var w = this.white;
      var url = SERVER_ADDRESS
        + '/setColor?'
        + 'r=' + r
        + '&g=' + g
        + '&b=' + b
        + '&w=' + w;
      console.log(url)
      fetch(url, {method: 'POST'}).then(function(res) {
        console.log(res);
      }).catch(function(err) {
        console.log(err);
      })
    },
  sendFade: function() {
    var url = SERVER_ADDRESS
      + '/setFade?'
    console.log(url)
    fetch(url, {method: 'POST'}).then(function(res) {
      console.log(res);
    }).catch(function(err) {
      console.log(err);
    })
  }
}
})
