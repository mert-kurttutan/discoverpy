import type { RouteParams, RouteRecordRaw } from 'vue-router'
import { createRouter, createWebHashHistory } from 'vue-router'
import AnalyzePackage from './components/AnalyzePackage.vue'
import Main from './components/Main.vue'

export type AppRouteNames =
  | 'search'

export const routes: RouteRecordRaw[] = [
  {
    name: 'home',
    path: '/',
    component: Main,
  },
  {
    name: 'search',
    path: '/search',
    component: AnalyzePackage,
  },
]
export const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export function routerPush(name: AppRouteNames, params?: RouteParams): ReturnType<typeof router.push> {
  console.log('routerPush', name, params)
  return params === undefined
    ? router.push({ name })
    : router.push({ name, params })
}

export function routerPushQuery(name: AppRouteNames, query: Record<string, string>): ReturnType<typeof router.push> {
  console.log('routerPushQuery', name, query)
  return router.push({ name, query })
}