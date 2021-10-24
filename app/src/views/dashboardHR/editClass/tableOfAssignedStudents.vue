<template>
  <v-card>
    <v-data-table
      :headers="headers"
      :items="usreList"
      item-key="student_name"
      class="table-rounded"
      hide-default-footer
      disable-sort
    >
      <template #[`item.serial_number`]="{item}">
        <div class="d-flex flex-column">
          <span class="d-block font-weight-semibold text--primary text-truncate">
            {{ item.serial_number }}
          </span>
        </div>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import assignedStudentData from './datatable-assignedStudentData'

export default {
  setup() {
    return {
      headers: [
        { text: 'SERIAL NUMBER', value: 'serial_number' },
        { text: 'STUDENT NAME', value: 'student_name' },
      ],
      usreList: assignedStudentData,
    }
  },
}
</script>
