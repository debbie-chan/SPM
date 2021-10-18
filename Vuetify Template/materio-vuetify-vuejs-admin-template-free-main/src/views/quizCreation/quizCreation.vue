<template>
  <v-row>
    <v-col cols="12">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              New Quiz for Course 1: Class 1: Section 1
            </v-col>
            <v-col cols= '2'>
              <v-btn color="primary">
                Add Quiz
              </v-btn>
            </v-col>
          </v-row>
        </v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              v-model="quizname"
              label="Quiz Name"
              outlined
              dense
              placeholder="Name"
            ></v-text-field>
            <v-row>
              <v-col cols= '4'>
                <v-checkbox
                  v-model="gradeSelection"
                  label="Graded"
                >
                </v-checkbox>
              </v-col>
              <v-col cols= '1'>
                <v-checkbox
                v-model="timedSelection"
                label="Timed"
                >
                </v-checkbox>
              </v-col>
              <v-col cols= '2'>
                <v-text-field
                  v-model="duration"
                  label="HH:MM:SS"
                  outlined
                  dense
                  class = 'mt-3'
                ></v-text-field>
              </v-col>
            </v-row>
            <v-btn color="primary">
                Add MCQ Question
            </v-btn>
            <v-btn color="primary" class= 'ml-6'>
                Add True/False Question
            </v-btn>
          </v-form>
        </v-card-text>
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
