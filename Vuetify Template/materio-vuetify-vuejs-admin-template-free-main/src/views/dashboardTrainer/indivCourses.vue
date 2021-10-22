<template>
  <v-row>
    <h1>Course 1 : Class 1</h1>
    <v-col cols= '12'>
        <v-btn
          color="primary"
          dark
          @click = allChapters()
        >
          Add Chapter
        </v-btn>
    </v-col>
    <v-col cols="12"
    v-for = 'chapter in chapters'
    :key = 'chapter'>
      <v-card>
        <v-card-title>
          <v-col cols = '10'>
            Chapter {{chapter.number}}
          </v-col>
          <v-col cols = '2'>
            <v-btn
              color="primary"
              dark
              @click = addMaterial()
            >
              Add Material
            </v-btn>
          </v-col>
        </v-card-title>
        <v-simple-table>
          <template>
            <thead>
              <tr>
                <th class="text-uppercase">
                  Syllabus Outline
                </th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="item in chapter.classMaterials"
                :key="item"
              >
                <td>{{ item }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

// import indivClassTable from './indivClassTable.vue'

export default {
  components: {

    // indivClassTable,
  },
  data() {
    const chapters = [
      {
        number: 1,
        classMaterials: ['Class Material 1', 'Class Material 2', 'Class Material 3', 'Quiz 1', 'Quiz 2'],
      },
    ]

    return {
      chapters,
    }
  },
  methods: {
    newChapter() {
      this.chapters.push({
        number: 2,
      })
    },
  },
  computed: {
    allChapters() {
      this.newChapter()

      return this.chapters
    },
  },
}
</script>
