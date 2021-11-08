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
      <dashboard-badges :completedCourses= completedCourses></dashboard-badges>
    </v-col>
    <v-col
      cols="12"
      md="12"
    >
      <dashboard-my-enrolled-courses :myEnrolledCourses= myEnrolledCourses></dashboard-my-enrolled-courses>
    </v-col>
    <v-col
      cols="12"
      md="12"
    >
      <dashboard-my-pending-courses :myPendingCourses= myPendingCourses></dashboard-my-pending-courses>
    </v-col>

    <v-col
      cols="12"
      md="12"
    >
      <dashboard-completed-courses :completedCourses= completedCourses></dashboard-completed-courses>
    </v-col>

  </v-row>
</template>

<script>
// eslint-disable-next-line object-curly-newline
import { mdiPoll, mdiLabelVariantOutline, mdiCurrencyUsd, mdiHelpCircleOutline } from '@mdi/js'

// demos
import DashboardWelcome from './DashboardWelcome.vue'
import DashboardBadges from './DashboardBadges.vue'
import DashboardMyEnrolledCourses from './DashboardMyEnrolledCourses.vue'
import DashboardMyPendingCourses from './DashboardMyPendingCourses.vue'
import DashboardCompletedCourses from './DashboardCompletedCourses.vue'
import axiosIns from '@/plugins/axios'

export default {
  components: {
    DashboardWelcome,
    DashboardBadges,
    DashboardMyEnrolledCourses,
    DashboardMyPendingCourses,
    DashboardCompletedCourses,
  },
  setup() {
    const totalProfit = {
      statTitle: 'Total Profit',
      icon: mdiPoll,
      color: 'success',
      subtitle: 'Weekly Project',
      statistics: '$25.6k',
      change: '+42%',
    }

    const totalSales = {
      statTitle: 'Refunds',
      icon: mdiCurrencyUsd,
      color: 'secondary',
      subtitle: 'Past Month',
      statistics: '$78',
      change: '-15%',
    }

    // vertical card options
    const newProject = {
      statTitle: 'New Project',
      icon: mdiLabelVariantOutline,
      color: 'primary',
      subtitle: 'Yearly Project',
      statistics: '862',
      change: '-18%',
    }

    const salesQueries = {
      statTitle: 'Sales Quries',
      icon: mdiHelpCircleOutline,
      color: 'warning',
      subtitle: 'Last week',
      statistics: '15',
      change: '-18%',
    }

    return {
      totalProfit,
      totalSales,
      newProject,
      salesQueries,
    }
  },

  data() {
    return {
      completedCourses: [],
      myPendingCourses: [],
      myEnrolledCourses: [],
    }
  },
  mounted() {
    axiosIns
      .get('/learner/emmajones')
      .then(response => {
        this.myEnrolledCourses = response.data.enrolledCourses
        this.myPendingCourses = response.data.pendingCourses
        this.completedCourses = response.data.completedCourses
      })
  },
}
</script>
