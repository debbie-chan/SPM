<template>
  <v-row>
    <v-col cols="12">
      <dashboard-welcome></dashboard-welcome>
    </v-col>
    <v-col
      cols="12"
      md="12"
    >
      <div class="mb-4 d-flex">
        <span class= "font-weight-semibold text-xl"> Ongoing/Upcoming Courses: </span>
        <v-btn
          medium
          color= 'primary'
          class= 'ml-5 font-weight-semibold'
          to = "/HR/addNewCourse"
        >
          + New Course
        </v-btn>
      </div>
      <dashboard-current-table :ongoingCourses= ongoingCourses></dashboard-current-table>
    </v-col>
    <v-col cols="12">
      <div class="mb-4 d-flex">
        <span class= "font-weight-semibold text-xl"> Completed Courses: </span>
      </div>
      <dashboard-completed-table :completedCourses= completedCourses></dashboard-completed-table>
    </v-col>
  </v-row>
</template>

<script>

// demos
import DashboardWelcome from './DashboardWelcome.vue'
import DashboardCurrentTable from './DashboardCurrentTable.vue'
import DashboardCompletedTable from './DashboardCompletedTable.vue'
import axiosIns from '@/plugins/axios'

export default {
  components: {
    DashboardWelcome,
    DashboardCurrentTable,
    DashboardCompletedTable,
  },
  data() {
    return {
      completedCourses: [],
      ongoingCourses: [],
    }
  },
  mounted() {
    axiosIns
      .get('/course')
      .then(response => {
        console.log(response.data)
        this.ongoingCourses = response.data
      })
  },
}
</script>
