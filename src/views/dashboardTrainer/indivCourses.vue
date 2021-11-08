<template>
  <v-row>
    <v-btn
      color="primary"
      class= 'mb-5'
      to= '/dashboardTrainer'>
        Back to Dashboard
    </v-btn>
    <v-col cols = '12'>
      <h1>{{ courseCode }} {{ classCode }}</h1>
    </v-col>
    <v-col cols= '9'>
        <v-btn
          color="primary"
          dark
          @click = newLesson()
        >
          Add Lesson
        </v-btn>
    </v-col>
    <v-col cols= '3'>
        <v-btn
          color="primary"
          dark
          to = '/Trainer/studentProgress'
        >
          View Students' Progress
        </v-btn>
    </v-col>
    <v-col cols="12"
      v-for= '(lesson, index) in lessons'
      :key= 'index'>
      <v-card>
        <v-card-title>
          <v-col cols = '10'>
            {{lesson.lessonName}}
          </v-col>
          <v-col cols = '2'>
            <v-btn
              color="primary"
              dark
              @click = addMaterial()
            >
              Add Material
            </v-btn>
          </v-col>
        </v-card-title>
        <v-simple-table>
        <template>
          <thead>
            <tr>
              <th class="text-uppercase">
                Description
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for= "(value, key) in lesson.hyperlinks"
              :key="key"
            >
              <td>
                <a v-bind:href= "value.link">
                  {{value.description}}
                </a>
              </td>
            </tr>
          </tbody>
        </template>
        </v-simple-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

// import indivClassTable from './indivClassTable.vue'
import axiosIns from '@/plugins/axios'

export default {
  setup() {
    return {}
  },
  data() {
    return {
      lessons: [],
      nextLessonNumber: 0,
      courseCode: this.$route.params.courseCode,
      classCode: this.$route.params.classCode,
      lessonCode: '',
      endpoint: '',
    }
  },
  mounted() {
    this.endpoint = `/lessons/${this.courseCode}/${this.classCode}`
    axiosIns
      .get(this.endpoint)
      .then(response => {
        this.lessons = response.data
        this.nextLessonNumber = this.lessons.length + 1
      })
  },
  methods: {
    newLesson() {
      this.lessonCode = `${this.lessons[0].courseCode}${this.lessons[0].classCode}L${this.nextLessonNumber}`
      console.log(this.lessonCode)
      axiosIns
        .post('/lesson/createLesson', {
          lessonName: `Week${this.nextLessonNumber.toString()}`,
          hyperlinks: [],
          quiz: [],
          classCode: this.lessons[0].classCode,
          lessonCode: `${this.lessons[0].courseCode}${this.lessons[0].classCode}L${this.nextLessonNumber}`,
          courseCode: this.lessons[0].courseCode,
        })
        .then(res => {
          console.log(res)
          window.location.reload()
        })
    },
    newMaterial() {

    },
  },
}
</script>
