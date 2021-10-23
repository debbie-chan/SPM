<template>
  <v-row>
    <h1>Course 1 : Class 1</h1>
    <v-col cols="12">
      <v-card>
        <v-card-title>Chapter 1</v-card-title>
        <indiv-class-table></indiv-class-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import indivClassTable from './indivClassTable.vue'

export default {
  components: {
    indivClassTable,
  },
  setup() {
    return {}
  },
  data: () => ({
    items: [
      { title: 'Chapter 1' },
      { title: 'Chapter 2' },
      { title: 'Chapter 3' },
      { title: 'Chapter 4' },
    ],
  }),
}
</script>
