<template>
  <v-row>
    <v-col>
      <v-btn
      color="primary"
      class= 'mb-5'
      to= '/dashboardHR'>
        Back to Dashboard
    </v-btn>
    </v-col>
   <v-col cols="12">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              {{courseCode}}: {{course.courseName}}
            </v-col>
          </v-row>
        </v-card-title>
      </v-card>
       </v-col>
    <v-col cols = "12">
      <table-of-classes :courseCode= courseCode :classes= classes></table-of-classes>
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
      course: {},
      classes: [],
      courseCode: this.$route.params.courseCode,
      classEndpoint: '',
      courseEndpoint: '',
    }
  },
  mounted() {
    this.courseEndpoint = `/course/${this.courseCode}`
    axiosIns
      .get(this.courseEndpoint)
      .then(response => {
        console.log(response.data)
        this.course = response.data
      })
    this.classEndpoint = `/course/${this.courseCode}/classes`
    axiosIns
      .get(this.classEndpoint)
      .then(response => {
        console.log(response.data)
        this.classes = response.data
      })
  },
}
</script>
