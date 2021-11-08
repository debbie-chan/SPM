<template>
  <v-form>
  <v-row>
    <v-col cols="12" v-show = "showAlert">
      <v-alert type="success">
        You've added a new quiz!
      </v-alert>
    </v-col>
    <v-col cols="12" v-show = 'showRest'>
      <v-card>
        <v-card-title>
          <v-row>
            <v-col cols= '10'>
              New Quiz
            </v-col>
          </v-row>
        </v-card-title>
        <v-card-text>
            <v-row>
              <v-col
                class="d-flex"
                cols="12"
                sm="6"
              >
                <v-select
                  v-model= "selectedCourse"
                  :items="courses"
                  label="Course"
                  dense
                  outlined
                ></v-select>
              </v-col>
              <v-col
                class="d-flex"
                cols="12"
                sm="6"
              >
                <v-select
                  v-model= "selectedClass"
                  :items="classes"
                  label="Class"
                  dense
                  outlined
                ></v-select>
              </v-col>
               <v-col
                class="d-flex"
                cols="12"
                sm="6"
              >
                <v-select
                  v-model= "selectedLesson"
                  :items="lessons"
                  label="Lesson"
                  dense
                  outlined
                ></v-select>
              </v-col>
            </v-row>
            <v-btn
              color="primary"
              @click= "showMCQ = true">
                Add MCQ Question
            </v-btn>
            <v-btn
              color="primary"
              class= 'ml-6'
              @click= "showTF = true">
                Add True/False Question
            </v-btn>
        </v-card-text>
      </v-card>
    </v-col>
  <v-col cols='12'>
    <v-card v-show= "showMCQ">
        <v-card-text>
            <v-text-field
              v-model= 'mcqQuestion'
              label="Question"
              outlined
              dense
            ></v-text-field>
            <v-text-field
              v-model= 'mcqOption1'
              label="Option 1"
              outlined
              dense
            ></v-text-field>
            <v-text-field
              v-model= 'mcqOption2'
              label="Option 2"
              outlined
              dense
            ></v-text-field>
            <v-text-field
              v-model= 'mcqOption3'
              label="Option 3"
              outlined
              dense
            ></v-text-field>
            <v-text-field
              v-model= 'mcqOption4'
              label="Option 4"
              outlined
              dense
            ></v-text-field>
            <v-text-field
              v-model= 'mcqAnswer'
              label="Answer Option Number"
              outlined
              dense
            ></v-text-field>
        </v-card-text>
    </v-card>
  </v-col>
  <v-col cols='12'>
    <v-card v-show= "showTF">
        <v-card-text>
            <v-text-field
              v-model= "tfQuestion"
              label="Question"
              outlined
              dense
            ></v-text-field>
            <v-radio-group v-model= "tfOptions">
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
  </v-row>
  <v-col cols= '2' v-show = "showRest">
    <v-btn
      color="primary"
      @click = "submitQuiz()">
      Add Quiz
    </v-btn>
  </v-col>
  </v-form>
</template>

<script>
import axiosIns from '@/plugins/axios'

export default {
  data() {
    return {
      courses: [],
      classes: [],
      lessons: [],
      selectedCourse: null,
      selectedClass: null,
      selectedLesson: null,
      showMCQ: false,
      showTF: false,
      mcqQuestion: '',
      mcqOption1: '',
      mcqOption2: '',
      mcqOption3: '',
      mcqOption4: '',
      mcqAnswer: null,
      tfQuestion: '',
      tfOptions: ['True', 'False'],
      showRest: true,
      showAlert: false,
    }
  },
  mounted() {
    axiosIns
      .get('/course')
      .then(response => {
        // console.log(response.data)
        response.data.forEach((item => {
          this.courses.push(item.courseCode)
        }))
      })
    axiosIns
      .get('/course/X1010/classes')
      .then(response => {
        console.log(response.data)
        response.data.forEach((item => {
          this.classes.push(item.classCode)
        }))
      })
    axiosIns
      .get('/lessons/X1010/G1')
      .then(response => {
        response.data.forEach((item => {
          this.lessons.push(item.lessonName)
        }))
      })
  },
  methods: {
    submitQuiz() {
      axiosIns
        .post('/addQuestions', {
          lessonCode: 'X1010G1L2',
          q1: this.mcqQuestion,
          options1: {
            0: this.mcqOption1,
            1: this.mcqOption2,
            2: this.mcqOption3,
            3: this.mcqOption4,
          },
          answer1: this.mcqAnswer - 1,
          q2: this.tfQuestion,
          options2: {
            0: 'True',
            1: 'False',
          },
          answer2: this.tfOptions,
        })
        .then(response => {
          console.log(response)
          this.showTF = false
          this.showMCQ = false
          this.showRest = false
          this.showAlert = true
          console.log(this.showRest)
        })
    },
  },
}
</script>
