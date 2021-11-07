<template>
  <v-row>
    <v-col
      cols="12"
      md="12"
    >
      <dashboard-current-classes :myCourses= myCourses></dashboard-current-classes>
    </v-col>

    <v-col
      cols="12"
      md="12"
    >
      <dashboard-completed-classes :completedCourses= completedCourses></dashboard-completed-classes>
    </v-col>

  </v-row>
</template>

<script>

// demos
import DashboardCurrentClasses from './DashboardCurrentClasses.vue'
import DashboardCompletedClasses from './DashboardCompletedClasses.vue'
import axiosIns from '@/plugins/axios'

export default {
  components: {
    DashboardCurrentClasses,
    DashboardCompletedClasses,
  },
  data() {
    return {
      completedCourses: [],
      myCourses: [],
    }
  },
  mounted() {
    axiosIns
      .get('http://localhost:5000/trainer/emilymariko')
      .then(response => {
        console.log(response.data)
        this.myCourses = response.data.trainingCourses
        this.completedCourses = response.data.trainedCourses
      })
  },
}
</script>
