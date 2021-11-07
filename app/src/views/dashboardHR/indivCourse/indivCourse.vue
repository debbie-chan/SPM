<template>
  <v-row>
   <v-col cols="12">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              Course {{classes[0].courseCode}}:
            </v-col>
          </v-row>
        </v-card-title>
      </v-card>
       </v-col>
    <v-col cols = "12">
      <table-of-classes :classes= classes></table-of-classes>
    </v-col>
  </v-row>

</template>

<script>

import tableOfClasses from './tableOfClasses.vue'
import axiosIns from '@/plugins/axios'

export default {

  components: {
    tableOfClasses,
  },
  data() {
    return {
      classes: [],
    }
  },
  mounted() {
    axiosIns
      .get('http://localhost:5000/course/X1010/classes')
      .then(response => {
        console.log(response.data)
        this.classes = response.data
      })
  },
}
</script>
