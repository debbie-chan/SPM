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
            <v-radio
                v-for= "index in ['True', 'False']"
                :key="index"
                :label="`${index}`"
                class= 'pb-4'
            ></v-radio>
        </v-card-text>
    </v-card>

</template>
