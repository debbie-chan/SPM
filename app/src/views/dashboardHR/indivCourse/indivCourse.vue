<template>
  <v-row>
   <v-col cols="12">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              Course 1:
            </v-col>
          </v-row>
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols= '6'>
              Start Date:
            </v-col>
            <v-col cols= '6'>
              End Date:
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
       </v-col>
    <v-col cols = "12">
      <table-of-classes></table-of-classes>
    </v-col>
  </v-row>

</template>

<script>
import tableOfClasses from './tableOfClasses.vue'

export default {
  components: {
    tableOfClasses,
  },
}
</script>
