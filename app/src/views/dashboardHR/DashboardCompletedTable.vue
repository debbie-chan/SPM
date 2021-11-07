<template>
  <v-card>
    <v-data-table
      :headers="headers"
      :items="completedCourses"
      item-key="course_name"
      class="table-rounded"
      hide-default-footer
      disable-sort
    >
      <!-- name -->
      <template #[`item.course_name`]="{item}">
        <div class="d-flex flex-column">
          <span class="d-block font-weight-semibold text--primary text-truncate">{{ item.course_name }}</span>
        </div>
      </template>
      <!-- status -->
      <template #[`item.status`]="{item}">
        <v-chip
          small
          :color="statusColor[status[item.status]]"
          class="font-weight-medium"
        >
          {{ status[item.status] }}
        </v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>

export default {
  setup() {
    return {
      headers: [
        { text: 'COURSE NAME', value: 'course_name' },
        { text: 'NO. OF CLASSES', value: 'no_of_classes' },
        { text: 'START DATE', value: 'start_date' },
        { text: 'END DATE', value: 'end_date' },
      ],
    }
  },
  props: ['completedCourses'],
}
</script>
