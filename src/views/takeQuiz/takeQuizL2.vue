<template>
  <v-row>
    <v-col cols="12" v-if = "result === 'Pass'">
      <v-alert type="success">
        You've Passed!
      </v-alert>
    </v-col>
    <v-col cols="12" v-if = "result === 'Fail'">
      <v-alert type="error">
        You've Failed :(
      </v-alert>
    </v-col>
    <v-col cols="12" v-show = "showRest">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              Quiz 1 for X1010: Week 2
            </v-col>
          </v-row>
        </v-card-title>
      </v-card>
    </v-col>
  <v-col cols='12' v-show = "showRest">
    <v-card>
      <v-card-title>
        Question 1
      </v-card-title>
      <v-card-text>
          {{quiz.q1}}
          <v-radio-group v-model="mcqAnswer">
            <v-radio
              v-for= "(value,index) in quiz.options1"
              :key="index"
              :label="`${value}`"
            ></v-radio>
          </v-radio-group>
      </v-card-text>
    </v-card>
  </v-col>
  <v-col cols='12' v-show = "showRest">
    <v-card>
        <v-card-title>
            Question 2
        </v-card-title>
        <v-card-text>
            {{quiz.q2}}
            <v-radio-group v-model="tfAnswer">
              <v-radio
                  v-for= "index in ['True', 'False']"
                  :key="index"
                  :label="`${index}`"
                  class= 'pb-4'
              ></v-radio>
            </v-radio-group>
        </v-card-text>
    </v-card>
  </v-col>
  <v-col cols= '2'>
    <v-btn
      color="primary"
      @click = "submitQuiz()"
      v-show = "showRest">
      Submit Quiz
    </v-btn>
  </v-col>
  </v-row>
</template>

<script>
import axiosIns from '@/plugins/axios'

export default {

  data() {
    return {
      quiz: [],
      mcqAnswer: null,
      tfAnswer: null,
      showRest: true,
      result: null,
    }
  },
  mounted() {
    axiosIns
      .get('/getQuiz/X1010G1L2')
      .then(response => {
        this.quiz = response.data
      })
  },
  methods: {
    submitQuiz() {
      console.log(this.mcqAnswer)
      console.log(this.tfAnswer)
      axiosIns
        .post('/gradeQuiz', {
          username: 'emmajones',
          lessonCode: 'X1010G1L2',
          courseCode: 'X1010',
          classCode: 'G1',
          answer1: this.mcqAnswer,
          answer2: this.tfAnswer,
        })
        .then(res => {
          console.log(res)
          axiosIns
            .get('/getFinalGrade/emmajones/X1010')
            .then(response => {
              this.showAlert = true
              this.showRest = false
              this.result = response.data
            })
        })
    },
  },
}
</script>
