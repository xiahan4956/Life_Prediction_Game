const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    host: '0.0.0.0',
    port: 8080, // 你想要运行的端口，如果是默认的8080，可以不写
  },
  transpileDependencies: true
})
