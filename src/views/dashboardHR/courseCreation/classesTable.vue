<template>
  <v-row>
    <v-col cols = '12'>
      <v-card>
        <v-card-title>
              Add Class:
        </v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
                v-model= "classNumber"
                label="Class Number"
                outlined
                dense
            ></v-text-field>
            <v-text-field
                  v-model= "numberOfStudents"
                  label="Number of Students"
                  outlined
                  dense
            ></v-text-field>
            <v-text-field
                  v-model= "trainer"
                  label="Trainer"
                  outlined
                  dense
            ></v-text-field>
            <v-btn class= 'primary'>
              Add New Class
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col>
      <v-simple-table
        height="250"
        fixed-header
      >
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center text-uppercase">
                Class Number
              </th>
              <th class="text-center text-uppercase">
                Number of Students
              </th>
              <th class="text-center text-uppercase">
                Trainer
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in classes"
              :key="item.classes"
            >
              <td class="text-center">{{ item.classNumber }}</td>
              <td class="text-center">
                {{ item.numberOfStudents}}
              </td>
              <td class="text-center">
                {{ item.trainer }}
              </td>
    <!-- can replace trainer with v-autocomplete -->
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-col>
  </v-row>
</template>

<script>
export default {
  setup() {
    const classes = [
      {
        classNumber: '1',
        numberOfStudents: 50,
        trainer: 'Trainer 1',

      },
      {
        classNumber: '2',
        numberOfStudents: 52,
        trainer: 'Trainer 2',

      },
      {
        classNumber: '3',
        numberOfStudents: 48,
        trainer: 'Trainer 3',

      },
    ]

    return {
      classes,
    }
  },
  data: () => ({
    classNumber: '',
    numberOfStudents: 0,
    trainer: '',
  }),
}
</script>
