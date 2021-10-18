<template>
  <div>
    <h1>All Courses</h1>
    <br>
    <v-row>
      <!-- card explore -->
      <v-col
        md="4"
        sm="6"
        cols="12"
        class="align-self-start"
      >
        <v-card>
          <v-img
            src="@/assets/images/pages/card-basic-person.png"
            height="250"
          ></v-img>
          <v-card-title>
            Course 1
          </v-card-title>
          <v-card-text>
            Some description here
          </v-card-text>
          <v-card-actions class="dense">
            <v-btn
              color="primary"
              text
            >
              Details
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              icon
              @click="isCardDetailsVisible = !isCardDetailsVisible"
            >
              <v-icon>{{ isCardDetailsVisible ? icons.mdiChevronUp : icons.mdiChevronDown }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-expand-transition>
            <div v-show="isCardDetailsVisible">
              <v-divider></v-divider>
              <v-card-text>
                Detailed description here
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
      <!-- card explore -->
      <v-col
        md="4"
        sm="6"
        cols="12"
        class="align-self-start"
      >
        <v-card>
          <v-img
            src="@/assets/images/pages/card-basic-person.png"
            height="250"
          ></v-img>
          <v-card-title>
            Course 2
          </v-card-title>
          <v-card-text>
            Some description here
          </v-card-text>
          <v-card-actions class="dense">
            <v-btn
              color="primary"
              text
            >
              Details
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              icon
              @click="isCardDetailsVisible = !isCardDetailsVisible"
            >
              <v-icon>{{ isCardDetailsVisible ? icons.mdiChevronUp : icons.mdiChevronDown }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-expand-transition>
            <div v-show="isCardDetailsVisible">
              <v-divider></v-divider>
              <v-card-text>
                Detailed description here
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
      <!-- card explore -->
      <v-col
        md="4"
        sm="6"
        cols="12"
        class="align-self-start"
      >
        <v-card>
          <v-img
            src="@/assets/images/pages/card-basic-person.png"
            height="250"
          ></v-img>
          <v-card-title>
            Course 3
          </v-card-title>
          <v-card-text>
            Some description here
          </v-card-text>
          <v-card-actions class="dense">
            <v-btn
              color="primary"
              text
            >
              Details
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              icon
              @click="isCardDetailsVisible = !isCardDetailsVisible"
            >
              <v-icon>{{ isCardDetailsVisible ? icons.mdiChevronUp : icons.mdiChevronDown }}</v-icon>
            </v-btn>
          </v-card-actions>
          <v-expand-transition>
            <div v-show="isCardDetailsVisible">
              <v-divider></v-divider>
              <v-card-text>
                Detailed description here
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { ref } from '@vue/composition-api'
import {
  mdiChevronUp,
  mdiChevronDown,
  mdiCartPlus,
  mdiShareVariantOutline,
  mdiLockOpenOutline,
  mdiStarOutline,
  mdiAccountOutline,
  mdiTrendingUp,
  mdiHelpCircleOutline,
} from '@mdi/js'

export default {
  setup() {
    const isCardDetailsVisible = false
    const rating = ref(5)

    return {
      isCardDetailsVisible,
      rating,

      // icons
      icons: {
        mdiChevronUp,
        mdiChevronDown,
        mdiCartPlus,
        mdiShareVariantOutline,
        mdiLockOpenOutline,
        mdiStarOutline,
        mdiAccountOutline,
        mdiTrendingUp,
        mdiHelpCircleOutline,
      },
    }
  },
}
</script>

<style lang="scss" scoped>
@import '@/plugins/vuetify/default-preset/preset/mixins.scss';

.avatar-center {
  top: -2rem;
  left: 1rem;
  border: 3px solid white;
  position: absolute;
}

// membership pricing
@include theme--child(memberpricing-bg) using ($material) {
  background-color: rgba(map-deep-get($material, 'primary-shade'), map-deep-get($material, 'states', 'hover'));
}

.memberpricing-bg {
  position: relative;
}
.membership-pricing {
  text-align: center;
  sup {
    font-size: 3.75rem;
    top: 9px;
  }
}
</style>
