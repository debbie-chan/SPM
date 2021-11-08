<template>
  <v-row>
    <v-col
      cols="12"
      md="12"
    >
      <dashboard-welcome></dashboard-welcome>
    </v-col>
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
import DashboardWelcome from './DashboardWelcome.vue'
import DashboardCurrentClasses from './DashboardCurrentClasses.vue'
import DashboardCompletedClasses from './DashboardCompletedClasses.vue'
import axiosIns from '@/plugins/axios'

export default {
  components: {
    DashboardWelcome,
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
      .get('/trainer/emilymariko')
      .then(response => {
        console.log(response.data)
        this.myCourses = response.data.trainingCourses
        this.completedCourses = response.data.trainedCourses
      })
  },
}
</script>
