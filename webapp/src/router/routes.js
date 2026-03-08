const routes = [
  {
    path: "/",
    component: () => import("layouts/WelcomeLayout.vue"),
    children: [{ path: "", component: () => import("pages/1WelcomePage.vue") }],
    meta: { transition: "slide-left" },
  },
  {
    path: "/intro",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/2IntroductionPage.vue") }],
  },
  {
    path: "/sm",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/3ScientificBackground.vue") }],
  },

  {
    path: "/ampl-project",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/4AmplProject.vue") }],
  },
  {
    path: "/details",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/4aDetailsAmpl.vue") }],
  },
  {
    path: "/try-it",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/5TryIt.vue") }],
  },
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
]
export default routes
