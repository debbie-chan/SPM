<template>
  <v-row>
    <v-col cols = '12'>
    <v-btn
      color="primary"
      class= 'mb-5'
      to= '/dashboardHR'>
        Back to Dashboard
    </v-btn>
    </v-col>
    <v-col cols = '12'>
      <v-card>
        <v-card-title>
          {{courseCode}} - {{classCode}}
        </v-card-title>
      </v-card>
    </v-col>
    <v-col cols ='12'>
      <v-card>
        <v-card-title>
          Enrolled Students:
        </v-card-title>
        <v-simple-table>
          <thead>
            <tr>
              <th class="text-left">
                Student Name
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="student in assignedStudents"
              :key="student"
            >
              <td>
                {{student.employeeName}}
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-card>
    </v-col>
    <v-col cols = '12'>
      <v-btn
        medium
        color= 'primary'
        class= 'ml-5 font-weight-semibold'
        @click ='showAllStudents = true'>
        Add Students
      </v-btn>
    </v-col>
    <v-col cols = '12' v-if = 'showAllStudents'>
      <v-card>
        <v-card-title>
          Students Pending Enrollment:
        </v-card-title>
        <v-simple-table>
          <thead>
            <tr>
              <th class="text-left">
                Student Name
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="student in pendingStudents"
              :key="student"
            >
              <td>
                 {{student.employeeName}}
                 <v-btn
                  class= 'primary ml-4'
                  @click= "assignStudent(student.username)">
                  Assign
                 </v-btn>
                 <v-btn
                  class= 'primary ml-4'
                  @click= "rejectStudent(student.username)">
                  Reject
                 </v-btn>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-card>
    </v-col>
    <v-col cols = '12' v-if = 'showAllStudents'>
      <v-card>
        <v-card-title>
          Unenrolled Students:
        </v-card-title>
        <v-simple-table>
          <thead>
            <tr>
              <th class="text-left">
                Student Name
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="student in allStudents"
              :key="student"
            >
              <td>
                 {{student.employeeName}}
                 <v-btn
                  class= 'primary ml-4'
                  @click= "assignStudent(student.username)">
                  Assign
                 </v-btn>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

import axiosIns from '@/plugins/axios'

export default {
  data() {
    return {
      assignedStudents: [],
      showAllStudents: false,
      pendingStudents: [],
      allStudents: [],
      courseCode: this.$route.params.courseCode,
      classCode: this.$route.params.classCode,
    }
  },
  mounted() {
    axiosIns
      .get(`/getEnrolledLearners/${this.courseCode}/${this.classCode}`)
      .then(response => {
        console.log(response.data)
        this.assignedStudents = response.data
      })
    axiosIns
      .get(`/getPendingLearners/${this.courseCode}/${this.classCode}`)
      .then(response => {
        console.log(response.data)
        this.pendingStudents = response.data
      })
    axiosIns
      .get(`/getUnenrolledLearners/${this.courseCode}/${this.classCode}`)
      .then(response => {
        console.log(response.data)
        this.allStudents = response.data
      })
  },
  methods: {
    assignStudent(username) {
      const link = `/assignLearnerToClass/${username}/${this.courseCode}/${this.classCode}`
      axiosIns
        .get(link)
        .then(window.location.reload())
    },
    rejectStudent(username) {
      const link = `/deletePendingCourse/${username}/${this.courseCode}/${this.classCode}`
      axiosIns
        .get(link)
        .then(window.location.reload())
    },
  },
}
</script>
