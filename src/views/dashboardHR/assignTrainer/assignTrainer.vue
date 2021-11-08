<template>
  <v-row>
    <v-col cols = '12'>
      <v-card>
        <v-card-title>
          X1010 - G2
        </v-card-title>
        <v-card-subtitle>
          Trainer: {{currentTrainer}}
        </v-card-subtitle>
      </v-card>
    </v-col>
    <v-col cols ='12'>
      <v-card>
        <v-card-title>
          Assign Trainer To Class:
        </v-card-title>
        <v-simple-table>
          <thead>
            <tr>
              <th class="text-left">
                Trainer Name
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="trainer in allTrainers"
              :key="trainer"
            >
              <td>
                 {{trainer.employeeName}}
                 <v-btn
                  class= 'primary ml-4'
                  @click= "assignTrainer(trainer.username)">
                  Assign
                 </v-btn>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

import axiosIns from '@/plugins/axios'

export default {
  data() {
    return {
      currentTrainer: '',
      allTrainers: [],
      courseCode: 'X1010',
      classCode: 'G2',
    }
  },
  mounted() {
    axiosIns
      .get('/trainer')
      .then(response => {
        this.allTrainers = response.data
      })
    axiosIns
      .get('/class/G2')
      .then(response => {
        console.log(response.data)
        this.currentTrainer = response.data.trainerName
      })
  },
  methods: {
    assignTrainer(username) {
      const link = `/assignTrainerToClass/${username}/${this.courseCode}/${this.classCode}`
      axiosIns
        .get(link)
        .then(window.location.reload())
    },
  },
}
</script>
