<template>
  <v-simple-table>
    <template>
      <thead>
        <tr>
          <th class="text-uppercase">
            Lesson Materials
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(value, key) in lessons.hyperlinks"
          :key="key"
        >
          <td>
            <a v-bind:href= "value.link">
              {{value.description}}
            </a>
          </td>
        </tr>
        <tr>
          <td v-if = "getLessonNum(lessons.lessonCode) < parseInt(numLessons, 10)">
            <a v-bind:href= "'/Learner/takeQuiz/' + courseCode + '/' + classCode + '/' + lessons.lessonCode ">
              Quiz
            </a>
          </td>
          <td v-else>
            <a v-bind:href= "'/Learner/takeFinalQuiz/' + courseCode + '/' + classCode + '/' + lessons.lessonCode ">
              Final Quiz
            </a>
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>

export default {
  setup() {
    return {}
  },
  data() {
    return {
      lessonNum: '',
      endpoint: '',
    }
  },
  props: ['courseCode', 'classCode', 'lessons', 'numLessons'],
  methods: {
    getLessonNum(lessonCode) {
      this.lessonNum = parseInt(lessonCode.substr(lessonCode.length - 1), 10)

      return this.lessonNum
    },
    debug(event) {
      console.log(typeof event)
    },
  },
}
</script>
