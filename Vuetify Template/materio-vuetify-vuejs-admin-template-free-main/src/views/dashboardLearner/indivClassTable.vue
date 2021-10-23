<template>
  <v-simple-table>
    <template>
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
          <td v-if = "item.status === 'Completed'" class="text-center">
            {{ item.status }}
          </td>
          <td v-else class = 'text-center'>
            <a href = "./takeQuiz">
              {{item.status}}
            </a>
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
        status: 'Start',
      },
    ]

    return {
      classMaterials,
    }
  },
}
</script>
