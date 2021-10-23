<template>
    <v-card>
      <v-card-title>
        Question 1
      </v-card-title>
      <v-card-text>
          <v-text> This is MCQ</v-text>
          <v-radio-group v-model="radioGroup">
            <v-radio
              v-for= "index in 4"
              :key="index"
              :label="`Option ${index}`"
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
