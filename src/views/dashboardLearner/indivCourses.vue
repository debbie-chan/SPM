<template>
  <v-row>
    <h1>{{ courseCode }} {{ classCode }}</h1>
    <v-col cols="12"
      v-for= '(lesson, key) in lessons' :key= 'key'>
      <v-card>
        <v-card-title> {{lesson.lessonName}} </v-card-title>
        <indiv-class-table
        :lessons= lesson>
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
      lessons: [],
      courseCode: this.$route.params.courseCode,
      classCode: this.$route.params.classCode,
      endpoint: '',
    }
  },
  mounted() {
    this.endpoint = `/lessons/${this.courseCode}/${this.classCode}`
    axiosIns
      .get(this.endpoint)
      .then(response => {
        this.lessons = response.data
        console.log(this.lessons)
      })
  },
}
</script>
