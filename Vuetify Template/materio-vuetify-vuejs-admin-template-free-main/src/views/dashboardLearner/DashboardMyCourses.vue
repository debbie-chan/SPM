<template>
  <v-card class="greeting-card">
    <v-card-title class="text-no-wrap pt-4 ps-4 pb-2">
      My Courses
    </v-card-title>
    <v-row class="ma-2 pa-0 ">
      <v-card
        v-for= "index in 4" :key="index"
        class="mx-10 mt-3 mb-5 col-md-2"
        max-width="344"
        outlined
      >
        <v-list-item three-line>
          <v-list-item-content>
            <v-list-item-title class="text-h5 mb-1">
              Course {{index}}
            </v-list-item-title>
            <v-list-item-subtitle>
              Class {{index}}
            </v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-avatar
            tile
            size="80"
            color="grey"
          ></v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn
            medium
            color= "primary"
          >
            Go to Class
          </v-btn>
        </v-card-actions>
      </v-card>
      <v-col cols="4">
        <v-img
          contain
          height="150"
          width="129"
          :src="require(`@/assets/images/misc/triangle-${$vuetify.theme.dark ? 'dark':'light'}.png`)"
          class="greeting-card-bg"
        ></v-img>
      </v-col>
    </v-row>
  </v-card>
</template>

<style lang="scss" scoped>
.greeting-card {
  position: relative;
  .greeting-card-bg {
    position: absolute;
    bottom: 0;
    right: 0;
  }
  .greeting-card-trophy {
    bottom: 10%;
    right: 8%;
  }
}
// rtl
.v-application {
  &.v-application--is-rtl {
    .greeting-card-bg {
      right: initial;
      left: 0;
      transform: rotateY(180deg);
    }
    .greeting-card-trophy {
      left: 8%;
      right: initial;
    }
  }
}
</style>
