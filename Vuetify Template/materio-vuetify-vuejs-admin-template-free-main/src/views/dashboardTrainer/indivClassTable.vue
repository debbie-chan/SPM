<template>
  <v-simple-table>
    <template>
      <thead>
        <tr>
          <th class="text-uppercase">
            Syllabus Outline
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in classMaterials"
          :key="item.classMaterials"
        >
          <td>{{ item.classMaterials }}</td>
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
      },
      {
        classMaterials: 'Class Material 2',
      },
      {
        classMaterials: 'Class Material 3',
      },
      {
        classMaterials: 'Quiz 1',
      },
      {
        classMaterials: 'Quiz 2',
      },
    ]

    return {
      classMaterials,
    }
  },
}
</script>
