<template>
  <v-card>
    <v-data-table
      :headers="headers"
      :items= "ongoingCourses"
      item-key="course_name"
      class="table-rounded"
      hide-default-footer
      disable-sort
    >
      <!-- name -->
      <template #[`item.courseCode`]="{item}">
        <div class="d-flex flex-column">
          <span class="d-block font-weight-semibold text--primary text-truncate">
          <a :href= "'/HR/indivCourse/' + item.courseCode" >
            {{ item.courseCode }}
          </a>
          </span>
        </div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  setup() {
    return {
      headers: [
        { text: 'COURSE NAME', value: 'courseName' },
        { text: 'COURSE CODE', value: 'courseCode' },
        { text: 'NO. OF CLASSES', value: 'numClasses' },
      ],
    }
  },
  props: ['ongoingCourses'],
}
</script>
