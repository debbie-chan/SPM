<template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-uppercase">
            Syllabus Outline
          </th>
          <th class="text-center text-uppercase">
            Status
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in classMaterials"
          :key="item.classMaterials"
        >
          <td>{{ item.classMaterials }}</td>
          <td class="text-center">
            {{ item.status }}
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
  setup() {
    const classMaterials = [
      {
        classMaterials: 'Class Material 1',
        status: 'Completed',
      },
      {
        classMaterials: 'Class Material 2',
        status: 'Completed',
      },
      {
        classMaterials: 'Class Material 3',
        status: 'Completed',
      },
      {
        classMaterials: 'Quiz 1',
        status: 'Completed',
      },
      {
        classMaterials: 'Quiz 2',
        status: 'In Progress',
      },
    ]

    return {
      classMaterials,
    }
  },
}
</script>
