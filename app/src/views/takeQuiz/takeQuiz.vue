<template>
  <v-row>
    <v-col cols="12">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              Quiz 1 for Course 1: Class 1
            </v-col>
          </v-row>
        </v-card-title>
      </v-card>
    </v-col>
  <v-col cols='12'>
    <mcqquestion></mcqquestion>
  </v-col>
  <v-col cols='12'>
    <tfquestion></tfquestion>
  </v-col>
  </v-row>
</template>

<script>
import mcqquestion from './MCQquestion.vue'
import tfquestion from './TFquestion.vue'

export default {
  components: {
    mcqquestion,
    tfquestion,
  },
}
</script>
