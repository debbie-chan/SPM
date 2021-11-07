<template>
  <v-simple-table>
    <template>
      <thead>
        <tr>
          <th class="text-uppercase">
            Description
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(value, key) in lessons.hyperlinks"
          :key="key"
        >
          <td>
            <a v-bind:href= "value.link">
              {{value.description}}
            </a>
          </td>
        </tr>
        <tr>
          <td>
            <a v-bind:href= "'/Learner/takeQuiz/' + lessons.lessonCode">
              Quiz 1
            </a>
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
  props: ['lessons'],
}
</script>
