import { createWebHistory, createRouter } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: () => import('@/views/DashBoard.vue'),    
    children: [
      {
        path: '/',
        name: 'products',
        component: () => import('@/views/Product.vue'),            
      },
    ]
  },  
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;
