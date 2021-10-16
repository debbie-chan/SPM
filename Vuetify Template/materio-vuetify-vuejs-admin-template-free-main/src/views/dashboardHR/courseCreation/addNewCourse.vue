<template>
  <v-row>
    <v-col cols='12'>
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              New Course:
            </v-col>
          </v-row>
          </v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field
              v-model= "courseName"
              label="Course Name"
              outlined
              dense
              ></v-text-field>
              <v-row class = 'pl-0'>
                <v-col cols="2">
                  <v-text-field
                    v-model="courseDuration"
                    label="Course Duration"
                    readonly
                  ></v-text-field>
                </v-col>
                <v-col cols="4">
                  <v-date-picker
                    v-model="courseDurationDates"
                    range
                    class= 'pr-0'
                  ></v-date-picker>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                    v-model="registrationPeriod"
                    label="Registration Period"
                    readonly
                  ></v-text-field>
                </v-col>
                <v-col cols="4">
                  <v-date-picker
                    v-model="registrationDuration"
                    range
                  ></v-date-picker>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
      </v-card>
  </v-col>
  <v-col>
    <v-card>
      <classes-table></classes-table>
    </v-card>
  </v-col>
</v-row>
</template>

<script>

import classesTable from './classesTable.vue'

export default {
  components: {
    classesTable,
  },
  data: () => ({
    courseName: '',
    courseDurationDates: [],
    registrationDuration: [],
  }),
  computed: {
    courseDuration() {
      return this.courseDurationDates.join('~')
    },
    registrationPeriod() {
      return this.registrationDuration.join('~')
    },
  },
}
</script>
