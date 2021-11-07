<template>
  <v-row>
    <h1>{{lessons[0].classCode}} : Class 1</h1>
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
    }
  },
  mounted() {
    axiosIns
      .get('http://localhost:5000/lessons/X1010/G1')
      .then(response => {
        this.lessons = response.data
        console.log(this.lessons)
      })
  },
}
</script>
