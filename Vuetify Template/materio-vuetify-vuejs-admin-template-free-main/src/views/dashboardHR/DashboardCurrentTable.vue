<template>
  <v-card>
    <v-data-table
      :headers="headers"
      :items="usreList"
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
import { mdiSquareEditOutline, mdiDotsVertical } from '@mdi/js'
import data from './datatable-data'

export default {
  setup() {
    const statusColor = {
      /* eslint-disable key-spacing */
      Current: 'primary',
      Upcoming: 'success',
      /* eslint-enable key-spacing */
    }

    return {
      headers: [
        { text: 'COURSE NAME', value: 'course_name' },
        { text: 'NO. OF CLASSES', value: 'no_of_classes' },
        { text: 'START DATE', value: 'start_date' },
        { text: 'END DATE', value: 'end_date' },
        { text: 'STATUS', value: 'status' },
      ],
      usreList: data,
      status: {
        1: 'Current',
        2: 'Upcoming',
      },
      statusColor,

      // icons
      icons: {
        mdiSquareEditOutline,
        mdiDotsVertical,
      },
    }
  },
}
</script>
