import Vue from 'vue'

// axios
import axios from 'axios'

const axiosIns = axios.create({

  // You can add your headers here
  // ================================
  baseURL: '/api/',

  // timeout: 1000,
  // headers: {'X-Custom-Header': 'foobar'}
})

Vue.prototype.$axios = axiosIns

export default axiosIns
