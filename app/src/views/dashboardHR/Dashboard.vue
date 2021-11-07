<template>
  <v-row>
    <v-col cols="12">
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
import DashboardCurrentTable from './DashboardCurrentTable.vue'
import DashboardCompletedTable from './DashboardCompletedTable.vue'
import axiosIns from '@/plugins/axios'

export default {
  components: {
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
      .get('http://localhost:5000/course')
      .then(response => {
        console.log(response.data)
        this.ongoingCourses = response.data
      })
  },
}
</script>
