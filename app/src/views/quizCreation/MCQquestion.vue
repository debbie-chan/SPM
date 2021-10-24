<template>
    <v-card>
        <v-card-title>
            Question 1
        </v-card-title>
        <v-card-text>
            <v-text-field
              label="Question"
              outlined
              dense
            ></v-text-field>
            <v-text-field
                v-for= "index in 4"
                :key="index"
                :label="`Option ${index}`"
            ></v-text-field>
        </v-card-text>
    </v-card>

</template>
