import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: 'dashboardLearner',
  },
  {
    path: '/dashboardLearner',
    name: 'dashboardLearner',
    component: () => import('@/views/dashboardLearner/Dashboard.vue'),
  },
  {
    path: '/Learner/indivCourse',
    name: 'learnerIndivCourse',
    component: () => import('@/views/dashboardLearner/indivCourses.vue'),
  },
  {
    path: '/HR/indivCourse',
    name: 'HRIndivCourse',
    component: () => import('@/views/dashboardHR/indivCourse/indivCourse.vue'),
  },
  {
    path: '/takeQuiz',
    name: 'takeQuiz',
    component: () => import('@/views/takeQuiz/takeQuiz.vue'),
  },
  {
    path: '/dashboardTrainer',
    name: 'dashboardTrainer',
    component: () => import('@/views/dashboardTrainer/Dashboard.vue'),
  },
  {
    path: '/Trainer/indivCourse',
    name: 'TrainerIndivCourse',
    component: () => import('@/views/dashboardTrainer/indivCourses.vue'),
  },
  {
    path: '/dashboardHR',
    name: 'dashboardHR',
    component: () => import('@/views/dashboardHR/Dashboard.vue'),
  },
  {
    path: '/editClass',
    name: 'editClass',
    component: () => import('@/views/dashboardHR/editClass/editAssignedStudents.vue'),
  },
  {
    path: '/trainer/quizCreation',
    name: 'quizCreation',
    component: () => import('@/views/quizCreation/quizCreation.vue'),
  },
  {
    path: '/allCourses',
    name: 'allCourses',
    component: () => import('@/views/allCourses/allCourses.vue'),
  },
  {
    path: '/HR/addNewCourse',
    name: 'addNewCourse',
    component: () => import('@/views/dashboardHR/courseCreation/addNewCourse.vue'),
  },
  {
    path: '/typography',
    name: 'typography',
    component: () => import('@/views/typography/Typography.vue'),
  },
  {
    path: '/icons',
    name: 'icons',
    component: () => import('@/views/icons/Icons.vue'),
  },
  {
    path: '/cards',
    name: 'cards',
    component: () => import('@/views/cards/Card.vue'),
  },
  {
    path: '/simple-table',
    name: 'simple-table',
    component: () => import('@/views/simple-table/SimpleTable.vue'),
  },
  {
    path: '/form-layouts',
    name: 'form-layouts',
    component: () => import('@/views/form-layouts/FormLayouts.vue'),
  },
  {
    path: '/pages/account-settings',
    name: 'pages-account-settings',
    component: () => import('@/views/pages/account-settings/AccountSettings.vue'),
  },
  {
    path: '/pages/login',
    name: 'pages-login',
    component: () => import('@/views/pages/Login.vue'),
    meta: {
      layout: 'blank',
    },
  },
  {
    path: '/pages/register',
    name: 'pages-register',
    component: () => import('@/views/pages/Register.vue'),
    meta: {
      layout: 'blank',
    },
  },
  {
    path: '/error-404',
    name: 'error-404',
    component: () => import('@/views/Error.vue'),
    meta: {
      layout: 'blank',
    },
  },
  {
    path: '*',
    redirect: 'error-404',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
