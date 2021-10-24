<template>
    <v-card>
        <v-card-title>
            Question 2
        </v-card-title>
        <v-card-text>
            <v-text-field
              label="Question"
              outlined
              dense
            ></v-text-field>
            <v-radio-group v-model="radioGroup">
              <v-radio
                  v-for= "index in ['True', 'False']"
                  :key="index"
                  :label="`${index}`"
                  class= 'pb-4'
              ></v-radio>
            </v-radio-group>
        </v-card-text>
    </v-card>

</template>

<script>
export default {
  data() {
    return {
      radioGroup: null,
    }
  },
}
</script>
