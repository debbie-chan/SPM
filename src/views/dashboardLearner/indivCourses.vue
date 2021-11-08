<template>
  <v-row>
    <v-col cols = "12">
      <v-btn
      color="primary"
      class= 'mb-5'
      to= '/dashboardLearner'>
        Back to Dashboard
    </v-btn>
    </v-col>
    <v-col cols = "12">
      <h1>{{courseCode}} {{classCode}}</h1>
    </v-col>
    <v-col cols="12"
      v-for= '(lesson, key) in lessons' :key= 'key'>
      <v-card>
        <v-card-title> {{lesson.lessonName}} </v-card-title>
        <indiv-class-table
        :courseCode= courseCode :classCode= classCode :lessons= lesson :numLessons= numLessons>
        </indiv-class-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

import indivClassTable from './indivClassTable.vue'
import axiosIns from '@/plugins/axios'

export default {
  components: {
    indivClassTable,
  },
  setup() {
    return {}
  },
  data() {
    return {
      class: [],
      numLessons: null,
      lessons: [],
      courseCode: this.$route.params.courseCode,
      classCode: this.$route.params.classCode,
      classendpoint: '',
      lessonendpoint: '',
    }
  },
  created() {
    this.classendpoint = `/class/${this.courseCode}/${this.classCode}`
    axiosIns
      .get(this.classendpoint)
      .then(response => {
        this.class = response.data
        this.numLessons = this.class.numLessons
        console.log(this.numLessons)
      })
    this.lessonendpoint = `/lessons/${this.courseCode}/${this.classCode}`
    axiosIns
      .get(this.lessonendpoint)
      .then(response => {
        this.lessons = response.data
        console.log(this.lessons)
      })
  },
}
</script>
