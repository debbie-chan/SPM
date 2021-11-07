<template>
  <v-row>
    <v-col cols="12" v-if = "result === 'submitted'">
      <v-alert type="success">
        You've Submitted Your Quiz!
      </v-alert>
      <v-btn
      color="primary"
      to = '/Learner/indivCourse'>
      Back to Class
      </v-btn>
    </v-col>
    <v-col cols="12" v-show = "showRest">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              Quiz 1 for X1010: Week 1
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
  <v-col cols= '2' v-show = "showRest">
    <v-btn
      color="primary"
      @click = "submitQuiz()">
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
      .get('http://localhost:5000/getQuiz/X1010G1L1')
      .then(response => {
        this.quiz = response.data
        console.log(this.quiz)
      })
  },
  methods: {
    submitQuiz() {
      axiosIns
        .post('http://localhost:5000/gradeQuiz', {
          username: 'emmajones',
          lessonCode: 'X1010G1L2',
          courseCode: 'X1010',
          classCode: 'G1',
          answer1: this.mcqAnswer - 1,
          answer2: this.tfOptions,
        })
        .then(response => {
          console.log(response)
          this.result = 'submitted'
          this.showRest = false
        })
    },
  },
}
</script>
