<template>
  <v-card>
    <v-data-table
      :headers="headers"
      :items="usreList"
      item-key="class_number"
      class="table-rounded"
      hide-default-footer
      disable-sort
    >
      <template #[`item.class_number`]="{item}">
        <div class="d-flex flex-column">
          <span class="d-block font-weight-semibold text--primary text-truncate">
            {{ item.class_number }}
          </span>
        </div>
      </template>
      <template #[`item.no_of_students`]="{item}">
        <a href = '/editClass'>
          {{item.no_of_students}}
        </a>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import courseData from './datatable-coursedata'

export default {
  setup() {
    return {
      headers: [
        { text: 'CLASS NUMBER', value: 'class_number' },
        { text: 'NO. OF STUDENTS', value: 'no_of_students' },
        { text: 'TRAINER', value: 'trainer' },
        { text: 'EDIT', value: 'edit' },
      ],
      usreList: courseData,
    }
  },
}
</script>
