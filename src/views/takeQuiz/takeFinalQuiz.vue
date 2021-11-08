<template>
  <v-row>
    <v-col cols="12" v-if = "result === 'Pass'">
      <v-alert type="success">
        You've Passed!
      </v-alert>
      <v-btn
      color="primary"
      :to = "'/Learner/indivCourse' + '/' + courseCode + '/' + classCode">
      Back to Class
      </v-btn>
    </v-col>
    <v-col cols="12" v-if = "result === 'Fail'">
      <v-alert type="error">
        You've Failed :(
      </v-alert>
      <v-btn
      color="primary"
      :to = "'/Learner/indivCourse' + '/' + courseCode + '/' + classCode">
      Back to Class
      </v-btn>
    </v-col>
    <v-col cols="12" v-show = "showRest">
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              Quiz for {{courseCode}}: Week 2
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
      courseCode: this.$route.params.courseCode,
      classCode: this.$route.params.classCode,
      lessonCode: this.$route.params.lessonCode,
      endpoint: '',
    }
  },
  mounted() {
    this.endpoint = `/getQuiz/${this.lessonCode}`
    axiosIns
      .get(this.endpoint)
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
          lessonCode: this.lessonCode,
          courseCode: this.courseCode,
          classCode: this.classCode,
          answer1: this.mcqAnswer,
          answer2: this.tfAnswer,
        })
        .then(res => {
          console.log(res)
          axiosIns
            .get(`/getFinalGrade/emmajones/${this.courseCode}`)
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
