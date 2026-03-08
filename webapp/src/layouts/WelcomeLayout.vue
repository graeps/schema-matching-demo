<template>
  <transition
    enter-active-class="animated fadeIn slower"
    leave-active-class="animated fadeOut slower"
    mode="out-in"
    :duration="3000"
  >
    <q-layout view="hHh lpR fFf">
      <q-header position="absolute" flat class="bg-container no-padding no-margin">
        <q-toolbar>
          <q-avatar class="q-ml-xl" size="xl">
            <q-img src="../assets/scads-corp-design/icons/scads-ai-logo.png" />
          </q-avatar>
          <q-toolbar-title>
            <div class="q-ml-sm" style="color: #d7f7ff">Schema-Matching-Demonstrator</div>
          </q-toolbar-title>
        </q-toolbar>

        <q-tabs align="center" class="q-mt-sm navigation-tabs">
          <q-route-tab to="/" label="Start" />
          <q-route-tab to="/intro" label="Einführung" />
          <q-route-tab to="/sm" label="Hintergrund" />
          <q-route-tab to="/ampl-project" label="Schema Matching am ScaDS.AI" />
          <q-route-tab to="/details" label="Details" />
          <q-route-tab to="/try-it" label="Ausprobieren" />
        </q-tabs>
      </q-header>

      <q-page-container class="column items-center bg-black">
        <transition
          enter-active-class="animated fadeIn slower"
          leave-active-class="animated fadeOut slower"
          mode="out-in"
          :duration="3000"
        >
          <router-view />
        </transition>
      </q-page-container>
    </q-layout>
  </transition>
</template>

<script></script>

<style>
.bg-container {
  background-image: url('../assets/scads-corp-design/waves/wave-top-old.svg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top;
  background-color: transparent;
  height: 60px;
  font-family: Barlow, sans-serif;
}

.navigation-tabs {
  color: #0194c4;
}
</style>
