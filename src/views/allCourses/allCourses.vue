<template>
  <div>
    <v-btn
      medium
      color= 'primary'
      class= 'mt-5 mb-5 font-weight-semibold'
      to = '/dashboardLearner'
    >
      Back to Dashboard
    </v-btn>
    <h1>All Courses</h1>
    <v-alert type="success"
      v-show = showAlert>
      You've successfully enrolled in the course.
    </v-alert>
    <br>
    <v-row>
      <!-- card explore -->
      <v-col
        v-for = '(value, index) in classes'
        :key="index"
        cols="5"
        class="align-self-start"
      >
        <v-card>
          <v-card-title>
            {{value.courseName}}
          </v-card-title>
          <v-card-text>
            <v-btn
              medium
              color= 'primary'
              class= 'ml-5 mt-5 font-weight-semibold'
              @click = 'enroll(value.courseCode, value.classCode)'
              :disabled='verified[index] === "rejected"'
            >
              Enroll
            </v-btn>
            <p class = 'mt-4'>
              Course Code: {{value.courseCode}}
            </p>
            <p class = 'mt-4'>
              Class: {{value.classCode}}
            </p>
            <p>
              Description: {{value.courseDescription}}
            </p>
            <p v-if = "value.preRequisites[0]">
              Pre-requisites:
              <span v-for = "prereq in value.preRequisites" :key="prereq">
              {{prereq}}
              </span>
            </p>
            <p v-else>
              Pre-requisites: -
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axiosIns from '@/plugins/axios'

export default {
  data() {
    return {
      classes: [],
      showCards: [],
      showAlert: false,
      verified: [],
    }
  },
  mounted() {
    const promises = []
    const promiseResults = []
    axiosIns
      .get('/course/displayAllCourses')
      .then(response => {
        this.classes = response.data
        for (let i = 0; i < response.data.length; i += 1) {
          promises.push(axiosIns
            .get(`/verifyLearner/emmajones/${response.data[i].courseCode}/${response.data[i].classCode}`))
        }
        console.log(promises)
        Promise.allSettled(promises)
          .then(results => {
            results.forEach(result => {
              console.log(typeof (result.status))
              promiseResults.push(result.status)
            })
          })
        console.log(promiseResults)
        this.verified = promiseResults
        console.log(this.verified)
      })
  },
  methods: {
    enroll(courseCode, classCode) {
      axiosIns
        .get(`/addPendingCourse/emmajones/${courseCode}/${classCode}`)
        .then(response => {
          this.showAlert = true
          console.log(response)
        })
    },
  },
}

</script>
