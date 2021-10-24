<template>
  <v-row>
    <v-col cols = '12'>
      <h1>Course 1 : Class 1: </h1>
    </v-col>
    <v-col cols= '9'>
        <v-btn
          color="primary"
          dark
          to = '/Trainer/indivCourse'
        >
          Class Materials
        </v-btn>
    </v-col>
    <v-col cols="12">
      <v-card>
        <v-card-title>
          <v-col cols = '10'>
            Students' Progress
          </v-col>
        </v-card-title>
        <v-simple-table>
          <template>
            <thead>
              <tr>
                <th class="text-uppercase">
                  Student Name
                </th>
                <th class="text-uppercase">
                  % completed
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="item in students"
                :key="item"
              >
                <td>{{ item.student_name }}</td>
                <td>{{ item.percent_complete }}%</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>
    </v-col>
    <v-col cols="12">
      <v-card>
        <v-card-title>
          <v-col cols = '10'>
            Quiz Result Summary
          </v-col>
        </v-card-title>
        <v-simple-table>
          <template>
            <thead>
              <tr>
                <th class="text-uppercase">
                  Quiz Number
                </th>
                <th class="text-uppercase">
                  % completed
                </th>
                <th class="text-uppercase">
                  Average
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="quiz in quizzes"
                :key="quiz"
              >
                <td>{{ quiz.quiz_number }}</td>
                <td>{{ quiz.percent_complete }}%</td>
                <td>{{ quiz.average }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

// import indivClassTable from './indivClassTable.vue'

export default {
  components: {

    // indivClassTable,
  },
  data() {
    const students = [
      {
        student_name: 'Student 1',
        percent_complete: 10,
      },
      {
        student_name: 'Student 2',
        percent_complete: 100,
      },
      {
        student_name: 'Student 3',
        percent_complete: 50,
      },
    ]
    const quizzes = [
      {
        quiz_number: 'Student 1',
        percent_complete: 10,
        average: 50,
      },
      {
        quiz_number: 'Student 2',
        percent_complete: 50,
        average: 40,
      },
      {
        quiz_number: 'Student 3',
        percent_complete: 100,
        average: 80,
      },
    ]

    return {
      students,
      quizzes,
    }
  },
}
</script>
