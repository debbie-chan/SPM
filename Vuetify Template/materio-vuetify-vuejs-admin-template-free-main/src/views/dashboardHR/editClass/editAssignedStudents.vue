<template>
  <v-row>
    <v-col cols = '12'>
      <v-card>
        <v-card-title>
          Course 1: Class 1
        </v-card-title>
      </v-card>
    </v-col>
    <v-col cols ='12'>
      <v-card>
        <v-card-title>
          Enrolled Students:
        </v-card-title>
        <assigned-student-data></assigned-student-data>
      </v-card>
    </v-col>
    <v-col cols = '12'>
      <v-btn
        medium
        color= 'primary'
        class= 'ml-5 font-weight-semibold'
        @click ='showAllStudents = true'>
        Add Students
      </v-btn>
    </v-col>
    <v-col cols = '12' v-if = 'showAllStudents'>
      <v-card>
        <v-card-title>
          All Students:
        </v-card-title>
        <v-simple-table>
          <thead>
            <tr>
              <th class="text-left">
                Student Name
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in student_name"
              :key="item"
            >
              <td>
                 <v-checkbox
                  v-model="selected"
                  :label="item"
                  value = "item"
                ></v-checkbox>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-card>
    </v-col>
    <v-col cols = '12' v-if = 'showAllStudents'>
      <v-btn
        medium
        color= 'primary'
        class= 'ml-5 font-weight-semibold'>
        Assign Selected Students
      </v-btn>
    </v-col>
 </v-row>
</template>

<script>
import assignedStudentData from './tableOfAssignedStudents.vue'

export default {
  components: {
    assignedStudentData,
  },
  data() {
    return {
      student_name: ['Student 4', 'Student 5', 'Student 6', 'Student 7', 'Student 8'],
      showAllStudents: false,
    }
  },
}
</script>
