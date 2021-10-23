<template>
  <div>
    <h1>All Courses</h1>
    <br>
    <v-row>
      <!-- card explore -->
      <v-col
        md="4"
        sm="6"
        cols="12"
        class="align-self-start"
        v-for = 'index in courses'
        :key="index"
      >
        <v-card>
          <v-img
            src="@/assets/images/pages/card-basic-person.png"
            height="250"
          ></v-img>
          <v-card-title>
            Course {{index.course_number}}
            <v-chip
              class="ma-2"
            >
              Eligible
            </v-chip>
            <v-btn
              medium
              color= 'primary'
              class= 'ml-5 font-weight-semibold'>
              Enroll
            </v-btn>
          </v-card-title>
          <v-card-text>
            {{index.course_description}}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>

export default {
  setup() {
    const courses = [
      {
        course_number: 1,
        course_description: 'Course Description1 Here',
      },
      {
        course_number: 2,
        course_description: 'Course Description2 Here',
      },
      {
        course_number: 3,
        course_description: 'Course Description3 Here',
      },
    ]

    return {
      courses,
    }
  },
}
</script>
