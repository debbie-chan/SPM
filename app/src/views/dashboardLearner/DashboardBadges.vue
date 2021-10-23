<template>
  <v-card class="greeting-card">
    <v-row class="ma-0 pa-0">
      <v-col cols="8">
        <v-card-title class="text-no-wrap pt-1 ps-2">
          My Badges
        </v-card-title>
        <v-card-text class="d-flex align-center mt-2 ms-5 pb-2 ps-5">
          <div class='row'>
            <div
              v-for= "(course, index) in completedCourses" :key="index"
              class="col-md-3"
              >
              <p>
                <v-img
                  contain
                  height="98"
                  max-width="83"
                  class="greeting-card-trophy"
                  src="@/assets/images/misc/trophy.png"
                ></v-img>
              </p>
              <p>
                {{course}} {{index}}
              </p>
            </div>
          </div>
        </v-card-text>
      </v-col>
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

<script>
  export default {
    props: ['completedCourses']
  }
</script>
