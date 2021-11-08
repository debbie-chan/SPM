<template>
  <v-simple-table>
    <template>
      <thead>
        <tr>
          <th class="text-uppercase">
            Class Number
          </th>
          <th class="text-uppercase">
            Number of Students
          </th>
          <th class="text-uppercase">
            Assigned Trainer
          </th>
          <th class="text-uppercase">
            Start Date
          </th>
          <th class="text-uppercase">
            End Date
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(value, key) in classes"
          :key="key"
        >
          <td>
              {{value.classCode}}
          </td>
          <td>
              <a :href="'/assignStudent/' + courseCode + '/' + value.classCode" >
                {{value.currentEnrollment}}
              </a>
          </td>
          <td v-if = 'value.trainerName===""'>
              <a :href="'/assignTrainer/' + courseCode + '/' + value.classCode">
                Assign Trainer
              </a>
          </td>
          <td v-else>
            {{value.trainerName}}
          </td>
          <td>
              {{value.startDate}}
          </td>
          <td>
              {{value.endDate}}
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>

export default {
  props: ['courseCode', 'classes'],
}
</script>
